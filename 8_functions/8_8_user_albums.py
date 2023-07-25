'''
Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.
'''

def make_album(artist_name, album_title, songs_number=None):
    """Create dictionaries that store information about a music albums."""
        
    music_album = {'artist': artist_name,
                   'title': album_title,
                   }
    
    if songs_number:
        music_album['number_of_songs'] = songs_number
    
    return music_album

while True:
    print("Enter the name of artist, album title, and number of songs (optional).\nEnter 'q' if you are finished.")

    name_of_artist = input("Name of the artist: ")
    if name_of_artist.lower() == 'q':
        break
    
    title_of_album = input("Title of the album: ")
    if title_of_album.lower() == 'q':
        break
    
    number_of_songs = input("Number of songs (optional): ")
    if number_of_songs.lower() == 'q':
        break
    
    print(make_album(name_of_artist, title_of_album, number_of_songs))

    
