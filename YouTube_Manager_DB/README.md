# YouTube Video Manager

This project is a simple YouTube video manager that allows users to add, update, delete, and list YouTube videos. The video data is stored in a SQLite database (`youtube_videos.db`).

## Features

- **List all YouTube videos**: Display all videos with their names and durations.
- **Add a YouTube video**: Add a new video with its name and duration.
- **Update YouTube video details**: Update the details of an existing video.
- **Delete a YouTube video**: Remove a video from the list.

## Requirements

- Python 3.x
- SQLite

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/youtube-video-manager.git
    cd youtube-video-manager
    ```

2. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Execute the `youtube_videos.db` file to create and initialize the SQLite database.
2. Run the `youtube_video_manager_db.py` file to start the application.
3. Follow the on-screen prompts to manage your YouTube videos.

## Code Structure

- `youtube_video_manager_db.py`: Main script that implements the YouTube video manager application with database integration.
- `youtube_videos.db`: SQLite database file for storing video data.

## Functions

- `list_videos()`: Displays a list of all YouTube videos stored in the database.
- `add_video(name, time)`: Adds a new YouTube video to the database with the specified name and duration.
- `update_video(video_id, new_name, new_time)`: Updates the details of an existing YouTube video in the database.
- `delete_video(video_id)`: Deletes a YouTube video from the database based on its ID.
- `main()`: Main function that drives the application's functionality and user interaction.

## Example Usage

```bash
YouTube Video Manager App with DB
1. List all YouTube videos
2. Add a YouTube video
3. Update a YouTube video details
4. Delete a YouTube video
5. Exit the app
Enter your choice: 1

**********************************************************************
1. Name: Video1, Duration: 10:00
2. Name: Video2, Duration: 15:30
**********************************************************************
