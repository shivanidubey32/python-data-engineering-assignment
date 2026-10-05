# Python Data Engineering Assignment

## 📌 Project Overview

This project demonstrates a simple **data collection and processing pipeline using Python**.

The project collects:

* User data from a REST API
* Book data through web scraping
* Processes and cleans the collected data
* Stores the data in JSON files
* Performs basic data analysis
* Generates a combined report

The project was developed as part of a **Python for Data Engineering** assignment.

---

## 🎯 Objectives

The main objectives of this project are:

* Work with JSON data using Python
* Consume data from REST APIs
* Perform web scraping using BeautifulSoup
* Clean and transform collected data
* Store processed data in JSON files
* Perform basic data analysis
* Build a simple end-to-end data collection pipeline

---

## 🛠️ Technologies Used

* **Python 3**
* **Requests** – API requests and website access
* **BeautifulSoup4** – Web scraping
* **JSON** – Data storage and processing
* **Git & GitHub** – Version control

---

## 📂 Project Structure

```text
python-data-engineering-assignment/
│
├── api_data.py
├── web_scraping.py
├── json_processing.py
├── analysis.py
│
├── users.json
├── books.json
├── report.json
│
└── README.md
```

### File Description

| File                 | Description                                          |
| -------------------- | ---------------------------------------------------- |
| `api_data.py`        | Fetches user data from the REST API and processes it |
| `web_scraping.py`    | Scrapes book information from Books to Scrape        |
| `json_processing.py` | Loads JSON files and generates a combined report     |
| `analysis.py`        | Performs user and book data analysis                 |
| `users.json`         | Processed user data collected from the API           |
| `books.json`         | Book data collected through web scraping             |
| `report.json`        | Combined report containing important statistics      |
| `README.md`          | Project documentation                                |

---

## 🔗 Data Sources

### User API

The project uses JSONPlaceholder:

```text
https://jsonplaceholder.typicode.com/users
```

The API provides user information such as:

* Name
* Username
* Email
* Company

### Book Website

Book information is collected from:

```text
https://books.toscrape.com
```

The scraper collects:

* Book title
* Price
* Rating

At least **20 books** are collected.

---

## ⚙️ Installation

Make sure Python 3 is installed.

Install the required Python libraries:

```bash
python -m pip install requests beautifulsoup4
```

---

## ▶️ How to Run the Project

### 1. Collect User Data

Run:

```bash
python api_data.py
```

This fetches user data from the API and creates:

```text
users.json
```

The script also displays:

* Total number of users
* User names
* Usernames
* Emails
* Company names

---

### 2. Scrape Book Data

Run:

```bash
python web_scraping.py
```

The scraper collects at least 20 books and extracts:

* Title
* Price
* Rating

Ratings are converted from words to numbers:

```text
One   → 1
Two   → 2
Three → 3
Four  → 4
Five  → 5
```

The processed data is saved in:

```text
books.json
```

The program also calculates:

* Most expensive book
* Least expensive book
* Average book price

---

### 3. Process JSON Data

Run:

```bash
python json_processing.py
```

This program:

* Loads `users.json`
* Loads `books.json`
* Counts total users
* Counts total books
* Displays books with rating greater than 4
* Finds users belonging to companies containing `"Group"`
* Calculates the average book price

It generates:

```text
report.json
```

Example report structure:

```json
{
    "total_users": 10,
    "total_books": 20,
    "average_price": 35.50
}
```

---

### 4. Perform Data Analysis

Run:

```bash
python analysis.py
```

The analysis includes:

### User Analysis

* Total users
* Number of unique companies
* Top 5 companies alphabetically

### Book Analysis

* Average book price
* Highest-rated books
* Number of books in each rating category

Example:

```text
USER ANALYSIS
----------------------------------------
Total Users: 10
Unique Companies: 10

Top 5 Companies Alphabetically:
Company A
Company B
Company C
...
```

---

## 🔄 Data Pipeline

The overall workflow is:

```text
             REST API
                │
                ▼
          api_data.py
                │
                ▼
           users.json
                │
                │
                │
Books Website ──┤
                ▼
        web_scraping.py
                │
                ▼
           books.json
                │
                ▼
       json_processing.py
                │
                ▼
           report.json
                │
                ▼
          analysis.py
                │
                ▼
        Analysis Results
```

---

## 📊 Data Processing

### User Data

The original API contains detailed user information.

The project processes each user into:

```json
{
    "name": "User Name",
    "email": "user@example.com",
    "company": "Company Name"
}
```

### Book Data

Each scraped book is stored as:

```json
{
    "title": "Book Name",
    "price": "£45.17",
    "rating": 4
}
```

---

## 📈 Analysis Performed

The project performs the following calculations:

### User Data

* Total number of users
* Unique companies
* Top 5 companies alphabetically
* Users associated with companies containing `"Group"`

### Book Data

* Average book price
* Most expensive book
* Least expensive book
* Highest-rated books
* Number of books for each rating from 1 to 5

---

## 🧹 Data Cleaning

The scraped book price may contain encoding characters around the pound symbol.

The project cleans the price before performing numerical calculations so that values such as:

```text
£51.77
```

can be converted into:

```text
51.77
```

for analysis.

---

## 💡 Key Python Concepts Demonstrated

This project demonstrates practical usage of:

* Functions
* Lists
* Dictionaries
* Sets
* Loops
* Conditional statements
* Exception handling
* File handling
* JSON processing
* REST API requests
* Web scraping
* Data cleaning
* Lambda functions
* Sorting
* Basic data analysis

---

## 🚀 Future Improvements

Possible improvements include:

* Add a menu-driven program
* Scrape more than 20 books
* Add logging
* Add automated error handling and retries
* Store data in a database
* Add Pandas-based analysis
* Schedule the pipeline using a job scheduler
* Add automated tests
* Create visualizations using Matplotlib
* Deploy the pipeline to a cloud platform

---

## 👩‍💻 Author

**Shivani Dubey**

GitHub: [shivanidubey32](https://github.com/shivanidubey32)

---

## 📄 License

This project was created for educational and academic purposes.
