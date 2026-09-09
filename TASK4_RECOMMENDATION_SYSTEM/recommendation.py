# Simple Movie Recommendation System

movies = {
    "Inception": "Sci-Fi Thriller",
    "Interstellar": "Sci-Fi Adventure",
    "The Matrix": "Sci-Fi Action",
    "Avengers": "Action Adventure",
    "John Wick": "Action Thriller",
    "Titanic": "Romance Drama",
    "The Notebook": "Romance Drama",
    "Harry Potter": "Fantasy Adventure",
    "Lord of the Rings": "Fantasy Adventure"
}

genre = input("Enter your favorite genre: ").lower()

print("\nRecommended Movies:")

found = False

for movie, genres in movies.items():
    if genre in genres.lower():
        print("-", movie)
        found = True

if not found:
    print("Sorry, no movies found for this genre.")