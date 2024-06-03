# YouTube Video Manager

This project is a simple YouTube video manager that allows users to add, update, delete, and list YouTube videos. The video data is stored in a JSON file (`youtube.txt`).

## Features

- **List all YouTube videos**: Display all videos with their names and durations.
- **Add a YouTube video**: Add a new video with its name and duration.
- **Update YouTube video details**: Update the details of an existing video.
- **Delete a YouTube video**: Remove a video from the list.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chughkirat06/YouTube-Manager.git
    cd youtube-video-manager
    ```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Run the script:
    ```bash
    python youtube_manager.py
    ```

2. Follow the on-screen prompts to manage your YouTube videos.

## Code Structure

- `youtube_manager.py`: Main script that runs the YouTube video manager.
- `youtube.txt`: JSON file where video data is stored.

## Functions

### `load_data()`

Loads video data from `youtube.txt`. Returns an empty list if the file does not exist or cannot be read.

### `save_data_helper(videos)`

Saves the video data to `youtube.txt`.

### `list_all_videos(videos)`

Prints a list of all videos.

### `add_video(videos)`

Prompts the user to enter a video name and time, then adds it to the list and saves the data.

### `update_video(videos)`

Prompts the user to select a video to update and enter new details, then updates the video and saves the data.

### `delete_video(videos)`

Prompts the user to select a video to delete, then removes it from the list and saves the data.

### `main()`

Main function that runs the YouTube video manager application, presenting a menu to the user and handling their choices.

## Example

```bash
YouTube Manager | Choose an option 
1. List all YouTube videos 
2. Add a YouTube video 
3. Update YouTube video details 
4. Delete a YouTube video 
5. Exit the app 
Enter your choice: 1

**********************************************************************
1. Name: Video1, Duration: 10:00
2. Name: Video2, Duration: 15:30
**********************************************************************