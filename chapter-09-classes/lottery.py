import random

# Problem 9-14: Lottery

lottery_series = [4, 8, 111, 5, 11, 13, 7, 26, 49, 216]
lottery_letters = ['D', 'I', 'V', 'Y', 'A']
lottery_series.extend(lottery_letters)

winning_list = []

while len(winning_list) <4:
    no = random.choice(lottery_series)
    if no not in winning_list:
        winning_list.append(no)

print(f"\nWINNING TICKETS:")
for win in winning_list:
    print(f"\t{win}")

# Problem 9-15: Lottery Analysis

my_win = False
trials = 0

while not my_win:
    my_ticket = random.choice(lottery_series)

    if my_ticket in winning_list:
        print(f"\nI got a '{my_ticket}' ticket on my '{trials+1}' try, and finally won!")
        my_win = True

    else:
        trials += 1
        print(f"I got a '{my_ticket}' ticket.")
        print("Let's try again!!\n")