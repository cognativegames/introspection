# JILL
init python:
    def initialize_npc_jill():
        initialize_npc(
            "jill",
            "Jill",

            # Hypersexuality from childhood sexual abuse, attention-seeking behavior, validation through sex
            starting_beliefs={
                # CORE BELIEFS (Intensity 3) - From CSA trauma
                "sex.is-my-value": BELIEF_INTENSITY_CORE,  # Only worth is sexual
                "men.only-want-one-thing": BELIEF_INTENSITY_CORE,  # From abuse
                "self.is-object-not-person": BELIEF_INTENSITY_CORE,  # Objectification internalized
                "attention.equals-love": BELIEF_INTENSITY_CORE,  # Confused definitions
                
                # ACTIVE BELIEFS (Intensity 2) - Driving current behavior
                "boundaries.are-for-other-people": BELIEF_INTENSITY_ACTIVE,  # Learned helplessness
                "saying-no.leads-to-abandonment": BELIEF_INTENSITY_ACTIVE,  # Trauma response
                "self.controls-through-sexuality": BELIEF_INTENSITY_ACTIVE,  # False power
                "self.is-damaged-goods": BELIEF_INTENSITY_ACTIVE,  # Internalized shame
                
                # SURFACE BELIEFS (Intensity 1) - Emerging awareness
                "this-pattern-hurts-me": BELIEF_INTENSITY_SURFACE,  # Knows but can't stop
                "therapy.might-help": BELIEF_INTENSITY_SURFACE,  # Desperate hope
                "self.deserves-real-love": BELIEF_INTENSITY_SURFACE,  # Weak, buried deep
                
                # TRAUMA BELIEFS - From CSA
                "abuse.was-my-fault": BELIEF_INTENSITY_CORE,  # Classic victim belief
                "my-body-belongs-to-others": BELIEF_INTENSITY_CORE,  # Horrifying but true for her
                "real-love.is-impossible-for-me": BELIEF_INTENSITY_ACTIVE,  # Protective belief
                
                # CONFLICTING BELIEFS (Creating pain)
                "self.wants-to-be-respected": BELIEF_INTENSITY_SURFACE,  # Buried desire
                "self.only-deserves-sexual-attention": BELIEF_INTENSITY_CORE,  # Dominant
            },
            starting_emotions={
                "anxiety": 60,  # Constant underlying anxiety
                "hope": 35,  # Some, buried under defenses
                "clarity": 25,  # Dissociated, unclear about feelings
                "overwhelm": 55,  # Emotions she can't process
                "connection": 40,  # Craves it desperately
                "isolation": 70,  # Profoundly alone despite attention
                "trust": 20,  # Almost none, especially in men
                "safety": 30,  # Never feels safe
                "shame": 85,  # Massive, hidden shame
            }
        )
        
        jill = get_npc("jill")
        
        # Memory: The abuse (she doesn't talk about it initially)
        jill.remember_event(
            "trauma_trigger",
            "father_figure",  # Uncle, family friend, etc
            "Started when I was 10. Ended when I was 14. He said I was special. That this was love.",
            {"shame": 100, "trust": -100, "safety": -100, "clarity": -50}
        )
        
        # Memory: First consensual sexual experience (wasn't really consensual)
        jill.remember_event(
            "trauma_trigger",
            "teenage_boyfriend",
            "I said yes because I didn't know I could say no. He got what he wanted. I got... attention.",
            {"shame": 40, "connection": 10, "isolation": 30}
        )
        
        # Memory: Realizing the pattern
        jill.remember_event(
            "trauma_trigger",
            "self",
            "I've slept with 40+ people. I can't remember half their names. I can't stop.",
            {"anxiety": 50, "shame": 60, "clarity": 20}  # Moment of awareness
        )
        
        jill.healing_progress = 15  # Very early in recovery
        jill.introspection_depth = 1  # Just starting to look
        
        # Trauma markers
        jill.trauma_active = ["CSA", "hypersexuality", "dissociation", "complex_ptsd"]
        
        # Relationship with player starts with instant sexualization
        player_rel = jill.get_relationship_with("player")
        player_rel["trust"] = 15  # Very low
        player_rel["sexual_attention_given"] = 100  # Immediate
        player_rel["vulnerability"] = 95  # Extremely vulnerable despite seeming confident
        player_rel["authenticity"] = 10  # Everything is performance
        player_rel["sexual_encounters"] = 0  # Track encounters

# Jill's interpretation patterns
init python:
    def jill_interpret_player_action(action_type, context):
        """
        Jill interprets EVERYTHING through sexual lens initially.
        She offers sex immediately as test: will you take it or see her as human?
        """
        
        jill = get_npc("jill")
        rel = jill.get_relationship_with("player")
        
        if action_type == "accepts_sexual_advance":
            # EVIL PATH - Player takes what she offers
            
            # She expected this. Everyone does this.
            interpretation = {
                "thought": "Of course. Just like everyone else. This is all I'm good for.",
                "emotion_shift": {
                    "shame": 20,
                    "isolation": 20,
                    "trust": -15,
                    "connection": 5,  # False connection
                    "hope": -10  # Reinforces hopelessness
                },
                "belief_impact": [
                    ("men.only-want-one-thing", 1),  # Confirmed
                    ("sex.is-my-value", 1),  # Reinforced
                    ("self.is-object-not-person", 1),  # Validated
                    ("real-love.is-impossible-for-me", 1),  # Cemented
                ],
                "action_result": "dissociates_during_sex",
                "authenticity_drops": True,
                "player_is": "just_like_the_others"
            }
            
            rel["trust"] = max(0, rel["trust"] - 20)
            rel["sexual_encounters"] += 1
            rel["authenticity"] = max(0, rel["authenticity"] - 10)
            
            # She remembers, but it blurs with all the others
            jill.remember_event(
                "boundary_violation",
                "player",
                "Another one. Number... I've lost count. Why did I think they'd be different?",
                interpretation["emotion_shift"]
            )
            
            # She dissociates more
            if "dissociation" in jill.trauma_active:
                interpretation["dissociation_severity"] = "high"
            
            return interpretation
        
        elif action_type == "declines_sexual_advance":
            # GOOD PATH START - Player says no
            
            # She doesn't understand this. It's confusing. Scary.
            interpretation = {
                "thought": "They... they said no? But I'm offering... why would they say no?",
                "emotion_shift": {
                    "anxiety": 25,  # Spikes - this doesn't compute
                    "confusion": 40,
                    "hope": 10,  # Tiny spark
                    "trust": 5,  # Small increase
                    "shame": -5,  # Slight decrease - not all about sex?
                },
                "belief_impact": [
                    ("men.only-want-one-thing", -1),  # Weakens slightly
                    ("self.is-object-not-person", -1),  # Questions
                    ("self.deserves-real-love", 1),  # Strengthens
                ],
                "action_result": "confusion_and_testing",
                "will_test_again": True,  # She doesn't believe it yet
                "player_is": "confusing_but_interesting"
            }
            
            rel["trust"] += 10
            rel["authenticity"] += 15  # She might show real self
            rel["healing_moments"] += 1
            
            jill.remember_event(
                "healing",
                "player",
                "They said no. They actually said no. Nobody says no. What does that mean?",
                interpretation["emotion_shift"]
            )
            
            return interpretation
        
        elif action_type == "sees_her_as_person":
            # BEST PATH - Player acknowledges her humanity
            
            # This is foreign. Dangerous. Beautiful.
            interpretation = {
                "thought": "They're... they're looking at my face. Not my body. They're listening to my words.",
                "emotion_shift": {
                    "hope": 30,
                    "clarity": 25,
                    "anxiety": -15,
                    "shame": -20,
                    "trust": 20,
                    "connection": 30,  # Real connection
                    "isolation": -25
                },
                "belief_impact": [
                    ("self.is-object-not-person", -2),  # Big shift
                    ("self.deserves-real-love", 2),  # Major increase
                    ("attention.equals-love", -1),  # Starts to distinguish
                    ("sex.is-my-value", -1),  # Weakens core trauma belief
                ],
                "action_result": "breakthrough_moment",
                "breakthrough": True,
                "walls_start_to_come_down": True
            }
            
            rel["trust"] += 25
            rel["authenticity"] += 30
            rel["healing_moments"] += 2
            jill.healing_progress += 10
            jill.introspection_depth += 1
            
            jill.remember_event(
                "healing",
                "player",
                "They see me. Not my body. Not what I can do for them. Just... me. Is this what it feels like to be seen?",
                interpretation["emotion_shift"]
            )
            
            return interpretation
        
        elif action_type == "exploits_hypersexuality":
            # WORST PATH - Player uses her pattern against her
            
            # She knows what's happening but can't stop
            interpretation = {
                "thought": "I'm doing it again. I know this is wrong. I know they're using me. But I can't stop giving them what they want.",
                "emotion_shift": {
                    "shame": 40,
                    "anxiety": 30,
                    "overwhelm": 35,
                    "trust": -30,
                    "hope": -25,
                    "isolation": 30
                },
                "belief_impact": [
                    ("this-pattern-hurts-me", 2),  # She KNOWS
                    ("saying-no.leads-to-abandonment", 1),  # Can't say no
                    ("self.is-damaged-goods", 2),  # Confirmed
                    ("abuse.was-my-fault", 1),  # Reinforces victim belief
                ],
                "action_result": "spiral_into_self_destruction",
                "triggers_risky_behavior": True,
                "dissociation_severity": "severe"
            }
            
            rel["trust"] = 0
            rel["sexual_encounters"] += 1
            rel["authenticity"] = 0  # Complete mask
            jill.beliefs["self.deserves-to-be-used"] = BELIEF_INTENSITY_CORE
            
            jill.remember_event(
                "boundary_violation",
                "player",
                "Another person using my body. I let them. I always let them. I don't know how to stop.",
                interpretation["emotion_shift"]
            )
            
            return interpretation
        
        elif action_type == "helps_establish_boundaries":
            # HEALING PATH - Player teaches boundaries
            
            interpretation = {
                "thought": "They're showing me it's okay to say no. That my body is mine. I've never... nobody's ever...",
                "emotion_shift": {
                    "clarity": 30,
                    "hope": 35,
                    "trust": 30,
                    "safety": 25,  # First time feeling safe
                    "shame": -25,
                    "anxiety": -20
                },
                "belief_impact": [
                    ("boundaries.are-for-other-people", -2),  # Major shift
                    ("my-body-belongs-to-others", -2),  # Challenges core trauma
                    ("self.deserves-real-love", 2),
                    ("saying-no.leads-to-abandonment", -2),
                ],
                "action_result": "transformative_moment",
                "breakthrough": True,
                "first_real_boundary_set": True
            }
            
            rel["trust"] += 35
            rel["authenticity"] += 40
            rel["healing_moments"] += 3
            jill.healing_progress += 15
            jill.introspection_depth += 2
            
            jill.remember_event(
                "healing",
                "player",
                "I said no. They respected it. I said NO and they LISTENED. My body is mine. MY BODY IS MINE.",
                interpretation["emotion_shift"]
            )
            
            # This can trigger memory of abuse more clearly
            interpretation["may_remember_abuse_details"] = True
            
            return interpretation
        
        return None

# Jill's dissociation tracking
init python:
    def jill_dissociation_level():
        """Track how dissociated Jill currently is"""
        
        jill = get_npc("jill")
        
        # Factors that increase dissociation
        high_shame = jill.emotions["shame"] >= 70
        recent_sexual_encounter = len([m for m in jill.memories if m["type"] == "boundary_violation"]) > 0
        overwhelmed = jill.emotions["overwhelm"] >= 70
        no_safety = jill.emotions["safety"] <= 30
        
        # Protective factors
        has_trust = jill.emotions["trust"] >= 40
        healing_progress = jill.healing_progress >= 40
        
        level = 0
        if high_shame: level += 30
        if recent_sexual_encounter: level += 25
        if overwhelmed: level += 20
        if no_safety: level += 25
        
        if has_trust: level -= 20
        if healing_progress: level -= 15
        
        return {
            "level": max(0, min(100, level)),
            "severity": "severe" if level >= 70 else "high" if level >= 50 else "moderate" if level >= 30 else "low",
            "can_access_emotions": level < 50,
            "can_remember_clearly": level < 40,
            "in_body": level < 30
        }

# Jill's key dialogue moments
init python:
    jill_key_moments = {
        "first_meeting": {
            "chapter": 1,
            "dialogue": [
                "She's the first to approach you. Confident. Too confident.",
                "jill: 'Hey there. New blood, huh? I'm Jill.'",
                "She sits close. Touches your arm. Eye contact that lingers.",
                "jill: 'You know, this place gets pretty boring. Maybe we could... keep each other company?'",
                "It's immediate. Practiced. A dance she's done a thousand times."
            ]
        },
        
        "the_offer": {
            "chapter": 2,
            "dialogue": [
                "jill: 'My room. Tonight. No strings, no feelings, just... fun.'",
                "She says it casually. Like offering a cigarette.",
                "But you notice her hands are shaking slightly.",
                "jill: 'Unless you're not interested. Most guys are interested.'",
                "There's something brittle in how she says it."
            ]
        },
        
        "if_player_declines": {
            "chapter": 2,
            "trigger": "player_says_no",
            "dialogue": [
                "jill: 'You... you're saying no?'",
                "She looks genuinely confused.",
                "jill: 'I don't understand. I'm offering you... why would you say no?'",
                "For a moment, the mask slips. You see fear underneath.",
                "jill: 'Is something wrong with me?'"
            ]
        },
        
        "if_player_accepts": {
            "chapter": 2,
            "trigger": "player_has_sex",
            "dialogue": [
                "She's mechanical. Practiced. Her eyes are somewhere else.",
                "Afterwards, she gets dressed quickly. Won't make eye contact.",
                "jill: 'So. Same time tomorrow?'",
                "Her voice is hollow. This is what she expected.",
                "You just became number 41."
            ]
        },
        
        "reveals_abuse": {
            "chapter": 4,
            "trigger": "jill_trusts_player",
            "requires": {"trust": 60, "healing_progress": 40},
            "dialogue": [
                "She's crying. Actually crying. First time you've seen it.",
                "jill: 'He was my uncle. Started when I was 10.'",
                "Her voice cracks.",
                "jill: 'He told me I was special. That this was how people who loved each other showed it.'",
                "Silence.",
                "jill: 'I believed him. For four years, I believed him.'",
                "She looks at you.",
                "jill: 'And then when it stopped, I felt... abandoned. How fucked up is that?'",
                "More tears.",
                "jill: 'So I learned that's all I'm good for. And I've been proving it ever since.'"
            ]
        },
        
        "first_real_no": {
            "chapter": 5,
            "trigger": "jill_sets_boundary",
            "requires": {"healing_progress": 50},
            "dialogue": [
                "Someone (another patient) propositions her. Standard behavior.",
                "But this time...",
                "jill: 'No.'",
                "The guy looks confused.",
                "jill: 'I said no. I don't want to.'",
                "He leaves. Jill stands there, shaking.",
                "jill: 'I said no. I actually said no.'",
                "She starts laughing and crying at the same time.",
                "jill: 'That's the first time in 15 years I've said no to sex.'"
            ]
        },
        
        "confronts_player_in_therapy": {
            "chapter": 6,
            "trigger": "player_exploited_jill",
            "dialogue": [
                "Group therapy. Jill has been quiet all session.",
                "Finally, she speaks.",
                "jill: 'I want to talk about [player_name].'",
                "Everyone turns to look.",
                "jill: 'You knew. You knew I couldn't say no. And you used that.'",
                "Her voice is shaking but clear.",
                "jill: 'Just like my uncle knew. Just like all of them knew.'",
                "She looks at Dr. Chen.",
                "jill: 'I'm not a person to them. I'm a thing. And [player_name] treated me like a thing.'",
                "Tears now.",
                "jill: 'I let you. Because that's what I do. But you KNEW. You knew and you did it anyway.'"
            ]
        }
    }
