# ============================================================================
# MAIN SCRIPT
# Game entry point and flow control
# ============================================================================

label start:
    # Official entry point for the game.
    # RenPy automatically calls this label when the game starts.
    
    # Initialize core engine and dependencies
    python:
        if game_state is None:
            game_state = GameState()
    
        initialize_all_npcs();
    
    # Start with prologue
    jump prologue

# ============================================================================
# MAIN GAME FLOW
# ============================================================================

label main_game_flow:
    # Master flow controller - call this to resume after loading a save
    
    python:
        current_chapter = game_state.chapter
    
    if current_chapter == 1:
        jump chapter_01
    elif current_chapter == 2:
        jump chapter_02
    elif current_chapter == 3:
        jump chapter_03
    else:
        jump chapter_01

# ============================================================================
# THERAPY INTEGRATION
# Connect therapy sessions to main game flow
# ============================================================================

label transition_to_therapy:
    # Called when transitioning from story to therapy
    scene dr_chen_office
    show dr_chen
    
    dr_chen "Before we continue, let's process what just happened."
    
    # Trigger any needed introspection
    if game_state.should_trigger_introspection():
        call offer_introspection(game_state)
    
    # Offer encounter
    call offer_encounter(game_state)
    
    # Dr. Chen reflection
    call dr_chen_reflection
    
    # Determine if ready to continue story
    menu:
        "I'm ready to continue":
            return
        
        "I need more time here":
            jump start_therapy_day

label after_encounter_reflection:
    # Called after an encounter completes - offers Dr. Chen's reflection
    show dr_chen
    
    dr_chen "That was illuminating. Let me share what I observed..."
    
    $ dominant_emotion = game_state.get_dominant_emotion()
    "Your dominant emotion right now: [dominant_emotion]"
    
    if game_state.should_trigger_introspection():
        dr_chen "I think there's something important to explore here."
        call offer_introspection(game_state)
    
    return

# ============================================================================
# CHAPTER PLACEHOLDERS
# ============================================================================

label chapter_02:
    scene black
    centered "Chapter 2: Coming Soon"
    return

label chapter_03:
    scene black
    centered "Chapter 3: Coming Soon"
    return

# ============================================================================
# ENDING AND CREDITS
# ============================================================================

label game_end:
    # Called when game is complete
    
    python:
        # Determine ending based on choices
        # (ending logic would go here)
        ending = "redemption"
    
    if ending == "redemption":
        jump epilogue_redemption
    elif ending == "partial":
        jump epilogue_partial
    else:
        jump epilogue_failure

label epilogue_redemption:
    scene black
    centered "EPILOGUE: REDEMPTION\n\n(To be written)"
    jump credits

label epilogue_partial:
    scene black
    centered "EPILOGUE: PARTIAL HEALING\n\n(To be written)"
    jump credits

label epilogue_failure:
    scene black
    centered "EPILOGUE: CONSEQUENCES\n\n(To be written)"
    jump credits

label credits:
    scene black with fade
    centered "{size=+20}INTROSPECTION{/size}\n\nA game about belief, choice, and transformation\n\nCreated by [Your Name]\n\nBased on Bashar's teachings on belief systems"
    pause 3.0
    return
