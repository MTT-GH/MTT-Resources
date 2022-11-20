# python solution to test href links in a section of a web page
from bs4 import BeautifulSoup
import urllib3
import os
from github import Github




def link_index_page():
    # Analyze the links in INDEX page
    github_repo_index="https://github.com/ESI-EMEA/ESI_Resources/blob/main/index.md"

    #open the url and read the content using urllib3
    http = urllib3.PoolManager()
    response = http.request('GET', github_repo_index, retries=urllib3.Retry(5,redirect=5))
    #print HTML page content
    #print(response.data)
    soup = BeautifulSoup(response.data, 'html.parser')

    #read article element in HTML page
    article = soup.find('article')
    #print(article)

    #find all links in article element href starting with https
    https_links=[]
    links = article.find_all('a', href=True)
    for link in links:
        if link['href'].startswith('https'):
            #print(link['href'])
            https_links.append(link['href'])

    # Get a list of non working links
    bad_links=[]
    for link in https_links:
        print ("Checking link: ", link)
        #Pretend to open from browser --> too many redirects issue
        HEADER = {'User-Agent': 'Microsoft Edge'}
        #req = urllib.request.Request(link, headers=HEADER)
        response = http.request('GET', link, headers=HEADER, retries=urllib3.Retry(100,redirect=100))
        if response.status != 200:
            print("Bad link: ", link, "Status: ", response.status)
            bad_links.append(link)

    # if list is not empty, print the list
    if bad_links:
        print("Bad links: ", bad_links)
    else:
        print("All links are working for INDEX page")


def link_exam_page():
    
    ## Analyze individual Exam Pages
    # Get a list of all exam pages
    exam_pages=["AZ104", "AZ120", "AZ140", "AZ204", "AZ220", "AZ305", "AZ400", "AZ500",
                "AZ700", "AZ800", "AZ801", "AZ900", "AI102", "AI900", "DP090", "DP100", 
                "DP203", "DP420", "DP900", "PL300", "SC100", "SC200", "SC300", "SC400", "SC900"]

    # Loop through each exam page
    for exam_page in exam_pages:
        exam_page_url="https://github.com/ESI-EMEA/ESI_Resources/blob/main/_exams/"+exam_page+".md"

        #open the url and read the content using urllib3
        http = urllib3.PoolManager()
        response = http.request('GET', exam_page_url, retries=urllib3.Retry(5,redirect=5))
        soup = BeautifulSoup(response.data, 'html.parser')

        #read article element in HTML page
        article = soup.find('article')

        #find all links in article element href starting with https
        https_links=[]
        links = article.find_all('a', href=True)
        for link in links:
            if link['href'].startswith('https'):
                #print(link['href'])
                https_links.append(link['href'])

        # Get a list of non working links
        bad_links=[]
        for link in https_links:
            print ("Checking link: ", link)
            #Pretend to open from browser --> too many redirects issue
            HEADER = {'User-Agent': 'Microsoft Edge'}
            #req = urllib.request.Request(link, headers=HEADER)
            response = http.request('GET', link, headers=HEADER, retries=urllib3.Retry(100,redirect=100))
            if response.status != 200:
                print("Bad link: ", link, "Status: ", response.status)
                bad_links.append(link)

        # if list is not empty, print the list
        if bad_links:
            print("Bad links: ", bad_links)
        else:
            print("All links are working for ", exam_page, " page")
            
##Create a GitHub Issue on the repository
def create_issue():
    #Create a GitHub Issue on the repository
    #
    # This script requires the PyGithub library
    #   pip install PyGithub
    
    # Get the GitHub token from the environment
    token = os.environ['GITHUB_TOKEN']

    # Create a GitHub connection
    g = Github(token)

    # Get the repository
    repo = g.get_repo("ESI-EMEA/ESI_Resources")
    
    # Create the issue
    issue = repo.create_issue(title="Broken Links", body="Broken Links in the ESI Resources Repository")


def main():
    #link_index_page()
    #link_exam_page()
    create_issue()

if __name__ == "__main__":
    main()