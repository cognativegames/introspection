# ============================================================================
# ENCOUNTER VAULT
# Clustered encounter database for therapist-offered encounters
# Organized by belief clusters: self-worth, relationships, capability
# ============================================================================

init python:
    # Belief clusters map to encounter clusters
    ENCOUNTER_BELIEF_TIERS = {
        1: ["self-worth", "relationships", "capability"],
        2: ["self-acceptance", "intimacy", "authenticity"],
        3: ["all_clusters"]
    }
    
    # Main encounter vault - organized by cluster
    ENCOUNTER_VAULT = {
        "self-worth": {
            "tier": 1,
            "beliefs_targeted": ["self.is-unworthy", "self.is-fundamentally-flawed", "self.must-earn-love"],
            "encounters": [
                {
                    "id": "sw_001",
                    "title": "The Mirror",
                    "description": "You catch your reflection in a store window while walking past.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.is-unworthy", "delta": {"shame": 2, "inadequacy": 2}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.is-worthy", "delta": {"self_compassion": 2, "hope": 1}}
                    ]
                },
                {
                    "id": "sw_002",
                    "title": "The Achievement",
                    "description": "You receive recognition for something you've accomplished.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.must-earn-love", "delta": {"anxiety": 1, "emptiness": 1}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.is-worthy", "delta": {"hope": 2, "connection": 1}}
                    ]
                },
                {
                    "id": "sw_003",
                    "title": "The Rejection",
                    "description": "Someone you care about doesn't respond to your message.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.is-fundamentally-flawed", "delta": {"shame": 2, "loneliness": 2}},
                        {"type": "neutral", "belief": None, "delta": {}},
                        {"type": "positive", "belief": "self.is-worthy", "delta": {"self_compassion": 1, "clarity": 1}}
                    ]
                }
            ]
        },
        "relationships": {
            "tier": 1,
            "beliefs_targeted": ["others.are-threatening", "others.use-me", "abandonment.is-inevitable"],
            "encounters": [
                {
                    "id": "rel_001",
                    "title": "The Phone Call",
                    "description": "A friend cancels plans at the last minute.",
                    "interpretations": [
                        {"type": "negative", "belief": "abandonment.is-inevitable", "delta": {"loneliness": 2, "fear": 1}},
                        {"type": "neutral", "belief": None, "delta": {}},
                        {"type": "positive", "belief": "others.are-complex", "delta": {"empathy": 1, "clarity": 1}}
                    ]
                },
                {
                    "id": "rel_002",
                    "title": "The Request",
                    "description": "Someone asks you for help with a difficult situation.",
                    "interpretations": [
                        {"type": "negative", "belief": "others.use-me", "delta": {"resentment": 2, "fear": 1}},
                        {"type": "neutral", "belief": None, "delta": {}},
                        {"type": "positive", "belief": "others.are-friendly", "delta": {"connection": 2, "purpose": 1}}
                    ]
                },
                {
                    "id": "rel_003",
                    "title": "The Conflict",
                    "description": "Someone expresses disagreement with something you said.",
                    "interpretations": [
                        {"type": "negative", "belief": "others.are-threatening", "delta": {"defensiveness": 2, "fear": 1}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "others.are-complex", "delta": {"empathy": 1, "connection": 1}}
                    ]
                }
            ]
        },
        "capability": {
            "tier": 1,
            "beliefs_targeted": ["self.is-failure", "self.is-not-enough", "others.are-better"],
            "encounters": [
                {
                    "id": "cap_001",
                    "title": "The Presentation",
                    "description": "You're asked to present your work to the team.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.is-failure", "delta": {"anxiety": 2, "vulnerability": 2}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.is-capable", "delta": {"hope": 2, "connection": 1}}
                    ]
                },
                {
                    "id": "cap_002",
                    "title": "The Comparison",
                    "description": "You learn about a peer's success in something you care about.",
                    "interpretations": [
                        {"type": "negative", "belief": "others.are-better", "delta": {"inadequacy": 2, "shame": 1}},
                        {"type": "neutral", "belief": None, "delta": {}},
                        {"type": "positive", "belief": "self.is-capable", "delta": {"inspiration": 1, "clarity": 1}}
                    ]
                },
                {
                    "id": "cap_003",
                    "title": "The Mistake",
                    "description": "You make an error on an important task.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.is-failure", "delta": {"shame": 2, "anxiety": 1}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.is-resilient", "delta": {"self_compassion": 2, "clarity": 1}}
                    ]
                }
            ]
        }
    }
    
    # Tier 2 clusters (unlocked after resolving tier 1 beliefs)
    ENCOUNTER_VAULT_TIER2 = {
        "self-acceptance": {
            "tier": 2,
            "beliefs_targeted": ["self.is-worthy-and-striving", "self.can-accept-imperfection"],
            "encounters": [
                {
                    "id": "sa_001",
                    "title": "The Imperfection",
                    "description": "You notice a flaw in yourself that you've been hiding.",
                    "interpretations": [
                        {"type": "negative", "belief": "self.is-fundamentally-flawed", "delta": {"shame": 2}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.can-accept-imperfection", "delta": {"self_compassion": 2, "clarity": 1}}
                    ]
                }
            ]
        },
        "intimacy": {
            "tier": 2,
            "beliefs_targeted": ["others.are-safe", "vulnerability.is-strength"],
            "encounters": [
                {
                    "id": "int_001",
                    "title": "The Disclosure",
                    "description": "You consider sharing something vulnerable with someone close.",
                    "interpretations": [
                        {"type": "negative", "belief": "others.use-me", "delta": {"fear": 2, "detachment": 1}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "vulnerability.is-strength", "delta": {"connection": 2, "hope": 1}}
                    ]
                }
            ]
        },
        "authenticity": {
            "tier": 2,
            "beliefs_targeted": ["self.can-be-real", "others.see-real-me"],
            "encounters": [
                {
                    "id": "auth_001",
                    "title": "The Mask",
                    "description": "You realize you've been performing a version of yourself.",
                    "interpretations": [
                        {"type": "negative", "belief": "others.are-threatening", "delta": {"fear": 2, "emptiness": 1}},
                        {"type": "neutral", "belief": None, "delta": {"clarity": 1}},
                        {"type": "positive", "belief": "self.can-be-real", "delta": {"hope": 2, "connection": 1}}
                    ]
                }
            ]
        }
    }
    
    # Helper function to get encounters by cluster
    def get_encounters_by_cluster(cluster_name):
        """Get all encounters for a specific cluster"""
        if cluster_name in ENCOUNTER_VAULT:
            return ENCOUNTER_VAULT[cluster_name]["encounters"]
        elif cluster_name in ENCOUNTER_VAULT_TIER2:
            return ENCOUNTER_VAULT_TIER2[cluster_name]["encounters"]
        return []
    
    # Helper function to get all available clusters
    def get_available_clusters(tier=1):
        """Get clusters available at given tier"""
        if tier >= 2:
            return list(ENCOUNTER_VAULT.keys()) + list(ENCOUNTER_VAULT_TIER2.keys())
        return list(ENCOUNTER_VAULT.keys())
