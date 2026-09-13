from datetime import datetime
import pandas
import smtplib
import random
my_mail = "kottakotanikhil75@gmail.com"
my_password = "uwsxroquikzosunp"
today = datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv(r"C:\python\100_days_bootcamp\Birthday wishing project\birthdays.csv")

birthday_month = 0
birthday_day = 0
data_row = ""

birthdays_dict = {
    (birthday_month, birthday_day): data_row
}

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    path = fr"C:\python\100_days_bootcamp\Birthday wishing project\letter_{random.randint(1,3)}.txt"
    with open (path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_mail,my_password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs = birthday_person["email"],
            msg=f"Subject:Birthday Wishes\n\n{contents}"
        )