init 20 python:
    def activate_belief(self, belief_id, intensity=BELIEF_INTENSITY_SURFACE):
        """Activate or intensify a belief"""
        current = self.beliefs.get(belief_id, BELIEF_INTENSITY_DORMANT)
        new_intensity = max(current, intensity)
        self.beliefs[belief_id] = new_intensity
        self.belief_history.append({
            "belief": belief_id,
            "intensity": new_intensity,
            "scene": self.scene_count
        })
    
    GameState.activate_belief = activate_belief