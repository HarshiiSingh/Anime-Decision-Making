# This is a decision maker project that will help to reccomend what anime to watch
# Lists, Random Module, Input()
# Pandas (for data frames), APIs
# Jikan
# Use dataframes to create tables to query through the sites

import random


def show_selector(genres, input_list):

    anime_list = [
        ["Tokyo Ghoul", "horror", "action"], ["Eighty Six", "action", "drama", "sci-Fi"],
        ["Vivy: Fluorite Song", "action", "sci-Fi", "suspense"], ["Re:Zero", "drama", "fantasy", "suspense"],
        ["Chainsaw Man", "action", "fantasy"]
    ]
    for show_genres in anime_list:
        if all(show in show_genres for show in genres):
            input_list.append(show_genres)


show_list = []
genre = input("What genre's do you wish to watch? (Use a comma to separate between genres) ").lower()
all_genres = genre.split(", ")
show_selector(all_genres, show_list)

if not show_list:
    print("There is no show with those selected genres.")
else:
    answers = input("Do you wish to have all options or randomly pick one? (All or Random) ").lower()
    if answers == "all":
        print("These shows below match with the genre's you've selected.")
        for show in show_list:
            print(show)
    elif answers == "random":
        print("You should watch: ", random.choice(show_list))
    else:
        print("Please type either All or random.")


