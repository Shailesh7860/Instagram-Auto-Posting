# Instagram Auto Posting

## Overview
This Python script automates posting images to Instagram using the `Instabot` library. It is designed for users who want to upload multiple images over time without manual intervention.

## Features
- **Automated Posting**: Uploads images sequentially from a specified folder.
- **Customizable Schedule**: Posts an image every hour (adjustable via `time.sleep`).
- **Bulk Upload Support**: Designed to handle hundreds of images.
- **Auto Login**: Logs into Instagram automatically before posting.
- **Safe Execution**: Deletes old session files to avoid login issues.

## Installation
Ensure Python is installed, then install the required package:

```bash
pip install instabot
```

## Usage
1. Place all images in the `images/` folder.
2. Ensure images are named sequentially (`1.jpg`, `2.jpg`, `3.jpg`, etc.).
3. Modify the script with your Instagram **username** and **password**.
4. Run the script:

```bash
python auto_post.py
```

## Configuration
- The script will **post up to 149 images**.
- Images are uploaded from the `images/` directory.
- The script **waits 1 hour** between each post (can be adjusted in `time.sleep(3600)`).
- Captions can be modified inside the `bot.upload_photo` function.

## Notes
- Make sure to replace `<username>` and `<password>` with your actual Instagram credentials.
- Running automation on Instagram may violate Instagram’s terms of service; use it responsibly.

## License
This project is open-source under the MIT License.

---
