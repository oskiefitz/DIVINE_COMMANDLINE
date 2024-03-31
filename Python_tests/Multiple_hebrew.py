import re
from urllib.request import urlopen

def extract_hebrew_text(html_content):   
    div_position = html_content.find('<div class="vheading2">Hebrew Texts</div>')
    if div_position != -1:  
        content_before_div = html_content[:div_position] 
        hebrew_text = re.findall(r'[\u0590-\u05FF]+', content_before_div)
        return hebrew_text
    else:   
        print("no tag 'hebrew texts' on this page!")
        return []

def save_to_file(hebrew_text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for word in hebrew_text:
            f.write(word + '\n')

# need each verse , testing here with gen 12 verses 1 - 20
urls = ['https://biblehub.com/text/genesis/12-' + str(i) + '.htm' for i in range(1, 21)]

for i, url in enumerate(urls, start=1):
    try:
        with urlopen(url) as response:
            html_content = response.read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch HTML content from URL: {url}")
        print(f"Error: {e}")
        continue

    hebrew_text = extract_hebrew_text(html_content)

    file_name = f'Genesis_{i}.txt'
    save_to_file(hebrew_text, file_name)
    print(f"hebrew text on '{file_name}'.")


