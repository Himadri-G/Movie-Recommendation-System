# Sample movie database: (title, genre, rating)
movies = [
    ("Inception", "Sci-Fi", 8.8),
    ("The Dark Knight", "Action", 9.0),
    ("Titanic", "Romance", 7.8),
    ("Avengers: Endgame", "Action", 8.4),
    ("Interstellar", "Sci-Fi", 8.6),
    ("The Notebook", "Romance", 7.9)
]

# Set to store movies the user has already seen
seen_movies = set()

# Function to display genres
def display_genres():
    genres = {"Action", "Romance", "Sci-Fi", "Comedy"}
    print("\nAvailable genres:")
    for genre in genres:
        print(genre)
    return genres

# Function to get user's favorite genres
def get_user_genres():
    user_genres = input("\nEnter your favorite genres, separated by commas: ").split(',')
    return [genre.strip() for genre in user_genres]

# Function to recommend movies
def recommend_movies(favorite_genres):
    recommendations = []
    for movie in movies:
        title, genre, rating = movie
        if genre in favorite_genres and title not in seen_movies:
            recommendations.append(movie)
    return recommendations

# Function to mark a movie as watched
def mark_as_watched(movie_title):
    seen_movies.add(movie_title)
    print(f"\nYou have marked '{movie_title}' as watched.")

# Main Program
def main():
    while True:
        print("\n--- Movie Recommendation System ---")
        available_genres = display_genres()
        
        # Get user genres
        user_genres = get_user_genres()
        
        # Recommend movies
        recommendations = recommend_movies(user_genres)
        if recommendations:
            print("\nRecommended Movies:")
            for title, genre, rating in recommendations:
                print(f"{title} - {genre} (Rating: {rating})")
        else:
            print("\nNo recommendations available for your selected genres.")

        # Mark a movie as watched
        watched_movie = input("\nEnter the name of the movie you watched (or 'exit' to quit): ")
        if watched_movie.lower() == 'exit':
            break
        else:
            mark_as_watched(watched_movie)

# Run the program
main()
