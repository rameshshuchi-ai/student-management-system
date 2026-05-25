# Book Recommendation System using Python

print("=================================")
print("   BOOK RECOMMENDATION SYSTEM")
print("=================================")

# Dictionary containing book categories and books
books = {
    "Story": ["Harry Potter", "Cinderella", "Aladdin"],
    
    "Science": ["Physics Basics", 
                "Space Science", 
                "Human Body"],

    "Technology": ["Python Programming", 
                   "Web Development", 
                   "Artificial Intelligence"],

    "History": ["Indian History", 
                "World War 2", 
                "Ancient Civilization"]
}

# Display categories
print("\nAvailable Categories:")
for category in books:
    print("-", category)

# Get user input
choice = input("\nEnter your favorite category: ")

# Check category and display books
if choice in books:

    print("\nRecommended Books:")
    
    for book in books[choice]:
        print("•", book)

else:
    print("\nSorry! Category not available.")

print("\nThank You for Using the System")