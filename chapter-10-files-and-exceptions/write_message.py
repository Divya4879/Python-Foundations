from pathlib import Path

# writing a single-line message

path = Path('written_message.txt')
message = 'I love Programming.'
path.write_text(message)

# Writing a multi-line message to a new_file

message = "I love programming.\n"
message += 'I adore Python language, doing by DSA in it, as well as FastAPI later on.\n'
message += 'I am in love with building & shipping products, and winning hackathons!!'

# write_text overwrites a file contents, if it already exists, and create a new_file if it didn't before.
path.write_text(message)