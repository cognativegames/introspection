init 20 python:
    def get_relationship_level(self, character, stat="trust"):
        """Get relationship tier: stranger, friend, close, intimate"""
        value = self.relationships.get(character, {}).get(stat, 0)
        if value < 25: return "stranger"
        elif value < 50: return "acquaintance"
        elif value < 75: return "friend"
        else: return "close"

    GameState.get_relationship_level = get_relationship_level