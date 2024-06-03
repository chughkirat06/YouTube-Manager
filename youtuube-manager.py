import json

def load_data():
    """
    Load video data from the file.
    If the file does not exist, return an empty list.
    """
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    """
    Save video data to the file.
    """
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    """
    Print a list of all the videos.
    """
    print('\n' + '*' * 70)
    if videos:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']}, Duration: {video['time']}")
    else:
        print("No videos found.")
    print('*' * 70 + '\n') 

def add_video(videos):
    """
    Add a new video to the list.
    """
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully.")

def update_video(videos):
    """
    Update the details of an existing video.
    """
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
        print("Video updated successfully.")
    else:
        print("Invalid video index selected.")

def delete_video(videos):
    """
    Delete a video from the list.
    """
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to be deleted: "))
        if 1 <= index <= len(videos):
            del videos[index-1]
            save_data_helper(videos)
            print("Video deleted successfully.")
        else:
            print("Invalid video index selected.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Main function to run the YouTube video manager
    """
    videos = load_data()

    while True:
        print("\n YouTube Manager | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()