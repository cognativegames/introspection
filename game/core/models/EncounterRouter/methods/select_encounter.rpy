init 20 python:
    def select_encounter(self, state):
        """Select best encounter for current state"""
        
        candidates = []
        
        # If they have high anxiety, offer calming encounters
        if state.emotions["anxiety"] > 70:
            candidates = [e for e in self.encounter_vault.values() 
            if "calming" in e.get("tags", [])]
        
        # If they've resolved core beliefs, unlock deeper encounters
        elif state.introspection_depth >= 3:
            candidates = [e for e in self.encounter_vault.values() 
            if e.get("requires_depth", 0) <= state.introspection_depth]
        
        # If certain belief is active, address it
        elif "self.is_unworthy" in state.get_active_negative_beliefs():
            candidates = [e for e in self.encounter_vault.values() 
            if "self.is_unworthy" in e["addresses_beliefs"]]
        
        # Default encounters
        else:
            candidates = [e for e in self.encounter_vault.values() 
            if e.get("is_default")]
        
        # Filter out recently used
        candidates = [e for e in candidates if e['id'] not in self.used_encounters]
        
        if candidates:
            return random.choice(candidates)
        else:
            # Reset and pick any
            self.used_encounters.clear()
            return random.choice(list(self.encounter_vault.values()))

    EncounterRouter.select_encounter = select_encounter