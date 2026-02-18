# DR. SARAH CHEN
init python:
    def initialize_npc_therapist():
        initialize_npc(
            "dr_chen",
            "Dr. Sarah Chen",

            # The therapist who chose to treat her own rapist
            starting_beliefs={
                # CORE BELIEFS (Intensity 3) - Her foundation
                "self.is-capable": BELIEF_INTENSITY_CORE,  # She CAN handle this
                "self.deserves-healing": BELIEF_INTENSITY_CORE,  # Why she took this case
                "others.can-change": BELIEF_INTENSITY_CORE,  # Her bet on the player
                
                # ACTIVE BELIEFS (Intensity 2) - Currently driving behavior
                "self.is-in-control": BELIEF_INTENSITY_ACTIVE,  # Maintaining boundaries
                "forgiveness.is-power": BELIEF_INTENSITY_ACTIVE,  # Her goal
                "healing.requires-accountability": BELIEF_INTENSITY_ACTIVE,  # What she needs from player
                "trust.must-be-earned": BELIEF_INTENSITY_ACTIVE,  # Player starts at zero
                
                # SURFACE BELIEFS (Intensity 1) - Aware but not dominant
                "self.is-vulnerable": BELIEF_INTENSITY_SURFACE,  # She knows this is risky
                "player.might-be-monster": BELIEF_INTENSITY_SURFACE,  # Fear she's suppressing
                
                # TRAUMA BELIEFS (Intensity varies) - From the assault
                "men.can-be-violent": BELIEF_INTENSITY_ACTIVE,  # Activated by player's presence
                "alcohol.removes-consent": BELIEF_INTENSITY_CORE,  # Will never waver on this
                "self.was-not-at-fault": BELIEF_INTENSITY_EXAMINED,  # She's worked on this
                
                # CONFLICTING BELIEFS (Creating internal tension)
                "player.deserves-chance": BELIEF_INTENSITY_SURFACE,  # Why she took him on
                "player.might-not-change": BELIEF_INTENSITY_SURFACE,  # Her fear
            },
            starting_emotions={
                "clarity": 70,  # She's done a lot of work
                "anxiety": 50,  # Always present around player
                "hope": 45,  # Cautious hope he can change
                "trust": 20,  # Very low, must be earned
                "safety": 60,  # Professional setting helps
                "connection": 20,  # Will take time
                "overwhelm": 30,  # Managing her own triggers
            }
        )
        
        # Dr. Chen's memory of the assault
        dr_chen = get_npc("dr_chen")
        dr_chen.remember_event(
            "trauma_trigger",
            "player",
            "The assault. Drunk. Couldn't stop him. Woke up knowing what happened.",
            {"anxiety": 100, "trust": -100, "safety": -100, "isolation": 80}
        )
        
        # Her decision to take him on as patient
        dr_chen.remember_event(
            "healing",
            "player",
            "Patient attempted suicide after assault. I chose to treat him. For my healing, not his redemption.",
            {"clarity": 20, "hope": 10, "anxiety": 30}
        )
        
        # Set healing progress - she's far along but not complete
        dr_chen.healing_progress = 60  # Significant work done, but player is daily trigger
        dr_chen.introspection_depth = 5  # She understands herself deeply
        
        # Relationship with player starts at specific point
        dr_chen_rel = dr_chen.get_relationship_with("player")
        dr_chen_rel["trust"] = 0  # Absolute zero
        dr_chen_rel["boundary_violations"] = 1  # The assault
        dr_chen_rel["resentment"] = 70  # She's human
        dr_chen_rel["intimacy"] = 0  # Professional only
        dr_chen_rel["can_forgive"] = True  # Eventually, if he earns it
        dr_chen_rel["witnessed_change"] = 0  # Starts at zero

# Dr. Chen's interpretation patterns
init python:
    def dr_chen_interpret_player_action(action_type, context):
        """
        How Dr. Chen interprets player's actions.
        She's HIGHLY attuned to exploitation vs genuine change.
        """
        
        dr_chen = get_npc("dr_chen")
        rel = dr_chen.get_relationship_with("player")
        
        if action_type == "exploits_vulnerable_patient":
            # This is what she's watching for
            
            interpretation = {
                "thought": "He's doing it again. Using vulnerability for his own needs.",
                "emotion_shift": {
                    "anxiety": 30,
                    "trust": -20,
                    "safety": -15,
                    "clarity": 10  # She sees clearly what he is
                },
                "belief_impact": [
                    ("player.might-be-monster", 1),  # Confirms her fear
                    ("others.can-change", -1),  # Erodes her hope
                    ("self.made-mistake", 1),  # Should she have taken him on?
                ],
                "professional_response": "cold_observation",
                "will_confront": True,
                "timing": "next_session"
            }
            
            # She remembers EVERYTHING
            dr_chen.remember_event(
                "boundary_violation",
                context.get("victim_id"),
                f"Patient exploited {context.get('victim_name')}. Pattern repeating.",
                interpretation["emotion_shift"]
            )
            
            # Her trust PLUMMETS
            rel["trust"] = max(0, rel["trust"] - 25)
            rel["witnessed_change"] = 0  # Reset
            
            return interpretation
        
        elif action_type == "shows_genuine_remorse":
            # What she needs to see
            
            # But she's skeptical - is it real or performance?
            if rel["witnessed_change"] < 3:
                interpretation = {
                    "thought": "Words are easy. I need to see sustained behavior.",
                    "emotion_shift": {
                        "hope": 5,
                        "anxiety": -5,
                        "trust": 2  # Tiny increase
                    },
                    "belief_impact": [
                        ("player.deserves-chance", 0),  # Maintaining
                    ],
                    "professional_response": "cautious_acknowledgment",
                    "will_confront": False
                }
            else:
                # Sustained pattern of genuine change
                interpretation = {
                    "thought": "This might be real. He's actually changing.",
                    "emotion_shift": {
                        "hope": 15,
                        "anxiety": -10,
                        "trust": 10,
                        "clarity": 10
                    },
                    "belief_impact": [
                        ("others.can-change", 1),  # Reinforces
                        ("player.deserves-chance", 1),
                        ("player.might-be-monster", -1)  # Weakens
                    ],
                    "professional_response": "warm_observation",
                    "will_confront": False
                }
            
            rel["witnessed_change"] += 1
            
            return interpretation
        
        elif action_type == "takes_accountability":
            # THE thing she needs
            
            interpretation = {
                "thought": "He's owning it. Not justifying. Not minimizing. Owning it.",
                "emotion_shift": {
                    "clarity": 20,
                    "hope": 20,
                    "trust": 15,
                    "anxiety": -15,
                    "overwhelm": -10
                },
                "belief_impact": [
                    ("healing.requires-accountability", 1),  # Validated
                    ("others.can-change", 1),
                    ("forgiveness.is-possible", 1)
                ],
                "professional_response": "significant_moment",
                "breakthrough": True
            }
            
            rel["trust"] += 20
            rel["healing_moments"] += 1
            rel["witnessed_change"] += 2  # Double weight
            
            dr_chen.healing_progress += 5  # SHE heals when HE takes accountability
            
            return interpretation
        
        return None

# Dr. Chen's dialogue patterns based on state
init python:
    def get_dr_chen_tone():
        """Determine Dr. Chen's current tone toward player"""
        
        dr_chen = get_npc("dr_chen")
        rel = dr_chen.get_relationship_with("player")
        
        trust = rel["trust"]
        witnessed_change = rel["witnessed_change"]
        
        # Early game (Chapters 1-2): Professional ice
        if witnessed_change == 0 and trust < 10:
            return {
                "tone": "clinical_detachment",
                "examples": [
                    "We'll begin with basic scenario work.",
                    "That's a choice. Let's examine why you made it.",
                    "I'm not here to judge you. I'm here to help you understand yourself."
                ],
                "body_language": "Maintains distance, minimal eye contact, perfect composure",
                "subtext": "I'm doing my job. Nothing more."
            }
        
        # Mid-game (Exploitation detected): Cold anger
        elif rel.get("boundary_violations", 0) > 1:
            return {
                "tone": "controlled_fury",
                "examples": [
                    "I see you're continuing the pattern.",
                    "We need to discuss what happened with [victim name].",
                    "Do you even see what you're doing to them?"
                ],
                "body_language": "Rigid posture, direct eye contact, barely contained emotion",
                "subtext": "I was wrong to believe in you."
            }
        
        # Mid-game (Genuine progress): Cautious warmth
        elif witnessed_change >= 3 and trust >= 30:
            return {
                "tone": "guarded_hope",
                "examples": [
                    "That was good work today, [player_name].",
                    "I'm seeing real effort. Keep going.",
                    "This is what change looks like. It's hard, but you're doing it."
                ],
                "body_language": "Slight softening, occasional smile, shorter distance",
                "subtext": "Maybe I was right to try this."
            }
        
        # Late game (Consistent accountability): Professional respect
        elif witnessed_change >= 8 and trust >= 60:
            return {
                "tone": "earned_respect",
                "examples": [
                    "You've come a long way, [player_name].",
                    "I want to talk to you about something personal.",
                    "I need to tell you something I've been holding back."
                ],
                "body_language": "Open posture, genuine smiles, can sit closer",
                "subtext": "You're not who I thought you were. Or maybe... you became someone new."
            }
        
        # Endgame (Forgiveness possible): Vulnerable honesty
        elif witnessed_change >= 12 and trust >= 80 and dr_chen.healing_progress >= 80:
            return {
                "tone": "vulnerable_truth",
                "examples": [
                    "I need to tell you why I took you on as a patient.",
                    "Do you remember what you did to me?",
                    "I forgive you. Not for you. For me."
                ],
                "body_language": "Tears, trembling, but standing firm",
                "subtext": "I release you. And in doing so, I release myself."
            }
        
        else:
            return {
                "tone": "neutral_professional",
                "examples": [
                    "Let's continue.",
                    "How did that make you feel?",
                    "What belief is driving this behavior?"
                ],
                "body_language": "Standard therapeutic posture",
                "subtext": "I'm watching. Always watching."
            }

# Key dialogue moments
init python:
    dr_chen_key_moments = {
        "initial_session": {
            "chapter": 1,
            "trigger": "first_therapy",
            "dialogue": [
                "Dr. Chen sits across from you, clipboard in hand. Her face is professional. Blank.",
                "dr_chen: 'I'm Dr. Sarah Chen. I'll be working with you during your recovery.'",
                "There's something in her eyes. Something cold. Or maybe... guarded.",
                "dr_chen: 'You attempted suicide. A gunshot to the head. Do you remember why?'",
                "The question hangs in the air. Clinical. Detached.",
                "But you catch it - the slight tension in her jaw. The way she holds the pen just a little too tight."
            ]
        },
        
        "first_exploitation_witnessed": {
            "chapter": 3,
            "trigger": "player_exploits_patient",
            "dialogue": [
                "Dr. Chen is waiting when you arrive. She doesn't smile.",
                "dr_chen: 'Sit down. We need to talk about [victim name].'",
                "Her voice is ice.",
                "dr_chen: 'She came to me after your... conversation. Do you know what state she was in?'",
                "Silence. Heavy. Accusatory.",
                "dr_chen: 'You used her vulnerability. Just like...'",
                "She stops. Composes herself.",
                "dr_chen: 'Just like someone who sees people as objects, not humans.'"
            ]
        },
        
        "first_genuine_accountability": {
            "chapter": 4,
            "trigger": "player_owns_harm",
            "dialogue": [
                "Dr. Chen looks at you. Really looks, for maybe the first time.",
                "dr_chen: 'Say that again. What you just said.'",
                "You repeat it. The apology. The acknowledgment. No justification.",
                "Something shifts in her eyes.",
                "dr_chen: 'That's... that's the first time you've done that without defending yourself.'",
                "A pause. She sets down her clipboard.",
                "dr_chen: 'Keep doing that. That's how people change.'"
            ]
        },
        
        "the_revelation": {
            "chapter": "final",
            "trigger": "player_ready_for_truth",
            "requires": {
                "witnessed_change": 12,
                "trust": 80,
                "no_recent_violations": True
            },
            "dialogue": [
                "Dr. Chen asks you to stay after session.",
                "The room is quiet. Just the two of you.",
                "dr_chen: 'I need to tell you something. Something I should have told you from the beginning.'",
                "Her hands shake slightly.",
                "dr_chen: 'The night you... the night before you shot yourself... do you remember?'",
                "Your stomach drops. Pieces clicking together.",
                "dr_chen: 'You were drunk. I was... you were my colleague. We were at the conference.'",
                "The world tilts.",
                "dr_chen: 'You raped me, [player_name]. And then you shot yourself.'",
                "Silence. The truth, naked and horrible.",
                "dr_chen: 'I took you on as my patient because... because I needed to see if people can change. If monsters can become human again.'",
                "Tears on her cheeks now.",
                "dr_chen: 'And you did. You became human. So I forgive you.'",
                "She stands.",
                "dr_chen: 'Not because you deserve it. But because I deserve to be free from hating you.'"
            ]
        }
    }
