import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_video(name, time):
    pass

def update_video(video_id):
    pass

def delete_video(video_id):
    pass

def main():
    while True:
        print("\n YouTube Video Manager App with DB ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            update_video(video_id)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 5.")

    conn.close()

if __name__ == "__main__":
    main()