init 20 python: 
    def adjust_relationship(self, character, **changes):
        """Change relationship values"""
        if character not in self.relationships:
            self.relationships[character] = {"trust": 50, "romance": 0}
        
        for stat, delta in changes.items():
            current = self.relationships[character].get(stat, 0)
            self.relationships[character][stat] = max(0, min(100, current + delta))

    GameState.adjust_relationship = adjust_relationship