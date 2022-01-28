import requests
from bs4 import BeautifulSoup
import pandas as pd
if __name__ == '__main__':

    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    #print(page.text)

    """
    class="title is-5" contains the title of the job posting.
    class="subtitle is-6 company" contains the name of the company that offers the position.
    class="location" contains the location where you’d be working.
    """
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    #print(results.prettify())
    job_elements = results.find_all("div", class_="card-content")
    df = pd.DataFrame(columns=['title', 'company', 'location'])

    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        #print(title_element.text)
        #print(company_element.text)
        #print(location_element.text)
        #print()
        df = df.append({'title': title_element.text, 'company': company_element.text, 'location': location_element.text}, ignore_index=True)

    print(df.to_markdown())