with open("mal_watched.txt") as f:
    watched = f.read()

with open("mal_data.txt") as f:
    lines = f.readlines()

with open("mal_data_filtered.txt", "w") as f:
    f.write("")


# settings

remove_watched = True  # remove anime you have already watched
min_mem = 100000  # min members required that have added
min_ep_duration = 18  # min episode duration in minutes
req_genres_all = ["romance"]  # list of required genres all must be present
req_genres_either = ["romance", "comedy"]  # list of required genres one must be present
no_allow_genre = ["boys love"]  # genres to remove
excluded_strings = ["To LOVE-Ru", "Date A Live"]  # strings that can't be in name
remove_ova = True  # try to remove OVA's, will very likely have false positives
remove_movie = True  # try to remove movies, possibly false positives
max_episodes = 30  # max amount of episodes
min_episodes = 9  # min amount of episodes

count = 0
for line in lines:
    link, line = line.split(" --- ")
    name, line = line.split(" -- ")
    episodes, line = line.split(" Episodes with a duration of ")
    try:
        duration, line = line.split(". per ep. (")
        runtime, line = line.split(" hours total), Score: ")
    except ValueError:
        duration, line = line.split(", Score: ")
        runtime = duration
    score, line = line.split(", Ranked: ")
    rank, line = line.split(", Popularity: ")
    pop, line = line.split(", Members: ")
    mem, genres = line.split(", Genres: ")

    allow = False
    for genre_name in req_genres_either:
        if genre_name in genres.lower():
            allow = True

    for genre_name in req_genres_all:
        if genre_name not in genres.lower():
            allow = False

    for genre_name in no_allow_genre:
        if genre_name in genres.lower():
            allow = False

    if int(mem.replace(",", "")) < min_mem:
        allow = False

    if "min" in duration:
        duration = duration.split(" (")[0].replace(" min", "")
        if "hr." in duration:
            hrs, duration = duration.replace(" hr.", "").replace(".", "").split(" ")[:2]
            duration = int(duration)
            duration += int(hrs)*60
        if int(str(duration).replace(".", "")) < min_ep_duration:
            allow = False

    if remove_ova:
        if episodes != "Unknown" and duration != "NULL":
            duration = int(str(duration).replace(".", ""))
            if int(episodes) == 1 and duration < 40:  # ova removal
                allow = False

            if 1 < int(episodes) < min_episodes:
                allow = False

            if int(episodes) > max_episodes:
                allow = False

    if remove_movie:
        if episodes != "Unknown" and duration != "NULL":
            duration = int(str(duration).replace(".", ""))
            if int(episodes) == 1 and duration > 39:  # movie removal
                allow = False

    if remove_watched:
        if link in watched:
            allow = False

    for string in excluded_strings:
        if string.lower() in name.lower():
            allow = False

    if allow:
        with open("mal_data_filtered.txt", "a+", encoding="utf-8") as f:
            f.write(f"{link} {name} -- {duration}Mpe x {episodes} ({runtime}Hrs) Score:{score} Rank:{rank} "
                    f"Popularity:{pop} Members:{mem} Genres:{genres}")
        print(f"{link} {name} -- {duration}Mpe x {episodes} ({runtime}Hrs) Score:{score} Rank:{rank} "
              f"Popularity:{pop} Members:{mem} Genres:{genres}".replace("\n", ""))
        count += 1

print(f"There are {count}/{len(lines)} anime's that meet your requirements")
