import smtplib
from __main__ import *
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


