# app.py (Flask backend)
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Create SQLite database and tables if not exist
if not os.path.exists('users.db'):
    with sqlite3.connect('users.db') as conn:
        conn.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                full_name TEXT,
                gender TEXT,
                age INTEGER,
                email TEXT UNIQUE,
                password TEXT
            )
        ''')

# Always ensure mood_logs table exists
with sqlite3.connect('users.db') as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS mood_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            typed_sentence TEXT,
            typing_speed REAL,
            backspace_rate REAL,
            burst_duration REAL,
            idle_time REAL,
            hold_time REAL,
            detected_mood TEXT
        )
    ''')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with sqlite3.connect('users.db') as conn:
            user = conn.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password)).fetchone()
            if user:
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid login credentials", "danger")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']
        password = request.form['password']

        try:
            with sqlite3.connect('users.db') as conn:
                conn.execute("INSERT INTO users (full_name, gender, age, email, password) VALUES (?, ?, ?, ?, ?)",
                             (full_name, gender, age, email, password))
                flash("Registration successful!", "success")
                return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash("Email already registered.", "danger")
    return render_template('register.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    mood_result = None
    if request.method == 'POST':
        typed_sentence = request.form['typed_sentence']
        typing_speed = float(request.form['typing_speed'])
        backspace_rate = float(request.form['backspace_rate'])
        burst_duration = float(request.form['burst_duration'])
        idle_time = float(request.form['idle_time'])
        hold_time = float(request.form['hold_time'])

        # Dummy mood detection logic
        if "happy" in typed_sentence.lower():
            mood_result = "happy"
        elif "sad" in typed_sentence.lower():
            mood_result = "sad"
        elif "angry" in typed_sentence.lower():
            mood_result = "angry"
        else:
            mood_result = "anxious"

        # Save mood log
        with sqlite3.connect('users.db') as conn:
            conn.execute('''
                INSERT INTO mood_logs 
                (typed_sentence, typing_speed, backspace_rate, burst_duration, idle_time, hold_time, detected_mood)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (typed_sentence, typing_speed, backspace_rate, burst_duration, idle_time, hold_time, mood_result))

    return render_template('dashboard.html', mood_result=mood_result)

if __name__ == '__main__':
    app.run(debug=True)
