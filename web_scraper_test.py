import requests 
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser') ## Creates object from .html and the .html parser
results = soup.find(id="ResultsContainer") ## Looks for HTML <div id> attribute
#job_elements = soup.find_all("div", class_="card-content") ## Stores specific <div id> in list (object made from object)

python_jobs = results.find_all( "h2", string=lambda text:"python" in text.lower() ) ## lamba function converts "h2" string to lowercase and checks for "python"
#print(results)
python_job_elements = [ h2_element.parent.parent.parent for h2_element in python_jobs] ## Move up parent tree to capture entire element (move up to the "card" class) for each "h2" filtered


#title_element = results.find("h2", class_="title")

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    print(title_element.text.strip() )
    company_element = job_element.find("h3", class_="company")
    print(company_element.text.strip() )

    links = job_element.find_all("a") ## finds "a" class
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}")
    print()