init 20 python:
    def get_dominant_emotion(self):
        """Return the strongest current emotion"""
        return max(self.emotions.items(), key=lambda x: x[1])[0]

    GameState.get_dominant_emotion = get_dominant_emotion