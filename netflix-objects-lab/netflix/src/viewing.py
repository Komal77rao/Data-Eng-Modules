class Viewing:
    def __init__(self, store, user, episode):
        self.store = store
        self.user = user
        self.episode = episode
        self.id = len(store['viewings']) + 1
        store['viewings'][self.id] = self
        if episode:
            self.episode_id = episode.id

    def words(self):
        total_words = int((self.stop_time - self.start_time ) *2.5)
        list_of_words = self.episode.words()
        result = list_of_words[0:total_words]
        return result
    
    def script(self):
        return " ".join(self.words())
        

