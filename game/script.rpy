# Introspection - Main Script File
# This file integrates all the components and contains the main story flow
# ./game/script.rpy

# Placeholder images (add after 'define config.name')
image bg apartment morning = "#2c3e50"
image bg park = "#27ae60"
image bg cafe = "#c0392b"
image bg office = "#3a3a4a"
image bg black = "#000000"
image bg void = "#1a1a2e"
image bg light = "#ecf0f1"
image bg apartment evening = "#34495e"

# Placeholder sounds - comment these out if you don't have audio files
# play music "audio/ambient_thoughtful.mp3"
# becomes:
# (silence for now)

# ============================================
# CONFIGURATION
# ============================================

# Game metadata
define config.name = "Introspection"
define config.version = "0.1.0"
define config.save_directory = "Introspection-1"

# Window settings
define config.window = "auto"
define config.narrator_menu = True

# ============================================
# CHARACTERS
# ============================================

define mc = Character("[player_name]", color="#c8c8ff")
define inner = Character("Inner Voice", color="#9370db", what_italic=True)
define narrator = Character(None, what_color="#ffffff")

# Supporting characters (add more as needed)
define alex = Character("Alex", color="#ff6b6b")
define jordan = Character("Jordan", color="#4ecdc4")

# ============================================
# TRANSITIONS & EFFECTS
# ============================================

define flash = Fade(0.1, 0.0, 0.3, color="#ffffff")
define slowdissolve = Dissolve(1.5)
define quickfade = Fade(0.3, 0.0, 0.3)

# ============================================
# DEFAULT VARIABLES
# ============================================

default player_name = "Alex"
default current_enc = None
default chosen_interpretation = None
default selected_belief = None
default intro_options = []

# ============================================
# MAIN ENTRY POINT
# ============================================

label start:
    # Initialize game state
    $ game = GameState()
    $ router = EncounterRouter()
    $ router.encounter_vault = encounters
    
    # Get player name
    $ player_name = renpy.input("What's your name?", default="Alex")
    $ player_name = player_name.strip() or "Alex"
    
    # Opening sequence
    scene bg black
    with fade
    
    # Content warning
    narrator "{color=#ff6b6b}Content Warning{/color}"
    narrator "This game explores beliefs about self-worth, relationships, and personal struggles."
    narrator "If you're experiencing a mental health crisis, please reach out:"
    narrator "988 - Suicide & Crisis Lifeline (US)"
    narrator "This game is not a substitute for professional help."
    
    menu:
        "Ready to begin?"
        
        "Yes, I understand":
            pass
        
        "Exit":
            return
    
    # Opening hook
    scene bg black
    with slowdissolve
    
    narrator "The mind is a storyteller."
    narrator "Every moment, it interprets what things mean."
    
    pause 0.8
    
    narrator "But what if the stories it tells you..."
    
    with flash
    
    narrator "...aren't true?"
    
    pause 1.0
    
    scene bg apartment morning
    with slowdissolve
    
    # Show HUD
    show screen emotional_hud
    
    narrator "This is a story about [player_name]."
    narrator "And the invisible beliefs that shape their world."
    
    pause 0.5
    
    inner "Every moment is filtered through what you believe."
    inner "Let's discover what you really believe..."
    
    menu:
        inner "Are you ready?"
        
        "Yes, show me":
            $ game.story_flags.add("willing_participant")
        
        "I'm nervous...":
            inner "That's perfectly natural. We'll go slow."
            $ game.story_flags.add("cautious_participant")
    
    jump chapter1_intro

# ============================================
# CHAPTER 1 - INTRODUCTION
# ============================================

label chapter1_intro:
    scene bg apartment morning
    with dissolve
    
    narrator "Saturday morning."
    narrator "You're meeting your friend Jordan for coffee later."
    narrator "It's been a good week. Productive. Calm."
    
    $ game.adjust_emotions(hope=10, clarity=5)
    
    mc "Today feels... good."
    
    pause 0.5
    
    inner "Does it?"
    
    # Queue the intro sequence
    $ router.queue_narrative_sequence("chapter1_intro")
    
    # Transition to walking
    scene bg park
    with dissolve
    
    narrator "You decide to walk to the coffee shop."
    narrator "It's a beautiful day."
    
    jump encounter_loop

# ============================================
# CORE ENCOUNTER LOOP
# ============================================

label encounter_loop:
    """Main game loop"""
    
    $ game.scene_count += 1
    
    # Get next encounter
    python:
        current_enc = get_next_encounter()
        if not current_enc:
            renpy.jump("chapter1_complete")
    
    # Set scene based on encounter
    scene expression "bg " + current_enc['scene']
    with dissolve
    
    # Present observation
    narrator "[current_enc['observation']]"
    
    pause 0.5
    
    # Internal moment
    inner "This moment... how do you see it?"
    
    jump present_interpretations

label present_interpretations:
    """Present interpretation choices"""
    
    # Build menu from encounter
    python:
        interp_list = current_enc['interpretations']
        
        # Present choices
        choices = [(interp['display'], interp) for interp in interp_list]
        
        # Add introspection option if available
        if game.introspection_depth > 0:
            choices.append(("I want to look deeper...", "introspect"))
        
        result = renpy.display_menu(choices)
        
        if result == "introspect":
            renpy.jump("begin_introspection")
        else:
            chosen_interpretation = result
    
    jump process_choice

label process_choice:
    """Process the player's interpretation"""
    
    # Show internal thought
    mc "[chosen_interpretation['internal_thought']]"
    
    pause 0.3
    
    # Show belief activation visually
    python:
        for belief_id in chosen_interpretation['activates']:
            belief = beliefs[belief_id]
            renpy.show_screen("belief_notification", 
                            belief['statement'], 
                            belief['type'])
            renpy.pause(1.5)
            renpy.hide_screen("belief_notification")
    
    # Process through state machine
    python:
        next_phase = process_interpretation(chosen_interpretation, current_enc)
    
    # Show consequence
    if chosen_interpretation['aligns']:
        call show_aligned_consequence
    else:
        call show_misaligned_consequence
    
    # Route to next phase
    if next_phase == "introspect_offer":
        jump introspect_offer
    elif should_offer_reflection():
        jump reflection_moment
    else:
        jump encounter_loop

label show_aligned_consequence:
    """Show positive outcome"""
    
    with flash
    
    narrator "✨ Reality: [current_enc['npc_intent']['true_intent']]"
    
    # Specific reactions based on encounter
    if current_enc['id'] == "dog_park":
        narrator "The dog licks your hand enthusiastically."
        narrator "Its owner jogs up, smiling. 'Sorry! He's very friendly!'"
        mc "It's okay! He's sweet!"
        
    elif current_enc['id'] == "stranger_smile":
        narrator "They smile wider and give a small wave."
        narrator "A brief connection between strangers."
        mc "(That felt... nice.)"
    
    elif current_enc['id'] == "compliment_received":
        narrator "Your colleague means it. They appreciated your work."
        mc "Thank you. I worked hard on it."
    
    $ game.adjust_emotions(clarity=5, hope=5)
    
    return

label show_misaligned_consequence:
    """Show suffering from misinterpretation"""
    
    with Dissolve(0.5)
    
    narrator "❌ But actually: [current_enc['npc_intent']['true_intent']]"
    
    # Show the gap
    if current_enc['id'] == "dog_park":
        narrator "The dog sits, confused by your fear."
        narrator "Its tail stops wagging."
        narrator "The owner calls it back, concerned."
        inner "The dog was never dangerous. Your belief made it so."
        
    elif current_enc['id'] == "stranger_smile":
        narrator "Their smile fades to confusion."
        narrator "They turn away, wondering what happened."
        inner "They offered kindness. You saw mockery."
        
    elif current_enc['id'] == "friend_cancel":
        narrator "Jordan really did have a conflict."
        narrator "But you're already spiraling..."
        inner "You turned their honesty into rejection."
    
    $ game.adjust_emotions(overwhelm=5, anxiety=5)
    
    return

label alex_confession:
    $ alex_level = game.get_relationship_level("alex", "trust")
    $ alex_romance = game.relationships["alex"]["romance"]
    
    if alex_level == "close" and alex_romance > 60:
        alex "I... I need to tell you something."
        alex "I think I'm falling for you."
        
        menu:
            "I feel the same way":
                $ game.adjust_relationship("alex", romance=20, trust=10)
                $ game.story_flags.add("alex_romance_begun")
                jump alex_romance_path
            
            "I care about you, but as a friend":
                $ game.adjust_relationship("alex", trust=5, romance=-30)
                jump alex_friendship_path
    
    else:
        # Not ready for this conversation yet
        alex "Hey, want to grab lunch?"

label check_for_rewards:
    $ game.check_achievements()
    
    if game.rewards_unlocked:
        $ reward = game.rewards_unlocked.pop(0)
        
        with flash
        scene bg light
        
        narrator "✨ Achievement Unlocked ✨"
        narrator "[reward['name']]"
        narrator "[reward['description']]"
        
        pause 2.0
    
    return

label deep_introspection:
    inner "Let's go deeper. Why do you believe you're fundamentally flawed?"
    
    menu:
        inner "What would happen if someone saw the 'real' you?"
        
        "They would reject me":
            $ selected_belief = "others.would-reject-real-me"
            inner "And if they rejected you... what would that mean?"
            
            menu:
                "It would prove I'm unlovable":
                    $ selected_belief = "self.unlovable-core"
                    inner "That's the deepest belief. Let's examine it."
                    jump examine_core_belief
                
                "I'd be alone forever":
                    $ selected_belief = "self.cannot-survive-alone"
                    jump examine_core_belief
        
        "They might accept me anyway":
            inner "Yes... what if they could?"
            jump positive_realization
            


# ============================================
# INTROSPECTION SEQUENCE
# ============================================

label introspect_offer:
    """Offer introspection"""
    
    scene bg black
    with slowdissolve
    
    pause 0.5
    
    inner "You feel it, don't you?"
    inner "That tightness. That voice saying 'something's wrong.'"
    
    pause 1.0
    
    inner "Want to look deeper?"
    
    menu:
        "Explore this feeling":
            jump begin_introspection
        
        "Not right now":
            inner "Okay. But notice how it feels."
            jump encounter_loop

label begin_introspection:
    """Introspection sequence"""
    
    $ game.phase = GamePhase.INTROSPECT
    
    scene bg void
    with slowdissolve
    
    # Get active negative belief
    python:
        active_negatives = game.get_active_negative_beliefs()
        if not active_negatives:
            renpy.jump("encounter_loop")
        
        current_belief_id = active_negatives[0]
        current_belief = beliefs[current_belief_id]
    
    inner "Let's look at what you believe..."
    
    pause 0.5
    
    inner "You believe: '{color=#ff6b6b}[current_belief['statement']]{/color}'"
    
    pause 1.5
    
    inner "But {i}why{/i}?"
    inner "What deeper belief makes this feel true?"
    
    # Get introspection options
    python:
        intro_options = get_introspection_options(current_belief_id)
        if not intro_options:
            renpy.jump("encounter_loop")
    
    jump present_introspection_choices

label present_introspection_choices:
    """Present deeper beliefs"""
    
    menu:
        inner "When you really look inside... what do you believe?"
        
        "[intro_options[0]['statement']]" if len(intro_options) > 0:
            $ selected_belief = intro_options[0]
            jump examine_belief
        
        "[intro_options[1]['statement']]" if len(intro_options) > 1:
            $ selected_belief = intro_options[1]
            jump examine_belief
        
        "[intro_options[2]['statement']]" if len(intro_options) > 2:
            $ selected_belief = intro_options[2]
            jump examine_belief

label examine_belief:
    """Examine selected belief"""
    
    inner "[selected_belief['statement']]"
    
    pause 1.5
    
    # Check if positive resolution
    if selected_belief['type'] == 'positive' or selected_belief.get('resolution'):
        jump belief_resolution
    
    # If absurd, help them see it
    if selected_belief.get('absurdity') == 'extreme':
        inner "Really? Is that actually true?"
        
        pause 1.0
        
        inner "Think about it..."
        inner "If someone you loved believed this about themselves..."
        inner "Would you think it was true?"
        
        menu:
            "No... that would be cruel":
                jump absurdity_realization
            
            "I don't know...":
                inner "Sit with it."
                pause 1.0
                jump absurdity_realization

label absurdity_realization:
    """Seeing through the belief"""
    
    with flash
    
    inner "Exactly."
    inner "So why believe it about yourself?"
    
    pause 2.0
    
    inner "What if... it's not true?"
    
    # Get resolution
    python:
        resolution_id = selected_belief.get('resolution')
        if resolution_id and resolution_id in beliefs:
            resolution_belief = beliefs[resolution_id]
        else:
            renpy.jump("encounter_loop")
    
    inner "What if instead..."
    
    pause 0.5
    
    inner "{color=#4ecdc4}[resolution_belief['statement']]{/color}"
    
    pause 2.0
    
    inner "Does that feel true?"
    
    menu:
        "Yes... it does":
            jump belief_resolution
        
        "I'm not ready":
            inner "That's okay. We'll keep exploring."
            jump return_to_story

label belief_resolution:
    """Transform belief"""
    
    with flash
    
    scene bg light
    with Dissolve(2.0)
    
    inner "✨ Yes."
    
    # Process transformation
    python:
        game.resolve_belief(current_belief_id, selected_belief['id'])
        game.adjust_emotions(hope=25, anxiety=-25, clarity=20, overwhelm=-20)
    
    inner "Something shifts."
    inner "The old belief dissolves."
    
    pause 1.5
    
    narrator "You feel lighter."
    
    $ game.story_flags.add("transformation_experienced")
    
    jump return_to_story

label return_to_story:
    """Return to narrative"""
    
    scene bg apartment evening
    with slowdissolve
    
    narrator "You take a breath."
    narrator "The world looks different."
    
    jump encounter_loop

# ============================================
# REFLECTION MOMENTS
# ============================================

label reflection_moment:
    """Brief emotional check-in"""
    
    $ dominant = game.get_dominant_emotion()
    
    if dominant == "hope":
        mc "I feel... hopeful."
        inner "Notice that. Hold onto it."
    
    elif dominant == "anxiety":
        mc "Why am I so anxious?"
        inner "What are you afraid is true?"
    
    elif dominant == "clarity":
        mc "Things are clearer now."
        inner "You're seeing more truly."
    
    pause 1.0
    
    jump encounter_loop

# ============================================
# PLOT STUFF
# ============================================
label talk_to_alex:
    alex "Hey, how are you really doing?"
    
    menu:
        # Normal option - always available
        "I'm fine":
            mc "Just fine, you know..."
        
        # Only show if they've resolved self-worth issues
        "Actually... I've been working on myself" if game.beliefs.get("self.is-worthy") == BELIEF_INTENSITY_RESOLVED:
            mc "I've realized some things about how I see myself."
            alex "That's... really great to hear."
            $ game.adjust_emotions(connection=15)
        
        # Only show if they're struggling
        "I feel like I'm drowning" if game.emotions["overwhelm"] > 60:
            mc "Everything feels too heavy."
            alex "I'm here for you. Want to talk about it?"
            jump alex_support_scene

label coffee_with_jordan:
    scene bg cafe
    
    # Check relationship + beliefs + flags
    python:
        jordan_trust = game.relationships.get("jordan", 0)
        has_opened_up = "shared_truth_jordan" in game.story_flags
        is_hopeful = game.emotions["hope"] > 60
    
    if jordan_trust > 50 and has_opened_up:
        jordan "You seem different lately. In a good way."
        
        menu:
            "I've been doing a lot of introspection":
                $ game.story_flags.add("jordan_knows_growth")
                jordan "That takes real courage. I'm proud of you."
            
            "Just trying to figure things out":
                jordan "Well, you're doing great."
    
    elif is_hopeful:
        jordan "You seem lighter today!"
        mc "I guess I am feeling pretty good."
    
    else:
        jordan "Everything okay? You seem tense."
        # ... different path for low emotional state

# ============================================
# CHAPTER COMPLETION
# ============================================

label chapter1_complete:
    scene bg black
    with slowdissolve
    
    narrator "Chapter 1 Complete"
    
    pause 1.0
    
    narrator "You've begun to see how beliefs shape experience."
    
    # Show stats
    python:
        resolved_count = len([b for b, i in game.beliefs.items() 
                            if i == BeliefIntensity.RESOLVED])
    
    narrator "Beliefs transformed: [resolved_count]"
    narrator "Introspection depth: [game.introspection_depth]"
    
    pause 2.0
    
    narrator "This is how it works in every moment."
    narrator "You always have a choice."
    
    pause 1.0
    
    narrator "Thank you for playing."
    
    return