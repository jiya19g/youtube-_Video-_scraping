from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


# Setting up WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def save_data(data, filename, file_type):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['title', 'video_Url', 'description', 'channel_title', 'keywords_tag', 'video_publish_at', 'video_duration', 'views', 'commets', 'caption', 'caption_avail', 'location', 'video_category', 'topic_details']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        

genre = "music"
def video(genre):
    driver.get('https://www.youtube.com/')
    time.sleep(2)
    search = driver.find_element(By.XPATH,'//*[@id="center"]/yt-searchbox/div[1]/form/input')   
    search.send_keys(genre)
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    data=[]
    # Scroll to the bottom of the page
    
    for i in range(30):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)

    videos = driver.find_elements(By.XPATH,'//div[@id="title-wrapper"][@class="style-scope ytd-video-renderer"]')
    
    for video in videos:
        try:
            title = video.find_element(By.XPATH, './/*[@id="video-title"]/yt-formatted-string').text
        except:
            title = "Not available"
         
        video_Url = driver.find_element(By.LINK_TEXT, title).get_attribute('href')
        driver.execute_script("window.open(arguments[0]);", video_Url)
        driver.switch_to.window(driver.window_handles[1])
        try:
            # to skip ads
            ads = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="ytp-skip-ad-button"]')))
            ads.click()
        except:
            pass
            #to stop the video
        videostop = driver.find_element(By.XPATH, '//*[@id="movie_player"]')
        videostop.send_keys(Keys.SPACE)
        for i in range(2):
            driver.execute_script("window.scrollBy(0, 500)")
            time.sleep(2)

        try:
            description = driver.find_element(By.XPATH, '//*[@id="description-inline-expander"]').text
        except:
            description = "Not available"
        try:
            channel_title = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a').text
        except:
            channel_title = "Not available"
        try:
            keywords_tag = driver.find_element(By.XPATH, '//*[@id="description-inline-expander"]/yt-attributed-string/span/span[10]/a').text
        except:
            keywords_tag = "Not available"
        try:
            video_category = driver.find_element(By.XPATH, '//*[@id="microformat"]/player-microformat-renderer/script').get_property('genre')
        except:
            video_category = "Not available"
        try:
            topic_details = driver.find_element(By.XPATH, '//*[@id="description-inline-expander"]/yt-attributed-string/span/span[1]').text
        except:
            topic_details = "Not available"
        try:
            video_publish_at = driver.find_element(By.XPATH, '//*[@id="info"]/span[3]').text
        except:
            video_publish_at = "Not available"
        try:
            video_duration = driver.find_element(By.XPATH, '//span[@class="ytp-time-duration"]').text
        except:
            video_duration = "Not available"
        try:
            views = driver.find_element(By.XPATH, '//*[@id="info"]/span[1]').text.strip()
        except:
            views = "Not available"
        try:
            commets = driver.find_element(By.XPATH, '//*[@id="count"]/yt-formatted-string/span[1]').text
        except:
            commets = "Not available"

        try:
            caption = driver.find_element(By.XPATH, '//yt-formatted-string[@id="description-text"]').text
        except:
            caption = "Not available"
            
        try:
            location = driver.find_element(By.XPATH, '//yt-formatted-string[@id="description-text"]').text
        except:     
            location = "Not available"

        if caption != "Not available":
            caption_avail = "Yes"
        else:
            caption_avail = "No"
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        
        
           
        data.append({
            'title': title,
            'video_Url': video_Url,
            'description': description,
            'channel_title': channel_title,
            'keywords_tag': keywords_tag,
            'video_publish_at': video_publish_at,
            'video_duration': video_duration,
            'views': views,
            'commets': commets,
            'caption': caption,
            'caption_avail': caption_avail,
            'location': location,
            'video_category': video_category,
            'topic_details': topic_details,
        })  
        save_data(data,'yt_data.csv', 'csv')
    driver.quit()  
      
def main():
    video(genre)      

if __name__ == '__main__':
    main()