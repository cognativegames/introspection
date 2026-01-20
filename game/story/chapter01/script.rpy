# Introspection - Chapter 1: Awakening
# Initial hospital sequence with reality-shifting mechanic

# Define character
define nurse = Character("???", color="#c8ffc8")
define mc = Character("[player_name]", color="#c8c8ff")
define therapist = Character("Dr. Sarah Chen", color="#ffc8c8")

# Initial game state - will expand as belief system is built
default player_state = {
    "awareness_level": 0,  # 0-10, tracks how much player understands the shifts
    "panic_level": 5,      # 0-10, affects dialogue options
    "core_beliefs": {},    # Populated during therapy
    "name_chosen": False,
    "evil_acts": [],       # Track harmful actions for redemption arcs
    "redemption_moments": []  # Track when player shows genuine change
}

default reality_stability = 0  # 0-10, increases as player gains awareness

# Track which dramatic shifts have occurred
default shifts_seen = {
    "giraffe": False,
    "jungle": False,
    "underwater": False,
    "void": False
}

# NPC forgiveness and healing system
# Each character has capacity to forgive based on their trauma work and belief system
default npc_states = {
    # Example structure for each NPC
    # "character_name": {
    #     "trust": 0-10,
    #     "trauma_healing": 0-10,  # How much they've healed their own wounds
    #     "betrayal_count": 0,     # How many times player has hurt them
    #     "forgiveness_capacity": 0-10,  # Based on their beliefs about redemption
    #     "can_forgive": True/False,
    #     "forgiveness_timer": 0,  # In-game days before they can process and forgive
    #     "boundaries_established": True/False,  # Have they learned to set boundaries?
    #     "witnessed_change": 0-10,  # How much genuine change have they seen in player?
    # }
}

# Forgiveness arc tracking
# This is the redemption path for evil-aligned players
default forgiveness_arcs = {
    "enabled": True,  # Can evil players find redemption?
    "requirements": {
        "self_awareness": 6,  # Player must reach this awareness level
        "genuine_remorse_shown": 0,  # Count of real apology moments
        "consistent_good_acts": 0,  # Must show sustained change, not just one-off
        "time_passed": 0,  # Some wounds need time, not just words
    },
    "mature_character_wisdom": {
        # Older/wiser characters can model forgiveness for the player
        # Teaching them that forgiveness isn't about condoning harm
        # It's about releasing the poison of hatred
        "teaches_self_forgiveness": True,
        "explains_cycle_of_hurt": True,  # Hurt people hurt people
        "models_boundary_setting": True,  # Forgiveness ≠ allowing more harm
        "offers_path_forward": True,  # Shows them who they could be
    }
}

# Reality shift severity system
# Triggered when player deviates from core beliefs
default shift_severity = {
    "catastrophic": {  # 0-2 reality_stability, major evil acts
        "visual": "complete_breakdown",  # Everything changes, impossible geometry
        "physical": "severe_headpain",    # Character clutches head, vision darkens
        "duration": 5.0,                  # Seconds before player can continue
        "message": "Your skull feels like it's splitting apart. Reality tears at the seams."
    },
    "severe": {  # 3-4 reality_stability, significant evil acts
        "visual": "major_distortion",     # Rooms change, people morph
        "physical": "sharp_headpain",     # Quick painful jolt
        "duration": 3.0,
        "message": "A spike of pain lances through your head. The world lurches sideways."
    },
    "moderate": {  # 5-6 reality_stability, minor evil acts or good acts against evil beliefs
        "visual": "reality_flicker",      # Things shimmer, details swap
        "physical": "dull_throb",         # Uncomfortable but manageable
        "duration": 1.5,
        "message": "Your head throbs. Something feels wrong."
    },
    "minor": {  # 7-8 reality_stability, small deviations
        "visual": "subtle_shift",         # Just details change
        "physical": "brief_discomfort",   # Momentary twinge
        "duration": 0.5,
        "message": "A brief flutter of discomfort."
    },
    "harmony": {  # 9-10 reality_stability, acting in perfect alignment
        "visual": "stable_clarity",       # World is clear, consistent
        "physical": "no_pain",           # Feels good, natural
        "duration": 0,
        "message": "Everything feels... right."
    }
}

label start:
    
    # Black screen, sound of heartbeat monitor
    play sound "heartbeat.mp3" fadein 2.0
    
    scene black with fade
    
    "Beep... Beep... Beep..."
    
    "Voices. Muffled. Like I'm underwater."
    
    "My head... something's wrong with my head."
    
    # Fade in to hospital room - first render
    scene hospital_room_1 with dissolve
    show nurse_normal at center with dissolve
    
    nurse "Oh! You're awake. Can you hear me?"
    
    # First choice - establishes player's initial panic response
    menu:
        "Where... where am I?":
            $ player_state["panic_level"] = 6
            mc "Where... where am I?"
            
        "What happened to me?":
            $ player_state["panic_level"] = 5
            mc "What happened to me?"
            
        "[Say nothing, just stare]":
            $ player_state["panic_level"] = 7
            "I try to speak but nothing comes out. My throat is dry, my thoughts scattered like puzzle pieces on a floor."
    
    nurse "You're in Sacred Heart Hospital. You've been in a coma. Try to stay calm, okay? I'm going to get the doctor—"
    
    # FIRST DRAMATIC SHIFT - Screen blinks
    play sound "reality_glitch.mp3"
    scene white with flash
    pause 0.3
    
    # Everything changes dramatically
    scene jungle_hospital with flash
    show nurse_giraffe at center with dissolve
    
    $ shifts_seen["giraffe"] = True
    $ shifts_seen["jungle"] = True
    
    mc "What the—"
    
    "The walls are gone. Vines crawl up where medical equipment should be. The fluorescent lights have become shafts of golden sunlight breaking through a canopy of leaves."
    
    "And the nurse..."
    
    mc "You're... you're a giraffe."
    
    nurse "What? Sweetie, you need to calm down. The injury—"
    
    # Her neck is impossibly long, spotted fur, but she's still wearing scrubs, still holding a clipboard with her hooved hands
    
    mc "This isn't real. This can't be real."
    
    menu:
        "Am I dead?":
            $ player_state["panic_level"] = 9
            mc "Am I dead? Is this... is this what death is?"
            
            nurse "No, no honey. You're very much alive. What you're experiencing is a side effect of your injury."
            
        "I'm dreaming. I have to be dreaming.":
            $ player_state["panic_level"] = 7
            mc "I'm dreaming. I have to be dreaming."
            
            nurse "Not a dream. This is real. But what you're *seeing* might not match what's actually here."
            
        "[Close your eyes tight, try to reset]":
            $ player_state["panic_level"] = 6
            $ player_state["awareness_level"] = 1
            
            "I squeeze my eyes shut. Count to three. This is just my brain misfiring. Just neurons firing wrong. Just—"
            
            nurse "That's good. That's a good instinct actually. Breathe. Let's try this again."
    
    # SECOND SHIFT - Less dramatic but still wild
    play sound "reality_glitch.mp3"
    scene white with flash
    pause 0.2
    
    scene underwater_hospital with flash
    show nurse_mermaid at center with dissolve
    
    $ shifts_seen["underwater"] = True
    
    "When I open my eyes, we're underwater. Bubbles drift lazily past the window. The nurse is there but her lower half is a shimmering fish tail, scales catching nonexistent light."
    
    nurse "Better?"
    
    mc "You're a mermaid now."
    
    nurse "I'm still Nurse Reyes. Your brain is trying to make sense of a lot of damage right now. The gunshot—"
    
    mc "Gunshot?"
    
    "The word hits like a physical thing. Gunshot. My hand goes to my head, finds bandages."
    
    nurse "You don't remember?"
    
    menu:
        "I don't remember anything.":
            $ player_state["panic_level"] = 8
            mc "I don't... I don't remember anything. How did I get shot?"
            
            nurse "We were hoping you could tell us. You were found three days ago. Do you remember your name?"
            
        "It's all blank.":
            $ player_state["panic_level"] = 7
            $ player_state["awareness_level"] = 1
            mc "It's all blank. Everything before waking up here is just... nothing."
            
            nurse "That's okay. That's actually normal with this type of trauma. Let's start simple. Do you know your name?"
            
        "Someone shot me?":
            $ player_state["panic_level"] = 9
            mc "Someone shot me? Who? Why?"
            
            nurse "We don't know yet. The police will want to talk to you when you're ready. But first... do you remember your name?"
    
    mc "My name..."
    
    "I reach for it. Surely I know my own name. But there's nothing. Just fog where memories should be."
    
    nurse "Close your eyes. Don't force it. What's the first name that comes to mind? Even if it doesn't feel right, just... what do you hear?"
    
    # THIRD SHIFT - while eyes are closed, reality tries to stabilize
    play sound "reality_glitch.mp3"
    scene black with dissolve
    
    "Darkness. Floating. A voice in the void, maybe mine, maybe not..."
    
    # NAME INPUT
    $ player_name = renpy.input("What name do you hear?", length=20)
    $ player_name = player_name.strip() or "Alex"
    $ player_state["name_chosen"] = True
    
    scene hospital_room_2 with dissolve
    show nurse_normal_variant at center with dissolve
    
    $ reality_stability = 1
    
    "When I open my eyes, she's human again. Mostly. The hospital room is back but... different. The chair in the corner is blue now. Wasn't it green? And there are flowers on the windowsill that definitely weren't there before."
    
    mc "[player_name]. That's... that's my name. Isn't it?"
    
    nurse "If that's what feels right to you, then yes. I'm Nurse Reyes. It's good to meet you, [player_name]."
    
    "She smiles. Her scrubs have buttons now. I could swear they didn't before. Or did they?"
    
    mc "Everything keeps changing."
    
    nurse "I know it does."
    
    "Her voice is gentle, like she's talking to a frightened child. Maybe she is."
    
    nurse "The gunshot caused significant trauma to your frontal lobe. The part of your brain that helps you process reality, maintain consistency in what you perceive... it's damaged."
    
    mc "So I'm just going to see crazy things forever?"
    
    nurse "No. Well, maybe not. The brain is incredible at healing itself, at finding new pathways. But right now, it's like your mind is trying to put together a puzzle with half the pieces missing. So it fills in the gaps with whatever it can find."
    
    # Player awareness moment
    if player_state["awareness_level"] > 0:
        mc "When I closed my eyes before... it helped, didn't it? Things were less... extreme when I opened them again."
        
        $ player_state["awareness_level"] = 2
        $ reality_stability = 2
        
        nurse "Yes! You noticed. That's very good. When you're aware of what's happening, when you center yourself, your brain has an easier time constructing something closer to reality."
        
        nurse "We're going to help you rebuild that ability. Dr. Chen—she's our neuropsychologist—will be working with you on that. She specializes in helping people like you."
        
    else:
        nurse "Dr. Chen will explain more. She's our neuropsychologist. She specializes in helping people whose perception of reality has been... compromised."
    
    mc "People like me."
    
    nurse "People who've been through trauma. Physical, psychological, or both."
    
    # SUBTLE SHIFT - nurse's hair is different length
    play sound "soft_glitch.mp3"
    show nurse_normal_variant_2 with dissolve
    
    "Her hair is shorter. Or longer? I can't tell anymore. The flowers are tulips. Were they roses a moment ago?"
    
    mc "It's happening again."
    
    nurse "I know. But it's smaller this time, right? Less intense than the jungle? The mermaid?"
    
    menu:
        "Yes. It's not as scary.":
            $ player_state["panic_level"] = 5
            $ player_state["awareness_level"] = 3
            $ reality_stability = 3
            
            mc "Yes. It's not as scary. I can... I can tell something's off but it's not overwhelming."
            
            nurse "That's progress already. Your brain is learning."
            
        "I don't know what's real anymore.":
            $ player_state["panic_level"] = 8
            
            mc "I don't know what's real anymore. How do I know YOU'RE real? How do I know any of this isn't just my dying brain making up one last dream?"
            
            nurse "I understand that fear. I can't prove to you that I'm real. But I'm going to be here, consistently, every day. And over time, you'll start to recognize the patterns of what's real versus what's your mind filling in gaps."
            
        "[Touch your bandages, ground yourself in physical sensation]":
            $ player_state["awareness_level"] = 4
            $ player_state["panic_level"] = 4
            $ reality_stability = 4
            
            "I press my fingers against the bandages. They hurt. Real, sharp, physical pain. An anchor."
            
            mc "Pain is real. I can feel pain."
            
            nurse "Yes. Sensation, especially discomfort, that's harder for your brain to falsify. Good instinct. Dr. Chen is going to teach you more techniques like that."
    
    nurse "I'm going to get her now. Try to rest. And [player_name]?"
    
    mc "Yes?"
    
    nurse "You're going to be okay. This is frightening, I know. But we're going to help you put your mind back together."
    
    # She leaves
    hide nurse_normal_variant_2 with dissolve
    
    # Alone moment - introspection
    "Alone. The heart monitor beeps steadily. Real? Probably. The window shows a grey sky. Real? Maybe."
    
    "Gunshot to the head."
    
    "I don't remember who I was before this. Don't remember who shot me or why."
    
    "Don't even know if [player_name] is really my name or just the first sound my broken brain could grasp."
    
    # VERY SUBTLE SHIFT - just lighting changes
    play sound "soft_glitch.mp3"
    scene hospital_room_2_evening with dissolve
    
    "The light has changed. More golden now, evening sun through the window. Or was it always evening? Time feels slippery."
    
    # Establish the introspection mechanic intro
    "But there's something else. Underneath the fear, underneath the confusion... a thought. Faint but growing stronger:"
    
    "If my brain can create jungles and mermaids..."
    
    "If reality is this malleable, this responsive to my mind..."
    
    "What else might I be able to change?"
    
    # Door opens - therapist enters
    play sound "door_open.mp3"
    show therapist_normal at center with dissolve
    
    therapist "Hello, [player_name]. I'm Dr. Chen. How are you feeling?"
    
    # This leads into the therapy/belief system building sequence
    menu:
        "Terrified.":
            $ player_state["panic_level"] = 7
            mc "Terrified. Nothing makes sense. I don't know who I am."
            
        "Confused but... curious?":
            $ player_state["awareness_level"] = 5
            $ player_state["panic_level"] = 4
            mc "Confused. But also... I don't know. Curious? Is that strange?"
            
            therapist "Not strange at all. Curiosity in the face of fear is a sign of resilience."
            
        "I'm fine.":
            $ player_state["panic_level"] = 6
            # Suppressing - will track this as potential belief about showing vulnerability
            mc "I'm fine."
            
            therapist "It's okay to not be fine, you know. You've been through significant trauma."
    
    therapist "Nurse Reyes told me about the visual distortions you're experiencing. The shifts in reality."
    
    mc "Is it going to stop?"
    
    therapist "That depends. The physical healing will happen regardless—your brain will rewire, find new pathways. But *how* stable your perception becomes... that's largely up to you."
    
    mc "How is it up to me?"
    
    therapist "Because what you're experiencing isn't just brain damage, [player_name]. It's your mind trying to construct reality from incomplete information. And construction requires... beliefs."
    
    # SUBTLE SHIFT - her glasses appear/disappear
    show therapist_normal_variant with dissolve
    
    therapist "You see that? Just now, something shifted. You noticed it."
    
    mc "Your glasses..."
    
    therapist "What about them?"
    
    menu:
        "You weren't wearing them before.":
            mc "You weren't wearing them before. Were you?"
            
        "Did you always have those?":
            mc "Did you always have those?"
            
        "I don't know what's real.":
            mc "I don't know. I don't know what's real anymore."
    
    therapist "The truth? I've been wearing glasses this whole time. They're real. But your brain wasn't processing them until just now. You believed you saw my face clearly, so you did—your mind filled in the details."
    
    therapist "This is what I mean by beliefs constructing reality. Not in some mystical sense, but in a very literal, neurological way. Your beliefs about what *should* be there determine what you actually perceive."
    
    mc "So if I believed hard enough, I could make you turn into a giraffe again?"
    
    therapist "In your perception, yes. But that's not the goal. The goal is to align your beliefs with consensus reality—what's actually there—so you can function in the world."
    
    therapist "Over the next few days, we're going to work on identifying and building a belief system that serves you. One that helps you perceive clearly, respond healthily, and ultimately... heal."
    
    mc "And then I'll stop seeing things that aren't there?"
    
    therapist "The shifts will become subtler. Maybe they'll never fully stop—your brain has been changed permanently. But you'll learn to recognize them, to ground yourself, to choose what to focus on."
    
    # Sets up the therapy sessions where belief system is built
    therapist "We'll start tomorrow. For now, rest. And [player_name]?"
    
    mc "Yes?"
    
    therapist "The fact that you woke up, that you're asking questions, that you're still fighting to understand... that tells me something important about who you are."
    
    if player_state["awareness_level"] >= 3:
        therapist "You're someone who adapts. Someone who looks for patterns. Those are gifts, even now."
    
    # She leaves
    hide therapist_normal with dissolve
    
    # Final moment of chapter 1
    scene hospital_room_night with fade
    
    "Night falls. Or maybe it was always night. The room is dark except for the glow of monitors."
    
    "Somewhere in this broken mind is the truth of what happened. Who I was. Why someone put a bullet in my head."
    
    "Or why I put it there myself."
    
    "The thought comes unbidden, unwelcome. I push it away."
    
    "Tomorrow, Dr. Chen will help me build a framework for understanding reality."
    
    "Tonight, I close my eyes and hope that when I open them, the world will make just a little more sense."
    
    # FINAL SUBTLE SHIFT as they drift to sleep - peaceful version
    play sound "soft_glitch.mp3"
    scene hospital_room_dream with dissolve
    
    "The edges of the room soften. Stars appear beyond the window—impossible stars, constellations I don't recognize but somehow feel familiar."
    
    "Maybe it's not real."
    
    "But for now, it's beautiful."
    
    "And that's enough."
    
    scene black with fade
    
    # End Chapter 1
    
    return

# PLACEHOLDER FUNCTIONS FOR FUTURE IMPLEMENTATION

# Reality shift function - called when player acts against beliefs
label trigger_reality_shift(severity="moderate", reason=""):
    # Determine shift level based on reality_stability and severity
    python:
        if reality_stability <= 2:
            shift_level = "catastrophic"
        elif reality_stability <= 4:
            shift_level = "severe"
        elif reality_stability <= 6:
            shift_level = "moderate"
        elif reality_stability <= 8:
            shift_level = "minor"
        else:
            shift_level = "harmony"
        
        # Can override with severity parameter for specific dramatic moments
        if severity in shift_severity:
            shift_level = severity
        
        shift_data = shift_severity[shift_level]
    
    # Visual effect
    if shift_level == "catastrophic":
        play sound "reality_shatter.mp3"
        scene void_nightmare with flash
        pause 0.5
        scene geometric_impossible with dissolve
        show pain_overlay with dissolve
        
    elif shift_level == "severe":
        play sound "reality_glitch_harsh.mp3"
        scene white with flash
        pause 0.3
        # Room transforms dramatically
        
    elif shift_level == "moderate":
        play sound "reality_glitch.mp3"
        # Flicker effect, details change
        
    elif shift_level == "minor":
        play sound "soft_glitch.mp3"
        # Subtle visual shift only
    
    # Physical pain response
    if shift_data["physical"] == "severe_headpain":
        mc "AHHH!"
        "[shift_data['message']]"
        "You collapse to your knees, hands clutching your skull. Behind your eyes, something fundamental is breaking."
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "sharp_headpain":
        mc "Agh!"
        "[shift_data['message']]"
        "You stagger, vision swimming. The pain is sharp, accusatory."
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "dull_throb":
        "[shift_data['message']]"
        pause shift_data["duration"]
        
    elif shift_data["physical"] == "brief_discomfort":
        "[shift_data['message']]"
        pause shift_data["duration"]
    
    # Optional introspection prompt for severe shifts
    if shift_level in ["catastrophic", "severe"]:
        menu:
            "What's happening to me?"
            
            "Stop. Breathe. Think about what you just did.":
                $ player_state["awareness_level"] += 1
                call introspect(reason)
                
            "Push through the pain.":
                $ player_state["panic_level"] += 1
                "You grit your teeth and force yourself forward. The pain doesn't care about your determination."
                
            "I don't care. Keep going.":
                $ player_state["awareness_level"] -= 1
                $ reality_stability -= 1
                "You ignore the warning. Your brain screams at you. You don't listen."
    
    return

label introspect(reason=""):
    # Pause mechanic when player acts against beliefs
    # Show belief system, current emotion, allow player to process
    
    scene introspection_space with fade
    
    "You close your eyes. Center yourself. Try to understand what just happened."
    
    if reason != "":
        "You just [reason]."
    
    # Show relevant belief that was violated
    python:
        violated_belief = None
        # Logic to determine which belief was violated based on recent action
        # This will be populated during therapy sessions
    
    if violated_belief:
        "You believe: [violated_belief['statement']]"
        "But you just acted against that belief."
        
        menu:
            "Why did I do that?"
            
            "I was scared.":
                "Fear overrode your values. It happens. But now you know."
                $ player_state["awareness_level"] += 1
                
            "I wanted something more than I wanted to be that person.":
                "Desire. The ego's favorite tool. It promised you something, and you believed it."
                $ player_state["awareness_level"] += 1
                
            "Maybe that belief is wrong.":
                "Maybe. Beliefs can change. But changing them requires honest reflection, not reactive justification."
                
            "I don't know.":
                "That's honest. And honesty is the first step toward understanding."
                $ player_state["awareness_level"] += 1
    
    "The pain in your head begins to subside as you acknowledge what happened."
    
    menu:
        "What do you want to do?"
        
        "I want to apologize.":
            $ player_state["last_action"] = "attempt_apology"
            "You can try. Whether they accept it depends on their beliefs, not your regret."
            return
            
        "I want to do better.":
            $ player_state["awareness_level"] += 1
            $ reality_stability += 1
            "Wanting is the first step. Doing is the second."
            return
            
        "I want to keep doing what I'm doing.":
            $ player_state["awareness_level"] -= 1
            "Then the pain will continue. The world will become less stable. And eventually..."
            "Well. You'll find out."
            return
    
    return

# Belief system check - call before major choices
label check_belief_alignment(action_belief, action_description):
    # Check if action aligns with core beliefs
    python:
        alignment_score = 0
        is_aligned = False
        
        # Calculate alignment between action and core beliefs
        if action_belief in player_state["core_beliefs"]:
            core_belief_strength = player_state["core_beliefs"][action_belief]
            
            if core_belief_strength >= 7:  # Strong belief
                is_aligned = True
                alignment_score = 10
            elif core_belief_strength >= 4:  # Moderate belief
                is_aligned = True
                alignment_score = 5
            else:  # Weak belief or opposite
                is_aligned = False
                alignment_score = -5
        else:
            # Acting on belief not in core system
            alignment_score = 0
    
    if is_aligned:
        # Acting in alignment - positive feeling
        "As you [action_description], something clicks into place. This feels right. Natural."
        $ reality_stability = min(10, reality_stability + 1)
        
        if reality_stability >= 9:
            call trigger_reality_shift("harmony", action_description)
        
    else:
        # Acting against beliefs - negative feeling  
        "As you [action_description], something inside you recoils. This isn't who you are. Is it?"
        
        python:
            # Determine severity based on how opposed the action is
            if alignment_score <= -5:
                shift_severity_level = "severe"
            else:
                shift_severity_level = "moderate"
        
        call trigger_reality_shift(shift_severity_level, action_description)
    
    return

label therapy_session_1:
    # Build core beliefs through scenario questions
    # Populate player_state["core_beliefs"] dictionary
    
    scene therapy_room with fade
    show therapist_normal at center with dissolve
    
    therapist "Good morning, [player_name]. How did you sleep?"
    
    # Reality should be relatively stable by now (reality_stability ~3-4)
    # Only minor shifts during therapy
    
    therapist "Today we're going to do something that might seem strange, but I promise it has a purpose."
    
    therapist "I'm going to describe some scenarios to you. Hypothetical situations. And I want you to tell me how you'd respond. Not how you think you *should* respond—how you actually *would* respond."
    
    mc "What's this for?"
    
    therapist "You don't remember who you were before the injury. But your values, your beliefs about the world... those are still in there somewhere. We're going to help you find them, and then we're going to build a framework around them."
    
    therapist "A belief system that will help stabilize your perception and guide you as you heal."
    
    mc "Okay. I'm ready."
    
    therapist "Let's start with something simple."
    
    # SCENARIO 1: Honesty vs Kindness
    therapist "You're walking down the street and you see someone—a friend, let's say—coming toward you. They're wearing a new outfit and they're clearly excited about it."
    
    therapist "But... you think the outfit looks terrible. They ask you: 'What do you think? Do you like it?'"
    
    menu:
        "What do you do?"
        
        "Tell them the truth. They deserve honesty.":
            $ player_state["core_beliefs"]["values_honesty_over_feelings"] = 8
            $ player_state["core_beliefs"]["values_kindness_over_truth"] = 2
            
            therapist "Interesting. So honesty is more important to you than protecting someone's feelings?"
            
            mc "People can't grow if everyone lies to them. Even kind lies."
            
            therapist "That's a strong belief. We'll mark that down: You value truth over comfort."
            
        "Lie. Say it looks great. Why hurt their feelings?":
            $ player_state["core_beliefs"]["values_kindness_over_truth"] = 8
            $ player_state["core_beliefs"]["values_honesty_over_feelings"] = 2
            
            therapist "So preserving their happiness matters more than being truthful?"
            
            mc "Sometimes kindness is more important than honesty. They're excited. Why take that away from them?"
            
            therapist "Noted. You prioritize emotional wellbeing over strict truth."
            
        "Find something genuinely positive about it and focus on that.":
            $ player_state["core_beliefs"]["seeks_middle_ground"] = 7
            $ player_state["core_beliefs"]["values_honesty_over_feelings"] = 5
            $ player_state["core_beliefs"]["values_kindness_over_truth"] = 5
            
            therapist "Ah. A diplomatic approach. You look for the truth within kindness."
            
            mc "There's usually something good if you look for it. Focus on that."
            
            therapist "A balanced belief. I like it."
    
    # SCENARIO 2: Self-Sacrifice vs Self-Preservation
    therapist "Next scenario. You're in a sinking ship. There are lifeboats, but not enough for everyone."
    
    therapist "You have a spot secured, but you see a young mother with a child desperately looking for a way off. What do you do?"
    
    menu:
        "Give them your spot. Their lives matter more.":
            $ player_state["core_beliefs"]["self_sacrificing"] = 9
            $ player_state["core_beliefs"]["self_preserving"] = 1
            
            mc "I give them my spot. A child deserves to live. A mother deserves to see them grow up."
            
            therapist "Even if it means you die?"
            
            mc "Even then."
            
            therapist "Profound self-sacrifice. That's... that's a beautiful belief, [player_name]. But also a dangerous one."
            
        "Keep my spot. I want to live too.":
            $ player_state["core_beliefs"]["self_preserving"] = 8
            $ player_state["core_beliefs"]["self_sacrificing"] = 2
            
            mc "I keep my spot. I'm sorry for them, but I want to live."
            
            therapist "No judgment here. Self-preservation is a valid drive. It's honest."
            
            mc "Dying won't help them. It just means one more person dead."
            
            therapist "Pragmatic. I'll note that."
            
        "Try to find another solution. Maybe we can make room.":
            $ player_state["core_beliefs"]["problem_solver"] = 8
            $ player_state["core_beliefs"]["seeks_middle_ground"] = 6
            
            mc "I'd look for another way. Maybe someone smaller, the child, could share a spot. Maybe we're missing something."
            
            therapist "You resist binary choices. You believe there's always another option if you look hard enough."
            
            mc "Usually, yes."
            
            therapist "An optimistic belief. Let's hope reality agrees with you."
    
    # SCENARIO 3: Justice vs Mercy
    therapist "Third scenario. Someone has wronged you. Badly. They cost you something precious—a job, a relationship, an opportunity."
    
    therapist "Later, you discover they're in trouble. You're in a position to help them or to let them suffer the consequences of their own actions. What do you do?"
    
    menu:
        "Help them anyway. Everyone deserves a second chance.":
            $ player_state["core_beliefs"]["values_mercy"] = 9
            $ player_state["core_beliefs"]["values_justice"] = 3
            
            mc "I help them. What they did to me doesn't mean I should become cruel."
            
            therapist "Mercy over justice. Forgiveness over revenge."
            
            mc "We all make mistakes. We all hurt people. If no one ever helped anyone who'd wronged them, we'd all be alone."
            
            therapist "That's... actually quite profound."
            
        "Let them face the consequences. They made their choices.":
            $ player_state["core_beliefs"]["values_justice"] = 8
            $ player_state["core_beliefs"]["values_mercy"] = 2
            
            mc "I let them deal with it. I'm not cruel, but I'm not responsible for saving people from their own actions."
            
            therapist "Justice. Consequences. You believe in accountability."
            
            mc "If people never face consequences, they never change."
            
            therapist "A firm belief. Black and white."
            
        "It depends on whether they've shown remorse.":
            $ player_state["core_beliefs"]["values_mercy"] = 5
            $ player_state["core_beliefs"]["values_justice"] = 5
            $ player_state["core_beliefs"]["requires_accountability"] = 7
            
            mc "If they've acknowledged what they did, if they've tried to make it right... then yes. I'd help. But if they're just in trouble and expect me to fix it without ever taking responsibility? No."
            
            therapist "Conditional mercy. Earned forgiveness. You believe people have to meet you halfway."
            
            mc "Yes. Exactly that."
    
    # Continue with more scenarios...
    # Each one builds out the core_beliefs dictionary
    # These will be referenced throughout the game
    
    therapist "We're going to do a few more of these over the next couple of days. By the end, we'll have a clear picture of your belief system."
    
    therapist "And here's the important part, [player_name]: these beliefs? They're going to determine how you feel and how you act as you move through the world."
    
    therapist "When you act in alignment with your beliefs, you'll feel good. Centered. Reality will become more stable."
    
    # Small visual demonstration - world becomes clearer
    play sound "soft_harmonic.mp3"
    show therapist_normal_clear with dissolve
    scene therapy_room_clear with dissolve
    
    $ reality_stability += 1
    
    "The room sharpens. Dr. Chen's features are crisp, consistent. The walls are solid. Real."
    
    mc "It's clearer. Everything is clearer."
    
    therapist "Yes. Because you're building structure. Foundation. Your mind has something to anchor to."
    
    therapist "But [player_name]... when you act *against* your beliefs—when you betray your own values—you'll feel it. Immediately."
    
    therapist "The world will shift. You'll experience pain. Disorientation. It's your brain telling you: this doesn't align. This isn't who you are."
    
    mc "Like a built-in conscience."
    
    therapist "Exactly like that. And if you keep ignoring it, keep acting against who you believe you are..."
    
    # Visual demonstration - minor shift
    play sound "reality_glitch.mp3"
    show therapist_normal_blur with dissolve
    scene therapy_room_distorted with dissolve
    
    "The room wavers. Dr. Chen's face blurs at the edges."
    
    therapist "Reality becomes less stable. The pain gets worse. Eventually, you might not be able to tell what's real at all."
    
    # Stabilize again
    play sound "soft_harmonic.mp3"
    show therapist_normal_clear with dissolve
    scene therapy_room_clear with dissolve
    
    therapist "So the path forward is simple, if not easy: Know your beliefs. Act in alignment with them. And when you can't—when you slip, when you make mistakes—pause. Reflect. Introspect."
    
    therapist "That's where the title of our work together comes from. Introspection. Looking inward to understand outward."
    
    mc "And if I want to change a belief?"
    
    therapist "Then you examine it. Question it. Decide if it serves you. And if it doesn't, you consciously choose a new one. But that takes time. Awareness. Honesty."
    
    therapist "You can't just decide to believe something different and make it so. The belief has to integrate. Become part of your foundation."
    
    mc "This is a lot."
    
    therapist "It is. But you're already doing it. Every choice you made in our scenarios today—those weren't random. They came from somewhere deep inside you. We're just making the implicit explicit."
    
    therapist "Tomorrow, we'll continue. More scenarios, more refinement. And then..."
    
    therapist "We'll release you to the world. To see if you can maintain who you've decided to be."
    
    # End therapy session 1
    scene black with fade
    
    return

label assisted_living_intro:
    # Transition to main game area
    # Reality shifts should be minimal by this point (reality_stability >= 7)
    pass

# Forgiveness scene template - for mature characters teaching redemption
label forgiveness_scene(character_name, evil_act_committed):
    # This scene triggers when:
    # 1. Player has committed evil acts against this character
    # 2. Character has healed enough to forgive (trauma_healing >= 7)
    # 3. Player has shown genuine awareness and change
    # 4. Enough time has passed for processing
    
    python:
        char_state = npc_states[character_name]
        can_offer_forgiveness = (
            char_state["trauma_healing"] >= 7 and
            char_state["witnessed_change"] >= 5 and
            char_state["forgiveness_timer"] <= 0 and
            player_state["awareness_level"] >= 6
        )
    
    if not can_offer_forgiveness:
        return
    
    # Example with a mature character named Sarah
    # Adjust for your actual characters
    
    scene character_room_evening with fade
    show sarah_thoughtful at center with dissolve
    
    "Sarah asked you to meet her. There's something in her expression—not anger, not hurt. Something softer. Sadder, maybe."
    
    sarah "I've been thinking a lot about what happened between us."
    
    # Player may feel defensive - reality might flicker if they're not ready
    if player_state["awareness_level"] < 7:
        play sound "soft_glitch.mp3"
        "Your head twinges. Guilt? Fear? You're not sure."
    
    sarah "When you [evil_act_committed], it hurt. Deeply. I want you to know that. I'm not going to pretend it didn't happen or that it was okay."
    
    menu:
        "I know. I'm sorry.":
            $ player_state["redemption_moments"].append(f"apologized_to_{character_name}")
            $ forgiveness_arcs["requirements"]["genuine_remorse_shown"] += 1
            
            mc "I know. I'm sorry, Sarah. I was... I was wrong."
            
            sarah "Thank you for saying that. And I believe you mean it. I've watched you these past weeks. I've seen you trying."
            
        "I don't know what you want me to say.":
            $ player_state["awareness_level"] -= 1
            
            mc "I don't know what you want me to say. It happened. I can't change it."
            
            sarah "I'm not asking you to change the past. I'm trying to talk about the future."
            
        "[Say nothing]":
            "You stay quiet. Sometimes words feel inadequate."
            
            sarah "It's okay. You don't have to say anything right now."
    
    sarah "I spent a long time being angry at you. Replaying it over and over. Imagining all the things I wished I'd said or done differently."
    
    sarah "And you know what I realized?"
    
    mc "What?"
    
    sarah "That anger was poisoning me more than what you did. I was letting what happened define me. Control me. Keep me trapped."
    
    show sarah_gentle at center with dissolve
    
    sarah "So I've decided to forgive you."
    
    # This might shock the player - reality stabilizes briefly
    play sound "soft_harmonic.mp3"
    $ reality_stability = min(10, reality_stability + 1)
    
    mc "You... what?"
    
    sarah "I forgive you. Not because what you did was okay—it wasn't. Not because you've earned it or because enough time has passed. But because *I* need to let this go."
    
    sarah "Carrying hatred doesn't hurt you, [player_name]. It hurts *me*. And I'm tired of hurting."
    
    menu:
        "I don't deserve your forgiveness.":
            mc "I don't deserve your forgiveness. Not after what I did."
            
            sarah "Maybe not. But forgiveness isn't about what you deserve. It's about what I need to heal."
            
            sarah "And here's the thing I want you to understand: forgiving you doesn't mean I'm okay with what happened. It doesn't mean we go back to how things were."
            
        "Thank you.":
            mc "Thank you. I... I don't know what to say."
            
            sarah "You don't have to say anything. Just... try to be better. For yourself, not for me."
            
        "Why are you telling me this?":
            mc "Why are you telling me this?"
            
            sarah "Because I think you need to hear it. And because I think you're carrying something heavier than what you did to me."
    
    sarah "Can I ask you something?"
    
    mc "Sure."
    
    sarah "When you hurt me, when you used my trauma against me... where did that come from?"
    
    # Critical moment - player must confront their own pain
    menu:
        "I don't know. I just... did it.":
            sarah "I don't believe that. Nobody just does something like that for no reason."
            
        "I was hurt too. A long time ago.":
            $ player_state["awareness_level"] += 2
            $ player_state["redemption_moments"].append("acknowledged_own_trauma")
            
            mc "I was hurt too. A long time ago. By someone I trusted."
            
            sarah "And you've been carrying that ever since?"
            
            mc "I guess so. I didn't even realize until now."
            
            sarah "That's what hurt people do, [player_name]. We hurt others. We recreate our pain in different forms, with different faces."
            
        "Because I'm a monster.":
            $ player_state["awareness_level"] += 1
            
            mc "Because I'm a monster. That's what you want to hear, right?"
            
            sarah "No. That's what *you* believe. And that belief is making you act like one."
    
    show sarah_compassionate at center with dissolve
    
    sarah "Listen to me carefully, because this is important: You are not defined by the worst thing you've ever done."
    
    sarah "I know what it's like to hate yourself. To think you're broken beyond repair. I carried that for years after... after what happened to me."
    
    sarah "But healing taught me something: we get to choose who we are going forward. Not who we were. Not what was done to us. Not what we did in our pain."
    
    sarah "*Who we choose to be.*"
    
    # Visual effect - reality becomes very stable, clear
    play sound "soft_harmonic.mp3"
    scene character_room_clear with dissolve
    show sarah_clear at center with dissolve
    
    $ reality_stability = min(10, reality_stability + 2)
    
    "The room sharpens. Everything becomes crystalline, vivid. Sarah's eyes are kind. Tired, but kind."
    
    sarah "If I can forgive you, [player_name]... can you forgive whoever hurt you?"
    
    # THE CRITICAL QUESTION
    # This is where the player might break through their own pain
    menu:
        "I... I don't know if I can.":
            mc "I don't know if I can. What they did... it changed me."
            
            sarah "It did change you. But it doesn't have to control you. Not anymore."
            
            sarah "Forgiving them doesn't mean what they did was okay. It means you're not going to let it keep poisoning you."
            
        "Maybe. If you can forgive me... maybe I can try.":
            $ player_state["awareness_level"] += 3
            $ player_state["redemption_moments"].append("considered_forgiving_own_abuser")
            $ reality_stability = min(10, reality_stability + 2)
            
            mc "Maybe. If you can forgive me... maybe I can try."
            
            sarah "That's all any of us can do. Try. One day at a time. One choice at a time."
            
            play sound "soft_harmonic.mp3"
            "Something inside you shifts. Not reality this time. Something deeper. A knot you didn't know you were carrying begins to loosen."
            
        "I want to. I'm just so angry.":
            mc "I want to. I'm just... I'm so angry. All the time. And I don't know how to stop."
            
            sarah "Then start with forgiving yourself. For being angry. For being hurt. For not knowing how to process it."
            
            sarah "Anger is just pain that doesn't know where to go. Give it permission to exist, and then... let it start to heal."
    
    sarah "I'm not going to tell you we're okay, [player_name]. I'm not going to say we can be what we were before you hurt me."
    
    sarah "But I am going to tell you this: I see you trying. I see you becoming aware. And that matters."
    
    sarah "So here's what forgiveness looks like for me: I release you from the narrative that you're a monster. You're a person who did a monstrous thing. Those are different."
    
    sarah "And I set a boundary: if you hurt me again, I'm done. Forgiveness isn't a free pass to keep causing harm. It's a gift, not an invitation."
    
    sarah "Can you respect that?"
    
    menu:
        "Yes. I can. I will.":
            $ char_state["trust"] = 4  # Not full trust, but foundation for rebuilding
            $ char_state["boundaries_established"] = True
            $ player_state["redemption_moments"].append(f"accepted_boundaries_{character_name}")
            
            mc "Yes. I can. I will."
            
            sarah "Then we can try again. Slowly. Carefully. As different people than we were before."
            
        "I don't know if I can promise that.":
            $ char_state["boundaries_established"] = True
            
            mc "I don't know if I can promise that. I'm still... figuring myself out."
            
            sarah "That's honest. I appreciate that more than a promise you're not sure you can keep."
            
            sarah "The boundary stands either way. But thank you for not lying to me."
    
    sarah "One more thing."
    
    mc "Yes?"
    
    sarah "Whatever you decide to do with this—with my forgiveness, with your own pain, with who you want to become—make sure it's your choice. Not because you think you owe me. Not because you're trying to prove something."
    
    sarah "Choose to heal because *you* deserve to be free from this. Just like I deserved to be free from hating you."
    
    # End scene
    hide sarah_clear with dissolve
    scene black with fade
    
    "You sit with her words long after she's gone."
    
    "Forgiveness. Not for what you did. Not even really for you. But for her. For her own peace."
    
    "And somehow... that makes it more powerful. Not less."
    
    if len(player_state["redemption_moments"]) >= 3:
        "Maybe you're not a monster after all."
        "Maybe you're just someone who got hurt, and hurt others, and is learning—finally learning—how to stop the cycle."
        
        $ reality_stability = 10
        
        play sound "soft_harmonic.mp3"
        "The world feels solid. Real. Clear. For the first time since you woke up in that hospital."
        
        "Like you finally know where you are."
        "Like you finally know who you are."
        "Or at least... who you could choose to be."
    
    return