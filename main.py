import smtplib
from datetime import datetime
import random

MY_EMAIL = "your_email"
PASSWORD = "your_password" # You should get this from the settings of ur gmail account.

now = datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt","r") as file:
        txt_file = file.read()
        quotes = txt_file.split("\n")
        quote = random.choice(quotes)

    message = f"Subject:Monday Reminder\n\n{quote}"

    with smtplib.SMTP("smtp.gmail.com") as connection:    #gmail.com should be changed accoring the type of mail server.
        connection.starttls()    #To secure the connection
        connection.login(user = MY_EMAIL, password= PASSWORD )
        connection.sendmail(from_addr= my_email
                            ,to_addrs="to_where@gmail.com"
                            ,msg = message)







