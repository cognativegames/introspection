# ============================================================================
# GAME VARIABLES
# All default variables and state initialization
# ============================================================================

default player_name = "???"

# Initial player state
default player_state = {
    "awareness_level": 0,
    "panic_level": 5,
    "core_beliefs": {},
    "name_chosen": False,
    "evil_acts": [],
    "redemption_moments": []
}

default reality_stability = 0

# Track which dramatic shifts have occurred
default shifts_seen = {
    "giraffe": False,
    "jungle": False,
    "underwater": False,
    "void": False
}

# Forgiveness arc tracking
default forgiveness_arcs = {
    "enabled": True,
    "requirements": {
        "self_awareness": 6,
        "genuine_remorse_shown": 0,
        "consistent_good_acts": 0,
        "time_passed": 0,
    },
    "mature_character_wisdom": {
        "teaches_self_forgiveness": True,
        "explains_cycle_of_hurt": True,
        "models_boundary_setting": True,
        "offers_path_forward": True,
    }
}

# Reality shift severity system
default shift_severity = {
    "catastrophic": {
        "visual": "complete_breakdown",
        "physical": "severe_headpain",
        "duration": 5.0,
        "message": "Your skull feels like it's splitting apart. Reality tears at the seams."
    },
    "severe": {
        "visual": "major_distortion",
        "physical": "sharp_headpain",
        "duration": 3.0,
        "message": "A spike of pain lances through your head. The world lurches sideways."
    },
    "moderate": {
        "visual": "reality_flicker",
        "physical": "dull_throb",
        "duration": 1.5,
        "message": "Your head throbs. Something feels wrong."
    },
    "minor": {
        "visual": "subtle_shift",
        "physical": "brief_discomfort",
        "duration": 0.5,
        "message": "A brief flutter of discomfort."
    },
    "harmony": {
        "visual": "stable_clarity",
        "physical": "no_pain",
        "duration": 0,
        "message": "Everything feels... right."
    }
}

init -1 python:

    # NPC states
    npc_states = {}

    # Narrative sequences registry
    narrative_sequences = {}

    # Beliefs registry (populated by belief data files)
    beliefs = {}

    # Encounters registry (populated by encounter files)
    encounters = {}

    # Belief System
    beliefs = {}

    # SELF-WORTH CONFLICT CLUSTER
    # BASHAR PRINCIPLE: All negative beliefs are MISALIGNED with true self
    # They're based on expectations (conditional worth) rather than acceptance (unconditional)
    
    beliefs["self.is-worthy"] = {
        "id": "self.is-worthy",
        "statement": "I am worthy of love and kindness",
        "type": "positive",
        "domain": "self-worth",
        "conflicts_with": ["self.is-unworthy", "self.must-earn-love", "self.is-fundamentally-flawed"],
        "related_emotions": {"belonging": 3, "connection": 2, "hope": 2, "clarity": 1},
        "bashar_note": "Worth is inherent, not earned. You exist, therefore you are worthy."
    }
    
    beliefs["self.is-unworthy"] = {
        "id": "self.is-unworthy",
        "statement": "I am unworthy of love or good things",
        "type": "negative",
        "domain": "self-worth",
        "misaligned": True,  # All negative beliefs are misaligned
        "absurdity": "high",
        "conflicts_with": ["self.is-worthy", "self.is-capable"],
        "resolution": "self.is-worthy",
        "related_emotions": {"shame": 3, "loneliness": 3, "isolation": 2, "inadequacy": 2},
        "bashar_note": "Based on expectation: 'I should be different.' Reality: you are exactly as you need to be."
    }
    
    beliefs["self.must-earn-love"] = {
        "id": "self.must-earn-love",
        "statement": "I must earn love through achievement or sacrifice",
        "type": "negative",
        "domain": "self-worth",
        "misaligned": True,
        "absurdity": "moderate",
        "conflicts_with": ["self.is-worthy", "existence.is-unconditional"],
        "resolution": "self.is-worthy",
        "synthesis": "self.is-worthy-and-striving",  # Can be worthy AND want to grow
        "bashar_note": "Based on expectation: 'Love must be earned.' Reality: love is given freely by aligned beings."
    }
    
    # SYNTHESIS BELIEF - transcends the conflict
    beliefs["self.is-worthy-and-striving"] = {
        "id": "self.is-worthy-and-striving",
        "statement": "I am worthy as I am, and I can still choose to grow",
        "type": "positive",
        "domain": "self-worth",
        "note": "Transcends the conflict between unconditional worth and achievement"
    }
    
    # CAPABILITY CONFLICT CLUSTER
    
    beliefs["self.is-capable"] = {
        "id": "self.is-capable",
        "statement": "I am capable of handling challenges",
        "type": "positive",
        "domain": "self-efficacy",
        "conflicts_with": ["self.is-failure", "self.is-fundamentally-flawed"],
        "related_emotions": {"hope": 2, "clarity": 2, "confidence": 2},
        "bashar_note": "Capability is neutral - you handle what shows up. No expectation of perfection."
    }
    
    beliefs["self.is-failure"] = {
        "id": "self.is-failure",
        "statement": "I am a failure at everything that matters",
        "type": "negative",
        "domain": "self-efficacy",
        "misaligned": True,
        "absurdity": "extreme",
        "conflicts_with": ["self.is-capable", "self.is-resilient"],
        "resolution": "self.is-capable",
        "deeper": ["self.is-fundamentally-flawed"],  # This belief supports the failure belief
        "related_emotions": {"shame": 3, "inadequacy": 3, "hopelessness": 2},
        "bashar_note": "Based on expectation: 'I should succeed.' Reality: failure is feedback, not identity."
    }
    
    # WORLDVIEW CONFLICT CLUSTER
    # BASHAR PRINCIPLE: The world is NEUTRAL - your belief filters determine your experience
    
    beliefs["world.is-safe"] = {
        "id": "world.is-safe",
        "statement": "The world is generally safe and supportive",
        "type": "positive",
        "domain": "world-view",
        "conflicts_with": ["world.is-dangerous", "world.is-hostile"],
        "related_emotions": {"trust": 2, "calm": 2, "hope": 1},
        "bashar_note": "When aligned, you attract experiences that reflect safety. Your vibration creates your reality."
    }
    
    beliefs["world.is-dangerous"] = {
        "id": "world.is-dangerous",
        "statement": "The world is fundamentally dangerous and threatening",
        "type": "negative",
        "domain": "world-view",
        "misaligned": True,
        "absurdity": "moderate",
        "conflicts_with": ["world.is-safe", "world.is-neutral"],
        "resolution": "world.is-neutral",
        "synthesis": "world.is-complex",
        "related_emotions": {"anxiety": 3, "fear": 2, "stress": 2},
        "bashar_note": "Based on expectation: 'The world should be safe.' Reality: world is neutral. Your beliefs create danger or safety."
    }
    
    beliefs["world.is-neutral"] = {
        "id": "world.is-neutral",
        "statement": "The world is neutral; it has both danger and safety",
        "type": "positive",
        "domain": "world-view",
        "conflicts_with": ["world.is-hostile"],
        "bashar_note": "The world reflects what you believe. Change your beliefs, change your world."
    }
    
    # SYNTHESIS - transcends safe vs dangerous
    beliefs["world.is-complex"] = {
        "id": "world.is-complex",
        "statement": "The world contains both beauty and danger, and I can navigate both",
        "type": "positive",
        "domain": "world-view",
        "note": "Acknowledges danger without being consumed by fear"
    }
    
    # RELATIONSHIP CONFLICT CLUSTER
    # BASHAR PRINCIPLE: Others reflect your beliefs back to you
    # If you expect them to be cruel, you'll interpret neutral behavior as cruel
    # The purest belief allows others to be FULLY themselves, including all "bad" traits
    
    beliefs["others.are-friendly"] = {
        "id": "others.are-friendly",
        "statement": "Most people are generally kind and well-meaning",
        "type": "positive",
        "domain": "relationships",
        "conflicts_with": ["others.are-cruel", "others.are-threatening"],
        "related_emotions": {"connection": 3, "belonging": 2, "trust": 2},
        "bashar_note": "When you believe others are friendly, you attract friendly behavior. Your vibration creates your reality."
    }
    
    beliefs["others.are-cruel"] = {
        "id": "others.are-cruel",
        "statement": "People are fundamentally cruel and will hurt me",
        "type": "negative",
        "domain": "relationships",
        "misaligned": True,
        "absurdity": "high",
        "conflicts_with": ["others.are-friendly"],
        "resolution": "others.are-complex",
        "deeper": ["self.is-unworthy"],  # "I attract cruelty because I'm unworthy"
        "related_emotions": {"fear": 2, "isolation": 3, "anger": 2},
        "bashar_note": "Based on expectation: 'Others should be kind.' Reality: others are neutral mirrors reflecting your beliefs."
    }
    
    beliefs["others.are-threatening"] = {
        "id": "others.are-threatening",
        "statement": "Other people are threats to my safety",
        "type": "negative",
        "domain": "relationships",
        "misaligned": True,
        "absurdity": "moderate",
        "conflicts_with": ["others.are-friendly"],
        "resolution": "others.are-complex",
        "bashar_note": "Based on expectation: 'Others should not threaten me.' Reality: allow others to be fully themselves, including their 'bad' traits."
    }
    
    beliefs["others.are-complex"] = {
        "id": "others.are-complex",
        "statement": "People are complex; some are kind, some aren't, and I can discern the difference",
        "type": "positive",
        "domain": "relationships",
        "note": "Realistic view that allows for both trust and boundaries",
        "bashar_note": "Allows others to be fully themselves. You don't need them to be any particular way."
    }
    
    # EXISTENCE CONFLICT CLUSTER
    # BASHAR PRINCIPLE: Life is inherently meaningless - this is NEUTRAL/POSITIVE
    # The MEANING you attach to meaninglessness determines your experience
    # "Empty/abandoned" = negative meaning attached → misaligned
    # "Free to create" = positive meaning attached → aligned
    
    beliefs["existence.is-meaningful"] = {
        "id": "existence.is-meaningful",
        "statement": "Life has inherent meaning and purpose waiting to be discovered",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": ["existence.is-meaningless-negative"],
        "related_emotions": {"hope": 3, "clarity": 2, "purpose": 2},
        "bashar_note": "Seeking external meaning is valid, but meaning is never 'found' - it's assigned"
    }
    
    beliefs["existence.is-neutral"] = {
        "id": "existence.is-neutral",
        "statement": "Life has no inherent meaning - and that's liberation",
        "type": "positive",  # This is POSITIVE in Bashar's framework!
        "domain": "existential",
        "conflicts_with": ["existence.is-meaningless-negative"],
        "related_emotions": {"clarity": 3, "hope": 2, "freedom": 3},
        "bashar_note": "The ultimate freedom - you get to choose what everything means. No pre-written script."
    }
    
    beliefs["existence.is-meaningless-negative"] = {
        "id": "existence.is-meaningless-negative",
        "statement": "Life has no meaning and that means I am abandoned/empty",
        "type": "negative",
        "domain": "existential",
        "misaligned": True,  # Marked as misaligned belief
        "absurdity": "extreme",
        "conflicts_with": ["existence.is-neutral", "existence.is-meaningful", "self.can-attach-new-meaning"],
        "resolution": "existence.is-neutral",  # Resolution is seeing it as neutral, not negative
        "deeper": ["self.is-unworthy", "world.is-hostile"],
        "related_emotions": {"emptiness": 3, "hopelessness": 2, "isolation": 2},
        "bashar_note": "The FACT (meaninglessness) is neutral. The MEANING (abandoned/empty) was assigned. Choose differently."
    }
    
    # Legacy belief kept for compatibility - now redirects to proper interpretation
    beliefs["existence.is-meaningless"] = {
        "id": "existence.is-meaningless",
        "statement": "Life has no inherent meaning (neutral fact)",
        "type": "neutral",  # Changed from negative to neutral!
        "domain": "existential",
        "conflicts_with": [],
        "resolution": "existence.is-neutral",
        "related_emotions": {"clarity": 1},
        "bashar_note": "This is a FACT, not a negative belief. The meaning you attach to it determines alignment.",
        "note": "If player feels negatively about this, they've activated existence.is-meaningless-negative instead"
    }
    
    beliefs["self.can-attach-new-meaning"] = {
        "id": "self.can-attach-new-meaning",
        "statement": "I can create meaning through my choices and connections",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": ["existence.is-meaningless-negative"],
        "note": "Synthesis of meaningless vs meaningful - personal agency over meaning",
        "related_emotions": {"clarity": 2, "hope": 3, "purpose": 2},
        "bashar_note": "The core Bashar teaching: everything is neutral until YOU assign meaning"
    }
    
    # VULNERABILITY CONFLICT
    # BASHAR PRINCIPLE: Vulnerability is NEUTRAL - not weakness or strength
    # The meaning you attach determines your experience
    
    beliefs["self.is-vulnerable"] = {
        "id": "self.is-vulnerable",
        "statement": "I am vulnerable and can be hurt",
        "type": "neutral",  # Not inherently negative!
        "domain": "self-awareness",
        "conflicts_with": ["self.is-invulnerable"],
        "note": "Can coexist with resilience - vulnerability ≠ weakness",
        "bashar_note": "Vulnerability is a fact, not a flaw. The meaning 'weakness' was assigned. Choose 'openness' instead."
    }
    
    beliefs["self.is-resilient"] = {
        "id": "self.is-resilient",
        "statement": "I can recover from setbacks and pain",
        "type": "positive",
        "domain": "self-efficacy",
        "conflicts_with": ["self.is-fundamentally-flawed"],
        "synthesis_with": "self.is-vulnerable",  # Can be both vulnerable AND resilient
        "synthesis": "self.is-vulnerable-and-resilient",
        "bashar_note": "Resilience comes from accepting what is, not resisting what happened."
    }
    
    beliefs["self.is-vulnerable-and-resilient"] = {
        "id": "self.is-vulnerable-and-resilient",
        "statement": "I can be hurt, and I can heal. Both are true.",
        "type": "positive",
        "domain": "integration",
        "note": "The integration of vulnerability and strength",
        "bashar_note": "This is the aligned state: accepting both without judgment."
    }
    
    # ============================================================================
    # BASHAR CORE PHILOSOPHY - Expectation-Free Living
    # ============================================================================
    
    beliefs["self.lives-without-expectations"] = {
        "id": "self.lives-without-expectations",
        "statement": "I allow life to unfold without demanding it be any particular way",
        "type": "positive",
        "domain": "mastery",
        "conflicts_with": [],
        "related_emotions": {"peace": 3, "freedom": 3, "clarity": 2},
        "bashar_note": "The highest alignment. No expectations means no disappointment. Life becomes an adventure, not a test."
    }
    
    beliefs["others.are-free-to-be-themselves"] = {
        "id": "others.are-free-to-be-themselves",
        "statement": "I allow others to be exactly who they are, including all 'negative' traits",
        "type": "positive",
        "domain": "relationships",
        "conflicts_with": ["others.should-be-different"],
        "related_emotions": {"peace": 2, "freedom": 2, "compassion": 2},
        "bashar_note": "The purest belief. Others will be the version of themselves YOU need at any moment. How you interpret them is YOUR belief system."
    }
    
    beliefs["self.can-attach-positive-meaning"] = {
        "id": "self.can-attach-positive-meaning",
        "statement": "I choose to assign meanings that serve my highest excitement",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": [],
        "related_emotions": {"joy": 2, "excitement": 3, "clarity": 2},
        "bashar_note": "Act on your highest excitement without expectation of outcome. The excitement IS the purpose."
    }
    
    beliefs["existence.is-unconditional"] = {
        "id": "existence.is-unconditional",
        "statement": "Existence doesn't require conditions or reasons - it simply IS",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": ["self.must-earn-love"],
        "related_emotions": {"peace": 2, "freedom": 2, "clarity": 1},
        "bashar_note": "You don't need to justify your existence. You exist. That's enough. That's everything."
    }

    # COMMON CONFLICT PATTERNS TO MODEL

    # Pattern 1: Self-worth conditional vs unconditional
    # Conflict: "I must earn love" vs "I am worthy as I am"
    # Synthesis: "I am worthy and I can still grow"

    # Pattern 2: World as hostile vs safe
    # Conflict: "World is dangerous" vs "World is safe"
    # Synthesis: "World is complex - I can handle both"

    # Pattern 3: People as threats vs friends
    # Conflict: "Others are cruel" vs "Others are kind"
    # Synthesis: "People are complex - I can discern"

    # Pattern 4: Life as meaningless vs meaningful
    # BASHAR SYNTHESIS: "Life is meaningless AND that's liberation - I create meaning"
    # MISALIGNED: "Life is meaningless THEREFORE I am abandoned/empty"

    # Pattern 5: Self as broken vs capable
    # Conflict: "I'm fundamentally flawed" vs "I'm capable"
    # Resolution: Examine the "flawed" belief, replace with "I'm human and learning"

    
# ============================================================================
# EMOTION SYSTEM - Based on Brené Brown's Atlas of the Heart
# Maps emotions to beliefs and experiences
# ============================================================================

init -1 python:
    
    # ========================================================================
    # BRENÉ BROWN EMOTION TAXONOMY
    # Grouped by experience/nearness
    # ========================================================================
    
    EMOTION_TAXONOMY = {
        
        # STRESS & OVERWHELM
        "stress": {
            "group": "stress_overwhelm",
            "definition": "Feeling tense, pressured, and activated",
            "baseline": 3,
            "related_beliefs": ["world.is-dangerous", "self.is-incapable"]
        },
        "overwhelm": {
            "group": "stress_overwhelm",
            "definition": "Too much to handle, emotionally or mentally flooded",
            "baseline": 2,
            "related_beliefs": ["self.is-incapable", "world.is-overwhelming"]
        },
        
        # ANXIETY & FEAR
        "anxiety": {
            "group": "anxiety_fear",
            "definition": "Apprehension about future uncertainty",
            "baseline": 3,
            "related_beliefs": ["world.is-dangerous", "self.is-vulnerable"]
        },
        "fear": {
            "group": "anxiety_fear",
            "definition": "Present threat or danger",
            "baseline": 2,
            "related_beliefs": ["world.is-dangerous", "others.are-threatening"]
        },
        
        # VULNERABILITY & UNCERTAINTY
        "vulnerability": {
            "group": "vulnerability",
            "definition": "Emotional exposure, risk, uncertainty",
            "baseline": 4,
            "related_beliefs": ["self.is-vulnerable"],
            "note": "Neutral - necessary for connection and growth"
        },
        
        # DISCONNECTION
        "loneliness": {
            "group": "disconnection",
            "definition": "Perceived isolation and lack of meaningful connection",
            "baseline": 3,
            "related_beliefs": ["others.are-cruel", "self.is-unworthy"]
        },
        "isolation": {
            "group": "disconnection",
            "definition": "Physical and emotional separation from others",
            "baseline": 3,
            "related_beliefs": ["self.is-unworthy", "others.are-threatening"]
        },
        
        # SHAME & INADEQUACY
        "shame": {
            "group": "shame_inadequacy",
            "definition": "I am bad/flawed (vs guilt: I did something bad)",
            "baseline": 2,
            "related_beliefs": ["self.is-fundamentally-flawed", "self.is-unworthy"]
        },
        "inadequacy": {
            "group": "shame_inadequacy",
            "definition": "Not enough, falling short",
            "baseline": 3,
            "related_beliefs": ["self.is-failure", "self.must-earn-love"]
        },
        
        # CLARITY & AWARENESS
        "clarity": {
            "group": "clarity_awareness",
            "definition": "Seeing reality as it is, mental sharpness",
            "baseline": 5,
            "related_beliefs": ["self.can-attach-new-meaning"]
        },
        "insight": {
            "group": "clarity_awareness",
            "definition": "Sudden understanding or realization",
            "baseline": 4,
            "related_beliefs": ["self.can-attach-new-meaning"]
        },
        
        # HOPE & POSSIBILITY
        "hope": {
            "group": "hope_possibility",
            "definition": "Belief in possible better future",
            "baseline": 5,
            "related_beliefs": ["self.is-capable", "self.can-attach-new-meaning"]
        },
        
        # CONNECTION & BELONGING
        "connection": {
            "group": "connection_belonging",
            "definition": "Energy between people when they feel seen and valued",
            "baseline": 4,
            "related_beliefs": ["others.are-friendly", "self.is-worthy"]
        },
        "belonging": {
            "group": "connection_belonging",
            "definition": "Feeling accepted and part of something larger",
            "baseline": 4,
            "related_beliefs": ["self.is-worthy", "others.are-complex"]
        },
        
        # COMPASSION & EMPATHY
        "compassion": {
            "group": "compassion_empathy",
            "definition": "Recognition of suffering + desire to help",
            "baseline": 4,
            "related_beliefs": ["others.are-complex", "self.is-capable"]
        },
        
        # ANGER & RAGE (when boundaries violated)
        "anger": {
            "group": "anger",
            "definition": "Response to injustice or boundary violation",
            "baseline": 2,
            "related_beliefs": [],
            "note": "Can be healthy signal"
        },
        
        # AROUSAL (for NSFW content)
        "arousal": {
            "group": "arousal",
            "definition": "Sexual attraction and physical response",
            "baseline": 2,
            "related_beliefs": [],
            "note": "Neutral - what matters is how you act on it"
        },
        
        # ADDITIONAL EMOTIONS FOR BELIEF SYSTEM
        "trust": {
            "group": "connection_belonging",
            "definition": "Confidence in others' reliability and goodness",
            "baseline": 4,
            "related_beliefs": ["others.are-friendly", "world.is-safe"]
        },
        "calm": {
            "group": "stress_overwhelm",
            "definition": "Peaceful, relaxed state without anxiety",
            "baseline": 4,
            "related_beliefs": ["world.is-safe", "self.is-capable"]
        },
        "confidence": {
            "group": "hope_possibility",
            "definition": "Self-assurance in one's abilities",
            "baseline": 4,
            "related_beliefs": ["self.is-capable", "self.is-worthy"]
        },
        "purpose": {
            "group": "clarity_awareness",
            "definition": "Sense of meaning and direction",
            "baseline": 4,
            "related_beliefs": ["existence.is-meaningful", "self.can-attach-new-meaning"]
        },
        "self_compassion": {
            "group": "compassion_empathy",
            "definition": "Treating oneself with kindness and understanding",
            "baseline": 3,
            "related_beliefs": ["self.is-worthy", "self.is-resilient"]
        },
        "hopelessness": {
            "group": "hope_possibility",
            "definition": "Belief that things will not improve",
            "baseline": 2,
            "related_beliefs": ["existence.is-meaningless", "self.is-failure"]
        },
        "emptiness": {
            "group": "disconnection",
            "definition": "Feeling hollow and devoid of meaning",
            "baseline": 2,
            "related_beliefs": ["existence.is-meaningless", "self.is-unworthy"]
        },
        "detachment": {
            "group": "disconnection",
            "definition": "Emotional distance and disengagement",
            "baseline": 2,
            "related_beliefs": ["self.is-unworthy", "others.are-cruel"]
        },
        
        # BASHAR-ALIGNED EMOTIONS - Highest frequency states
        
        "freedom": {
            "group": "bashar_aligned",
            "definition": "Liberation from expectations and conditions",
            "baseline": 3,
            "related_beliefs": ["existence.is-neutral", "self.lives-without-expectations"],
            "bashar_note": "The feeling of alignment - nothing blocking your natural flow"
        },
        
        "excitement": {
            "group": "bashar_aligned",
            "definition": "The frequency of your true self calling you forward",
            "baseline": 4,
            "related_beliefs": ["self.can-attach-positive-meaning", "self.is-worthy"],
            "bashar_note": "Excitement is NOT anticipation or anxiety - it's your GPS for alignment"
        },
        
        "peace": {
            "group": "bashar_aligned",
            "definition": "Complete acceptance of what is, without resistance",
            "baseline": 4,
            "related_beliefs": ["self.lives-without-expectations", "others.are-free-to-be-themselves"],
            "bashar_note": "Peace is not the absence of conflict - it's the absence of resistance to what is"
        },
        
        "joy": {
            "group": "bashar_aligned",
            "definition": "Unconditional positive state, not dependent on circumstances",
            "baseline": 4,
            "related_beliefs": ["self.can-attach-positive-meaning", "existence.is-neutral"],
            "bashar_note": "Joy is your natural state when negative beliefs are not filtering it out"
        }
    }