# ============================================================
#   Personal Study & Wellness Reminder
#   BYOP Project — Python Programming Course
#   Problem: Students forget water, meals & breaks while studying
# ============================================================

import json
import os
import time
from datetime import datetime

# ---------- File to save data ----------
DATA_FILE = "wellness_data.json"


# ---------- Load existing data from file ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {
        "student_name": "",
        "date": str(datetime.today().date()),
        "water_logs": [],
        "meal_logs": [],
        "break_logs": [],
        "study_hours": 0
    }


# ---------- Save data to file ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("\n✅ Data saved successfully!\n")


# ---------- Setup: Ask user for session info ----------
def setup_session(data):
    print("=" * 50)
    print("   PERSONAL STUDY & WELLNESS REMINDER")
    print("=" * 50)

    if data["student_name"]:
        print(f"\nWelcome back, {data['student_name']}! 👋")
        use_existing = input("Continue with saved data? (yes/no): ").strip().lower()
        if use_existing == "yes":
            return data

    name = input("\nEnter your name: ").strip()
    hours = input("How many hours will you study today? ").strip()

    data["student_name"] = name
    data["study_hours"] = int(hours) if hours.isdigit() else 4
    data["date"] = str(datetime.today().date())
    data["water_logs"] = []
    data["meal_logs"] = []
    data["break_logs"] = []

    print(f"\nHello {name}! Let's have a healthy and productive study session. 💪\n")
    return data


# ---------- Log water intake ----------
def log_water(data):
    print("\n--- LOG WATER INTAKE ---")
    amount = input("How many glasses of water did you drink? ").strip()

    if amount.isdigit():
        timestamp = datetime.now().strftime("%H:%M")
        entry = {"time": timestamp, "glasses": int(amount)}
        data["water_logs"].append(entry)

        total = sum(log["glasses"] for log in data["water_logs"])
        print(f"✅ Logged {amount} glass(es) at {timestamp}.")
        print(f"💧 Total water today: {total} glass(es)")

        if total < 8:
            remaining = 8 - total
            print(f"⚠️  Try to drink {remaining} more glass(es) to reach the daily goal of 8!")
        else:
            print("🎉 Great job! You've hit your daily water goal!")
    else:
        print("❌ Invalid input. Please enter a number.")

    return data


# ---------- Log a meal ----------
def log_meal(data):
    print("\n--- LOG MEAL ---")
    print("Meal types: 1. Breakfast  2. Lunch  3. Snack  4. Dinner")
    choice = input("Select meal type (1-4): ").strip()

    meal_types = {"1": "Breakfast", "2": "Lunch", "3": "Snack", "4": "Dinner"}
    meal = meal_types.get(choice, "Meal")

    description = input(f"What did you have for {meal}? ").strip()
    timestamp = datetime.now().strftime("%H:%M")

    entry = {"time": timestamp, "meal": meal, "description": description}
    data["meal_logs"].append(entry)

    print(f"✅ {meal} logged at {timestamp}: {description}")
    print("🍽️  Remember: Good food fuels great study sessions!")

    return data


# ---------- Take a break with timer ----------
def take_break(data):
    print("\n--- TAKE A BREAK ---")
    print("Choose break duration:")
    print("1. Quick break (5 minutes)")
    print("2. Short break (10 minutes)")
    print("3. Long break (20 minutes)")

    choice = input("Select (1-3): ").strip()
    durations = {"1": 5, "2": 10, "3": 20}
    minutes = durations.get(choice, 5)
    seconds = minutes * 60

    timestamp = datetime.now().strftime("%H:%M")
    print(f"\n⏳ Starting a {minutes}-minute break at {timestamp}...")
    print("Step away from your screen, stretch, and relax!")
    print("Press Ctrl+C at any time to skip the timer.\n")

    try:
        for remaining in range(seconds, 0, -1):
            mins, secs = divmod(remaining, 60)
            print(f"\r⏱️  Time remaining: {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)
        print("\n\n🔔 Break over! Time to get back to studying. You got this! 🚀")
    except KeyboardInterrupt:
        print("\n\n⚡ Break skipped.")

    entry = {"time": timestamp, "duration_minutes": minutes}
    data["break_logs"].append(entry)

    return data


# ---------- View daily summary ----------
def view_summary(data):
    print("\n" + "=" * 50)
    print(f"   DAILY SUMMARY — {data['date']}")
    print(f"   Student: {data['student_name']}")
    print("=" * 50)

    # Water summary
    total_water = sum(log["glasses"] for log in data["water_logs"])
    print(f"\n💧 Water Intake: {total_water} glass(es)")
    if data["water_logs"]:
        for log in data["water_logs"]:
            print(f"   • {log['time']} — {log['glasses']} glass(es)")
    else:
        print("   No water logged yet. Stay hydrated! 🚰")

    # Meal summary
    print(f"\n🍽️  Meals Logged: {len(data['meal_logs'])}")
    if data["meal_logs"]:
        for log in data["meal_logs"]:
            print(f"   • {log['time']} — {log['meal']}: {log['description']}")
    else:
        print("   No meals logged yet. Don't skip meals! 🥗")

    # Break summary
    total_break = sum(log["duration_minutes"] for log in data["break_logs"])
    print(f"\n☕ Breaks Taken: {len(data['break_logs'])} ({total_break} minutes total)")
    if data["break_logs"]:
        for log in data["break_logs"]:
            print(f"   • {log['time']} — {log['duration_minutes']} minutes")
    else:
        print("   No breaks taken. Remember to rest your eyes! 👀")

    # Wellness tips based on data
    print("\n📊 Wellness Check:")
    if total_water < 4:
        print("   ⚠️  You're drinking very little water. Aim for 8 glasses per day!")
    elif total_water < 8:
        print("   👍 Good start on water! Keep drinking more.")
    else:
        print("   ✅ Excellent hydration today!")

    if len(data["meal_logs"]) == 0:
        print("   ⚠️  No meals logged. Eating regularly boosts concentration!")
    elif len(data["meal_logs"]) >= 3:
        print("   ✅ You're eating regularly. Great for focus!")

    if len(data["break_logs"]) == 0:
        print("   ⚠️  No breaks taken. Short breaks improve long-term productivity!")
    else:
        print("   ✅ Good job taking breaks!")

    print("\n" + "=" * 50)


# ---------- Main menu ----------
def main_menu():
    print("\n--- MAIN MENU ---")
    print("1. 💧 Log water intake")
    print("2. 🍽️  Log a meal")
    print("3. ☕ Take a break (with timer)")
    print("4. 📊 View today's summary")
    print("5. 💾 Save and exit")
    return input("\nChoose an option (1-5): ").strip()


# ---------- Main program ----------
def main():
    data = load_data()
    data = setup_session(data)

    while True:
        choice = main_menu()

        if choice == "1":
            data = log_water(data)
        elif choice == "2":
            data = log_meal(data)
        elif choice == "3":
            data = take_break(data)
        elif choice == "4":
            view_summary(data)
        elif choice == "5":
            view_summary(data)
            save_data(data)
            print(f"Goodbye, {data['student_name']}! Keep up the great work! 🌟")
            break
        else:
            print("❌ Invalid option. Please choose between 1 and 5.")


# ---------- Run the program ----------
if __name__ == "__main__":
    main()