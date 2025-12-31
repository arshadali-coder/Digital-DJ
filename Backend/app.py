from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from collections import Counter, defaultdict

# --------------------
# App setup
# --------------------
app = Flask(__name__)

# Allow frontend domain only (change if needed)
CORS(app)

# --------------------
# File paths (PRODUCTION SAFE)
# --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "music_dataset.csv")

# Load dataset
data = pd.read_csv(DATA_PATH)

# --------------------
# In-memory analytics
# --------------------
mood_usage = Counter()
ratings = defaultdict(list)
transitions = defaultdict(Counter)
last_mood = None

# --------------------
# Health check endpoint
# --------------------
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "Digital DJ Backend",
        "version": "1.0.0"
    })

# --------------------
# Generate playlist
# --------------------
@app.route("/playlist", methods=["POST"])
def playlist():
    global last_mood

    payload = request.get_json()
    mood = payload.get("mood")

    if not mood:
        return jsonify({"error": "Mood is required"}), 400

    mood_data = data[data["Mood"] == mood]

    if mood_data.empty:
        return jsonify({"error": "No songs found for this mood"}), 404

    sample_size = min(5, len(mood_data))
    playlist = mood_data.sample(sample_size).to_dict("records")

    # analytics
    mood_usage[mood] += 1
    if last_mood:
        transitions[last_mood][mood] += 1

    recommendation = None
    if transitions[mood]:
        recommendation = transitions[mood].most_common(1)[0][0]

    last_mood = mood

    return jsonify({
        "mood": mood,
        "playlist": playlist,
        "recommendation": recommendation
    })

# --------------------
# Rate playlist
# --------------------
@app.route("/rate", methods=["POST"])
def rate():
    payload = request.get_json()
    mood = payload.get("mood")
    rating = payload.get("rating")

    if not mood or not rating:
        return jsonify({"error": "Mood and rating required"}), 400

    if not (1 <= int(rating) <= 5):
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    ratings[mood].append(int(rating))
    return jsonify({"status": "rating saved"})

# --------------------
# Analytics endpoint
# --------------------
@app.route("/analytics", methods=["GET"])
def analytics():
    avg_ratings = {
        mood: round(sum(r) / len(r), 2)
        for mood, r in ratings.items()
    }

    return jsonify({
        "top_moods": mood_usage.most_common(3),
        "average_ratings": avg_ratings
    })

# --------------------
# Entry point (local only)
# --------------------
if __name__ == "__main__":
    app.run()
