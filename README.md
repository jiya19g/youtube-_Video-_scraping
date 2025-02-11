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

    Requirements
    To run this script, ensure you have the following installed:
    1. Python  Make sure you have Python 3.x installed. You can check your version with:  python --version
    

If not installed, download it from [python.org](https://www.python.org/downloads/).

### 2\. Google Chrome

The script uses **Selenium WebDriver** with Chrome, so you must have Google Chrome installed and updated. Check your Chrome version:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`google-chrome --version # On Linux/macOS

chrome --version # On Windows (Command Prompt)` 

Download/update Chrome from google.com/chrome.

### 3\. ChromeDriver

Ensure ChromeDriver matches your installed Chrome version. The script automatically installs and manages the correct version using webdriver-manager, but if needed, you can install/update manually:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`pip install --upgrade webdriver-manager` 

### 4\. Required Python Libraries

Install the dependencies using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`pip install selenium webdriver-manager` 

### 5\. Stable Internet Connection

Since the script interacts with YouTube dynamically, ensure you have a **stable internet connection** to avoid timeouts or incomplete data scraping.

### 6\. Permissions (Linux/macOS)

If running on **Linux/macOS**, you might need to give executable permissions to ChromeDriver:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`chmod +x /path/to/chromedriver` 

After fulfilling these requirements, you are ready to run the script!

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




