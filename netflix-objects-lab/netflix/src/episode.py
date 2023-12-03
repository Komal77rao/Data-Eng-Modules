from src.index import build_store
store = build_store()

class Episode:
    def __init__(self, store, title):
        self.title = title
        self.store = store
        self.id = len(store['episodes']) + 1
        store['episodes'][self.id] = self

    def words(self):
        list_of_words = self.script.split()
        return list_of_words

    def viewings(self):
       return [v for k,v in self.store['viewings'].items() if self.id == v.episode_id]
    
    def users(self):
        return [v.user for k,v in self.store['viewings'].items() if self.id == v.episode_id]

    def end_time(self):
        return len(self.words()) * 2.5