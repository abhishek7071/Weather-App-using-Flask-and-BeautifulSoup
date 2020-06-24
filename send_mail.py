import smtplib

#from flask_weather_app import *


def send_mail():

               server = smtplib.SMTP('smtp.gmail.com', 587)
               server.ehlo()
               server.starttls()
               server.ehlo()
               server.login('aman765180@gmail.com', 'Neesu@123')
               subject = "Price drop alert"
               body = "Hey Rahul! \n The price of Boat Headphone on AMAZON has fallen down "
               msg = f"Subject: {subject} \n\n {body} "
               server.sendmail(
            'sender_email',
            'Abhishek7071631646@gmail.com', msg
        )
               server.quit()


