import requests, re, random, time
from enclib import search


def gogo_get_download(gogo_category_page, anime_nme):
    print(f"\nFinding gogoanime.pe watch pages for {anime_nme} --> {gogo_category_page}")
    ep_num = 0
    size_total = 0.00
    time_lst = []
    downloadable = []
    while True:
        ep_num += 1
        page = f"https://gogoanime.pe/{gogo_category_page[30:]}-episode-{ep_num}"
        download_link = search(requests.get(page).content, 'dowloads"><a href="', '" target=')
        if not download_link:
            break
        data = requests.get(download_link).content
        size = search(data, 'Size:</label><span id="filesize">', "</span>")
        duration = search(data, 'duration">', "</span>")
        res = search(data, 'Res:</label><span id="filesize">', "</span>")
        try:
            download = "https://storage" + search(data, 'href="https://storage', '" download>Download')
        except:
            download = "NULL"  # todo trigger alternative

        # flag 720p, total download size, total duration
        if res != "1920x1080":
            if res == "1280x720":
                res = "1280x720 <-- WARNING 720p FILE"  # todo trigger alternative
            else:
                res += " <-- WARNING VERY BAD DOWNLOAD. FIND ALTERNATIVE"  # todo trigger alternative

        size_int, null = size.split(" MB")
        if not size_int:
            size_int, null = size.split(" GB")
        size_total += float(size_int)

        time_lst.append(duration)
        print(f"{anime_nme} Ep {ep_num} {download} {size} {duration} {res}")
        downloadable.append(f"{anime_nme}, Ep {ep_num}, {download}, {size}, {duration}, {res}")

    dur_total = 0
    for tm in time_lst:
        time_parts = [int(s) for s in tm.split(':')]
        dur_total += (time_parts[0] * 60 + time_parts[1]) * 60 + time_parts[2]
    total_secs, sec = divmod(dur_total, 60)
    hr, min = divmod(total_secs, 60)
    print(f"Total size and duration for all {ep_num-1} above, size:"
          f" {round(size_total/1000, 2)}GB, dur: %d:%02d:%02d" % (hr, min, sec))

    input("\nWhat would you like to download? ")


def get_links(a, name):
    a = (re.findall(r'(https?://[^\s]+)', str(a))) + (re.findall(r'(http?://[^\s]+)', str(a)))
    urls = []
    for item in a:
        try:
            url, remove = item.split('"')
        except ValueError:
            url = item.lower()

        if not url.endswith("/video") and url.startswith("https://myanimelist.net/anime/") and url not in urls:
            urls.append(url)

    name = name.replace(" ", "_").replace(": ", "__")
    anime_name_1 = ""
    anime_name_2 = ""
    counter = 0
    for i in name:
        counter += 1
        if i in "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- ":
            anime_name_1 += i
            anime_name_2 += i
        else:
            if not len(name) == counter:
                anime_name_2 += "_"

    for url in urls:
        if name in url and url.endswith(name):
            return url
        if anime_name_1 in url and url.endswith(anime_name_1):
            return url
        if anime_name_2 in url and url.endswith(anime_name_2):
            return url

    def edits1(word):
        alphabet = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_: "
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a+b[1:] for a, b in splits if b]
        transposes = [a+b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
        replaces = [a+c+b[1:] for a, b in splits for c in alphabet if b]
        inserts = [a+c+b for a, b in splits for c in alphabet]
        return set(deletes + transposes + replaces + inserts)

    urls2 = []
    for item in edits1(name):
        for url in urls:
            if item.lower().replace(" ", "_").replace(": ", "__") in url.lower():
                if url not in urls2:
                    urls2.append(url)
            if item.lower().replace(" ", "_").replace(": ", "__ ") in url.lower():
                if url not in urls2:
                    urls2.append(url)
    if urls2:
        return urls2
    else:
        return urls


load_user_data = True

if load_user_data:
    user_anime_list = requests.get("https://myanimelist.net/animelist/rapidslayer101").content
    #user_anime_list = requests.get("https://myanimelist.net/animelist/BappoHacko").content
    table_data = search(user_anime_list, '<table class="list-table" data-items="',
                        '<tbody><tr class="list-table-header">')[:-12].split("{&quot;status&quot;:")

    watched_ttl = 0
    for item in table_data[1:]:
        if item[:1] == "1":
            status = "Watching"
        if item[:1] == "2":
            status = "Completed"
        if item[:1] == "3":
            status = "On Hold"
        if item[:1] == "4":
            status = "Dropped"
        if item[:1] == "6":
            status = "Plan to Watch"

        air_type = search(item, "anime_airing_status&quot;:", ",&quot;")
        if air_type == "1":
            air_type = "Airing"
        if air_type == "2":
            air_type = "Aired"
        if air_type == "3":
            air_type = "Not yet aired"

        anime_title = search(item, "anime_title&quot;:&quot;", "&quot;,&quot;")
        score = search(item, "score&quot;:", ",&quot;")
        watched = search(item, "num_watched_episodes&quot;:", ",&quot;")
        total_eps = search(item, "anime_num_episodes&quot;:", ",&quot;")  # todo amount aired, use gogo
        mpaa = search(item, "anime_mpaa_rating_string&quot;:&quot;", "&quot;,&quot;")
        media_type = search(item, "anime_media_type_string&quot;:&quot;", "&quot;,&quot;")
        anime_id = search(item, "anime_id&quot;:", ",&quot;")

        with open("mal_watched.txt", "a+") as f:
            f.write(f"https://myanimelist.net/anime/{anime_id} -- {anime_title} - {media_type} ({air_type})({mpaa}): {status},"
                    f" scored {score}, watched eps {watched}/{total_eps}")
        print(f"https://myanimelist.net/anime/{anime_id} -- {anime_title} - {media_type} ({air_type})({mpaa}): {status},"
              f" scored {score}, watched eps {watched}/{total_eps}")

        watched_ttl += int(watched)

        # todo add this data to a list thing that can be accessed later down script

    print(f"You have watched {watched_ttl} anime eps")


def anime_data(url):
    page_data = requests.get(url).content
    name_data = search(page_data, "<title>", "- MyAnimeList.net").replace("\\n", "")
    null, score = search(page_data, "score-label score-", "</span>").replace("\\n", "").split(">")
    rank = search(page_data, "Ranked:</span>", "<sup>").replace("\\n", "").replace(" ", "")
    popularity = search(page_data, "Popularity:</span>", "</div>").replace("\\n", "").replace(" ", "")
    members = search(page_data, "Members:</span>", "</div>").replace("\\n", "").replace(" ", "")
    eps = search(page_data, "Episodes:</span>", "</div>").replace("\\n", "").replace(" ", "")
    ep_duration = search(page_data, "Duration:</span>", "</div>")\
        .replace("\\n", "").replace("   ", "").replace("  ", "")

    genres = search(page_data, "Genres:</span>", "</div>").split('style="display: none">')
    genre_lst = "".join([genre.split("</span>")[0]+", " for genre in genres[1:]])[:-2]

    if name_data.endswith(" "):
        name_data = name_data[:-1]

    try:
        ep_dur, null = ep_duration.split(" min.")
    except:
        ep_duration = "NULL"

    try:
        dur_ttl = f" ({round(int(ep_dur) * int(eps) / 60, 2)} hours total)"
    except:
        dur_ttl = ""

    with open("mal_data.txt", "a+") as f:
        f.write(f"{url} --- {name_data} -- {eps} Episodes with a duration of {ep_duration}{dur_ttl},"
                f" Score: {score}, Ranked: {rank}, Popularity: {popularity}, Members: {members}, Genres: {genre_lst}\n")
    print(f"\n{url} --- {name_data}\n{eps} Episodes with a duration of {ep_duration}{dur_ttl},"
          f" Score: {score}, Ranked: {rank}, Popularity: {popularity}, Members: {members}, Genres: {genre_lst}")

    # linked anime's here

    prequel = False
    while prequel:
        try:
            prequel = "https://myanimelist.net/" \
                      + search(page_data, 'Prequel:</td><td width="100%" class="borderClass"><a href="', '">')
            print(prequel)
            page_data = requests.get(prequel).content
        except:
            prequel = False
    # print("Prequel loop exited, now checking upwards")  # todo go upwards / across if alternatives


anime_finder = True

if anime_finder:
    anime_name = input("Anime name: ").replace("(", "").replace(")", "")  # or link
    # print("\nEnter 'y' to include related anime search, leave blank for just download pages")
    # if input().lower() == "y": # todo toggles the searching of related anime

    print(f"\nSearching for: {anime_name}")
    print(f"\nSearching for: {anime_name}")
    anime_name = anime_name.replace(": ", "__")
    page = f"https://myanimelist.net/anime.php?q={anime_name.replace(' ', '+')}&cat=anime"
    print(f"Finding MAL page --> {page}")
    anime_mal_link = get_links(requests.get(page).content, anime_name)
    if type(anime_mal_link) == list:
        if len(anime_mal_link) == 1:
            anime_mal_link = str(anime_mal_link)[2:-2]
        else:
            print("Autodetect failed, enter a number from below")
            counter = 0
            for url in anime_mal_link:
                # todo redo the genre and season 2 links removal
                counter += 1
                if not counter > 30:
                    print(f"{counter} - {url}")
            while True:
                try:
                    anime_mal_link = anime_mal_link[int(input())-1]
                    break
                except:
                    print("Invalid input")
    print(f"MAL page found, collecting page data <--> {anime_mal_link}")

    anime_data(anime_mal_link)
    anime_name_old = anime_name.replace("__", " ")


#start_point = int(input("Input last number in txt: "))+1
#for i in range(53000-start_point):
#    try:
#        anime_data(f"https://myanimelist.net/anime/{i+start_point}")
#        time.sleep(1)
#    except AttributeError:
#        print(f"Error {i+start_point}")
#        time.sleep(0.35)
#input()
# grab name out of MAL url

anime_name = anime_mal_link.split("/")[-1].replace("__", ": ").replace("_", " ")

# generate watch sites

while True:
    lang = input("\nSUB or DUB: ").lower()
    if lang == "sub":
        sub = True
        break
    if lang == "dub":
        print("BELOW LINKS MAY NOT HAVE ANY RESULTS AS DUB IS SELECTED")
        sub = False
        break


print(f"{lang.upper()} pages for 9anime.to and gogoanime.pe")
# 9anime.to
if sub:
    print(f"https://9anime.to/filter?language%5B%5D=subbed&keyword={anime_name.replace(' ', '+').replace(':', '%3A')}")
else:
    print(f"https://9anime.to/filter?language%5B%5D=dubbed&keyword={anime_name.replace(' ', '+').replace(':', '%3A')}")

# gogoanime.pe
try:
    if sub:
        page = f"https://gogoanime.pe//search.html?keyword={anime_name.replace(' ', '%20')}"
    else:
        page = f"https://gogoanime.pe//search.html?keyword={anime_name.replace(' ', '%20')}%20(Dub)"
    data = requests.get(page).content
    gogo_category_page = "https://gogoanime.pe/category/" + search(data, '<a href="/category/', '" title=')
    print(f"{gogo_category_page}")
except:
    print("Special char caused an error")  # todo fix this

# generate download links

input("Hit enter to collect download links")
gogo_get_download(gogo_category_page, anime_name)
