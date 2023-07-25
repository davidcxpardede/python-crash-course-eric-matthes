'''
Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. Loop through the dictionary, and print each person's name and their favorite places.
'''

favorite_places = {'rinto': ['United States'],
                  'marbun': ['Japan', 'Argentina'],
                  'petrik': ['Russia', 'Japan', 'France'],}

for person, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{person.title()}'s favorite place is {places[0]}.")
    else:
        print(f"\n{person.title()}'s favorite places are: ")
        for place in places:
            print(f"\t{place}")
    