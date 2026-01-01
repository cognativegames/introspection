init 20 python:
    encounters["dog_park"] = {
        "id": "dog_park",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["animals.are-dangerous", "world.is-dangerous", "animals.are-friendly"],
        "scene": "park",
        "observation": "A dog runs up to you, tail wagging enthusiastically.",
        "context": "Afternoon walk, pleasant weather, other people around",
        "npc_intent": {
            "true_intent": "friendly_greeting",
            "belief_alignment": ["animals.are-friendly", "world.is-safe"]
        },
        "tags":["animals", "public"],
        "interpretations": [
            {
                "id": "friendly",
                "display": "This dog wants to play",
                "internal_thought": "Animals can be friendly and safe",
                "activates": ["animals.are-friendly", "world.is-safe"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"hope": 10, "anxiety": -10}
            },
            {
                "id": "dangerous",
                "display": "This dog might bite me",
                "internal_thought": "I need to protect myself",
                "activates": ["animals.are-dangerous", "world.is-dangerous"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 15, "hope": -10}
            }
        ]
    }