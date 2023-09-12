# Web-Crawler

A Scrapy project designed to scrape data from websites with various advanced features such as respecting `robots.txt`, handling CAPTCHAs, rotating user agents, proxy rotation, and more.

## Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/dmp1999/Web-Crawler.git
    cd Web-Crawler

2. **Set Up a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  
    
On Windows, use `venv\Scripts\activate`

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Configuration:**
Rename the `.env.sample` to `.env` and update the configurations as needed.

## Features
- Respects robots.txt.
- Handles CAPTCHAs using the 2Captcha service.
- Rotates user agents.
- Uses proxy rotation to avoid IP bans.
- Stores scraped data in both an SQLite database and as PDF files.
- Allows setting a custom depth limit for crawling.
- Allows setting a custom timeout duration for requests.
- Allows setting a custom duration after which the spider stops crawling.

## Running the Spider with Custom Depth Limit
To set a custom depth limit for the spider, use the following command:

    scrapy crawl advanced_spider -a depth_limit=YOUR_DEPTH_LIMIT

Replace YOUR_DEPTH_LIMIT with the desired depth limit value.

## Running the Spider with Custom Timeout:
To set a custom timeout duration for the spider, use the following command:

    scrapy crawl advanced_spider -a timeout=YOUR_TIMEOUT_DURATION
    
Replace YOUR_TIMEOUT_DURATION with the desired timeout duration in seconds.

## Running the Spider with Custom Crawl Duration:
To set a custom duration after which the spider stops crawling, use the following command:

    scrapy crawl advanced_spider -a crawl_duration=YOUR_CRAWL_DURATION
    
Replace YOUR_CRAWL_DURATION with the desired duration in minutes.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Licensing
The code in this project is licensed under MIT license.