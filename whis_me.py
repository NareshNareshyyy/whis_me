
# Whis_me Function

import datetime

def whis_me():

     hour = int(datetime.datetime.now().hour)

     if hour >= 0 and hour >= 12:
          print("Good Morning Sir")

     elif hour >= 12 and hour >= 18:
          print("Good Afternoon Sir")

     else:
          print("Good Evening Sir")

whis_me()