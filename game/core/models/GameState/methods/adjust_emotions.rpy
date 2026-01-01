init 20 python:
    def adjust_emotions(self, **changes):
        """Adjust emotional state with bounds"""
        for emotion, delta in changes.items():
            if emotion in self.emotions:
                self.emotions[emotion] = max(0, min(100, 
                    self.emotions[emotion] + delta))
    
    GameState.adjust_emotions = adjust_emotions