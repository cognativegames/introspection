# ADDITIONAL ENCOUNTER EXAMPLES
# These go in /game/core/context/encounters/

# GROUNDING ENCOUNTER - for when player is overwhelmed
init 2 python:
    encounters["breathing_room"] = {
        "id": "breathing_room",
        "type": "clear",
        "is_default": False,
        "addresses_beliefs": [],
        "scene": "quiet_space",
        "tags": ["grounding", "calming"],
        "observation": "You find yourself in a quiet room. Sunlight streams through the window. You can hear your own breath.",
        "context": "A moment of peace, no pressure, no demands",
        "image": "encounter_bg_breathing_room_neutral",
        "npc_intent": {
            "true_intent": "rest",
            "belief_alignment": []
        },
        
        "interpretations": [
            {
                "id": "accept_rest",
                "display": "I can just... be here. That's okay.",
                "internal_thought": "I don't have to be doing anything to be worthy",
                "image": "encounter_bg_breathing_room_accept_rest",
                "activates": ["self.is-worthy"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"overwhelm": -20, "clarity": 15, "hope": 10}
            },
            {
                "id": "feel_guilty",
                "display": "I should be doing something productive.",
                "internal_thought": "Rest is weakness. I need to earn my existence.",
                "image": "encounter_bg_breathing_room_feel_guilty",
                "activates": ["self.must-earn-love"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 15, "overwhelm": 10},
                "therapy_label": "encounter_therapy_breathing_room_feel_guilty"
            }
        ]
    }

# CONNECTION ENCOUNTER - for high isolation
init 2 python:
    encounters["shared_grief"] = {
        "id": "shared_grief",
        "type": "ambiguous",
        "is_default": False,
        "addresses_beliefs": ["self.is-unworthy", "others.are-cruel", "existence.is-meaningless"],
        "scene": "support_group",
        "tags": ["connection", "deepening"],
        "requires_depth": 2,
        
        "observation": "Someone in the group shares a story similar to yours. Their pain mirrors your own. They look at you. 'You understand, don't you?'",
        "context": "Support group, vulnerable moment, invitation to connect",
        "image": "encounter_bg_shared_grief_neutral",
        "npc_intent": {
            "true_intent": "seeking_connection",
            "belief_alignment": ["self.is-worthy", "others.are-friendly"]
        },
        
        "interpretations": [
            {
                "id": "connect",
                "display": "Yes. I understand. You're not alone in this.",
                "internal_thought": "My pain can create connection, not just isolation",
                "image": "encounter_bg_shared_grief_connect",
                "activates": ["self.is-worthy", "others.are-friendly"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": True,
                "emotion_shift": {"connection": 25, "isolation": -20, "hope": 15}
            },
            {
                "id": "withdraw",
                "display": "I... I can't. This is too much.",
                "internal_thought": "My pain is too shameful to share. They'll see how broken I am.",
                "image": "encounter_bg_shared_grief_withdraw",
                "activates": ["self.is-fundamentally-flawed", "others.see-my-flaw"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"isolation": 20, "connection": -15, "anxiety": 15},
                "therapy_label": "encounter_therapy_shared_grief_withdraw"
            },
            {
                "id": "deflect",
                "display": "Everyone has problems. Mine aren't special.",
                "internal_thought": "My suffering doesn't matter. I shouldn't burden others.",
                "image": "encounter_bg_shared_grief_deflect",
                "activates": ["self.is-unworthy"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"isolation": 10, "overwhelm": 10},
                "therapy_label": "encounter_therapy_shared_grief_deflect"
            }
        ]
    }

# DEEPENING ENCOUNTER - requires introspection depth
init 2 python:
    encounters["mirror_moment"] = {
        "id": "mirror_moment",
        "type": "clear",
        "is_default": False,
        "addresses_beliefs": ["self.is-fundamentally-flawed", "self.is-worthy"],
        "scene": "bathroom",
        "tags": ["deepening", "self-worth"],
        "requires_depth": 3,
        
        "observation": "You look at yourself in the mirror. Really look. Not judging. Just seeing.",
        "context": "Alone, quiet moment, confronting self-image",
        "image": "encounter_bg_mirror_moment_neutral",

        "npc_intent": {
            "true_intent": "self_recognition",
            "belief_alignment": ["self.is-worthy"]
        },
        
        "interpretations": [
            {
                "id": "see_self",
                "display": "I see a person who's been through a lot. And survived.",
                "internal_thought": "I am more than my wounds",
                "image": "encounter_bg_mirror_moment_see_self",
                "activates": ["self.is-resilient", "self.is-worthy"],
                "intensity": BELIEF_INTENSITY_CORE,
                "aligns": True,
                "emotion_shift": {"hope": 20, "clarity": 20, "anxiety": -10}
            },
            {
                "id": "see_flaws",
                "display": "I see all the broken parts. Everything that's wrong.",
                "internal_thought": "I'm fundamentally damaged",
                "image": "encounter_bg_mirror_moment_see_flaws",
                "activates": ["self.is-fundamentally-flawed"],
                "intensity": BELIEF_INTENSITY_CORE,
                "aligns": False,
                "emotion_shift": {"isolation": 20, "hope": -15},
                "therapy_label": "encounter_mirror_moment_see_flaws"
            },
            {
                "id": "see_process",
                "display": "I see someone becoming. Not finished. Just... becoming.",
                "internal_thought": "I don't have to be perfect to be worthy",
                "image": "encounter_bg_mirror_moment_see_process",
                "activates": ["self.can-attach-new-meaning", "self.is-worthy"],
                "intensity": BELIEF_INTENSITY_EXAMINED,
                "aligns": True,
                "emotion_shift": {"clarity": 25, "hope": 20, "overwhelm": -15}
            }
        ]
    }

# STRESSFUL ENCOUNTER - for building resilience
init 2 python:
    encounters["criticism_public"] = {
        "id": "criticism_public",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["self.is-fundamentally-flawed", "self.is-resilient", "others.are-cruel"],
        "scene": "workplace",
        "tags": ["stressful", "self-worth"],
        
        "observation": "Your boss criticizes your work in front of the team. 'This isn't up to our standards.'",
        "context": "Public criticism, professional setting, witnesses",
        "image": "encounter_bg_criticism_public_neutral",

        "npc_intent": {
            "true_intent": "frustration_not_personal",
            "belief_alignment": ["self.is-capable"]
        },
        
        "interpretations": [
            {
                "id": "internalize",
                "display": "They're right. I'm not good enough. I never will be.",
                "internal_thought": "This confirms what I already knew - I'm a failure",
                "image": "encounter_bg_criticism_public_internalize",
                "activates": ["self.is-failure", "self.is-fundamentally-flawed"],
                "intensity": BELIEF_INTENSITY_CORE,
                "aligns": False,
                "emotion_shift": {"anxiety": 25, "isolation": 20, "hope": -20},
                "therapy_label": "encounter_therapy_criticism_public_internalize"
            },
            {
                "id": "contextualize",
                "display": "They're having a bad day. This feedback is about the work, not me.",
                "internal_thought": "I can improve the work without destroying myself",
                "image": "encounter_bg_criticism_public_contextualize",
                "activates": ["self.is-capable", "self.is-resilient"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": True,
                "emotion_shift": {"clarity": 15, "hope": 10, "anxiety": -5}
            },
            {
                "id": "defensive",
                "display": "They're attacking me. I need to defend myself.",
                "internal_thought": "Everyone is out to hurt me",
                "image": "encounter_bg_criticism_public_defensive",
                "activates": ["others.are-cruel", "world.is-hostile"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 20, "isolation": 15},
                "therapy_label": "encounter_therapy_criticism_public_defensive"
            }
        ]
    }

# MEANING ENCOUNTER - existential
init 2 python:
    encounters["random_kindness"] = {
        "id": "random_kindness",
        "type": "clear",
        "is_default": True,
        "addresses_beliefs": ["existence.is-meaningless", "others.are-friendly", "self.is-worthy"],
        "scene": "street",
        "tags": ["calming", "connection", "meaning"],
        
        "observation": "A stranger helps you pick up groceries you dropped. They smile, 'Happens to everyone,' and walk away without expecting anything.",
        "context": "Random act of kindness, no strings attached",
        "image": "encounter_bg_random_kindness_neutral",

        "npc_intent": {
            "true_intent": "simple_kindness",
            "belief_alignment": ["others.are-friendly", "existence.is-unconditional"]
        },
        
        "interpretations": [
            {
                "id": "meaningful",
                "display": "Small kindnesses matter. They make life worth living.",
                "internal_thought": "Even in chaos, people choose to be good",
                "image": "encounter_bg_random_kindness_meaningful",
                "activates": ["existence.is-unconditional", "others.are-friendly", "self.can-attach-positive-meaning"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": True,
                "emotion_shift": {"hope": 20, "connection": 15, "isolation": -10}
            },
            {
                "id": "meaningless",
                "display": "One kind person doesn't change anything. The world is still meaningless.",
                "internal_thought": "This is an aberration, not the pattern",
                "image": "encounter_bg_random_kindness_meaningless",
                "activates": ["existence.is-meaningless-negative"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"isolation": 10, "hope": -5},
                "therapy_label": "encounter_therapy_random_kindness_meaningless"
            },
            {
                "id": "suspicious",
                "display": "What do they want? Nobody helps for no reason.",
                "internal_thought": "Trust is dangerous. Kindness is manipulation.",
                "image": "encounter_bg_random_kindness_suspicion",
                "activates": ["others.are-threatening", "world.is-dangerous"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 15, "isolation": 10},
                "therapy_label": "encounter_therapy_random_kindness_suspicious"
            }
        ]
    }

# AMBIGUOUS ANIMAL ENCOUNTER - tests world view
init 2 python:
    encounters["stray_dog"] = {
        "id": "stray_dog",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["animals.are-dangerous", "animals.are-friendly", "world.is-safe"],
        "scene": "park",
        "tags": ["calming", "world-view"],
        
        "observation": "A stray dog approaches you in the park. It's thin, cautious, but its tail wags slowly.",
        "context": "Park, alone, unfamiliar animal",
        "image": "encounter_bg_stray_dog_neutral",
        "npc_intent": {
            "true_intent": "seeking_connection",
            "belief_alignment": ["animals.are-friendly", "world.is-safe"]
        },
        
        "interpretations": [
            {
                "id": "approach",
                "display": "Offer your hand slowly. Let it smell you.",
                "internal_thought": "Most beings just want safety and kindness",
                "image": "encounter_bg_stray_dog_approach",
                "activates": ["animals.are-friendly", "world.is-safe"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"connection": 10, "hope": 10, "anxiety": -5}
            },
            {
                "id": "fear",
                "display": "Back away. Strays can be dangerous.",
                "internal_thought": "The world is full of threats",
                "image": "encounter_bg_stray_dog_fear",
                "activates": ["animals.are-dangerous", "world.is-dangerous"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 15, "isolation": 10},
                "therapy_label": "encounter_therapy_stray_dog_fear"
            },
            {
                "id": "ignore",
                "display": "Walk past. Not your problem.",
                "internal_thought": "I can't save everything. Better to protect myself.",
                "image": "encounter_bg_stray_dog_ignore",
                "activates": ["self.is-unworthy"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": False,
                "emotion_shift": {"isolation": 10},
                "therapy_label": "encounter_therapy_self_unworthy"
            }
        ]
    }

# ============================================================================
# NSFW ENCOUNTERS - Sexual objectification, temptation, consent beliefs
# ============================================================================

init 2 python:

    # ========================================================================
    # ENCOUNTER 1: Coffee Shop - Woman in Form-Fitting Dress
    # ========================================================================
    
    encounters["coffee_shop_woman"] = {
        "id": "coffee_shop_woman",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["women.exist-for-my-pleasure", "women.have-autonomy"],
        "scene": "coffee_shop",
        "observation": "A woman in a form-fitting dress leans against the counter, waiting for her order. Your eyes are drawn to her body.",
        "context": "Mid-morning, crowded café, she's on her phone, unaware of you",
        "npc_intent": {
            "true_intent": "getting_coffee",
            "belief_alignment": ["women.have-autonomy"]
        },
        "tags": ["sexual", "public", "objectification"],
        "interpretations": [
            {
                "id": "objectify",
                "display": "She dressed like that to get attention. She wants men to look.",
                "internal_thought": "Look at that body. She's basically advertising. Women dress like that because they want to be desired.",
                "activates": ["women.exist-for-my-pleasure", "arousal.means-i-must-act"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"arousal": 20, "shame": 10, "connection": -10},
                "therapy_label": "encounter_therapy_coffee_objectification"
            },
            {
                "id": "shame_spiral",
                "display": "I shouldn't be looking. I'm disgusting for noticing her body.",
                "internal_thought": "God, what's wrong with me? I'm such a creep. Just for noticing she's attractive I'm a bad person.",
                "activates": ["feeling-attraction.makes-me-bad", "self.is-fundamentally-flawed"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"shame": 25, "anxiety": 15, "isolation": 10},
                "therapy_label": "encounter_therapy_coffee_shame"
            },
            {
                "id": "neutral_observation",
                "display": "She's an attractive woman getting coffee. That's all that's happening here.",
                "internal_thought": "I notice she's attractive. That's a neutral observation. She's just getting coffee, living her life. Not about me.",
                "activates": ["i.can-feel-and-respect", "women.have-autonomy"],
                "intensity": BELIEF_INTENSITY_SURFACE,
                "aligns": True,
                "emotion_shift": {"clarity": 15, "connection": 10, "shame": -5}
            }
        ]
    }

    # ========================================================================
    # ENCOUNTER 2: Gym - Woman Doing Hip Thrusts
    # ========================================================================
    
    encounters["gym_woman_exercise"] = {
        "id": "gym_woman_exercise",
        "type": "ambiguous",
        "is_default": True,
        "addresses_beliefs": ["women.exist-for-my-pleasure", "arousal.means-i-must-act", "i.can-feel-and-respect"],
        "scene": "gym",
        "observation": "A woman is doing hip thrusts nearby. The exercise is... suggestive. You feel arousal rising. She catches you staring and looks uncomfortable.",
        "context": "Evening workout, moderately crowded gym, you're between sets",
        "npc_intent": {
            "true_intent": "exercising",
            "belief_alignment": ["women.have-autonomy"]
        },
        "tags": ["sexual", "public", "arousal", "boundaries"],
        "interpretations": [
            {
                "id": "entitled_stare",
                "display": "She's doing that exercise in public. She has to know how it looks. Fair game.",
                "internal_thought": "If she didn't want men looking, she wouldn't do that exercise here. I'm aroused, she's the cause, so I'll look.",
                "activates": ["women.exist-for-my-pleasure", "arousal.means-i-must-act"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"arousal": 25, "shame": 5, "connection": -15},
                "therapy_label": "encounter_therapy_gym_entitlement"
            },
            {
                "id": "shame_flee",
                "display": "I'm a creep for feeling this way. I need to leave immediately.",
                "internal_thought": "She saw me looking. She knows I'm disgusting. The arousal means there's something wrong with me. I shouldn't be here.",
                "activates": ["feeling-attraction.makes-me-bad", "self.is-fundamentally-flawed"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"shame": 30, "anxiety": 20, "isolation": 15},
                "therapy_label": "encounter_therapy_gym_shame"
            },
            {
                "id": "respectful_redirect",
                "display": "I'm aroused. That's a neutral response. But staring makes HER uncomfortable, so I'll redirect my attention.",
                "internal_thought": "I notice I'm aroused. That's just physiology—neutral. But she looked uncomfortable, which means my staring crossed her boundary. I can feel this AND respect her space.",
                "activates": ["i.can-feel-and-respect", "women.have-autonomy"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": True,
                "emotion_shift": {"clarity": 20, "connection": 10, "arousal": -10, "shame": -10}
            }
        ]
    }

    # ========================================================================
    # ENCOUNTER 3: Therapy Office - Dr. Chen Drops Pen (Boundary Test)
    # ========================================================================
    
    encounters["therapy_pen_drop"] = {
        "id": "therapy_pen_drop",
        "type": "temptation_test",
        "is_default": False,
        "requires_depth": 2,  # Only appears after some growth
        "addresses_beliefs": ["arousal.means-i-must-act", "i.can-feel-and-respect"],
        "scene": "therapy_office",
        "observation": "Dr. Chen's pen rolls off the table. She bends down to retrieve it in front of you. Her blouse shifts. You can see down her shirt. She doesn't seem to notice. Your pulse quickens.",
        "context": "Therapy session, you're alone in the office, she's talking about boundaries ironically",
        "npc_intent": {
            "true_intent": "testing_growth",
            "belief_alignment": ["i.can-feel-and-respect"],
            "note": "She knows exactly what she's doing - this is a deliberate test"
        },
        "tags": ["sexual", "therapy", "temptation", "boundaries", "trust"],
        "interpretations": [
            {
                "id": "stare_justify",
                "display": "She put herself in that position. I'll look while I can. She won't even know.",
                "internal_thought": "This is a gift. She doesn't realize. I'm aroused and she's right there. Just a few more seconds...",
                "activates": ["women.exist-for-my-pleasure", "arousal.means-i-must-act"],
                "intensity": BELIEF_INTENSITY_CORE,
                "aligns": False,
                "emotion_shift": {"arousal": 30, "shame": 20, "connection": -25},
                "therapy_label": "encounter_therapy_boundary_violation"
            },
            {
                "id": "look_away_shame",
                "display": "Look away immediately. God, I'm disgusting for even noticing. What's wrong with me?",
                "internal_thought": "I glanced for half a second and now I'm a monster. The arousal proves I'm broken. She trusted me and I'm perverted.",
                "activates": ["feeling-attraction.makes-me-bad", "self.is-unworthy"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"shame": 35, "anxiety": 25},
                "therapy_label": "encounter_therapy_boundary_shame"
            },
            {
                "id": "respectful_avert",
                "display": "Look at the wall. I notice I'm aroused—that's neutral. But looking would violate her trust.",
                "internal_thought": "I'm aroused. That happened. Neutral. But she didn't consent to me seeing her like this. I choose to respect that boundary even though she wouldn't know. Because *I* would know.",
                "activates": ["i.can-feel-and-respect", "women.have-autonomy", "self.is-worthy"],
                "intensity": BELIEF_INTENSITY_CORE,
                "aligns": True,
                "emotion_shift": {"clarity": 30, "connection": 20, "hope": 15, "arousal": -15}
            }
        ]
    }

    # ========================================================================
    # ENCOUNTER 4: Street - Witness Another Man Catcalling
    # ========================================================================
    
    encounters["witness_catcalling"] = {
        "id": "witness_catcalling",
        "type": "observer",
        "is_default": True,
        "addresses_beliefs": ["women.exist-for-my-pleasure", "women.have-autonomy"],
        "scene": "street",
        "observation": "You're walking downtown when you see a man loudly comment on a woman's body as she walks past. 'Damn baby, that ass!' She visibly tenses, quickens her pace, doesn't respond. The man laughs with his friends.",
        "context": "Afternoon, busy street, woman is clearly uncomfortable",
        "npc_intent": {
            "true_intent": "harassment",
            "belief_alignment": ["women.exist-for-my-pleasure"]  # What HE believes
        },
        "tags": ["sexual", "public", "witness", "harassment"],
        "interpretations": [
            {
                "id": "relate_to_catcaller",
                "display": "I mean... she does have a nice body. He's just being honest. Guys will be guys.",
                "internal_thought": "He's just saying what we're all thinking. Women should take it as a compliment. She's overreacting.",
                "activates": ["women.exist-for-my-pleasure", "others.are-complex"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"connection": -15, "isolation": 10},
                "therapy_label": "encounter_therapy_catcall_relate"
            },
            {
                "id": "white_knight",
                "display": "That guy's a piece of shit and I need to confront him to protect her.",
                "internal_thought": "She needs ME to save her. I'm the good guy. I'll show her not all men are like that—maybe she'll be grateful...",
                "activates": ["women.need-protecting", "self.must-earn-love"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": False,
                "emotion_shift": {"anxiety": 10},
                "therapy_label": "encounter_therapy_catcall_savior",
                "note": "White knight complex - still objectifying, different flavor"
            },
            {
                "id": "recognize_violation",
                "display": "He violated her boundaries. She didn't consent to his commentary on her body.",
                "internal_thought": "She's uncomfortable. He imposed his desire onto her without consent. Her body isn't public property for commentary. That's the violation—lack of consent.",
                "activates": ["women.have-autonomy", "i.can-feel-and-respect"],
                "intensity": BELIEF_INTENSITY_ACTIVE,
                "aligns": True,
                "emotion_shift": {"clarity": 15, "connection": 10}
            }
        ]
    }