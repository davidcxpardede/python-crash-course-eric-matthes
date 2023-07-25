'''
Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print eachr eturn value to show that the dictionaries are storing the album information correctly.
Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. IF the calling line includes a value for the nubmer of songs, add that value to the album's dictionary. Make at least one new function call that includes the number of songs on an album.
'''

def make_album(artist_name, album_title, number_of_songs=None):
    """Create dictionaries that store information about a music albums."""
    
    music_album = {'artist': artist_name,
                   'title': album_title,
                   }
    
    if number_of_songs:
        music_album['song_number'] = number_of_songs
    
    return music_album

print(make_album('MLTR', 'Nothing to Lose'))
print(make_album('Steelheart', 'Good 2B Alive', 7))
print(make_album('Marsada', 'Pulo Samosir'))

    