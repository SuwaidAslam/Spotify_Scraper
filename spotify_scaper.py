import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk

# Enter your spotify account credidentials here
email = "yopem79209@jrvps.com"
password = "damnbro101"

query = input("Input Keywords: ")

class DriverOptions(object):

    def __init__(self):

        self.options = Options()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        self.options.add_argument('--log-level=3')
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        prefs = {"credentials_enable_service": False,
        "profile.password_manager_enabled": False}
        self.options.add_experimental_option("prefs", prefs)
        self.options.add_argument("disable-infobars")


class WebDriver(DriverOptions):

    def __init__(self, path=''):
        DriverOptions.__init__(self)
        self.driver_instance = self.get_driver()

    def get_driver(self):
        webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

        path = 'chromedriver.exe'
        s=Service(path)
        driver = webdriver.Chrome(service=s, options=self.options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source":
                "const newProto = navigator.__proto__;"
                "delete newProto.webdriver;"
                "navigator.__proto__ = newProto;"
        })
        return driver

def main():
    # number of songs to scrap from a page
    songCountLimit = int(input("How many songs would you like to scrap?: "))

    driver= WebDriver()
    driverinstance = driver.driver_instance
    root = tk.Tk()
    root.withdraw()  # to hide the window
    
    numbers_list = []
    track_images_list = []
    tracks_list = []
    artists_list = []
    artists_links_list = []
    albums_name = []
    albums_link = []
    lengths_list = []
    links_list = []

    driverinstance.get('https://accounts.spotify.com/en/login')
    time.sleep(0.5)

    user_name_entry = driverinstance.find_element(by=By.ID, value="login-username")
    password_entry = driverinstance.find_element(by=By.ID, value="login-password")
    login_btn = driverinstance.find_element(by=By.ID, value="login-button")

    user_name_entry.send_keys(email)
    password_entry.send_keys(password)
    login_btn.click()
    time.sleep(8)

    # search in tracks for specifies keywords
    search_url = 'https://open.spotify.com/search/' + query + '/tracks'
    driverinstance.get(search_url)
    time.sleep(10)

    scroll_box = driverinstance.find_element(By.XPATH, value="/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div")
    time.sleep(2)

    songs_list = scroll_box.find_element(by=By.XPATH, value='/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main')
    first_song = songs_list.find_element(by=By.CLASS_NAME, value='h4HgbO_Uu1JYg5UGANeQ')

    ActionChains(driverinstance).click(first_song).perform()

    scroll_bar = driverinstance.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[3]/div[1]/div[2]/div[4]/div/div')
    scroll_bar_location = scroll_bar.location['y']

    songsCount = 0
    print('\tScraping in Progress...')

    # scrap song one by one | Loop ends when the limit of required songs reached OR Songs are no more left to scroll
    while songsCount < songCountLimit:

        active_elm = driverinstance.switch_to.active_element
        grand_parent = active_elm.find_element(By.XPATH, "../..")
        song = grand_parent.find_element(By.XPATH, "./..")

        number = song.find_element(by=By.CLASS_NAME, value='VrRwdIZO0sRX1lsWxJBe').get_attribute('innerText')
        track_image = song.find_element(by=By.CLASS_NAME, value='gvLrgQXBFVW6m9MscfFA').find_element(By.TAG_NAME, 'img').get_attribute('src')
        track = song.find_element(by=By.CLASS_NAME, value='t_yrXoUO3qGsJS4Y6iXX').get_attribute('innerText')
        artists = song.find_element(by=By.CLASS_NAME, value='rq2VQ5mb9SDAFWbBIUIn').find_elements(By.TAG_NAME, 'a')
        artist_name = []
        artist_link = []
        for artist in artists:
            artist_name.append(artist.get_attribute('innerText'))
            artist_link.append(artist.get_attribute('href'))

        album = song.find_element(by=By.CLASS_NAME, value='bfQ2S9bMXr_kJjqEfcwA').find_element(by=By.TAG_NAME, value='span').find_element(by=By.TAG_NAME, value='a')
        album_name = album.get_attribute('innerText')
        album_link = album.get_attribute('href')
        length = song.find_element(by=By.CLASS_NAME, value='Btg2qHSuepFGBG6X0yEN').get_attribute('innerText')


        numbers_list.append(number)
        track_images_list.append(track_image)
        tracks_list.append(track)
        artists_list.append(artist_name)
        artists_links_list.append(artist_link)
        albums_name.append(album_name)
        albums_link.append(album_link)
        lengths_list.append(length)

        try:
            ActionChains(driverinstance).context_click(song).perform()
            for times in range(0,8):
                ActionChains(driverinstance).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.2)
            ActionChains(driverinstance).send_keys(Keys.ARROW_RIGHT).send_keys(Keys.RETURN).perform()
            time.sleep(0.1)
            link = root.clipboard_get()
            links_list.append(link)
        except:
            links_list.append('Null')

        time.sleep(0.7)
        driverinstance.execute_script("arguments[0].scrollBy(0, 35);", scroll_box)
        ActionChains(driverinstance).send_keys(Keys.ARROW_DOWN).perform()
        scroll_bar_newLoc = scroll_bar.location['y']
        if scroll_bar_newLoc == scroll_bar_location:
            break
        scroll_bar_location = scroll_bar_newLoc
        songsCount+=1
    driverinstance.quit() #closes entire browser

    print('\tScraping Done!')

    songs_data = {'Number' : numbers_list, 'Track_Image_Link': track_images_list, 'Track' : tracks_list, 
                'Artist_name' : artists_list, 'Artist_Link': artists_links_list,
                'Album_Name': albums_name, 'Album_link': albums_link, 'Length' : lengths_list, 'Track_link' : links_list}
                
    df = pd.DataFrame(songs_data)
    # Exporting the DataFrame as csv
    df.to_csv(query+'.csv', index=False)

    print('\tData Saved to CSV file!')

if __name__ == "__main__":
    main()