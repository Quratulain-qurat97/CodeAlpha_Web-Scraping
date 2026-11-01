# Required libraries:
# Install once using: python -m pip install requests beautifulsoup4 pandas



# Step 1: Import the libraries and fetch the webpage
import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url, timeout=30)
response.raise_for_status()
# print(response.status_code)




# Step 2: Convert the HTML into something BeautifulSoup can search
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title.text)



# Step 3: Extract all job titles
job_titles = soup.find_all("h2", class_ = "title is-5") 
# for title in job_titles:
#     print(title.text.strip())



# Step 4: Extract company names
company_names = soup.find_all("h3", class_= "subtitle is-6 company")
# for company in company_names:
#     print(company.text.strip())




# Step 5: Extract locations
locations = soup.find_all("p", class_ = "location")
# for location  in locations:
#     print(location.text.strip())



# Step 6: Extract all posting dates
posting_dates = soup.find_all("time")
# for date in posting_dates:
#     print(date.get("datetime"))



# Step 7: Combine the four lists
assert len(job_titles) == len(company_names) == len(locations) == len(posting_dates), "Record counts do not match!"

jobs = []
for title, company, location, date in zip(
    job_titles, company_names, locations, posting_dates):
    jobs.append({
        "Job Title": title.text.strip(),
        "Company": company.text.strip(),
        "Location": location.text.strip(),
        "Posting Date": date.get("datetime")
    })



# Step 8: Check the complete dataset
print("Total job records:", len(jobs))
print("First job:", jobs[0])
print("Last job:", jobs[-1])



# Step 9: Export the dataset to CSV
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index= False)
print(df.head())




# Step 10: Data Quality Checks
print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())



# Step 11: Dataset Summary
print("\n========== DATASET SUMMARY ==========")
print("Total job listings:", len(df))
print("Total companies:", df["Company"].nunique())
print("Total unique job titles:", df["Job Title"].nunique())
print("Total unique locations:", df["Location"].nunique())
print("Date range:", df["Posting Date"].min(), "to", df["Posting Date"].max())
print("=====================================")