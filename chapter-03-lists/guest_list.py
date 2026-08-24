# Problem 3-4: Guest List

guests=['My father', 'Kim Taehyung', 'My crush']

msg0 = f"I'd have loved to invite {guests[0]} to dinner one day, with everything cooked by my own hands, and have a heartfelt chat, after I got settled in life."
msg1 = f"I feel like {guests[1]} is a great person, an amazing human being, apart from all his artistic talent & creativity, plus I'm a fan. So it'd be memorable."
msg2 = f"I'd love to have guests[0] on a dinner date. Perhaps it'd lead to a future together, perhaps just friendship, or perhaps nothing."

print(f"{msg0}\n\n{msg1}\n\n{msg2}\n")

# Problem 3-5: Changing Guest List

guest_not_coming=guests[0]
print(f"{guest_not_coming} can't make it to the dinner.")

del guests[0]

print(guests)

guests.insert(0,"My mother")

msg0 = f"I'd invite {guests[0]} to dinner, but only I've settled down and achieved enough in life. Career, family, kids, life.. I'd love to have a chat with her, with us eating my own cooked dinner."

print(f"{msg0}\n\n{msg1}\n\n{msg2}\n")

# Problem 3-6: More Guests

for guest in guests:
    print(f"Hello {guest}! Great news! I've found a bigger table for the dinner party. So, we're gonna have more guests:))\n")

guests.insert(0,'Anjali')

guests_count=len(guests)
guests.insert(guests_count//2,'Shomaila')
guests.append('Some other person')

print(guests)

for guest in guests:
    print(f"\nHello {guest}, I'm glad to invite to my dinner party, and I'd love to have a pleasant dinner with you.")

# Problem 3-7: SHrinking Guest List

for guest in guests:
    print(f"\nHello {guest}! I'm sincerely apologetic to be informing you that the 'bigger' table I'd been waiting on, won't be reserved by the deadline. I can only invite 2 people max to this dinner. I'm really sorry.")

for guest in guests[:1:-1]:
    popped_guest=guests.pop()
    print(f"\nI sincerely apologize {popped_guest} for being unable to book the bigger table, and hence being unable to host you for a dinner party I invited you to. I'm deeply regretful for my actions, and I hope to be able to invite you a dinner as soon as I can to make up for it.")

for guest in guests:
    print(f"\nHello {guest}. I'm pleased to inform you that you're still invited to the dinner party. You'll be one of the 2 people I've invited. Can you guess who the other one is?")

del guests[0]
del guests[0] # if you wanna empty a list using del operator only, use the index 0 for all the elements

print(guests)