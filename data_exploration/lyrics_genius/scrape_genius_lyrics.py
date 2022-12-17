import lyricsgenius as genius  # https://github.com/johnwmillr/LyricsGenius

LYRICS_DIR = "../data/genius_lyrics"


def scrape_lyrics(song_name, artist_name):
    """Scrape lyrcis on Genius and returns the lyrics.

    :param song_name: song name of the lyrics we want to scrape.
    :param artist_name: artist name of the lyrics we want to scrape.

    :return: Lyrics of given song and artist name.
    :rtype: String or None
    """

    api_token = "TQdTzth8QuovVPC3AWrU4EPADP2v2mil2_TXw0xWA-50wmFgsK8-04UWD6vRRLkR"

    api = genius.Genius(api_token)

    # Search for song
    song = api.search_song(song_name, artist_name)

    if song is not None:
        print("Song found.")
        # return lyrics
        return song.lyrics
    else:
        print("Song not found.")
        return None