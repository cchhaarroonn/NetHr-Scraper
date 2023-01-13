import requests
from bs4 import BeautifulSoup

topic = str(input("Topic [Danas/Sport/Hot/Magazin/Webcafe/Crna-Kronika]: "))

if topic.lower() == "crna-kronika":
    url = "https://net.hr/danas/" + topic.lower()
else:
    url = "https://net.hr/" + topic.lower()
    
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
text = soup.select("#article_card_title")
print("\n[*] Recent news in " + topic + " topic from Net.hr: \n")
for element in text:
    print(element.text + "\n")