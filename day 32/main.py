# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

# 2. Go to https://myaccount.google.com/
# Select Security on the left and scroll down to How you sign in to Google.
# Enable 2-Step Verification

# 3. Click on 2-Step Verification again, and scroll to the bottom.
# There you can add an App password.
# Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.
# COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.

# 4. Add a port number by changing your code to this:
# smtplib.SMTP("smtp.gmail.com", port=587)


# my_email = "myemail@gmail.com"
# password = "abcd12345@"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=password)
#   connection.sendmail(from_addr=my_email,
#                       to_addrs="otheremail@outlook.com",
#                       msg="Subject:Hello\n\nThis is the body of my email.")
  
import datetime as dt
from random import choice
import smtplib

EMAIL = "myemail@gmail.com"
PASSWORD = "abcd12345@"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
  with open("quotes.txt") as quotes:
    quotes_list = quotes.readlines()
    quote = choice(quotes_list)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs="otheremail@outlook.com",
                        msg=f"Subject:Monday Motivation\n\n{quote}")

  