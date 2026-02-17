# ============================================================================
# ENCOUNTER ROUTER CLASS
# Routes to appropriate encounters based on game state
# Hybrid: story progression + character state (beliefs, emotions)
# ============================================================================

init python:
    import random
    
    class EncounterRouter:
        """
        Routes to appropriate encounters based on game state.
        Manages the encounter vault and selection logic.
        
        Hybrid selection uses:
        - Story progression (narrative beats)
        - Character state (beliefs, emotions)
        - Tier system (based on resolved beliefs)
        """
        
        def __init__(self):
            self.encounter_vault = {}
            self.used_encounters = set()
            self.encounter_queue = []
            self.available_tiers = [1]  # Start at tier 1
        
        def select_encounter(self, game_state, story_progression=0):
            """
            Select encounter using hybrid of story + character state.
            
            Args:
                game_state: GameState instance with beliefs/emotions
                story_progression: 0-10 story progress indicator
            
            Returns:
                Encounter dict from vault or None
            """
            # Step 1: Identify target clusters based on active negative beliefs
            target_clusters = self._identify_target_clusters(game_state)
            
            # Step 2: Check emotional state for anxiety routing (ENCO-02)
            if game_state.emotions.get("anxiety", 0) > 7:
                # High anxiety (>7 on 0-10 scale) - prioritize calming encounters
                target_clusters = ["self-worth"] + target_clusters
            
            # Step 3: Select from appropriate tier
            tier = self._determine_accessible_tier(game_state, story_progression)
            
            # Step 4: Filter vault by clusters and tier
            candidates = self._get_candidates(target_clusters, tier)
            
            # Step 5: Avoid recent repeats
            candidates = self._filter_recent(candidates, game_state)
            
            # Step 6: Return selected or None if no candidates
            if candidates:
                return candidates[0]
            return None
        
        def _identify_target_clusters(self, game_state):
            """
            Map active negative beliefs to encounter clusters.
            
            Beliefs are mapped to clusters:
            - self.is-unworthy, self.is-fundamentally-flawed, self.must-earn-love -> self-worth
            - others.are-threatening, others.use-me, abandonment.is-inevitable -> relationships
            - self.is-failure, self.is-not-enough, others.are-better -> capability
            """
            cluster_mapping = {
                "self.is-unworthy": "self-worth",
                "self.is-fundamentally-flawed": "self-worth",
                "self.must-earn-love": "self-worth",
                "others.are-threatening": "relationships",
                "others.use-me": "relationships",
                "abandonment.is-inevitable": "relationships",
                "self.is-failure": "capability",
                "self.is-not-enough": "capability",
                "others.are-better": "capability"
            }
            
            targets = []
            for belief_id, intensity in game_state.beliefs.items():
                if intensity > 0 and belief_id in cluster_mapping:
                    cluster = cluster_mapping[belief_id]
                    if cluster not in targets:
                        targets.append(cluster)
            
            return targets if targets else ["self-worth"]  # Default to self-worth
        
        def _determine_accessible_tier(self, game_state, story_progression):
            """
            Determine which tier player can access based on resolved beliefs.
            
            Tier progression:
            - Tier 1: No resolved beliefs (self-worth, relationships, capability)
            - Tier 2: 1+ resolved beliefs (self-acceptance, intimacy, authenticity)
            - Tier 3: 3+ resolved beliefs (all clusters)
            """
            # Count resolved beliefs
            resolved_count = sum(1 for b, i in game_state.beliefs.items() 
                                if i >= BELIEF_INTENSITY_RESOLVED)
            
            # Determine tier based on resolved beliefs
            if resolved_count >= 3:
                tier = 3
            elif resolved_count >= 1:
                tier = 2
            else:
                tier = 1
            
            # Also consider story progression as a factor
            tier = min(tier + (story_progression // 4), 3)
            
            return tier
        
        def _get_candidates(self, clusters, tier):
            """Get encounter candidates from vault based on clusters and tier"""
            candidates = []
            
            # Get tier 1 encounters
            for cluster in clusters:
                if cluster in ENCOUNTER_VAULT:
                    for enc in ENCOUNTER_VAULT[cluster]["encounters"]:
                        candidates.append(enc)
            
            # Get tier 2 encounters if accessible
            if tier >= 2:
                for cluster in clusters:
                    if cluster in ENCOUNTER_VAULT_TIER2:
                        for enc in ENCOUNTER_VAULT_TIER2[cluster]["encounters"]:
                            candidates.append(enc)
            
            return candidates
        
        def _filter_recent(self, candidates, game_state):
            """Remove recently completed encounters"""
            recent = getattr(game_state, 'recent_encounters', [])
            return [c for c in candidates if c['id'] not in recent]
        
        def mark_encounter_completed(self, game_state, encounter_id):
            """Record completed encounter"""
            if not hasattr(game_state, 'recent_encounters'):
                game_state.recent_encounters = []
            game_state.recent_encounters.append(encounter_id)
            # Keep only last 10
            game_state.recent_encounters = game_state.recent_encounters[-10:]
            self.used_encounters.add(encounter_id)
        
        def select_encounter(self, state):
            """Legacy method - routes to new hybrid method"""
            return self.select_encounter(state, story_progression=0)
        
        def queue_narrative_sequence(self, sequence_id):
            """Queue a specific narrative sequence"""
            sequence = narrative_sequences.get(sequence_id, [])
            self.encounter_queue.extend(sequence)
