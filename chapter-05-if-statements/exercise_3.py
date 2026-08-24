# Problem 5-8: Hello Admin

usernames = ['admin',"Divya",'Ria','Dia','Isha']

for username in usernames:
    if username == 'admin':
        print('Hello admin! Would you like to check the status report?')
    else:
        print(f"Hello {username}! Thank you for logging in again:))\n")

# Problem 5-9: No users

if not usernames:
    print('We need more users ASAP.')
else:
    for i in range(len(usernames)):
        del usernames[-1]
    print('We need more users ASAP!\n')

# Problem 5-10: Checking Usernames

current_users = ['Divya','Ria','divya_techie','mysterious_here','khushi']
new_users = ['divya','KHUSHI','anjali','shomaila','harry']

current_users = [current_user.lower() for current_user in current_users]
new_users = [new_user.lower() for new_user in new_users]

for user in new_users:
    if user in current_users:
        print("Sorry! This username is taken. You need another username.\n")
    else:
        print("This username is available for you:)\n")

# Problem 5-11: Ordinal Numbers

for i in range(1,10):
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 3:
        print(f'{i}rd')
    else:
        print(f'{i}th')
