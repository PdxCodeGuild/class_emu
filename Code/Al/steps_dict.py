# filename: "steps_dict.py"
import requests
import datetime
my_steps = requests.get("http://127.0.0.1:8000/my_stepsv2.csv").content.decode('utf-8')
# print(my_steps.replace('\n', ',').split(','))
my_steps = my_steps.split('\n')
print(my_steps)
steps_dict = {}
for date_steps in my_steps[:-1]:
    date_steps_list = date_steps.split(',')
    one_date = date_steps_list[0]
    if not one_date[0].isdigit(): # check if the first character is a digit
        my_date = datetime.datetime.strptime(one_date, '%b %d %Y') # encode from month day year
        one_date = my_date.strftime('%m/%d/%y')

    one_steps = date_steps_list[1]

    steps_dict.update({one_date:one_steps})
print(steps_dict)
