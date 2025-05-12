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
