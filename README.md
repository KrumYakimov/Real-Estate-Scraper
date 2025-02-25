
# Real Estate Scraper

This Python script scrapes real estate price data for **all cities** from [imot.bg](https://www.imot.bg/pcgi/imot.cgi?act=14).  
It saves the results in a **CSV file**, making it easy to analyze trends in the real estate market.  

---

## ⚙️ Tech Stack
- **Language:** Python 3.11+
- **Libraries:** `requests`, `BeautifulSoup`, `pandas`
- **Data Format:** CSV
- **Automation:** `cron` (Linux/macOS), Task Scheduler (Windows)
- **Deployment:** Can be run locally or automated with cloud services

---

##  Features
- Scrapes real estate price data for **all cities** in imot.bg 
- Saves results as **CSV files**  
- Can be **automated with `cron` (Linux/macOS) or Task Scheduler (Windows)**  
- Uses **BeautifulSoup** for web scraping  
- Works in **Python 3.11+**  

---

## Installation

### **1. Clone the Repository**
First, download the project to your local machine:
```sh
git clone https://github.com/KrumYakimov/Real-Estate-Scraper.git
cd real-estate-scraper
```

### **2. Install Dependencies**
Make sure you have Python **3.11+**, then install the required libraries:
```sh
pip install -r requirements.txt
```

### **3. Run the Scraper**
To scrape data for **all cities**, run:
```sh
python scraper.py
```

---

## 📂 Output (Saved Data)

The script downloads real estate data **for the date when it is run**.  

| Date       | City  | District | 1-Bedroom Price | 1-Bedroom Price/m² | 2-Bedroom Price | 2-Bedroom Price/m² | 3-Bedroom Price | 3-Bedroom Price/m² | Link                                                                                                                                                    |
|------------|-------|----------|-----------------|--------------------|-----------------|--------------------|-----------------|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 25.02.2025 | София | Бъкстон  | 120,000         | 2,000              | 180,000         | 1,800              | 250,000         | 1,700              | [View](https://www.imot.bg//pcgi/imot.cgi?act=14&actions=2&pn=0&town=София&craion=Бъкстон&year=2025&date=25.2.2025&pt=1~2~3~~&nr=43~43~43~~&cr=7~7~7~~) |

### **Saved file format**:
```
real_estate_prices_YYYYMMDD.csv
```
Example: If the script is run on **March 1, 2025**, the file will be:
```
real_estate_prices_20250301.csv
```

---

## ⚙️ **Automating the Script**

You can schedule the script to **run automatically every day**.  

### **Linux & macOS (Using `cron`)**
1. Open a terminal and edit your `crontab`:
   ```sh
   crontab -e
   ```
2. Add the following line to schedule the script **every day at 03:30** (change the time as needed):
   ```sh
   30 3 * * * /path/to/python /path/to/scraper.py >> /path/to/logs/scraper.log 2>&1
   ```
   - `/path/to/python` → Path to your Python interpreter (e.g., `/usr/bin/python3` or from a virtual environment).  
   - `/path/to/scraper.py` → Full path to `scraper.py`.  
   - `/path/to/logs/scraper.log` → Optional log file to track execution.


### **Windows (Using Task Scheduler)**
1. Open **Task Scheduler** (`Win + R`, then type `taskschd.msc` and press `Enter`).
2. Click **Create Basic Task** → Give it a name (e.g., `RealEstateScraper`).
3. **Trigger**: Choose **Daily** and set the time (e.g., 03:30).
4. **Action**: Select **Start a program**.
5. **Browse to Python executable**:
   - If using Anaconda:  
     ```
     C:\path\to\anaconda\envs\myenv\python.exe
     ```
   - If using standard Python:  
     ```
     C:\path\to\python.exe
     ```
6. **Add arguments**:  
   ```
   C:\path\to\real-estate-scraper\scraper.py
   ```
7. Click **Finish**.  

**Now the script will run automatically every day at 03:30!**

---

## Want More Automation?
If you need **database storage, API integration, or advanced analytics**, feel free to reach out!  

Contact me via **GitHub Issues** or email: **krum.yakimov@gmail.com**  
Let's build something great together! 

---

## License
This project is open-source under the **MIT License**.