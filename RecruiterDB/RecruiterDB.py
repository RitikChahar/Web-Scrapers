import requests
import json
import os

def fetch_and_save_data(page):
    url = "https://37ala4v5gx-2.algolianet.com/1/indexes/recruiters/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser"
    
    payload = {
        "query": "",
        "hitsPerPage": 5,
        "page": page
    }
    
    headers = {
        'Content-Type': 'application/json',
        'x-algolia-api-key': '716b5d3ec9a5585d268ca3596c06ad62', 
        'x-algolia-application-id': '37ALA4V5GX',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
        'Accept': '*/*',
        'Origin': 'https://recruiterdb.web.app',
        'Referer': 'https://recruiterdb.web.app/',
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        extracted_data = []
        for hit in data["hits"]:
            extracted_item = {
                "firstname": hit.get("firstName"),
                "lastname": hit.get("lastName"),
                "email": hit.get("email"),
                "linkedin": hit.get("linkedIn"),
                "title": hit.get("title"),
                "company": hit["_highlightResult"]["company"].get("value")
            }
            extracted_data.append(extracted_item)
        
        json_file_path = 'emails.json'
        
        if os.path.exists(json_file_path) and os.path.getsize(json_file_path) > 0:
            with open(json_file_path, 'r') as file:
                existing_data = json.load(file)
        else:
            existing_data = []
        
        existing_data.extend(extracted_data)
        
        with open(json_file_path, 'w') as file:
            json.dump(existing_data, file, indent=2)
        
        print("Data successfully saved to JSON file.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print("Response content:", response.content)


for i in range(0, 20):
    fetch_and_save_data(i)
