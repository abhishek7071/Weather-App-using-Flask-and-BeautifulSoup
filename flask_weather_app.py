from flask import Flask,render_template

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        from bs4 import BeautifulSoup
import requests, time, smtplib
#from notify_run import Notify
from datetime import datetime
import re
import requests as r
from bs4 import BeautifulSoup as bs
searchquery = input("Enter the search query")
search_query = searchquery.replace(' ', '+') 
link="https://www.1mg.com/search/all?filter=true&name="+str(search_query)
#link ="https://www.1mg.com/search/all?filter=true&name=Combiflam"
html_page = r.get(link)
soup = BeautifulSoup(html_page.content,"lxml")

for i in soup.find_all('div',{'class':['style__horizontal-card___1Zwmt','style__product-box___3oEU6']}):
	link = i.find('a',href=True)
	if link is None:
	     continue
	link1 = link['href']
	#print(link['href'])
	print(link1)
	break
else:
	link1="N/A"
	print(link1)
	
if link1=="N/A":
	print(link1)
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
#print(soup.prettify())
for i in soup.find_all("div" , {"class":"GvJNB"}):
	link = i.find('a',href=True)
	if link is None:
		continue
	link2 = link['href']
	break
else:
	link2="N/A"
	#print(link['href'])
	#print(link2)
	
if link2=="N/A":
	print(link2)
else:
	url3="https://pharmeasy.in"+str(link2)
	print(url3)
	s=r.get(url3)
	soup1 = BeautifulSoup(s.text, 'html.parser')
	#print(soup.prettify())
	t=soup1.find("div" , {"class":"_1_yM9"}).text
	print(t)
          return render_template("flask_weather_app.html",price=price, product_name=product_name,desired_price=desired_price,status=status )
    return render_template("flask_weather_app.html")


