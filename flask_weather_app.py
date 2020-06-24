
from flask import Flask,request,render_template 
from bs4 import BeautifulSoup
import requests, time, smtplib
from datetime import datetime
#from send_mail import send_mail
import importlib
from flask_apscheduler import APScheduler
from pytz import timezone
moduleName = input('Enter module name:')
importlib.import_module(moduleName)
app = Flask(__name__)
scheduler = APScheduler()

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('URL')
        sender_email = request.form.get('Email')
        global desired_price
        desired_price = request.form.get('Desired_price',type=int)
        desired_price = int(desired_price)
        page1 = requests.get(url).text
        soup = BeautifulSoup(page1, 'lxml')
    

        product_name = soup.find('h1').text.strip()
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parser')
        global price
        price = soup.find("div", {"class": "_3qQ9m1"}).text
        price = price[1:]
    
    
        price_ar = price.split(",")
        price = ''.join(price_ar)
    
        price = int(price)
        
        if desired_price >= price:
          send_mail()
        else:
          format = "%Y-%m-%d %H:%M:%S %Z%z"
          now_utc = datetime.now(timezone('UTC'))
          now_asia = now_utc.             astimezone(timezone('Asia/Kolkata'))
          status="last checked at" +str(now_asia)
          return render_template("flask_weather_app.html",price=price, product_name=product_name,desired_price=desired_price,status=status )
    return render_template("flask_weather_app.html")
#def scheduledTask():
    #print("This task is running every 5 seconds")
scheduler.add_job(id ='Scheduled task', func = home, trigger = 'interval', seconds = 50)
scheduler.start()
app.run(debug=True)
    

    
