"""
To experiment with this code freely you will have to run this code locally.
Take a look at the main() function for an example of how to use the code. We
have provided example json output in the other code editor tabs for you to look
at, but you will not be able to run any queries through our UI.
"""
import json
import requests

BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"


# query parameters are given to the requests.get function as a dictionary; this
# variable contains some starter parameters.
query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print("requesting", r.url)

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    """
    After we get our output, we can use this function to format it to be more
    readable.
    """
    if type(data) == dict:
        print(json.dumps(data, indent=indent, sort_keys=True))
    else:
        print(data)


def main():
    """
    Below is an example investigation to help you get started in your
    exploration. Modify the function calls and indexing below to answer the
    questions on the next quiz.

    HINT: Note how the output we get from the site is a multi-level JSON
    document, so try making print statements to step through the structure one
    level at a time or copy the output to a separate output file. Experimenting
    and iteration will be key to understand the structure of the data!
    """
    # Quiz 1: How many bands named "First Aid Kit" => 2
    count_fak = 0
    query_fak = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
    for artist in query_fak["artists"]:
        if " ".join(artist["name"].lower().split()) == "first aid kit":
            count_fak += 1
    print(f"\nQuiz 1: How many bands named 'First Aid Kit': {count_fak}")

    # Quiz 2: Begin area for Queen => "London"
    query_queen = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    for artist in query_queen["artists"]:
        if (" ".join(artist["name"].lower().split()) == "queen") and ("begin-area" in artist):
            print("\nQuiz 2: Begin area for Queen")
            pretty_print(artist)

    # Quiz 3: Spanish alias for Beatles => Los Beatles
    query_beatles = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    for artist in query_beatles["artists"]:
        if (" ".join(artist["name"].lower().split()) == "the beatles") and ("aliases" in artist):
            for alias in artist["aliases"]:
                if alias["locale"] == "es":
                    print("\nQuiz 3: Spanish alias for Beatles")
                    pretty_print(alias)

    # Quiz 4: Nirvana disambiguation => 90s US grunge band
    query_nirvana = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    for artist in query_nirvana["artists"]:
        if (" ".join(artist["name"].lower().split()) == "nirvana") and ("disambiguation" in artist):
            print("\nQuiz 4: Nirvana disambiguation")
            pretty_print(artist)
 
    # Quiz 5: When was "One Direction" formed => 2010
    query_on = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    for artist in query_on["artists"]:
        if (" ".join(artist["name"].lower().split()) == "one direction")  and ("life-span" in artist):
            print("\nQuiz 5: When was "One Direction" formed")
            pretty_print(artist)


if __name__ == '__main__':
    main()