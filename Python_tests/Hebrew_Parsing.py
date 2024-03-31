import re
import requests

def scrape_hebrewparse_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        # grammatical parsing for each word
        content = re.findall(r'<a href="/hebrewparse\.htm" title="(.*?)">(.*?)</a>', response.text)
        if content:
            return '\n'.join(['{}: {}'.format(item[1], item[0]) for item in content])
        else:
            print("no data!")
            return None
    else:
        print("nothing")
        return None

def save_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Text saved to '{file_path}' successfully.")

urls = [f"https://biblehub.com/text/genesis/12-{i}.htm" for i in range(1, 21)]

for i, url in enumerate(urls, start=1):
    # scraping inside 
    scraped_content = scrape_hebrewparse_page(url)

    if scraped_content:
        file_name = f"Genesis12-{i}_PARSED.txt"
        save_to_file(scraped_content, file_name)

