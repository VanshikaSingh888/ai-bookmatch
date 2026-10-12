
print("=== AI BookMatch ===")
print("Find your next favourite book!")

name = input("What is your name? ")
genre = input("Choose a genre (fantasy, mystery, romance): ")

if genre.lower() == "fantasy":
    print("Try Harry Potter and the Philosopher's Stone!")
elif genre.lower() == "mystery":
    print("Try And Then There Were None!")
elif genre.lower() == "romance":
    print("Try Pride and Prejudice!")
else:
    print("Sorry, I don't know that genre yet.")

print("Happy reading,", name + "!")
