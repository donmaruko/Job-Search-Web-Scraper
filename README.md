# Job-Search-Web-Scraper
This Python web scraper extracts job listings from TimesJobs, applying user-defined skill filters to exclude roles requiring unfamiliar skills. It saves matching job details to text files.

## Purpose
This Python script is a web scraper designed to help you find job listings that match specific skills and filter out listings that require skills you're not familiar with. It uses web scraping techniques to extract job listings from a job search website (TimesJobs in this case), filters them based on your specified skills, and saves the relevant job details to individual text files.

## How It Works
1. **Setup**: Make sure you have Python installed on your system. You can also install the required libraries by running `pip install -r requirements.txt`.

2. **Run the Script**: Execute the `job_scraper.py` script.

3. **Enter Unfamiliar Skills**: You will be prompted to enter a list of skills you're not familiar with, separated by commas. These skills will be used as filters to exclude job listings that require them.

4. **Scraping**: The script will then access the TimesJobs website and scrape job listings related to Python.

5. **Filtering**: It filters the job listings based on the skills you provided earlier. Any job listing that requires at least one of the unfamiliar skills will be excluded.

6. **Output**: Relevant job listings are saved to individual text files in a directory named `PYTHON/Practice/Scraper/`. Each text file contains the following information:
   - Company Name
   - Required Skills
   - More Info (URL)
   - Filter(s) Applied (Skills you're not familiar with)

7. **Repeat**: The script runs continuously, periodically checking for new job listings and saving them to new text files. It waits for a specified amount of time (default: 10 minutes) between each scrape.

## Output
The output of this script is a collection of text files, each representing a job listing that matches your specified skills and filters. These text files contain essential information about the job, making it easy for you to review and explore relevant job opportunities.
