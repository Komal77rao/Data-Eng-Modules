
class User:
    def __init__(self,store, name):
        self.name = name
        self.store = store
        self.id = len(store['users']) + 1
        store['users'][self.id] = self
    
    def viewings(self):
        return [v for k,v in self.store['viewings'].items() if self.name == v.user.name ]

    def episodes(self):
        return [v.episode for k,v in self.store['viewings'].items() if self.name == v.user.name ]

    def find_viewings_for(self, episode):
        return [v for k,v in self.store['viewings'].items() if episode.id == v.episode.id]

    def last_stop_time_for(self, episode):
        viewings = self.find_viewings_for(episode)
        return viewings[-1].stop_time
