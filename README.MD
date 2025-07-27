**The Typing Mood Detector is a smart web application that predicts the mood of a user based on how they type a sentence and how they behave while typing.

**Instead of only analyzing the text (typed sentence), it also looks at typing behavior patterns like:

Typing speed

Backspace rate

Burst duration

Idle time

Key hold time

**These features are then processed by a machine learning model (ANN) to detect moods like Happy, Sad, Angry, Stressed, or Neutral.

**It’s useful for:

Monitoring mental well-being

Understanding emotional state

Adding emotion-awareness to digital platforms

**Step 1: User Types a Sentence
The user opens the website and sees a text area to type how they’re feeling.

Example: “I had a rough day at work and feel tired.”

🕹 Step 2: Keystroke Data Collection
While the user is typing, the app tracks keystroke dynamics, including:

Feature	Description
Typing Speed (WPM)	How fast the user is typing (words per minute).
Backspace Rate	How many times the user presses backspace (a high rate might show stress or uncertainty).
Burst Duration	How long the user types continuously without pausing.
Idle Time	How long the user pauses between keystrokes (more pause = hesitation or thinking).
Hold Time	How long each key is held down (indicates comfort or tension).

This data is collected using JavaScript on the frontend.

🧠 Step 3: Send Data to Backend
After the user finishes typing, all the data (text + typing behavior) is sent to the Flask backend using a form or AJAX.

The backend prepares these inputs as a feature vector for the model.

🤖 Step 4: Mood Prediction Using ANN
The backend loads a trained ANN model (mood_model.pkl).

It feeds the input features into the model.

The model returns a predicted mood label (e.g., "Stressed", "Happy").

🖼 Step 5: Show the Result
The mood is displayed to the user on the results page (e.g., “Your mood: 😔 Sad”).

You can also show charts or emojis based on mood for better UX.

🧪 Step 6: Optional - Store the Data
Optionally, the app can store:

Typed sentence

Typing metrics

Detected mood

Timestamp

This can be stored in SQLite for future analytics or reports.

**Tools Used
HTML/CSS/JS → Frontend UI, key tracking

Flask (Python) → Backend server

ANN Model (Trained with train_model.py) → Predict mood

Pandas + Scikit-learn → Preprocessing and model training

SQLite (Optional) → Store typing sessions

**1. Typing Speed (WPM)
Meaning: How fast the user types — measured in words per minute.

Example:

Person A (Happy Mood)	Person B (Sad Mood)
Typed 50 words in 1 minute	Typed 20 words in 1 minute
WPM = 50	WPM = 20

👉 High WPM = Confident, energetic mood
👉 Low WPM = Low energy, maybe sadness or tiredness

⌫ 2. Backspace Rate
Meaning: How often the user presses the backspace key while typing.

Example:

A confident person types:
"I am feeling great today!" → 0 backspaces

A stressed person types:
"I am fee... feee... feeling... ugh back... feeling bad" → Pressed backspace 8 times

👉 High backspace usage = Stress, confusion, hesitation
👉 Low backspace usage = Calm, clear mind

🔥 3. Burst Duration (Seconds)
Meaning: How long the user types continuously without pausing.

Example:

Person A types non-stop for 15 seconds (burst duration = 15s)

Person B types for 3 seconds, then pauses for 5 seconds (burst duration = 3s)

👉 Long bursts = Flowing thoughts, positive or energetic mood
👉 Short bursts = Breaks, distraction, or emotional overload

⏸ 4. Idle Time (Seconds)
Meaning: How long the user pauses between key presses.

Example:

Person A types steadily: pause between keys = 0.2 sec

Person B types: I [pause 3s] am [pause 2s] feeling... [pause 5s] bad

👉 Long idle times = Thinking hard, emotional disturbance, sadness
👉 Short idle times = Smooth thinking, positive or relaxed state

⌨ 5. Hold Time (Seconds)
Meaning: How long each key is held down (between press and release).

Example:

Calm person presses and releases each key in 0.1 seconds

Angry person presses hard and holds each key for 0.3–0.5 seconds

👉 High hold time = Frustration, tension (tight typing)
👉 Low hold time = Relaxed, fast typing

**| Feature        | Calm/Happy Example          | Sad/Angry Example          |
| -------------- | --------------------------- | -------------------------- |
| Typing Speed   | 50+ WPM                     | < 20 WPM                   |
| Backspace Rate | Low (0–2 per 100 words)     | High (10+ per 100 words)   |
| Burst Duration | Long (typing 15–20 seconds) | Short bursts (2–5 seconds) |
| Idle Time      | Short (0.2–0.5 sec pauses)  | Long (2–6 sec pauses)      |
| Hold Time      | Low (0.1–0.2 seconds)       | High (0.3–0.6 seconds)     |