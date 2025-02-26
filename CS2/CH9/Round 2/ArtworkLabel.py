class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            years = f"({self.birth_year} to {self.death_year})"
        elif self.birth_year >= 0 and self.death_year < 0:
            years = f"({self.birth_year} to present)"
        else:
            years = "(unknown)"
        print(f"Artist: {self.name} {years}")

class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        if artist is None:
            artist = Artist()
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")

if __name__ == "__main__":
    artist_name = input("Please enter the artist's name: ")
    birth_year = int(input("Please enter the artist's birth year: "))
    death_year = int(input("Please enter the artist's death year (or -1 if still alive): "))
    title = input("Please enter the title of the artwork: ")
    year_created = int(input("Please enter the year the artwork was created: "))

    artist = Artist(artist_name, birth_year, death_year)
    artwork = Artwork(title, year_created, artist)
    artwork.print_info()