##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
from random import randint
import smtplib

PLACEHOLDER = "[NAME]"
EMAIL = "myemail@gmail.com"
PASSWORD = "abcd12345@"

now = dt.datetime.now()
today_tuple = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
# birthdays = data.to_dict(orient="records")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
  with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
    letters = letter.read()
    new_letter = letters.replace(PLACEHOLDER, birthdays_dict[today_tuple]["name"])
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=f"{birthdays_dict[today_tuple]['email']}",
                        msg=f"Subject:Happy Birthday\n\n{new_letter}")


