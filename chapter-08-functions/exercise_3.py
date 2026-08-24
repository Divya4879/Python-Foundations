# Problem 8-6: City Names

def city_country(city, country):
    return f"{city.title()}, {country.title()}"

pairs = {
    'Patna' : 'India',
    'Seoul' : 'South Korea',
    'California' : 'USA'
}

for city, country in pairs.items():
    print(city_country(city,country))
print()

# Problem 8-7: Album

def make_album(artist_name, album_title, no_of_songs = None):
    if no_of_songs:
        return {
            'Artist': artist_name.title(),
            'Album Title': album_title.title(),
            'No of Songs': no_of_songs
            }
    
    return {
        'Artist': artist_name.title(),
        'Album Title': album_title.title()
        }

print(make_album('Taylor Swift', 'Lover'))
print(make_album('Taehyung', 'Layover'))
print(make_album('BTS', 'Arirang'))
print(make_album('XYZ', 'ABC', 14))

# Problem 8-8: User Albums

user_album = {}
flag = True

while flag:
    print("\nPlease enter your favourite album & artist.\n")

    album_title = input('Please enter one of your favourite album name: ').title()
    artist_name = input("Please enter its artist name: ").title()

    print()
    print(make_album(album_title, artist_name))

    more = input('\nPress q if you want to quit or press any other key if you want to add more: ')
    if more == 'q':
        flag = False