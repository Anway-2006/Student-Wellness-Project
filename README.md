📚 Personal Study & Wellness Reminder
BYOP Project — Python Programming Course

📋 Overview
The Personal Study & Wellness Reminder is a command-line tool designed to help students maintain a healthy balance between productivity and self-care. It tackles the common problem of "study-tunnel-vision" where students forget to hydrate, eat, or take necessary breaks during intense study sessions.

This project was developed as part of the BYOP (Build Your Own Project) series to demonstrate core Python concepts like data persistence, time manipulation, and modular programming.

✨ Key Features
💧 Hydration Tracking: Log your water intake and receive reminders to reach the daily goal of 8 glasses.

🍽️ Meal Logging: Keep a record of your meals (Breakfast, Lunch, Snacks, Dinner) to ensure you are fueling your brain.

☕ Integrated Break Timer: Choose between quick, short, or long breaks. The app includes a real-time countdown timer to encourage stepping away from the screen.

📊 Dynamic Daily Summary: Generates a comprehensive report of your wellness habits for the day, including personalized feedback and health tips.

💾 Data Persistence: Automatically saves your progress to a wellness_data.json file, allowing you to resume sessions or track history.

🛠️ Technical Implementation
The project utilizes several built-in Python modules:

json: To save and load user data for persistent storage.

os: To check for existing data files on the system.

time: To manage the countdown functionality for study breaks.

datetime: To timestamp entries and manage daily session resets.

🚀 How to Use
Run the script:

Bash
python wellness_reminder.py
Setup: Enter your name and your planned study hours for the day.

The Menu:

Press 1 to log water (input number of glasses).

Press 2 to log what you ate.

Press 3 to start a break timer (5, 10, or 20 mins).

Press 4 to see your current stats and "Wellness Check" tips.

Press 5 to save your progress and exit.

📂 File Structure
wellness_reminder.py: The main Python application script.

wellness_data.json: (Auto-generated) Stores your logs and session data in a structured format.

💡 Future Enhancements
[ ] Visual Notifications: Implement desktop alerts when a break timer ends.

[ ] Weekly Analytics: Generate graphs showing hydration trends over 7 days.

[ ] Custom Goals: Allow users to set their own water and break targets.

[ ] GUI: Transition from a Command Line Interface (CLI) to a Graphical User Interface (GUI).
