# Question One
# user = input('Type the elements of your list: ')
# user_list = user.split(',')
# print(user_list)
# if "c" or "C" in user_list:
#     print("Words exist")
#
# else:
#     print("The words cannot be found")


# Question 2
day = int(input("Type day between 0 and 10: "))
i = ''
for i in day:
    if day != 0 and day > 10:
        print('Type a day value between 0 and 10')


# hours = int(input("Type hours between 0 and 23: "))
# minutes = int(input("Type minutes between 0 and 59: "))
#
# if day <= 10:
#     day_convert = day * 24 * 60
# else:
#     print("Type a day value between 0 and 10")
#
# if hours <= 23:
#     hours_convert = hours * 60
# else:
#     print("Type a hours values between 0 and 23")
#
# if minutes <= 59:
#     minutes_convert = minutes
# else:
#     print("Type a minutes values between 0 and 59")
#
# new_time = day_convert + hours_convert + minutes_convert
# print(f'The total number of minutes is {new_time} minutes')