# ============================================================================
# THERAPY SESSIONS - Day-by-day with Groundhog Day Model
# Provides structured therapy experience with Dr. Chen
# ============================================================================

# Therapy session tracking
default THERAPY_DAY_COUNT = 1
default THERAPY_MILESTONE_PROGRESS = 3  # Days until milestone achieved
default THERAPY_SESSION_IN_PROGRESS = False

# ============================================================================
# THERAPY DAY START
# Groundhog day model: replay until milestone achieved
# ============================================================================

label start_therapy_day:
    # Groundhog day model: replay until milestone achieved
    $ day = THERAPY_DAY_COUNT
    "Day [day]: Session with Dr. Chen"
    
    # Check milestone progress
    $ milestone_progress = count_resolved_beliefs()
    
    if milestone_progress >= THERAPY_MILESTONE_PROGRESS:
        jump therapy_milestone_reached
    
    # Standard session flow
    call dr_chen_greeting
    call offer_encounter(game_state)
    call dr_chen_reflection
    call check_day_completion
    
    return

label dr_chen_greeting:
    scene dr_chen_office
    show dr_chen
    
    if THERAPY_DAY_COUNT == 1:
        dr_chen "Welcome to our therapy sessions. We'll work together to understand your inner world."
        dr_chen "This is a space where we can explore what's happening internally - your beliefs, your emotions, the stories you tell yourself."
    else:
        $ days_since_start = THERAPY_DAY_COUNT
        dr_chen "Good to see you again. We've had [days_since_start] sessions now."
        dr_chen "Let's continue the work."
    
    return

label dr_chen_reflection:
    # INTRO-05: Dr. Chen provides reflection after choices
    dr_chen "Let me share what I observe..."
    
    $ dominant_emotion = game_state.get_dominant_emotion()
    "Dr. Chen notes your current dominant emotion: [dominant_emotion]"
    
    $ recent_beliefs = game_state.get_active_negative_beliefs()
    if recent_beliefs:
        "Active negative beliefs: [', '.join([beliefs[b]['statement'] if b in beliefs else b for b in recent_beliefs[:3]])]"
    
    if game_state.should_trigger_introspection():
        dr_chen "I think it's time we explore what's happening internally."
        call offer_introspection(game_state)
    
    return

label check_day_completion:
    # Check if player achieved daily goal
    $ day_goal_met = check_daily_goal()
    
    if not day_goal_met:
        # Groundhog day - repeat
        "You haven't made meaningful progress today. The day will repeat..."
        $ THERAPY_DAY_COUNT += 1
        jump start_therapy_day
    
    # Progress made - advance day
    $ THERAPY_DAY_COUNT += 1
    "Good progress today. Let's continue tomorrow."
    return

label therapy_milestone_reached:
    # Major milestone achieved
    scene positive_transformation
    show dr_chen
    dr_chen "You've made significant progress. This marks an important transition."
    "Achievement unlocked: Core Beliefs Transformed"
    
    # Reset for future therapy cycles if needed
    $ THERAPY_DAY_COUNT = 1
    return

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

init python:
    def count_resolved_beliefs():
        """Count beliefs in RESOLVED state"""
        return sum(1 for b, i in game_state.beliefs.items() if i == BELIEF_INTENSITY_RESOLVED)
    
    def check_daily_goal():
        """Check if daily therapeutic goal was achieved"""
        # Goal: at least one positive interpretation OR one belief resolved
        # Or: no consecutive negatives (breaking the negative pattern)
        return (game_state.consecutive_negatives == 0 or 
                count_resolved_beliefs() > 0 or
                game_state.interpretation_streak['positive'] > 0)

# ============================================================================
# THERAPY SESSION INTEGRATION
# Connect to encounter system
# ============================================================================

label offer_encounter(game_state):
    # Offer player an encounter from the vault
    # This integrates with the encounter system from 02-01
    python:
        # Check if encounters are available
        if hasattr(game_state, 'encounter_queue') and game_state.encounter_queue:
            encounter_available = True
        else:
            encounter_available = False
    
    if encounter_available:
        dr_chen "Would you like to explore an encounter? This can help us understand how your beliefs affect your interactions."
        
        menu:
            "Yes, let's do an encounter":
                call run_therapy_encounter
            
            "Let's focus on reflection instead":
                dr_chen "Reflection is valuable. Let's explore what's happening internally."
                call dr_chen_reflection
    else:
        dr_chen "Let's focus on your internal state today. How are you feeling?"
        call dr_chen_reflection
    
    return

label run_therapy_encounter:
    # Run an encounter from the queue
    # This would integrate with the encounter router
    "The encounter system will guide you through a scenario..."
    # Placeholder - actual implementation in encounter_router
    return
