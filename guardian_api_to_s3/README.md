# 📰 Guardian API Scraper & S3 Data Pipeline

This project scrapes article data from **The Guardian Open Platform API**, filters content related to *Nigeria*, transforms the results into a structured format, and stores the data in **Amazon S3** in Parquet format.

---

## ✨ Features

- Fetches news articles using The Guardian’s public API
- Filters articles that mention *Nigeria* (case insensitive)
- Converts the extracted data into a tabular DataFrame
- Saves the final dataset in **Parquet** format in an **S3 bucket**
- Utilises environment variables for sensitive credentials
- Designed for scalability via pagination support

---

## 🛠 Requirements

- Python 3.8+
- AWS Account & S3 bucket
- Guardian API Key (free registration at [open-platform.theguardian.com](https://open-platform.theguardian.com/))
- Python packages:
  - `requests`
  - `pandas`
  - `boto3`
  - `awswrangler`
  - `python-dotenv`

### 📦 Installation

```bash
pip install requests pandas boto3 awswrangler python-dotenv

## 🚀 How It Works

1. **Scrape Data from The Guardian**  
   The `guardian_scrapper(pages)` function sends paginated API requests and filters articles containing the keyword `"Nigeria"` (case insensitive). The data is collected and returned as a list of dictionaries.

2. **Convert Data into a DataFrame**  
   The `convert_results_to_df()` function extracts article titles and URLs, and structures them into a Pandas DataFrame.

3. **Upload to Amazon S3**  
   The resulting DataFrame is uploaded to the specified S3 bucket using `awswrangler` and saved in Parquet format.


