# Prologue → Hospital sequence → First therapy → Encounter loop intro


# ============================================================================
# PROLOGUE - First Consciousness, Identity Formation
# Player's first introspective thoughts after brain injury
# Establishes core beliefs before story begins
# ============================================================================

label prologue:
    scene black
    
    # Content warning
    centered "{size=+10}CONTENT WARNING{/size}\n\nThis game contains depictions of:\n• Sexual assault\n• Suicidal ideation\n• Self-harm\n• Trauma\n\nPlayer discretion is advised.\n\nPress any key to continue."
    
    pause
    
    # ============================================================================
    # Pure consciousness - no visuals, just thoughts
    # ============================================================================
    
    scene black
    play sound "heartbeat_slow.mp3" fadein 3.0
    
    pause 2.0
    
    centered "{i}...{/i}"
    
    pause 1.0
    
    centered "{i}I am...{/i}"
    
    pause 1.0
    
    centered "{i}What am I?{/i}"
    
    pause 2.0
    
    # First thought
    "Darkness. Not sleep. Something else."
    
    "I can think. Therefore I... exist?"
    
    "But I don't know who I am."
    
    "No memories. No name. No past."
    
    "Just... awareness. Raw. Formless."
    
    pause 1.0
    
    "Questions rise from the void:"
    
    # ============================================================================
    # INTROSPECTION SEQUENCE - Building Core Beliefs
    # This is the encounter loop but in pure abstract space
    # No context, just philosophical/existential questions
    # ============================================================================
    
    scene introspection_void with fade
    play music "introspection_ambient.mp3" fadein 3.0
    
    centered "{size=+10}Who am I?{/size}"
    
    pause 1.0
    
    # Initialize game state
    python:
        game_state.phase = GAME_PHASE_INTROSPECT
    
    # ============================================================================
    # ENCOUNTER 1: Self-Worth (Core Identity)
    # ============================================================================
    
    "First question from the darkness:"
    
    centered "{i}Am I worthy of existence?{/i}"
    
    "No memories to base this on. Just... a feeling."
    
    menu:
        "What is your answer?"
        
        "Yes. I am worthy simply by existing.":
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("existence.is-unconditional", BELIEF_INTENSITY_ACTIVE)
            
            "A warmth. Small but certain."
            "I don't need to prove anything. I simply am."
            
        "I must earn my worth through actions.":
            $ game_state.activate_belief("self.must-earn-love", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_SURFACE)
            
            "Worth is earned. Not given."
            "I will have to prove I deserve to exist."
            
        "I don't know. How can I know without memories?":
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_SURFACE)
            $ game_state.activate_belief("self.is-unworthy", BELIEF_INTENSITY_SURFACE)
            
            "Uncertainty. Both possibilities exist."
            "I am... unformed. Potential."
    
    pause 1.0
    
    # ============================================================================
    # ENCOUNTER 2: Trust in Others (Relationship to World)
    # ============================================================================
    
    "Second question:"
    
    centered "{i}Can I trust others?{/i}"
    
    "I don't remember anyone. But the question itself implies others exist."
    
    "How do I feel about that?"
    
    menu:
        "What is your instinct?"
        
        "People are generally good. I can trust them.":
            $ game_state.activate_belief("others.are-friendly", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("world.is-safe", BELIEF_INTENSITY_SURFACE)
            
            "Openness. A belief in basic human decency."
            "Others will help me. They are not threats."
            
        "People will hurt me if I let them too close.":
            $ game_state.activate_belief("others.are-threatening", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("world.is-dangerous", BELIEF_INTENSITY_ACTIVE)
            
            "Caution. Self-protection."
            "I must guard myself. Trust is a vulnerability."
            
        "Some people are kind. Some are cruel. I must discern.":
            $ game_state.activate_belief("others.are-complex", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("world.is-neutral", BELIEF_INTENSITY_ACTIVE)
            
            "Balance. The world is not simple."
            "I will judge each person individually."
    
    pause 1.0
    
    # ============================================================================
    # ENCOUNTER 3: Capability (Self-Efficacy)
    # ============================================================================
    
    "Third question:"
    
    centered "{i}Can I handle what comes?{/i}"
    
    "I know nothing about what's coming. But I must believe something."
    
    menu:
        "What do you believe?"
        
        "I am capable. I can handle challenges.":
            $ game_state.activate_belief("self.is-capable", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.is-resilient", BELIEF_INTENSITY_SURFACE)
            
            "Strength. Not arrogance. Just... capability."
            "I will face what comes."
            
        "I will fail. I always fail.":
            $ game_state.activate_belief("self.is-failure", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("self.is-fundamentally-flawed", BELIEF_INTENSITY_ACTIVE)
            
            "Certainty of inadequacy."
            "Whatever happened to me, I probably deserved it."
            
        "I'm adaptable. I'll figure it out as I go.":
            $ game_state.activate_belief("self.is-resilient", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.can-attach-new-meaning", BELIEF_INTENSITY_SURFACE)
            
            "Flexibility. I don't need to know everything now."
            "I'll learn. I'll adapt."
    
    pause 1.0
    
    # ============================================================================
    # ENCOUNTER 4: Meaning (Existential Foundation)
    # BASHAR PRINCIPLE: Life IS meaningless - this is NEUTRAL and LIBERATING
    # You get to assign meaning. The question is: what meaning do you CHOOSE?
    # ============================================================================
    
    "Fourth question:"
    
    centered "{i}Why am I here?{/i}"
    
    "No memories of purpose. No mission. Just existence."
    
    "Does that mean anything?"
    
    "The void whispers: Meaning is not given. Meaning is created."
    
    menu:
        "What do you choose to believe?"
        
        "I will discover the meaning that already exists.":
            $ game_state.activate_belief("existence.is-meaningful", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.can-attach-positive-meaning", BELIEF_INTENSITY_SURFACE)
            
            "Purpose exists waiting to be found."
            "I will seek it. Discover it. It is there."
            
        "Existence has no inherent meaning... and that's LIBERATING.":
            # This is the BASHAR-ALIGNED choice - meaninglessness as freedom
            $ game_state.activate_belief("existence.is-neutral", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("self.can-attach-new-meaning", BELIEF_INTENSITY_ACTIVE)
            
            "Freedom. Total freedom."
            "No pre-written script to follow. No assigned role."
            "I get to CHOOSE what everything means."
            "This is not emptiness. This is power."
            
        "Existence has no inherent meaning... and that's EMPTY.":
            # This is the MISALIGNED interpretation - same fact, negative meaning attached
            $ game_state.activate_belief("existence.is-meaningless-negative", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("self.is-unworthy", BELIEF_INTENSITY_SURFACE)
            
            "Void. No purpose. No reason."
            "I exist in a universe that doesn't care... about me."
            "The meaninglessness feels like abandonment."
            
        "I create my own meaning through choice.":
            $ game_state.activate_belief("self.can-attach-new-meaning", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("existence.is-unconditional", BELIEF_INTENSITY_ACTIVE)
            
            "Agency. I decide what matters."
            "Meaning is what I make it."
            "I am the author of my own significance."
    
    pause 1.0
    
    # ============================================================================
    # ENCOUNTER 5: Vulnerability (Can I Be Hurt?)
    # ============================================================================
    
    "Final question from the void:"
    
    centered "{i}Am I vulnerable?{/i}"
    
    "Can I be hurt? Will I be hurt?"
    
    "Do I accept this?"
    
    menu:
        "What is true?"
        
        "Yes. I am vulnerable. And that's okay.":
            $ game_state.activate_belief("self.is-vulnerable", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.is-resilient", BELIEF_INTENSITY_SURFACE)
            
            "Acceptance. Vulnerability is not weakness."
            "I can be hurt and still continue."
            
        "I cannot let anyone hurt me. I must be invulnerable.":
            $ game_state.activate_belief("self.must-be-invulnerable", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("others.are-threatening", BELIEF_INTENSITY_ACTIVE)
            
            "Armor. Walls."
            "I will not let them see where I can be hurt."
            
        "I've already been hurt. Badly. I can feel it.":
            $ game_state.activate_belief("self.is-vulnerable", BELIEF_INTENSITY_CORE)
            $ game_state.activate_belief("self.deserves-healing", BELIEF_INTENSITY_SURFACE)
            
            "Pain. Even without memories, I know I'm wounded."
            "Something terrible happened. I need to heal."
    
    # ============================================================================
    # Consciousness Solidifying
    # ============================================================================
    
    pause 2.0
    
    scene black with fade
    stop music fadeout 3.0
    
    "The questions fade."
    
    "I have formed... something. A self. Provisional. Fragile."
    
    "Core beliefs established. Who I am, even without memories."
    
    # Check for conflicts and alignment
    python:
        initial_conflicts = game_state.detect_belief_conflicts()
        
        # Check for misaligned beliefs (all negative beliefs are misaligned)
        misaligned_beliefs = []
        for belief_id, intensity in game_state.beliefs.items():
            if intensity >= BELIEF_INTENSITY_ACTIVE:
                if belief_id in beliefs:
                    belief_data = beliefs.get(belief_id, {})
                    if belief_data.get("type") == "negative" or belief_data.get("misaligned"):
                        misaligned_beliefs.append(belief_id)
    
    if misaligned_beliefs:
        "I feel... tension. Contradictions within myself."
        
        "Some of my beliefs are out of alignment with who I truly am."
        
        "They feel like... expectations. Demands that reality be different."
        
        "This will create friction. Suffering. Until I examine them."
        
    elif initial_conflicts:
        "I feel... complexity. Different beliefs coexisting."
        
        "Not necessarily contradictions. Just... multiple truths."
        
        "I will need to navigate between them."
        
    else:
        "I feel... coherent. Aligned."
        
        "The beliefs I've formed fit together."
        
        "I am allowing life to be what it is, without demanding it be different."
        
        "This feels like freedom."
    
    pause 2.0
    
    "Now... awareness grows."
    
    "My body. I have a body."
    
    "Sensations. Touch. Temperature."
    
    "Sound... beeping. Steady. Rhythmic."
    
    "A voice. Distant."
    
    "Light, beyond my eyelids."
    
    pause 1.0
    
    "I could open my eyes."
    
    "I could see where I am."
    
    "Am I ready?"
    
    pause 2.0
    
    # ============================================================================
    # Transition to Chapter 1
    # ============================================================================
    
    scene white with Dissolve(3.0)
    
    "I open my eyes."
    
    # ============================================================================
    # Begin Chapter 1
    # ============================================================================
    
    jump chapter_1_start
