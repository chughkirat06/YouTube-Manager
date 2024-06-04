from pymongo import MongoClient
from bson.objectid import ObjectId

# Setup mongo db client
try:
    client = MongoClient("mongodb+srv://{YOURUSERNAME}:{YOURPASSWORD}@cluster0.y1lp9yp.mongodb.net/")
except Exception as e:
    print(str(e))

# Database name
db = client["ytmanager"]
video_collection = db["videos"]
print(video_collection)
"""
Collection(Database(MongoClient(host=['ac-boiuokx-shard-00-01.y1lp9yp.mongodb.net:27017', 'ac-boiuokx-shard-00-00.y1lp9yp.mongodb.net:27017', 'ac-boiuokx-shard-00-02.y1lp9yp.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, authsource='admin', replicaset='atlas-1comw4-shard-0', tls=True), 'ytmanager'), 'videos')
"""

def list_videos():
    """
    List all videos in the collection.
    """
    videos = video_collection.find()
    if videos:
        print('\n' + '*' * 70)
        for video in video_collection.find():
            print(f"Id: {video['_id']}. Name: {video['name']} and Duration: {video['time']}")
        print('*' * 70 + '\n')
    else:
        print("No videos found.")

def add_video(name, time):
    """
    Add a new video to the collection.

    :param name: The name of the video.
    :param time: The duration of the video.
    """
    video_collection.insert_one({"name": name, "time": time})
    print("Video added successfully.")

def update_video(video_id, new_name, new_time):
    """
    Update an existing video's details.
    
    :param video_id: The ID of the video to update.
    :param new_name: The new name of the video.
    :param new_time: The new duration of the video.
    """
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )
    print("Video updated successfully.")

def delete_video(video_id):
    """
    Delete a video from the collection.
    
    :param video_id: The ID of the video to delete.
    """
    try:
        result = video_collection.delete_one({"_id": ObjectId(video_id)})
        if result.deleted_count:
            print(f"Video {video_id} deleted successfully.")
        else:
            print(f"No video found with ID {video_id}.")
    except Exception as e:
        print(f"An error occured: {e}.")

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