import smtplib
from datetime import datetime
import random
import pandas
from env import MYEMAIL, PASSWORD



today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")

birthday_dict = {(data_row["month"],data_row["day"] ): data_row for (index, data_row) in data.iterrows()}


if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"

    with open(file_path) as file:
        contents = file.read()
        new= contents.replace("[NAME]", birthday_person["name"])

    # with open("quotes.txt")as quote_file:
    #     all_quotes = quotes = quote_file.readlines()
    #     quote = random.choice(all_quotes)

    with smtplib.SMTP('smtp.gmail.com') as connection:

        connection.starttls()
        connection.login(MYEMAIL, PASSWORD)
        connection.sendmail(from_addr = MYEMAIL, to_addrs="astlpeter@gmail.com",
                            msg= f"Subject: Happy Birthday\n\n {new}")
else:
    print("Sorry, no match")

#
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
#
# date_of_birth = dt.date(year = 2001,month = 4,day = 14)
# print(date_of_birth)