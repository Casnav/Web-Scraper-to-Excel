# Web-Scraper-to-Excel
This project is a combination of Python and Scrapy to extract book data from a real website. Including web scraping, data cleaning, and converting the results from CSV to XLSX format. The goal is to demonstrate how to automate data extraction and prepare it for analysis or reporting.


## Technologies
- Python 3.14
- Scrapy 2.14
- Pandas
- OpenPyXL

## How to use
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run: `scrapy crawl scrape_ex -o books.csv`
4. Convert to Excel: `python convert.py`
