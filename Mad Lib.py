# A Madlib game where users are asked to input a couple of words to create a fun story game.

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")

story = f"""
Today I went to {place}
I saw a very {adjective} {animal}
It {verb} past me while holding a {noun}
I couldn't believe how {adjective} it was!
"""
print("\nHere is your Mad Lib Story:")
print(story)