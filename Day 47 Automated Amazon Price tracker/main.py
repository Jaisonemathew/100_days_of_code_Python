import requests
import smtplib
from bs4 import BeautifulSoup
from config import passkey,email,receiver_email


response=requests.get("https://amzn.eu/d/hWwun6B", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36","Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"})
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
span_element = soup.find('span', class_="a-price-whole")
price=span_element.getText()
comma_removed_price=price.replace(",","")
dot_removed_price=int(comma_removed_price.split(".")[0])

if dot_removed_price<1500:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=passkey)
        connection.sendmail(from_addr=email,to_addrs=receiver_email,msg=f"Subject:Amazon Price Alert!\n\nThe price of the product has fallen below Rs.1500!\n\nhttps://amzn.eu/d/hWwun6B")
        print("Email sent successfully")


