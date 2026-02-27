# Typing Mood Detector 🕵️‍♂️⌨️

The Typing Mood Detector is a smart web application that predicts a user's mood based on their typing behavior and patterns. Instead of just analyzing *what* you type, it analyzes *how* you type.

## 🚀 New Features

### ⚡ Automated Metrics Detection
The app now automatically tracks your typing behavior in real-time. You no longer need to manually enter metrics. As you type in the dashboard, the following are calculated:
- **Typing Speed (WPM)**: Your confidence and energy level.
- **Backspace Rate**: Indicators of stress or hesitation.
- **Burst Duration**: Your flow and focus.
- **Idle Time**: Pauses and thinking patterns.
- **Key Hold Time**: Physical tension or relaxation.

### 🤖 Auto-Mood Prediction
The system features a "Smart Submission" logic. Once you stop typing for 1.5 seconds, the app automatically submits your data to the AI model and predicts your mood instantly.

---

## 🛠 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation
1. Clone the repository or download the source code.
2. Install the required dependencies:
   ```bash
   pip install flask
   ```

### Running the App
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   `http://127.0.0.1:5000`

---

## 🧠 How it Works

### Step 1: Real-time Keystroke Tracking
While you type your feelings, JavaScript on the frontend monitors keystroke dynamics:
| Feature | Description |
| --- | --- |
| **Typing Speed** | Words per minute. High WPM often indicates confidence/energy. |
| **Backspace Rate** | Frequency of corrections. High rate can indicate stress. |
| **Burst Duration** | Time spent typing continuously. Long bursts show flow. |
| **Idle Time** | Pauses between keys. Long pauses can show hesitation or sadness. |
| **Hold Time** | Duration a key is pressed. High hold time can indicate tension/anger. |

### Step 2: AI Mood Prediction
The data is sent to a Flask backend where an **Artificial Neural Network (ANN)** processes the features. It predicts moods such as:
- 😊 **Happy**
- 😔 **Sad**
- 😠 **Angry**
- 😰 **Anxious**

---

## 📊 Feature Comparison Table

| Feature        | Calm/Happy Example          | Sad/Angry Example          |
| -------------- | --------------------------- | -------------------------- |
| Typing Speed   | 50+ WPM                     | < 20 WPM                   |
| Backspace Rate | Low (0–2 per 100 words)     | High (10+ per 100 words)   |
| Burst Duration | Long (typing 15–20 seconds) | Short bursts (2–5 seconds) |
| Idle Time      | Short (0.2–0.5 sec pauses)  | Long (2–6 sec pauses)      |
| Hold Time      | Low (0.1–0.2 seconds)       | High (0.3–0.6 seconds)     |

---

## 🛡 Technologies Used
- **Frontend**: HTML5, CSS3, JavaScript (Keystroke Tracking)
- **Backend**: Flask (Python)
- **Database**: SQLite (User Logs)
- **AI/ML**: Scikit-learn (ANN Model)
