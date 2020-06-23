from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup
import requests, time, smtplib
from datetime import datetime
#from send_mail import send_mail
#import importlib
from pytz import timezone





#moduleName = input('Enter module name:')
#importlib.import_module(moduleName)
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method == 'POST':
        url = request.form.get('URL')
        sender_email = request.form.get('Email')
        desired_price = request.form.get('Desired_price',type=int)
        desired_price = int(desired_price)
        page1 = requests.get(url).text
        soup = BeautifulSoup(page1, 'lxml')
    

        product_name = soup.find('h1').text.strip()
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content,'html.parser')
        
        price = soup.find("div", {"class": "_3qQ9m1"}).text
        price = price[1:]
    
    
        price_ar = price.split(",")
        price = ''.join(price_ar)
    
        price = int(price)
        send(desired_price,price)
    def send_mail():

               server = smtplib.SMTP('smtp.gmail.com', 587)
               server.ehlo()
               server.starttls()
               server.ehlo()
               server.login('aman765180@gmail.com', 'Neesu@123')
               subject = "Price of " +str(product_name) +" has fallen down below Rs. " + str(desired_price)
               body = "Hey Rahul! \n The price of Boat Headphone on AMAZON has fallen down"  + ".\n So, hurry up & check the amazon link right now : " + url
               msg = f"Subject: {subject} \n\n {body} "
               server.sendmail(
            'sender_email',
            'Abhishek7071631646@gmail.com', msg
        )
               server.quit()


    def send(desired_price,price):
          count = 0
          if desired_price >= price:
             send_mail()
          else:
            count+= 1
          body = "last time refreshed"
                 
    count =0
    while(True):
       count+=1
       format = "%Y-%m-%d %H:%M:%S %Z%z"
       now_utc = datetime.now(timezone('UTC'))

       now_asia = now_utc.             astimezone(timezone('Asia/Kolkata'))
       status="last checked" +str(now_asia)
       #home()
       time.sleep(36)
    
       return render_template("flask_weather_app.html", price=price,product_name=product_name,desired_price=desired_price,status=status )
  
    return render_template("flask_weather_app.html")

app.run(debug=True)

    

    
