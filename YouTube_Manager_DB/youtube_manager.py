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
    """
    List all videos stored in the database.
    """
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if videos:
        print('\n' + '*' * 70)
        for row in videos:
            print(f"{row[0]}. Name: {row[1]}, Duration: {row[2]}")
        print('*' * 70 + '\n')
    else:
        print("No videos found.")

def add_video(name, time):
    """
    Add a new video to the database.
    """
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("Video added successfully.")

def update_video(video_id, new_name, new_time):
    """
    Update the details of the video in the database.
    """
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print("Video updated successfully.")

def delete_video(video_id):
    """
    Delete a video from the database.
    """
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id, ))
    conn.commit()
    print("Video deleted successfully.")

def main():
    """
    Main function to manage YouTube video database.
    """
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
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)
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