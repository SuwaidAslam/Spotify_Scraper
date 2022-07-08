# Spotify Web Scraper
Tool to scrape the Spotify web interface to extract all tracks information. Tracks are search based on some keywords.

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![pythonbadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This scraper will extract data about each track in bulk and save it to CSV file: 

- **Rank Number of the Track in the Search List**

- **Track Image**

- **Track Name**

- **Artists Names**

- **Artists Profile Links**

- **Album Name of the Track**

- **Album Link**

- **Length of the Track**

- **Track Link**


## Getting started

- These are the 2 parameters you will be asked when you run the script. The first parameter is where you enter your keywords like 'selena gomez songs' and the second parameter is to specify how many songs data would you like extract.
- When you run the script, a browser will open up, and you can see all the automation that is taking place to scrap the data. You can minimize the browser window if you want, but make sure you do not close it. It will be automatically closed when the script has done scraping all the songs.
- When the script is running make sure you do not use your clipboard (ctrl + C and ctrl V) because if you copy anything while the script is running, it will be written in the link of the song. The script works by clicking on each song and copying the link to that song in the clipboard and pasting that into CSV. So, if you try to use the copy, paste feature while the script is running that copied thing will be pasted in CSV instead of the link of the song.
- You can do other stuff in the background while the script is running but you cannot use the copy, paste feature.


# How to Run 
Source code file is provided. If you want to have a look at the code you can open spotify_scaper.py file. But to run 
it you will have to have python and dependencies (requirements.txt file) installed.

- Clone the repository
- Setup Virtual environment
```
$ python3 -m venv env
```
- Activate the virtual environment
```
$ source env/Source/activate
```
- Install dependencies using
```
$ pip install -r requirements.txt
```
- Chrome browser must be installed (103 version)
- Make sure you add your Spotify account credentials in the script
- Run the script and enter keywords and number of tracks you want to scrape

## Contact

For any feedback or queries, please reach out to me at [suwaidaslam@gmail.com](suwaidaslam@gmail.com).
