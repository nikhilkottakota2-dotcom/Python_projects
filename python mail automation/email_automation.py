import datetime as dt
import random
import smtplib
my_mail = "testitsnotcorrectmail75@gmail.com"
my_password = "uwsxroquikzosunp"
now = dt.datetime.now()
weekday = now.isoweekday()
if weekday == 7:
    with open (r"C:\python\100_days_bootcamp\python mail automation\motivational_quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail,password=my_password)
            connection.sendmail(from_addr=my_mail,to_addrs="testmailitsnot2@yahoo.com",
                                msg=f"Subject:Quote\n\n{quote}")
else:
    print()