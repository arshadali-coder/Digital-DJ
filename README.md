# 🎧 Digital DJ

**Digital DJ** is a web-based music recommendation platform that generates personalized playlists based on a user’s current mood. Designed for focus, relaxation, and emotional balance, the application combines intelligent recommendations with real-time user feedback and analytics.

---

## 🌐 Live Application

**Website:** [https://digital-dj.arshadali.site/](https://digital-dj.arshadali.site/)  
**Source Code:** [https://github.com/arshadali-coder/Digital-DJ](https://github.com/arshadali-coder/Digital-DJ)

---

## 📂 Project Structure

```

Digital-DJ/
│
├── backend/                 # Backend server (Flask API)
│   ├── app.py
│   ├── requirements.txt
│   ├── music_dataset.csv
│   └── supporting modules
│
├── index.html               # Frontend (HTML, CSS, JavaScript)
│
└── README.md

````

---

## ✨ Key Features

- 🎵 Mood-based playlist generation  
- 📚 Multiple curated tracks per mood  
- ⭐ Interactive song rating system (1–5 stars)  
- 📊 Mood usage analytics and insights  
- 🔁 Smart recommendations based on user preferences  
- 📁 Playlist export functionality in CSV format  
- ⚡ Fast and responsive user interface  

---

## 🧠 Recommendation Logic

Digital DJ adapts to user behavior by identifying patterns in mood preferences.  
If users frequently engage with certain moods, the system recommends related moods that similar users have enjoyed.

---

## 📈 Analytics & Insights

- Tracks user interactions with moods  
- Displays most frequently used moods  
- Calculates average ratings for each mood category  
- Provides meaningful feedback to improve recommendations

---

## 🛠️ Technology Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (Vanilla)  
- REST API integration using Fetch

### Backend
- Python  
- Flask  
- Flask-CORS  
- Pandas  
- CSV-based data handling

---

## ⚙️ Backend Setup (Local Development)

```bash
cd backend
python -m venv myenv
source myenv/bin/activate     # Windows: myenv\Scripts\activate
pip install -r requirements.txt
python app.py
````

Server runs at:

```
http://127.0.0.1:5000
```

---

## 🖥️ Frontend Usage

Open `index.html` in any modern browser.
The frontend communicates directly with the backend APIs for playlist generation, analytics, and exports.

---

## 📤 Data Export

Users can download their generated playlists as a `.csv` file, containing:

* Song title
* Mood category
* Duration
* User rating

---

## 👨‍💻 Author

**Arshad Ali**
B.Tech Data Science
GitHub: [https://github.com/arshadali-coder](https://github.com/arshadali-coder)

---

## 📄 License

This project is open for educational, personal, and portfolio use.
