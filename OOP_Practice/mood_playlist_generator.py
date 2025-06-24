# The Class Playlist is designed to generate a playlist based on the user's mood input.

class Playlist:
    def __init__(self):
        self.songs = []
        self.mood = "" 
        
    def set_mood(self, mood_input):
        self.mood = mood_input.lower()
    
    def generate_songs(self):
        if self.mood == "happy":
            self.songs = ["Happy - Pharrell", "Best Day of My Life - American Authors"]
        elif self.mood == "sad":
            self.songs = ["Someone Like You - Adele", "Fix You - Coldplay"]
        elif self.mood == "motivated":
            self.songs = ["Eye of the Tiger - Survivor", "Stronger - Kanye West"]
        elif self.mood == "chill":
            self.songs = ["Sunflower - Post Malone", "Better Together - Jack Johnson"]
        else:
            self.songs = ["No songs found for this mood."]

    
    def show_playlist(self):
        print("\n🎧 Your Playlist:")
        for song in self.songs:
            print(song)


# Creating object of Playlist
my_playlist = Playlist()

# Taking mood input from user
mood_input = input("What's your mood? (happy/sad/motivated/chill): ")
my_playlist.set_mood(mood_input)

# Generating and showing playlist
my_playlist.generate_songs()
my_playlist.show_playlist()

# End of the code