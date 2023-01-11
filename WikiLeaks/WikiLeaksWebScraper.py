import requests
from bs4 import BeautifulSoup

def WikiLeaksWebScraper():  

    url='https://wikileaks.org/+-Intelligence-+.html'
    
    header = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    r = requests.get(url,headers=header)

    soup = BeautifulSoup(r.content, 'html.parser')

    title = []
    information = []
    images = []
    date = []

    all_info = soup.find('div',class_='content')

    for i in all_info.find_all('h2',class_='title'):
        title.append(i.text)

    for i in all_info.find_all('div',class_='intro'):
        info=i.find('p')
        information.append(info.text)

    for i in all_info.find_all('div',class_='teaser'):
        image=i.find('img')['src']
        link=f'https://wikileaks.org/{image}'
        images.append(link)    

    for i in all_info.find_all('div',class_='timestamp art700'):
        date.append(i.text)        

    scraped_data = []
    for i in range(0, len(title)):
        scraped_data.append({
            'title' : title[i], 
            'information' : information[i], 
            'image' : images[i], 
            'date' : date[i], 
        })

    return scraped_data

if __name__ == "__main__":
    print(WikiLeaksWebScraper())