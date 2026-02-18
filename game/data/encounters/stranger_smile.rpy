init 2 python:
    encounters["stranger_smile"] = {
        "id": "stranger_smile",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["others.are-friendly", "others.are-threatening", "self.is-worthy"],
        "scene": "cafe",
        "observation": "A stranger catches your eye and smiles warmly at you.",
        "context": "Coffee shop, mid-morning, relaxed atmosphere",
        "npc_intent": {
            "true_intent": "friendly_acknowledgment",
            "belief_alignment": ["others.are-friendly", "self.is-worthy"]
        },
        "tags":["calming"],
        "interpretations": [
            {
                "id": "connection",
                "display": "They're being kind",
                "internal_thought": "People can be genuinely friendly",
                "activates": ["others.are-friendly", "self.is-worthy"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"connection": 15, "isolation": -10}
            },
            {
                "id": "mockery",
                "display": "They're probably mocking me",
                "internal_thought": "I'm not worthy of genuine kindness",
                "activates": ["others.are-cruel", "self.is-unworthy"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"isolation": 15, "connection": -15},
                "therapy_label": "encounter_therapy_self_unworthy"
            }
        ]
    }