
MENU_PROMPT = """\nEnter:- 
'a' to add a movie, 
'l' to see your movies, 
'f' to find a movie, 
'r' to remove a movie, 
'q' to quit.
Enter your selection: """
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        "title": title,
        "director": director,
        "year": year

    })

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
    print(f"{movie['title']}, by {movie['director']} and released in {movie['year']}.")

def find_movies():
    search_title = input("Enter the movie title: ")
    for movie in movies:
        if movie['title'] == search_title:
            print_movie(movie)

def remove_movie():
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie['title'] == title:
            movies.remove(movie)

def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movies()
        elif selection == 'r':
            remove_movie()
        else:
            print('Unknown command. Please try again.')
        selection = input(MENU_PROMPT)


menu()

