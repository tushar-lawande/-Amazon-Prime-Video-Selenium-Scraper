from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# CSS Variables
titleClass = "h1"
titleName = "_1GTSsh _2Q73m9"
ratingClass = "span"
ratingName = "XqYSS8 AtzNiv"
synopsisClass = "div"
synopsisName = "_3qsVvm _1wxob_"

storeFrontURL = "https://www.amazon.com/gp/video/storefront/"
vidDownloadURL = "/gp/video/detail/"

videoLinks = []
titles = []
ratings = []
synopsis = []

def scrapeText(lst, classType, className, is_rating=False):
    findClass = soup.find_all(classType, class_=className)
    if len(findClass) == 0:
        lst.append(None)
    else:
        for n in findClass:
            if is_rating:
                try:
                    rating = float(n.text[-3:])
                    lst.append(rating)
                except ValueError:
                    lst.append(None)
            else:
                lst.append(n.text.strip())

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/CORRE COMP/Downloads/chromedriver-win64/chromedriver.exe"

# Initialize the ChromeDriver service
service = ChromeService(executable_path=chrome_driver_path)

# Initialize the Chrome browser with the service
driver = webdriver.Chrome(service=service)

driver.get(storeFrontURL)

elems = driver.find_elements(By.XPATH, "//a[@href]")
for elem in elems:
    if vidDownloadURL in elem.get_attribute("href"):
        videoLinks.append(elem.get_attribute("href"))

videoLinks = list(dict.fromkeys(videoLinks))

for i in range(len(videoLinks)):
    driver.get(videoLinks[i])
    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    scrapeText(titles, titleClass, titleName)
    scrapeText(ratings, ratingClass, ratingName, is_rating=True)
    scrapeText(synopsis, synopsisClass, synopsisName)

data = {'Title': titles, 'Rating': ratings, 'Synopsis': synopsis}
df = pd.DataFrame(data)
df.to_csv('PrimeVid.csv', index=False, encoding='utf-8')

def wordcloud(df, filename):
    if len(df) > 0:
        text = ' '.join(df['Synopsis'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")

        plt.savefig(filename + ".png")
        plt.close()

dfBelow6 = df[df['Rating'] < 6]
df6To7 = df[(df['Rating'] >= 6) & (df['Rating'] < 8)]
dfAbove8 = df[df['Rating'] >= 8]

wordcloud(dfBelow6, "below6")
wordcloud(df6To7, "6to7")
wordcloud(dfAbove8, "above8")

driver.quit()
