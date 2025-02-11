# youtube-_Video-_scraping

This script automates YouTube searches for a given genre, extracts video details, and saves the data in a CSV file. It uses **Selenium WebDriver** to interact with YouTube and scrape video metadata.

## Features
- Searches YouTube for videos based on a specified keyword.
- Extracts details such as:
  - Video Title
  - Video URL
  - Description
  - Channel Name
  - Keywords
  - Category
  - Publish Date
  - Duration
  - Views
  - Comments
  - Captions (if available)
  - Location (if available)
  - Topic Details
- Saves the extracted data into a CSV file (`yt_data.csv`).

## Requirements
- Python 3.x
- Google Chrome installed
- Required Python libraries:
  ```
  pip install selenium webdriver-manager

## Usage
### Clone the repository:
```
git clone https://github.com/yourusername/youtube-video-scraper.git
cd youtube-video-scraper
```
### Run the script:
```
python script.py
```
## How It Works
- Opens YouTube and searches for a given genre or keyword.  
- Scrolls down the search results page to load more videos.  
- Extracts video details by opening each video's page.  
- Skips advertisements automatically (if detected).  
- Stops the video from playing to prevent interference.  
- Extracts metadata and saves it in a structured CSV format.  
- Closes the browser session once the data collection is complete.  

## File Output
The extracted data is saved as `yt_data.csv` with the following columns:

- `title`
- `video_Url`
- `description`
- `channel_title`
- `keywords_tag`
- `video_publish_at`
- `video_duration`
- `views`
- `commets`
- `caption`
- `caption_avail`
- `location`
- `video_category`
- `topic_details`

## Notes
- The script scrolls through the YouTube search results to load more videos.  
- To change the search keyword, modify the `video("games")` call in `main()`.  
- Ensure Google Chrome is installed and updated for WebDriver compatibility.  
- The script uses Selenium WebDriver to navigate YouTube, so a stable internet connection is recommended.  
- Due to YouTube's dynamic structure, some elements may change over time, requiring updates to XPaths.  

## Troubleshooting
- If the script fails to locate elements, check if YouTube's UI has changed.  
- Ensure ChromeDriver matches the installed Chrome version.  
- If encountering `SessionNotCreatedException`, update ChromeDriver using:  
```
pip install --upgrade webdriver-manager




