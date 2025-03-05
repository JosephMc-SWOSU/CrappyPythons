# TODO: Import Artist from Artist.py and Artwork from Artwork.py
from artist import Artist
from artwork import Artwork

if __name__ == "__main__":
    user_artist_name = input("Please enter the artist's name: ")
    user_birth_year = input("Please enter the artist's birth year: ")
    user_death_year = input("Please enter the artist's death year: ")
    user_title = input("Please enter the title of the artwork: ")
    user_year_created = input("Please enter the year the artwork was created: ")

    user_artist_name = user_artist_name if user_artist_name else "unknown"
    user_birth_year = int(user_birth_year) if user_birth_year else -1
    user_death_year = int(user_death_year) if user_death_year else -1
    user_title = user_title if user_title else "unknown"
    user_year_created = int(user_year_created) if user_year_created else -1
    
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    new_artwork = Artwork(user_title, user_year_created, user_artist)
 
    new_artwork.print_info()
