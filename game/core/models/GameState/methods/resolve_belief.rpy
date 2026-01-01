init 20 python:
    def resolve_belief(self, negative_id, positive_id):
        """Transform negative belief into positive"""
        self.beliefs[negative_id] = BELIEF_INTENSITY_RESOLVED
        self.beliefs[positive_id] = BELIEF_INTENSITY_CORE
        self.introspection_depth += 1
    
    GameState.resolve_belief = resolve_belief