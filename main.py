
print("===================================")
print("          AI BOOKMATCH")
print("===================================")
print("Let's find a book for you!\n")

# Step 1: Ask the user for preferences

name = input("What is your name? ")

mood = input(
    "How are you feeling? (happy, curious, stressed): "
).lower().strip()

genre = input(
    "Choose a genre (fantasy, mystery, romance, science, self-help): "
).lower().strip()

purpose = input(
    "Your goal? (fun, study, personal-growth): "
).lower().strip()


# Step 2: Create our book collection

books = [
    {
        "title": "Harry Potter and the Philosopher's Stone",
        "genre": "fantasy",
        "mood": "curious",
        "purpose": "fun"
    },
    {
        "title": "The Hobbit",
        "genre": "fantasy",
        "mood": "happy",
        "purpose": "fun"
    },
    {
        "title": "And Then There Were None",
        "genre": "mystery",
        "mood": "curious",
        "purpose": "fun"
    },
    {
        "title": "Gone Girl",
        "genre": "mystery",
        "mood": "stressed",
        "purpose": "fun"
    },
    {
        "title": "Pride and Prejudice",
        "genre": "romance",
        "mood": "happy",
        "purpose": "fun"
    },
    {
        "title": "The Fault in Our Stars",
        "genre": "romance",
        "mood": "stressed",
        "purpose": "fun"
    },
    {
        "title": "A Brief History of Time",
        "genre": "science",
        "mood": "curious",
        "purpose": "study"
    },
    {
        "title": "A Short History of Nearly Everything",
        "genre": "science",
        "mood": "happy",
        "purpose": "study"
    },
    {
        "title": "Atomic Habits",
        "genre": "self-help",
        "mood": "stressed",
        "purpose": "personal-growth"
    },
    {
        "title": "The Power of Now",
        "genre": "self-help",
        "mood": "happy",
        "purpose": "personal-growth"
    }
]


# Step 3: Calculate a score for every book

recommendations = []

for book in books:
    score = 0
    reasons = []

    if book["mood"] == mood:
        score += 1
        reasons.append("matches your mood")

    if book["genre"] == genre:
        score += 1
        reasons.append("matches your genre")

    if book["purpose"] == purpose:
        score += 1
        reasons.append("matches your goal")

    if score > 0:
        recommendations.append((score, book["title"], reasons))


# Step 4: Rank the books by score

recommendations.sort(key=lambda item: item[0], reverse=True)


# Step 5: Display the top three recommendations

print("\n===================================")
print("       YOUR BOOKMATCH RESULTS")
print("===================================")

if len(recommendations) == 0:
    print("No matching books found.")
    print("Try changing your preferences.")

else:
    print("Happy reading,", name + "!")
    print("\nHere are your top recommendations:\n")

    for score, title, reasons in recommendations[:3]:
        print("Book:", title)
        print("Match score:", score, "out of 3")
        print("Why:", ", ".join(reasons))
        print("-----------------------------------")

print("Thank you for using BookMatch!")
