# mongodb+srv://youtubepy:<youtubepy>@cluster0.y1lp9yp.mongodb.net/
from pymongo import MongoClient

# Setup mongo db client
client = MongoClient("mongodb+srv://youtubepy:<youtubepy>@cluster0.y1lp9yp.mongodb.net/")

# Database name
db = client["ytmanager"]
video_collection = db["videos"]

# print(video_collection)
"""
Collection(Database(MongoClient(host=['ac-boiuokx-shard-00-01.y1lp9yp.mongodb.net:27017', 'ac-boiuokx-shard-00-00.y1lp9yp.mongodb.net:27017', 'ac-boiuokx-shard-00-02.y1lp9yp.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, authsource='admin', replicaset='atlas-1comw4-shard-0', tls=True), 'ytmanager'), 'videos')
"""

def list_videos():
    pass

def add_video(name, time):
    pass

def update_video(video_id, new_name, new_time):
    pass

def delete_video(video_id):
    pass

def main():
    while True:
        print("\n YouTube Video Manager App ")
        print("1. List all videos: ")
        print("2. Add a new video: ")
        print("3. Update a video: ")
        print("4. Delete a video: ")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter updated video name: ")
            time = input("Enter updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()