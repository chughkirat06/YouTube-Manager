# YouTube Video Manager

This project is a simple YouTube video manager that allows users to add, update, delete, and list YouTube videos. The video data is stored in a MongoDB database.

## Features

- **List all YouTube videos**: Display all videos with their names and durations.
- **Add a YouTube video**: Add a new video with its name and duration.
- **Update YouTube video details**: Update the details of an existing video.
- **Delete a YouTube video**: Remove a video from the list.

## Requirements

- Python 3.x
- `pymongo` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/chughkirat06/YouTube-Manager.git
    cd youtube-video-manager
    ```

2. Install the required dependencies:
    ```bash
    pip install pymongo
    ```

3. Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

## Setup

1. Set up your MongoDB Atlas account and cluster. Create a database named `ytmanager` and a collection named `videos`.
2. Replace the `{REPLACEUSERNAME}` and `{REPLACEPASSWORD}` placeholders in the connection string with your actual MongoDB username and password.

## Usage

1. Run the script:
    ```bash
    python youtube_manager.py
    ```

2. Follow the on-screen prompts to manage your YouTube videos.

## Example

```bash
YouTube Video Manager App
1. List all videos
2. Add a new video
3. Update a video
4. Delete a video
5. Exit the app

Enter your choice: 1

**********************************************************************
Id: 60d5f9b0c8c3a72c2c63f214, Name: Video1, Duration: 10:00
Id: 60d5f9b0c8c3a72c2c63f215, Name: Video2, Duration: 15:30
**********************************************************************
