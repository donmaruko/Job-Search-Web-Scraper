from bs4 import BeautifulSoup
import requests
import time

print("Skills you aren't familiar with (comma-separated):")
unfamiliar_skills = input('> ')
unfamiliar_skills_list = [skill.strip() for skill in unfamiliar_skills.split(",")]
print(f"Filtering out: {', '.join(unfamiliar_skills_list)}")

def find_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    # find will bring the FIRST MATCH while find_all brings all

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text
        if 'few' in published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(" ", "")  # this replaces white spaces with nothing
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a['href']
            skills_list = [skill.strip() for skill in skills.split(",")]

            if not any(skill in skills_list for skill in unfamiliar_skills_list):
                with open(f'PYTHON/Practice/Scraper/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                    f.write(f"Filter(s) Applied: {unfamiliar_skills_list}")
                print(f"File saved in: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)