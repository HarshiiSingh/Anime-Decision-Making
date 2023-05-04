import requests
import random
from genre_names_and_id import genres

# Base URL for the Jikan API
BASE_URL = "https://api.jikan.moe/v4"

# Genre IDs for inputted genre
genre_list = []
genre_name = input("What genre's do you wish to watch? (Use a comma to separate between genres) ").title()
all_genres = genre_name.split(", ")
delimiter = ", "
anime_matchmaker = True


# Create a string to add towards the BASE_URL
for name in all_genres:
    if name not in genres:
        print("This is not an applicable genre")
        anime_matchmaker = False
        break
    genre_list.append(genres[name])
GENRE_ID = delimiter.join(str(word) for word in genre_list)

while anime_matchmaker:

    # Parameters for the API request
    params = {
        "genres": GENRE_ID,
        "limit": 100,
        "order_by": "score",
        "sort": "desc"
    }

    # Make the request to the API
    response = requests.get(f"{BASE_URL}/anime", params=params)

    # Check if the request was successful
    if response.status_code == 200:

        # Get the data from the response
        data = response.json()["data"]

        # Randomly select 10 anime from the data
        random_data = random.sample(data, 10)

        answers = input("Do you wish to have all options or randomly pick one? (All or Random) ").lower()

        if answers == "all":

            print("These shows below match with the genre's you've selected. \n")

            # Loop through the results and print the title of each anime
            for anime in random_data:
                print(anime["title"])

            anime_matchmaker = False

        elif answers == "random":

            anime_choice = []

            for anime in random_data:
                anime_choice.append(anime["title"])
            print("You should watch: ", random.choice(anime_choice))

            anime_matchmaker = False

        else:
            print("Please type either All or random.")

    else:

        # Print an error message if the request was unsuccessful
        print(f"Error: {response.status_code}")
