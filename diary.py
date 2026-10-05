import os
import datetime

JOURNAL_DIR = "diary_entries"

def create_journal_directory():
    if not os.path.exists(JOURNAL_DIR):
        os.makedirs(JOURNAL_DIR)

def get_today_filename():
    today = datetime.date.today().isoformat()
    return os.path.join(JOURNAL_DIR, f"{today}.txt")

def write_entry(entry_text):
    filename = get_today_filename()
    with open(filename, 'a', encoding='utf-8') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n{entry_text}\n\n")

def read_entries():
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No entries for today.")
        return
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\n---Today's Personal Thoughts---")
        print(content)

def read_entries_by_date(date_input):
    filename = os.path.join(JOURNAL_DIR, f"{date_input}.txt")

    if not os.path.exists(filename):
        print(f"No entries found for {date_input}.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    print(f"\n--- Entries from {date_input} ---")
    print(content)
