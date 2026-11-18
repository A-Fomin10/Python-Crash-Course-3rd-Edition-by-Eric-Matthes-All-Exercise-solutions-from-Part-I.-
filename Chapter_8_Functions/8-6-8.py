#8-6 City names 

# def city_country(city, country):
#     """country names+retun"""
#     location = f"{country.title()}, {city.title()}"
#     return(location)

# place = city_country("zbarazh", "Ukraine")
# print(place)

# place = city_country(country='ukraine', city='kyiv')
# print(place)

# place = city_country(city="warsaw", country="poland")
# print(place)

#8-7 Music Album

def make_album(artist_name, album_title, song_number=None):
    """name and title of a music album"""
    album_desc = {"name": artist_name, "title": album_title}
    if song_number:
        album_desc['Songs in the album'] = song_number
    return(album_desc)

# artist = make_album('bob', 'coolness', song_number=27)
# print(artist)

# artist1 = make_album('john', 'spacejesus')
# print(artist1)

# artist2 = make_album('anton', 'killit')
# print(artist2)

#8-8 User Albums

while True:
    print(f"Please tell us more about your music.")
    print(f"You may enter 'q' to stop the program anytime.")

    a_name = input("First name:")
    if a_name == 'q':
        break

    alb_name = input("Pkease tell us the name of your album:")
    if alb_name == 'q':
        break

    full_album = make_album(a_name, alb_name)
    print(full_album)