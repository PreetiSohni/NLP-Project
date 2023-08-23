import requests
from bs4 import BeautifulSoup

def extract_article_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the title of the article
        title = soup.find('title').get_text()
        
        # Find the main article content
        article_text = ''
        article_element = soup.find('article')  # Adjust the tag as per the webpage structure
        if article_element:
            paragraphs = article_element.find_all('p')  # Adjust the tag as per the webpage structure
            article_text = '\n'.join([p.get_text() for p in paragraphs])
        
        return title, article_text
    else:
        print("Error: Unable to fetch the webpage.")

# Provide the URL of the webpage you want to extract content from
# url = 'https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/'

# # Call the function to extract article content
# title, article_text = extract_article_content(url)

# # Print the extracted title and article text
# print("Title:", title)
# print("Article Text:\n", article_text)