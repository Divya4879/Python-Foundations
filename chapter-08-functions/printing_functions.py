def printing_dict(user_dict):
    for attribute,value in user_dict.items():
        print(f"{attribute.title()}: {value.title()}")
    print()