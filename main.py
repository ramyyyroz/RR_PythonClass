import datetime
import os


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


def read_todays_entries():
    filename = get_today_filename()
    if not os.path.exists(filename):
        print("No entries for today.")
        return 
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\n---Today's Personal Thoughts---")
        print(content)


def read_entries_by_date():
    date_input = input("Enter the date you want to read (YYYY-MM-DD): ")
    filename = os.path.join(JOURNAL_DIR, f"{date_input}.txt")

    if not os.path.exists(filename):
        print(f"No entries found for {date_input}.")
        return

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    print(f"\n--- Entries from {date_input} ---")
    print(content)


def display_menu():
    print("\nDaily Diary Menu")
    print("1. Write Entry")
    print("2. Read Today's Entries")
    print("3. Read Entries From Another Date")
    print("4. Exit")


def run_journal_app():
    create_journal_directory()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            entry_text = input("Write your entry: ")
            write_entry(entry_text)
            print("Entry saved.")
        elif choice == '2':
            read_todays_entries()
        elif choice == '3':
            read_entries_by_date()
        elif choice == '4':
            print("Exiting the diary app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_journal_app()