# Amazon Prime Video Scraper

This project is a web scraping tool designed to extract video data from Amazon Prime Video using Selenium and BeautifulSoup. The extracted data includes video titles, ratings, and synopses, which are then saved to a CSV file. Additionally, word clouds are generated based on the synopses of videos with different rating ranges.

## Features

- **Web Scraping**: Extract video titles, ratings, and synopses from Amazon Prime Video.
- **Data Cleaning**: Handle missing or malformed data.
- **CSV Export**: Save the scraped data into a CSV file.
- **Word Cloud Generation**: Create word clouds for video synopses based on rating ranges.

## Installation

### Prerequisites

- Python 3.x
- Chrome WebDriver
- Selenium
- BeautifulSoup
- pandas
- matplotlib
- wordcloud

### Install Required Libraries

```bash
pip install selenium beautifulsoup4 pandas matplotlib wordcloud
