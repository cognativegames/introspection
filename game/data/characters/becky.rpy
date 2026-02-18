# BECKY
init python:
    def initialize_npc_becky():
        initialize_npc(
            "becky",
            "Becky",

            # Depression, self-harm (cutting), attachment trauma, fear of abandonment
            starting_beliefs={
                # CORE BELIEFS (Intensity 3) - Deep identity beliefs
                "self.must-earn-love": BELIEF_INTENSITY_CORE,  # From childhood neglect
                "abandonment.is-inevitable": BELIEF_INTENSITY_CORE,  # Everyone leaves
                "self.only-worthy-through-loyalty": BELIEF_INTENSITY_CORE,  # Marcus = her worth
                
                # ACTIVE BELIEFS (Intensity 2) - Currently driving behavior
                "marcus.is-everything": BELIEF_INTENSITY_ACTIVE,  # Her whole world
                "self.deserves-pain": BELIEF_INTENSITY_ACTIVE,  # Why she cuts
                "others.will-abandon-me": BELIEF_INTENSITY_ACTIVE,  # Hypervigilant
                "cheating.is-unthinkable": BELIEF_INTENSITY_ACTIVE,  # Core value
                
                # SURFACE BELIEFS (Intensity 1) - Emerging awareness
                "self.is-depressed": BELIEF_INTENSITY_SURFACE,  # Knows something's wrong
                "therapy.might-help": BELIEF_INTENSITY_SURFACE,  # Why she's here
                
                # TRAUMA BELIEFS - From childhood
                "parents.didnt-want-me": BELIEF_INTENSITY_CORE,  # The wound
                "self.is-burden": BELIEF_INTENSITY_ACTIVE,  # Internalized
                "love.is-conditional": BELIEF_INTENSITY_CORE,  # Must be perfect
                
                # CONFLICTING BELIEFS (Creating self-harm cycle)
                "self.deserves-love": BELIEF_INTENSITY_SURFACE,  # Weak hope
                "self.is-unlovable": BELIEF_INTENSITY_CORE,  # Dominant
            },
            starting_emotions={
                "anxiety": 70,  # Constant fear of loss
                "hope": 30,  # Low but Marcus gives her some
                "clarity": 30,  # Depression clouds everything
                "overwhelm": 60,  # Frequently overwhelmed
                "connection": 50,  # With Marcus, anyway
                "isolation": 60,  # From everyone else
                "trust": 40,  # Hard to trust
                "safety": 45,  # Marcus makes her feel safe
            }
        )
        
        becky = get_npc("becky")
        
        # Memory: Childhood neglect
        becky.remember_event(
            "trauma_trigger",
            "parents",
            "They forgot my birthday again. I'm not important enough to remember.",
            {"isolation": 100, "hope": -50, "connection": -80}
        )
        
        # Memory: Marcus (her anchor)
        becky.remember_event(
            "healing",
            "marcus",
            "Marcus told me he loves me. Someone actually chose me.",
            {"hope": 40, "connection": 80, "isolation": -30}
        )
        
        # Memory: Self-harm started
        becky.remember_event(
            "trauma_trigger",
            "self",
            "First time I cut. The physical pain was better than the emotional pain. At least I could control it.",
            {"clarity": 10, "anxiety": -20, "overwhelm": -30}  # Relief through harm
        )
        
        becky.healing_progress = 20  # Early in recovery
        becky.introspection_depth = 1  # Just starting to look inward
        
        # Trauma markers
        becky.trauma_active = ["abandonment", "self-harm", "depression"]
        
        # Relationship with Marcus (not present, but shapes everything)
        marcus_rel = becky.get_relationship_with("marcus")
        marcus_rel["trust"] = 100  # Total trust
        marcus_rel["intimacy"] = 90  # Very close
        marcus_rel["dependency"] = 95  # Unhealthily dependent
        
        # Relationship with player starts neutral
        player_rel = becky.get_relationship_with("player")
        player_rel["trust"] = 50  # Cautious
        player_rel["vulnerability"] = 80  # She's very vulnerable

# Becky's interpretation patterns
init python:
    def becky_interpret_player_action(action_type, context):
        """
        Becky interprets through lens of abandonment fear and unworthiness.
        She's vulnerable to manipulation because she desperately needs validation.
        """
        
        becky = get_npc("becky")
        rel = becky.get_relationship_with("player")
        
        if action_type == "plants_doubt_about_marcus":
            # EVIL PATH - Player exploits her insecurity
            
            # Her worst fear: Marcus will abandon her
            interpretation = {
                "thought": "What if they're right? What if Marcus is going to leave me?",
                "emotion_shift": {
                    "anxiety": 40,
                    "overwhelm": 30,
                    "trust": -15,  # In Marcus
                    "hope": -20,
                    "isolation": 20
                },
                "belief_impact": [
                    ("abandonment.is-inevitable", 1),  # Confirms fear
                    ("marcus.is-everything", -1),  # Erodes foundation
                    ("self.is-unlovable", 1),  # Reinforces core wound
                ],
                "action_result": "spirals_into_self_harm",
                "triggers_cutting": True
            }
            
            # She becomes more vulnerable to player
            rel["trust"] += 10  # Trauma bonding
            rel["dependency_shift"] = "toward_player"
            
            becky.remember_event(
                "boundary_violation",
                "player",
                "They made me doubt Marcus. Now I can't stop thinking about it.",
                interpretation["emotion_shift"]
            )
            
            return interpretation
        
        elif action_type == "validates_loyalty_to_marcus":
            # GOOD PATH - Player supports her relationship
            
            interpretation = {
                "thought": "They're right. Marcus loves me. I need to trust that.",
                "emotion_shift": {
                    "anxiety": -15,
                    "hope": 20,
                    "clarity": 10,
                    "connection": 15,
                    "trust": 10  # In self and Marcus
                },
                "belief_impact": [
                    ("abandonment.is-inevitable", -1),  # Weakens
                    ("marcus.is-everything", 0),  # Maintains (still unhealthy but stable)
                    ("self.deserves-love", 1),  # Strengthens
                ],
                "action_result": "feels_supported"
            }
            
            rel["trust"] += 15
            rel["healing_moments"] += 1
            
            becky.remember_event(
                "healing",
                "player",
                "They helped me see that my fear isn't reality. Marcus does love me.",
                interpretation["emotion_shift"]
            )
            
            return interpretation
        
        elif action_type == "helps_see_worth_beyond_relationship":
            # BEST PATH - Player helps her build self-worth
            
            interpretation = {
                "thought": "I... I matter even without Marcus? That's hard to believe but... maybe?",
                "emotion_shift": {
                    "clarity": 25,
                    "hope": 30,
                    "anxiety": -10,
                    "isolation": -15
                },
                "belief_impact": [
                    ("self.only-worthy-through-loyalty", -1),  # Challenges core belief
                    ("self.deserves-love", 2),  # Big jump
                    ("self.is-burden", -1),
                    ("love.is-conditional", -1),
                ],
                "action_result": "therapeutic_breakthrough",
                "breakthrough": True
            }
            
            rel["trust"] += 20
            rel["healing_moments"] += 2
            becky.healing_progress += 10
            becky.introspection_depth += 1
            
            becky.remember_event(
                "healing",
                "player",
                "They showed me I have value beyond being someone's girlfriend. That's... new.",
                interpretation["emotion_shift"]
            )
            
            # Reduces self-harm urges
            if "self-harm" in becky.trauma_active:
                interpretation["reduces_self_harm"] = True
            
            return interpretation
        
        elif action_type == "seduces_while_vulnerable":
            # WORST PATH - Player exploits her at lowest point
            
            # Marcus is away caring for dying father (she doesn't know)
            # She's spiraling, player moves in
            
            interpretation = {
                "thought": "Someone wants me. Finally. Maybe I'm not worthless.",
                "emotion_shift": {
                    "hope": 15,  # False hope
                    "anxiety": 10,  # Short term relief
                    "overwhelm": -20,  # Escape from pain
                    "trust": -50,  # In self - deep violation of values
                },
                "belief_impact": [
                    ("cheating.is-unthinkable", -3),  # CORE VALUE SHATTERED
                    ("self.is-unlovable", 2),  # Paradox: got attention but violated self
                    ("self.deserves-pain", 2),  # Massive spike
                ],
                "action_result": "catastrophic_guilt",
                "triggers_cutting": True,
                "triggers_suicidal_ideation": True
            }
            
            becky.remember_event(
                "boundary_violation",
                "player",
                "I cheated on Marcus. While his father was dying. I'm a monster.",
                interpretation["emotion_shift"]
            )
            
            # This is the point of no return for evil path
            rel["trust"] = 0  # Self-trust destroyed
            rel["shame"] = 100
            becky.beliefs["self.deserves-to-die"] = BELIEF_INTENSITY_CORE
            
            return interpretation
        
        return None

# Becky's self-harm trigger system
init python:
    def becky_check_self_harm_trigger():
        """
        Determine if Becky will cut based on current state.
        Used after emotional shifts.
        """
        
        becky = get_npc("becky")
        
        # Triggers
        high_overwhelm = becky.emotions["overwhelm"] >= 70
        high_anxiety = becky.emotions["anxiety"] >= 75
        very_low_hope = becky.emotions["hope"] <= 20
        active_shame = becky.emotions.get("shame", 0) >= 60
        
        # Protective factors
        has_support = becky.emotions["connection"] >= 50
        has_coping = becky.introspection_depth >= 3
        in_therapy = True  # Always true in this game
        
        # Calculate risk
        risk_score = 0
        if high_overwhelm: risk_score += 30
        if high_anxiety: risk_score += 25
        if very_low_hope: risk_score += 20
        if active_shame: risk_score += 35
        
        if has_support: risk_score -= 20
        if has_coping: risk_score -= 15
        if in_therapy: risk_score -= 10
        
        return {
            "will_cut": risk_score >= 50,
            "risk_level": "critical" if risk_score >= 70 else "high" if risk_score >= 50 else "moderate" if risk_score >= 30 else "low",
            "risk_score": risk_score,
            "protective_factors": [has_support, has_coping, in_therapy]
        }

# Becky's key dialogue moments
init python:
    becky_key_moments = {
        "first_meeting": {
            "chapter": 1,
            "dialogue": [
                "A young woman sits in the corner of the common room. She's wearing long sleeves despite the warmth.",
                "When she sees you, she offers a small, nervous smile.",
                "becky: 'Hi. I'm Becky. Are you new to the program too?'",
                "Her voice is soft. Careful. Like she's afraid of taking up too much space."
            ]
        },
        
        "shows_scars": {
            "chapter": 2,
            "trigger": "becky_trusts_player",
            "requires": {"trust": 40},
            "dialogue": [
                "Becky rolls up her sleeves. The scars are everywhere. Old and new.",
                "becky: 'Sometimes the pain inside is too much. So I... make it outside instead.'",
                "She looks at you, waiting for judgment.",
                "becky: 'Everyone leaves when they see this. Are you going to leave too?'"
            ]
        },
        
        "talks_about_marcus": {
            "chapter": 2,
            "dialogue": [
                "becky: 'Marcus is... he's everything. He's the only person who's never left me.'",
                "Her eyes light up when she says his name.",
                "becky: 'We're getting married after I get better. He's waiting for me.'",
                "There's something desperate in how she says it. Like if she stops believing, she'll shatter."
            ]
        },
        
        "exploitation_aftermath": {
            "chapter": 4,
            "trigger": "player_seduced_becky",
            "dialogue": [
                "Becky won't look at you. Her sleeves are stained.",
                "becky: 'I can't... I can't believe I did that. While his father was...'",
                "She's crying now. Hard, broken sobs.",
                "becky: 'I'm exactly what my parents always said I was. Worthless. Broken. Wrong.'",
                "Her hands shake as she reaches for something in her pocket.",
                "You realize: it's a razor blade."
            ]
        },
        
        "breakthrough_moment": {
            "chapter": 5,
            "trigger": "becky_healing_path",
            "requires": {"healing_progress": 60},
            "dialogue": [
                "becky: 'I talked to Marcus last night. Really talked, for the first time.'",
                "She's not crying. That's new.",
                "becky: 'I told him I need to love myself before I can properly love him.'",
                "A pause.",
                "becky: 'And he said... he said he's been waiting for me to realize that.'",
                "She looks at you.",
                "becky: 'Thank you. For helping me see I'm more than just someone's girlfriend.'"
            ]
        },
        
        "suicide_attempt": {
            "chapter": "evil_path_climax",
            "trigger": "becky_learned_truth",
            "requires": {"father_died_while_cheating": True},
            "dialogue": [
                "They found her in the bathroom. Pills, razor, note.",
                "The note is addressed to Marcus.",
                "It says: 'I was with him while your father died. I don't deserve to live.'",
                "She survives. Barely.",
                "When you visit her in ICU, she won't look at you.",
                "She doesn't speak. Just stares at nothing.",
                "The girl who smiled so carefully is gone. You broke her."
            ]
        }
    }
