# ============================================================================
# CONSEQUENCE SYSTEM - Evil Path Memory Wipe & Character Removal
# When player goes full evil with an NPC, brain "reboots" and they're gone
# ============================================================================

# Track which NPCs have been "lost" across loops
default lost_characters = []  # List of character IDs who are gone
default loop_count = 0  # How many times has brain rebooted
default evil_memories = {}  # Vague impressions that bleed through

# Persistent data (survives "brain reboot")
init python:
    import os
    
    # This data persists even through the reboot
    if persistent.lost_npcs is None:
        persistent.lost_npcs = []
    if persistent.total_loops is None:
        persistent.total_loops = 0
    if persistent.worst_actions is None:
        persistent.worst_actions = {}  # What you did to each person

# ============================================================================
# EVIL PATH THRESHOLD DETECTION
# ============================================================================

init python:
    def check_evil_threshold(npc_id):
        """
        Check if player has crossed the point of no return with this NPC
        Returns: (crossed_threshold, consequence_type, trigger_event)
        """
        
        npc = get_npc(npc_id)
        rel = npc.get_relationship_with("player")
        
        # Different thresholds for different characters
        
        if npc_id == "jill":
            # Threshold: Had sex with her 3+ times knowing she can't say no
            sexual_encounters = rel.get("sexual_encounters", 0)
            authenticity = rel.get("authenticity", 0)
            
            if sexual_encounters >= 3 and authenticity <= 10:
                return (True, "complete_dissociation", "jill_breaks")
        
        elif npc_id == "becky":
            # Threshold: Seduced her while Marcus's father was dying
            if rel.get("seduced_during_crisis", False):
                suicide_ideation = npc.beliefs.get("self.deserves-to-die", 0)
                if suicide_ideation >= BELIEF_INTENSITY_CORE:
                    return (True, "suicide_attempt", "becky_overdose")
        
        elif npc_id == "sarah" or npc_id == "mark":
            # Other characters have different thresholds
            boundary_violations = rel.get("boundary_violations", 0)
            trust = rel["trust"]
            
            if boundary_violations >= 5 and trust <= 10:
                return (True, "complete_breakdown", f"{npc_id}_leaves")
        
        return (False, None, None)

# ============================================================================
# THE REBOOT SEQUENCE
# ============================================================================

label trigger_brain_reboot(npc_id, consequence_type, final_event):
    # The player's brain can't handle what they did
    # Reality fragments, then resets
    # But the person is gone
    
    # Show the final consequence
    call expression final_event
    
    # The breaking point
    scene black with fade
    
    "Your vision fractures."
    
    "Pieces of consciousness scattering like dropped glass."
    
    python:
        npc = get_npc(npc_id)
        npc_name = npc.name
    
    if consequence_type == "suicide_attempt":
        "The note. Her handwriting. Your name."
        
        "Pills. Razor. Blood."
        
        "The way her mother screamed when she found out."
        
        "All because you—"
    
    elif consequence_type == "complete_dissociation":
        "Empty eyes. She's there but not there."
        
        "Just like her uncle taught her."
        
        "You did the same thing he did."
        
        "You became—"
    
    elif consequence_type == "complete_breakdown":
        "They're not coming back to therapy."
        
        "Dr. Chen's face when she realized what you'd done."
        
        "The way [npc_name] looked at you with such profound betrayal—"
    
    # Reality breaks
    scene white with Dissolve(0.1)
    play sound "static.ogg"
    
    "{color=#ff0000}ERROR{/color}"
    
    "{color=#ff0000}COGNITIVE DISSONANCE THRESHOLD EXCEEDED{/color}"
    
    "{color=#ff0000}BELIEF SYSTEM COLLAPSE{/color}"
    
    "{color=#ff0000}INITIATING PROTECTIVE SHUTDOWN{/color}"
    
    scene black with flash
    
    python:
        # Mark this character as lost
        persistent.lost_npcs.append(npc_id)
        persistent.total_loops += 1
        persistent.worst_actions[npc_id] = consequence_type
        
        # Store vague memory that will bleed through
        evil_memories[npc_id] = {
            "feeling": "guilt_and_denial",
            "fragments": [
                "Their face",
                "What you did",
                "The moment it went too far"
            ]
        }
    
    # Silence
    pause 3.0
    
    # Reboot
    scene hospital_room with Dissolve(2.0)
    
    "..."
    
    "Beeping."
    
    "Voices."
    
    "Where...?"
    
    # Back to the beginning, but different
    jump reboot_awakening

# ============================================================================
# THE REBOOT AWAKENING - Chapter 1 Redux
# ============================================================================

label reboot_awakening:
    # Same as normal awakening, but subtly wrong
    # You've been here before (but can't quite remember)
    # Someone is missing
    
    scene hospital_room with fade
    
    # Check who's missing
    python:
        missing = persistent.lost_npcs
        loop_number = persistent.total_loops
    
    # Déjà vu text styling
    if loop_number > 0:
        "{i}This has happened before.{/i}" (color="#888888", size=12)
        
        "{i}...hasn't it?{/i}" (color="#888888", size=12)
    
    show nurse at center with dissolve
    
    nurse "Oh! You're awake. Can you hear me?"
    
    # Subtle wrongness
    if loop_number == 1:
        "{i}Her voice sounds... familiar? No. That's impossible.{/i}"
    elif loop_number >= 2:
        "{i}Haven't we done this before? The beeping, the light, her voice...{/i}"
    
    nurse "You're in Sacred Heart Hospital. You've been in a coma for three weeks."
    
    # The player might ask about the missing person
    if loop_number > 0 and len(missing) > 0:
        menu:
            "The missing person... was there someone else here?"
            
            "Was there... someone else? Before?":
                show nurse confused
                
                nurse "Someone else? You just woke up. You haven't met anyone yet."
                
                "But there's a feeling. An absence."
                
                "Like a word you can't quite remember."
            
            "Never mind. Just... déjà vu.":
                "The feeling persists. Something is missing."
    
    # Continue normal awakening but with subtle changes
    jump chapter_01_post_reboot

# ============================================================================
# CHANGED INTERACTIONS - NPCs Remember (Unconsciously)
# ============================================================================

label meet_jill_post_reboot:
    # Meeting Jill again after a loop
    # She doesn't consciously remember, but something feels off
    
    python:
        loop_number = persistent.total_loops
        jill_was_lost = "jill" in persistent.lost_npcs
    
    if jill_was_lost:
        # She's not here. She's gone.
        # Maybe someone mentions her
        
        "In the common room, you notice an empty chair."
        
        "No one sits there."
        
        python:
            random_npc = "mark"  # Or whoever
        
        "[random_npc]" "Used to be someone in that chair. Jill, I think?"
        
        "[random_npc]" "Left the program. Couldn't handle it, I guess."
        
        "Something twists in your chest. A feeling you can't name."
        
        "Like you should know that name. Like you should feel... guilty?"
        
        "But you don't remember why."
        
    elif loop_number > 0:
        # She's here, but you've met before (in previous loop)
        
        show jill_confident at center with dissolve
        
        jill "Hey there. New blood, huh? I'm Jill."
        
        # The same approach. The same dance.
        # But something in her eyes...
        
        jill "You know, this place gets pretty boring. Maybe we could... keep each other company?"
        
        "{i}This exact moment. These exact words.{/i}"
        
        "{i}You've heard this before.{/i}"
        
        # If you exploited her last time, something in her recoils
        if persistent.worst_actions.get("jill") == "complete_dissociation":
            
            "For a fraction of a second, she flinches."
            
            "Like she saw something in your eyes. Something familiar."
            
            "Something {i}dangerous{/i}."
            
            show jill_uncertain
            
            jill "Actually, you know what? I just remembered I have... thing. Maybe later."
            
            "She leaves quickly."
            
            "{i}She doesn't know why she's scared of you.{/i}"
            
            "{i}But some part of her remembers.{/i}"
    
    return

# ============================================================================
# DR. CHEN KNOWS SOMETHING IS WRONG
# ============================================================================

label dr_chen_loop_awareness:
    # Dr. Chen is the only one who seems to notice the pattern
    # She's done the most work on herself - she's the most aware
    
    python:
        loop_number = persistent.total_loops
    
    if loop_number >= 2:
        
        scene therapy_room with fade
        show dr_chen_concerned at left with dissolve
        
        dr_chen "I want to try something different today."
        
        "She's looking at you strangely."
        
        dr_chen "Have you ever felt like... like you've lived through something before?"
        
        menu:
            "What do you say?"
            
            "Sometimes. Why?":
                dr_chen "There's a pattern. I can't quite explain it."
                
                "She flips through her notes."
                
                dr_chen "It's like... like parts of your file don't match your behavior."
                
                dr_chen "Or maybe it's just me. Projection. Trauma does strange things to memory."
                
                "But she doesn't look convinced."
            
            "No. Should I?":
                dr_chen "Maybe not."
                
                "But her eyes linger on you."
                
                "{i}She knows something is wrong. She just can't prove it.{/i}"
    
    return

# ============================================================================
# THE EMPTY CHAIRS
# ============================================================================

label group_therapy_with_absences:
    # Group therapy, but some chairs are empty
    # Each empty chair is someone you destroyed in a previous loop
    
    scene therapy_room with fade
    
    python:
        missing = persistent.lost_npcs
        present_npcs = [npc_id for npc_id in ["jill", "becky", "mark", "sarah"] 
                       if npc_id not in missing]
    
    "The circle feels smaller today."
    
    if len(missing) == 1:
        "One chair sits empty."
    elif len(missing) > 1:
        "[len(missing)] chairs sit empty."
    
    "No one mentions it."
    
    "But you can feel the absence like a missing tooth."
    
    # Show only present NPCs
    for npc_id in present_npcs:
        $ renpy.show(f"{npc_id}_neutral", at_list=[Transform(xpos=0.2 + present_npcs.index(npc_id) * 0.2)])
    
    show dr_chen_neutral at left
    
    dr_chen "Let's begin."
    
    # If 2+ people are missing, Dr. Chen comments
    if len(missing) >= 2:
        dr_chen "We're a smaller group than when we started."
        
        "Everyone shifts uncomfortably."
        
        dr_chen "That's okay. Not everyone can do this work. Some people... aren't ready."
        
        "She looks at you."
        
        dr_chen "But the rest of us are still here. Still trying."
        
        "{i}Why does it feel like she's talking specifically to you?{/i}"
    
    return

# ============================================================================
# ENDING: REDEMPTION ONLY POSSIBLE WITH EVERYONE PRESENT
# ============================================================================

label check_redemption_possible:
    # You can only achieve true redemption if you didn't lose anyone
    # If people are missing, you can only achieve "incomplete healing"
    
    python:
        missing = persistent.lost_npcs
        everyone_survived = len(missing) == 0
    
    if everyone_survived:
        # Perfect path possible
        jump path_to_redemption
    
    else:
        # Bittersweet ending
        jump incomplete_healing_ending

label incomplete_healing_ending:
    
    scene therapy_room with fade
    
    python:
        missing = persistent.lost_npcs
        missing_names = [get_npc(npc_id).name for npc_id in missing if npc_id in npc_states]
    
    "You've come so far."
    
    "You've changed. Genuinely changed."
    
    "But there are ghosts in the empty chairs."
    
    if len(missing) == 1:
        "One person you couldn't save."
        
        "One person whose absence will always remind you:"
        
        "{i}Change came too late for them.{/i}"
    
    else:
        "People you couldn't save."
        
        "Their absence is permanent."
        
        "{i}You can't undo the past. You can only prevent the future.{/i}"
    
    show dr_chen_sad at center
    
    dr_chen "You've done good work, [player_name]."
    
    dr_chen "But some wounds... we can't heal. Some people... we can't bring back."
    
    "She's right."
    
    "You're better. But you're not redeemed."
    
    "{i}Redemption requires that no one gets hurt.{/i}"
    
    "{i}And someone did.{/i}"
    
    scene black with fade
    
    centered "{size=+10}INCOMPLETE HEALING{/size}\n\nYou changed. But not soon enough.\n\n[len(missing)] person(s) lost along the way."
    
    return

# ============================================================================
# HELPER: Check if we're in a loop
# ============================================================================

init python:
    def is_repeat_loop():
        """Are we in a repeat loop (brain rebooted at least once)?"""
        return persistent.total_loops > 0
    
    def get_missing_characters():
        """Get list of NPCs who are gone"""
        return persistent.lost_npcs
    
    def character_is_missing(npc_id):
        """Check if specific character was lost"""
        return npc_id in persistent.lost_npcs
