import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the article titles (modify the selector based on the website structure)
    titles = soup.find_all('h2', class_='article-title')

    # Print out the titles
    for title in titles:
        print(title.get_text())
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
