# Introspection - Core State Machine & Encounter Router
# ./game/introspection_core.rpy

init python:
    import json
    import random


    narrative_sequences = {
        "chapter1_intro": ["dog_park", "stranger_smile"],
        "chapter1_crisis": [],
        "chapter2_deeper": [],
    }
    
    # ============================================
    # HELPER FUNCTIONS
    # ============================================
    
    def process_interpretation(interpretation, encounter):
        """Process player's interpretation choice"""
        
        # Activate beliefs
        for belief_id in interpretation['activates']:
            game.activate_belief(belief_id, interpretation['intensity'])
        
        # Adjust emotions
        game.adjust_emotions(**interpretation['emotion_shift'])
        
        # Track streak
        if interpretation['aligns']:
            game.interpretation_streak['positive'] += 1
            game.interpretation_streak['negative'] = 0
        else:
            game.interpretation_streak['negative'] += 1
            game.interpretation_streak['positive'] = 0
        
        # Determine next phase
        if not interpretation['aligns'] and game.is_ready_for_introspection():
            game.phase = GAME_PHASE_INTROSPECT
            return "introspect_offer"
        else:
            game.phase = GAME_PHASE_CONSEQUENCE
            return "show_consequence"
    
    def get_next_encounter():
        """Get next encounter based on state"""
        
        # Check queue first
        if game.encounter_queue:
            enc_id = game.encounter_queue.pop(0)
            return router.encounter_vault.get(enc_id)
        
        # Otherwise route based on state
        return router.select_encounter(game)
    
    def should_offer_reflection():
        """Check if we should pause for emotional reflection"""
        # After every 3-4 encounters
        return game.scene_count > 0 and game.scene_count % 3 == 0
    
    def get_introspection_options(belief_id):
        """Get deeper beliefs to explore"""
        belief = beliefs.get(belief_id)
        if not belief:
            return []
        
        options = []
        
        # Add deeper beliefs
        for deeper_id in belief.get('deeper', []):
            if deeper_id in beliefs:
                options.append(beliefs[deeper_id])
        
        # Add resolution if available
        if 'resolution' in belief:
            res_id = belief['resolution']
            if res_id in beliefs:
                options.append(beliefs[res_id])
        
        return options