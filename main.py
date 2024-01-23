import requests
from bs4 import BeautifulSoup
import csv

url = "https://lenouvelliste.com/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')

    
        h1_tags = soup.find_all('h1')
        h1_data = [h1.text.strip() for h1 in h1_tags]

        
        img_tags = soup.find_all('img')
        img_links = [img['src'] for img in img_tags]



        p_tags = soup.find_all('p')
        p_data = [p.text.strip() for p in p_tags]
        
        a_tags = soup.find_all('a')
        a_data = [a.text.strip() for a in a_tags]
        
        
        # Enregistrement dans un fichier CSV
        data_list = list(zip(h1_data, img_links, p_data,a_data))
        header = ["H1", "Image","description","lien"]

        with open('lenouvelliste_data.csv', mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data_list)

        print("Donne anregistre nan fichier lenouvelliste_data.csv.")

    else:
        print(f"ou pa reyisi: {response.status_code}")

except requests.ConnectionError as e:
    print(f"Connection Error: {e}")
except requests.RequestException as e:
    print(f"Request Exception: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
