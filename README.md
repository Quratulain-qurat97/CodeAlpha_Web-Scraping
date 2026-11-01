# Job Listings Web Scraper

A Python web scraping project that collects job listing information from a publicly accessible demo website using Requests, BeautifulSoup, and Pandas.

## Project Overview

This project extracts job listing information from the [Fake Python Jobs](https://realpython.github.io/fake-jobs/) website and organizes it into a structured dataset.

The purpose of this project is to practice web scraping, HTML parsing, data extraction, data cleaning, and CSV export using Python.

**Note:** The website contains fictional job listings created for web scraping practice. This dataset does not represent real job vacancies.

## Technologies Used

- Python
- Requests – Fetch webpage HTML.
- BeautifulSoup – Parse HTML and extract information.
- Pandas – Organize and export the extracted data.

## Data Collected

The scraper extracts four fields:

| Field | Description |
|---|---|
| Job Title | Position advertised |
| Company | Company name |
| Location | Job location |
| Posting Date | Date of the listing |

## Dataset Summary

The scraper successfully collected **100 job listings**.

| Metric | Result |
|---|---:|
| Total job listings | 100 |
| Unique companies | 99 |
| Unique job titles | 92 |
| Unique locations | 100 |
| Missing values | 0 |
| Duplicate rows | 0 |

All listings on the demo page have the posting date `2021-04-08`.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd YOUR_REPOSITORY_FOLDER
```

### 3. Install the required libraries

```bash
python -m pip install requests beautifulsoup4 pandas
```

### 4. Run the scraper

```bash
python scraper.py
```

The script will extract the job listings, perform basic data quality checks, display a dataset summary, and export the results to `jobs.csv`.

## Project Files

- `scraper.py` – Main Python web scraping script.
- `jobs.csv` – Extracted job listings dataset.
- `README.md` – Project documentation.

## Learning Outcomes

Through this project, I practiced:

- Sending HTTP requests using Requests.
- Understanding and inspecting HTML elements.
- Extracting webpage data using BeautifulSoup.
- Combining extracted information using Python.
- Creating structured datasets with Pandas.
- Performing basic data quality checks.
- Exporting data into CSV format.

---

**Project:** CodeAlpha Internship – Task 1: Web Scraping

**Author:** [Your GitHub Profile](https://github.com/Quratulain-qurat97)
