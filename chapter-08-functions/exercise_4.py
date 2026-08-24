# Problem 8-9: Messages

def show_messages(messages):
    for message in messages:
        print(message)

messages = [
    'Good morning sweety!',
    'How is this day treating you so far?',
    'Top 3 accomplishments of this day?',
    'Sweet dreams!'
]

print("\nSome of my messages:-\n")
show_messages(messages)

# Problem 8-10: Sending Messages

sent_messages = []

def send_messages(messages,sent_messages):
    print()
    while messages:
        current_msg = messages.pop()
        print(f"Printing this message:- '{current_msg}'.")
        sent_messages.append(current_msg)

send_messages(messages,sent_messages)

print("\nSent Messages:-",end = '\n\t')
print(f"{'\n\t'.join(sent_messages)}")

print("\nMessages to be sent:-")
if not messages:
    print("\tNo messages left!")

# Problem 8-11: Archived Messages

messages = [
    'Good morning sweety!',
    'How is this day treating you so far?',
    'Top 3 accomplishments of this day?',
    'Sweet dreams!'
]

send_messages(messages[:],sent_messages)

print("\nSent Messages:-",end = '\n\t')
print(f"{'\n\t'.join(sent_messages)}")

print("\nMessages:-\n")
if not messages:
    print("\tNo messages left!")
else:
    show_messages(messages)
    print("\nMessages original list is still intact!")