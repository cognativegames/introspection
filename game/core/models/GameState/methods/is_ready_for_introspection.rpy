init 20 python:
    def is_ready_for_introspection(self):
        """Check if player should be offered introspection"""
        # Offer after 2+ negative interpretations
        if self.interpretation_streak['negative'] >= 2:
            return True
        # Or if emotional distress is high
        if self.emotions['anxiety'] > 70 or self.emotions['overwhelm'] > 70:
            return True
        return False

    GameState.is_ready_for_introspection = is_ready_for_introspection