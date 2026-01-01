init 20 python:
    def check_achievements(self):
        """Check for unlockable achievements"""
        # First breakthrough
        if (self.introspection_depth == 1 and 
            "first_breakthrough" not in self.achievements):
            self.achievements.add("first_breakthrough")
            self.rewards_unlocked.append({
                "type": "achievement",
                "name": "The First Crack",
                "description": "You saw through a limiting belief"
            })
        
        # Resolved 5 beliefs
        resolved = len([b for b, i in self.beliefs.items() 
                    if i == BELIEF_INTENSITY_RESOLVED])

        if resolved >= 5 and "five_beliefs" not in self.achievements:
            self.achievements.add("five_beliefs")
            self.rewards_unlocked.append({
                "type": "achievement",
                "name": "Metamorphosis",
                "description": "Transformed 5 limiting beliefs"
            })
            # Unlock special encounter
            self.story_flags.add("metamorphosis_unlocked")
    
        # Perfect positive streak
        if (self.interpretation_streak['positive'] >= 5 and
            "clarity_streak" not in self.achievements):
            self.achievements.add("clarity_streak")
            # Unlock bonus content
            self.story_flags.add("clarity_master")
    
    GameState.check_achievements = check_achievements