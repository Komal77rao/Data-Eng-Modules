class NetflixPlayer:
    def __init__(self):
        pass

    def play_viewing(self, viewing):
        return viewing.episode

    def play_episode_for(self, store, user, episode):
        last_stop_time = user.last_stop_time_for(episode)
        viewing = user.find_viewings_for(episode)[-1]
        #viewing = [v for k,v in store['viewings'].items() if episode.id == v.episode.id][-1]
        viewing.start_time = last_stop_time
        

        
        



