# # Day 10 - Work in Class - Classes and Objects
# 1. Song class
# define a class Song

# The class constructor needs to have three additional 3 parameters (self and 3 more!)

# title defaults to empty string
# author defaults to empty string
# lyrics by default empty tuple

# inside constructor method:

# set/store these three parameters inside objects variables of the same name (remember to use self!)
#  print on the screen "New Song made" - (try also printing here author and title!)

# Minimum:
# Write a method sing that prints the song line by line on the screen, 
# first printing the author and title, if any.

# Write a method yell that prints the song in capital letters 
# line by line on the screen, first printing the author and title, if any.

# Bonus: make the above sing and chain methods chainable, 
# so we can call them several times (chained)
# Bonus: create an additional parameter max_lines to yell and 
# sing methods that prints only a certain number of lines for both sing and yell. 
# Better do with some default value e.g. -1, at which all rows are then printed.

# Create multiple songs with lyrics

# Example:


# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","
# Garu, tālu ceļu veicu"])

# ziemelmeita.sing(1).yell()

# Outputs:

# Ziemeļmeita - Jumprava

# Gāju meklēt ziemeļmeitu

# Ziemeļmeita - Jumprava

# GĀJU MEKLĒT ZIEMEĻMEITU

# GARU, TĀLU CEĻU VEICU


# 2. Rap class
# For those feeling comfortable with class syntax, create a Rap class that inherits from Song

# # no new constructor method is necessary (you can if you want)


#  add a new method break_it with two default parameters max_lines=-1 and drop equal to "yeah", which is similar to sing, but adds a drop after each word .

# Example: 



# zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu","

# Garu, tālu ceļu veicu"])



# zrap.break_it(1, "yah")

# Ziemeļmeita - Jumprava

# Gāju YAH meklēt YAH ziemeļmeitu YAH

class Song:
    def __init__(self, title, author, lyrics):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"{title} by {author} - created {len(self.lyrics)} lines")

    # _ significies that this method is for internal use by the other methods in the object
    def _print_lyrics(self, lyrics, max_lines=-1):  # these lyrics will be processed already
        if max_lines == -1:
            max_lines = len(lyrics)
        for i in lyrics[:max_lines]:
            print(i)
        # we could return self here as well

    def sing(self, max_lines=-1):
        # self.max_lines = max_lines
        print(f" Singing {self.title} - {self.author}")
        self._print_lyrics(self.lyrics, max_lines)
        return self

    def yell(self, max_lines=-1):
        capital_lyrics = [line.upper() for line in self.lyrics]
        print(f"YELLING {self.title} - {self.author}")
        self._print_lyrics(capital_lyrics, max_lines)
        return self


ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1).yell()

vairogi = Song("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                   "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])
vairogi.sing(2).yell(1)

vairogi.sing().sing().sing()


class Rap(Song):

    # no need for custom __init__ in this case
    def break_it(self, max_lines=-1, drop="yeah"):
        print("Singer:", self.author, "-", self.title)
        for line in self.lyrics:
            print(line.replace(' ', f' {drop} '), sep="\n")
            max_lines -= 1
            if max_lines == 0:
                break
        return self


ziemelmeita = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.break_it(1).break_it()

ziemelmeita.sing().yell().break_it()

livi = Rap("Vairogi", "Līvi", ["Mūsu dziesmas ir vairogi seni", "Mēs tās par pagalvjiem liksim",
                                   "Daudzu likteņu pilni mēs elposim", "Kā pakalni Daugavas krastos"])

livi.sing().yell(2).break_it(drop="Jā!").break_it(2, "ahh")