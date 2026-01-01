init 20 python:
    def get_active_negative_beliefs(self):
        """Get all active negative beliefs"""
        result = []
        for bid, intensity in self.beliefs.items():
            if intensity in [BELIEF_INTENSITY_ACTIVE, BELIEF_INTENSITY_CORE]:
                if bid in beliefs:
                    if beliefs[bid]['type'] == 'negative':
                        result.append(bid)
        return result

    GameState.get_active_negative_beliefs = get_active_negative_beliefs