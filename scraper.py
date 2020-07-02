import requests
from bs4 import BeautifulSoup
import smtplib
import datetime

productURL = input("Enter the link of the Amazon product you want to track: ")
sendingMail = input("Enter the email address of the email address that sends the email: ")
sendingMailPassword = input("Enter the password of the sending email: ")
receivingMail = input("Enter the email address of the email address that receives the email alert: ")

URL = productURL

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:5])

    if(converted_price > 150):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sendingMail, sendingMailPassword)

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/dp/B00V4L6JC2/ref=s9_acsd_hps_bw_c2_x_4_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-4&pf_rd_r=52QHDA04SDK7HS2Z7QPA&pf_rd_t=101&pf_rd_p=7c00f914-cf00-443d-a66f-f9afe38e169a&pf_rd_i=21243324031'

    msg = f"Subject : {subject}\n\n{body}"

    server.sendmail(
        sendingMail,
        receivingMail,
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(3600)
