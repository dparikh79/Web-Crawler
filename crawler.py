import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import re
from langdetect import detect
from collections import deque
import time
from fpdf import FPDF

def get_all_links(url):
    # Return all links from the given URL
    primary_domain = urlparse(url).netloc  # Extract the primary domain from the provided URL
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(url, a_tag["href"])
            # Check if the link's domain matches the primary domain
            if urlparse(link).netloc == primary_domain:
                yield link
    except requests.RequestException as e:
        print(f"Error fetching links from {url}: {e}")

def scrape_content(url):
    # Scrape content from the given URL
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Get the text content and replace multiple white spaces with a single space
        content = re.sub(r'\s+', ' ', soup.get_text().strip())
        
        # Check if the content is in English
        if detect(content) == 'en':
            return content
        else:
            print(f"Content from {url} is not in English.")
            return None
    except requests.RequestException as e:
        print(f"Error scraping content from {url}: {e}")
        return None

def sanitize_content(content):
    # Retain alphabetic characters, numbers, spaces, and basic punctuation
    sanitized = re.sub(r'[^a-zA-Z0-9\s.,;?!()-]', '', content)
    return sanitized

def save_to_pdf(data, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in data:
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

def main(start_url, duration=30):
    start_time = time.time()
    visited = set()
    to_visit = deque([start_url])
    crawled_data = []

    while to_visit and (time.time() - start_time) < duration:
        current_url = to_visit.popleft()
        if current_url not in visited:
            visited.add(current_url)
            print(f"Visiting: {current_url}")
            content = scrape_content(current_url)
            if content:
                sanitized_content = sanitize_content(content)
                crawled_data.append(f"URL: {current_url}\nContent: {sanitized_content}\n{'-'*50}\n")
            for link in get_all_links(current_url):
                to_visit.append(link)

    # Save the crawled data to a PDF
    save_to_pdf(crawled_data)

if __name__ == "__main__":
    start_url = "https://www.northeastern.edu/"
    # start_url = "https://www.upsworld.net/"
    main(start_url)