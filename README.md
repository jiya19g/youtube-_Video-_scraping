# youtube-_Video-_scraping


This script automates YouTube searches for a given genre, extracts video details, and saves the data in a CSV file.

## Features
- Searches YouTube for videos based on a specified genre.
- Extracts details such as title, URL, description, channel name, keywords, category, views, comments, etc.
- Saves the extracted data into a CSV file.

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
- To change the genre, modify the `video("games")` call in `main()`.
- Ensure Chrome is installed and up to date for WebDriver compatibility.




