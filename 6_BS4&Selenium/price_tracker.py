 #AMAZON

import lxml

#url = "https://www.amazon.com/Cuckoo-CRP-P0609S-Cooker-10-10-11-60/dp/B01JRTZVVM/ref=sr_1_4?qid=1611738512&sr=8-4"
#url = "https://www.amazon.com/Cuckoo-CRP-P0609S-Cooker-10-10-11-60/dp/B01JRTZVVM/ref=sr_1_4?qid=1611738512"
#url = "https://www.amazon.com/Cuckoo-CRP-P0609S-Cooker-10-10-11-60/dp/B01JRTZVVM/ref=sr_1_4?dchild=1&keywords=cuckoo+rice+cooker&qid=1611738512&sr=8-4"

url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
   # "User-Agent":"Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price_get = soup.find(id="priceblock_ourprice")
price_text = price_get.getText()
price_without_currency = price_text.strip("$")
price_as_float = float(price_without_currency)
print(price_as_float)

p = 259.99
print(p)


price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)



#SSG.COM

import requests
from bs4 import BeautifulSoup
import lxml

URL = "http://www.ssg.com/item/itemView.ssg?itemId=1000025465383&siteNo=6004&salestrNo=6005&
tlidSrchWd=%EB%A9%94%EC%9D%B4%ED%94%8C%ED%8A%B8%EB%A6%AC%20%EC%9C%A0%EC%82%B0%EA%B7%A0&srchPgNo=1&src_area=ssglist"

headers={
    "User-Agent": "Defined",

}
response = requests.get(URL).text
soup = BeautifulSoup(response, "html.parser")
# print(soup.prettify())

get_price = soup.find(class_="ssg_price").getText()
# print(get_price)
price_str = get_price.replace(',', '')
# print(price_str)
price = int(price_str)
# print(type(price))

product_title = soup.find(class_="cdtl_info_tit").getText().encode()
#smtplib 'ascii' codec can't encode characters
# print(product_title)
link_to_buy = URL
# print(link_to_buy)


#ALERT EMAIL

import smtplib
my_email = "testpythondy@gmail.com"
my_password = "-"
yahoo_email = "testpythondy@yahoo.com"

target_price = 18000 #15420
encoding='UTF8'

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=yahoo_email,
            msg=f"Subject: SSG.com Price Alert! \n\n Your product is now at {get_price}won. \n Go to: {URL}")


