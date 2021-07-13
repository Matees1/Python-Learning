import random as r
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

adjectives = (
    "adorable",
    "agreeable",
    "alert",
    "amused",
    "angry",
    "annoying",
    "alive",
    "aggressive",
    "attractive",
    "average",
    "anxious",
    "ashamed",
    "awful"
)

nouns = (
    "people",
    "history",
    "way",
    "art",
    "world",
    "information",
    "map",
    "family",
    "government",
    "health",
    "system",
    "computer",
    "meat",
    "year",
    "thanks"
)

pluralNouns = (
    "women",
    "men",
    "children",
    "teeth",
    "feet",
    "people",
    "leaves",
    "mice",
    "geese",
    "halves",
    "knives",
    "wives",
    "lives",
    "elves",
    "pennies",
    "spies",
    "babies",
    "cities",
    "dasies"
)

femaleNames = (
    "Olivia",
    "Emma",
    "Ava",
    "Sofia",
    "Isabella",
    "Charlotte",
    "Amelia",
    "Mia",
    "Harper",
    "Evelyn",
    "Abagail",
    "Emily",
    "Ella",
    "Elizabeth",
    "Camila",
    "Luna",
    "Avery",
    "Mila",
    "Scarlett",
    "Layla",
    "Chole"
)

articleOfClothing = (
    "pants",
    "socks",
    "sunglasses",
    "baseball cap",
    "buisness suit",
    "hoodie",
    "boxer",
    "tank top",
    "t-shirt"
)

cities = (
    "Bankok",
    "Paris",
    "London",
    "Dubai",
    "Singapore",
    "Kuala Lumpur",
    "New York",
    "Istanbul",
    "Tokyo",
    "Antalya"
)

letters = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z"
)

celeberties = (
    "Johnny Depp",
    "Arnold Schwarzenegger",
    "Jim Carrey",
    "Emma Watson",
    "Daniel Radcliffe",
    "Lenardo DiCaprio",
    "Tom Cruise",
    "Brad Pitt",
    "Charles Chaplin",
    "Morgan Freeman",
    "Tom Hanks",
    "Hugh Jackman",
    "Matt Damon",
    "Sylvester Stallone",
    "Will Smith",
    "Clint Eastwood",
    "Cameron Diaz",
    "George Clooney",
    "Steven Spielberg",
    "Harrison Ford",
    "Robert De Niro",
    "Al Pacino",
    "Robert Downey Jr."
)

places = (
    "The Eiffel Tower",
    "The Colosseum",
    "The Statue of Liberty",
    "Machu Picchu",
    "The Arcopolist",
    "The Taj Mahal",
    "The Pyramids of Giza",
    "The Great Wall Of China",
    "Angkor Wat",
    "Petra",
    "The Grand Canyon",
    "The Stonehenge",
    "Niagra Falls",
    "The Sydney Opera House"
)

def generateMadLibs(filePath):
    print("Generating...")
    randomNumber = r.randint(1, 200)

    open("text.txt", "w").write("")

    fileToWrite = open(filePath, "a")

    fileToWrite.write(f"There are many {r.choice(adjectives)} ways to choose a/an {r.choice(nouns)} to read. First, you")
    fileToWrite.write(f"\ncould askk for recommendations from your friends and {r.choice(pluralNouns)}.")
    fileToWrite.write(f"\nJust don't ask Aunt {r.choice(femaleNames)}, she only reads {r.choice(adjectives)} books")
    fileToWrite.write(f"\nwith {r.choice(articleOfClothing)}-ripping goodness on the cover. If your friends and family are no help, ")
    fileToWrite.write(f"\ntry checking out the {r.choice(nouns)} Review in \"The {r.choice(cities)} Times\"")
    fileToWrite.write(f"\nIf the {r.choice(pluralNouns)} featured there are too {r.choice(adjectives)} for your taste, ")
    fileToWrite.write(f"\ntry something a little more low-brain, like \"{r.choice(letters)}: The {r.choice(celeberties)} Magazine\", ")
    fileToWrite.write(f"\n\"{r.choice(pluralNouns)} Magazine\". You could also choose a book the {r.choice(adjectives)}-Fashioned way. Head to your")
    fileToWrite.write(f"\nlocal library or {r.choice(places)} and browse the sheleves until something catches your eye.")
    fileToWrite.write(f"\nOr, you could save yourself a whole lot of {r.choice(adjectives)} trouble and log on to 'www.bookish.com', the")
    fileToWrite.write(f"\n{r.choice(adjectives)} new website to browse for books! With all the time you'll save not having to search for {r.choice(pluralNouns)},")
    fileToWrite.write(f"\nyou can read {randomNumber} more books!")
    

    fileToWrite.close()
    print("Done!")

generateMadLibs("text.txt")