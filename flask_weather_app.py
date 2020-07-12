from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests, time, smtplib
#from notify_run import Notify
from datetime import datetime
import re
import requests as r
from bs4 import BeautifulSoup as bs
app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():
  if request.method == 'POST':
    medicine_name= request.form.get('medicine_name')
    link="https://www.1mg.com/search/all?filter=true&name="+str(medicine_name)
    html_page = r.get(link)
    soup = BeautifulSoup(html_page.content,"lxml")
    for i in soup.find_all('div',{'class':['style__horizontal-card___1Zwmt','style__product-box___3oEU6']}):
      link = i.find('a',href=True)
      if link is None:
         continue
      link1 = link['href']
      print(link1)
      break
    else:
      link1="N/A"
    if link1=="N/A":
      print("product is not availble")
    else:
      url1= "https://www.1mg.com"  +str(link1)
      print(url1)
      page1 = r.get(url1)
      soup = bs(page1.content, "html.parser")
      price=soup.find("span" , {"class": "l3Regular"}).text
      price = price[1:]
      print(price)
    url2= "https://pharmeasy.in/search/all?name="+str(searchquery)
    p=r.get(url2)
    soup = BeautifulSoup(p.text, 'html.parser')
    for i in soup.find_all("div" , {"class":"GvJNB"}):
      link = i.find('a',href=True)
      if link is None:
         continue
      link2 = link['href']
    else:
      link2="N/A"
    if link2=="N/A":
	    print("not availble")
    else:
      url3="https://pharmeasy.in"+str(link2)
      print(url3)
      s=r.get(url3)
      soup1 = BeautifulSoup(s.text, 'html.parser')
      t=soup1.find("div" , {"class":"_1_yM9"}).text
      print(t)
      return render_template("flask_weather_app.html",aprice=price, fprice=t,alink=url1,flink=url3 )
    return render_template("flask_weather_app.html")

app.run(debug=True)
