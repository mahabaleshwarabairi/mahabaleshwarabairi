import datetime
date_string = '2017-12-31'
date_format = '%Y-%m-%d'
try:
  date_obj = datetime.datetime.strptime(date_string, date_format)
  #date_obj=datetime.datetime.strptime
  print(date_obj)
except ValueError:
  print("Incorrect data format, should be YYYY-MM-DD")
