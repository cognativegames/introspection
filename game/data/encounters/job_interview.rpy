init 2 python:
    encounters["job_interview"] = {
        "id": "job_interview",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["self.is-capable", "self.is-failure"],
        "scene": "office",
        
        "observation": "The interviewer pauses, then says: 'Interesting answer.'",
        "context": "Job interview, high stakes, unclear feedback",
        
        "npc_intent": {
            "true_intent": "thoughtful_consideration",
            "belief_alignment": ["self.is-capable"]
        },
        
        "tags": ["stressful", "career"],
        
        "interpretations": [
            {
                "id": "positive",
                "display": "They're genuinely considering my qualifications",
                "internal_thought": "I gave a good answer",
                "activates": ["self.is-capable"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"hope": 10, "anxiety": -5}
            },
            {
                "id": "negative",
                "display": "I bombed that question",
                "internal_thought": "I'm not good enough for this job",
                "activates": ["self.is-failure", "self.is-unworthy"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 20, "hope": -15},
                "therapy_label": "encounter_therapy_self_failure"
            }
        ]
    }