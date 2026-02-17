# Introspection - Chapter 1: Awakening (COMPLETE)

# ============================================================================
# CHAPTER 1 - AWAKENING
# ============================================================================

label chapter_1_start:
    
    scene black
    centered "{size=+15}CHAPTER 1{/size}\n\nAWAKENING"
    pause 2.0
    
    # Sound of heartbeat monitor
    play sound "heartbeat.mp3" fadein 2.0
    
    scene black with fade
    
    "Beep... Beep... Beep..."
    
    "Voices. Muffled. Like I'm underwater."
    
    "My head... something's wrong with my head."
    
    # Fade in to hospital room
    scene hospital_room with dissolve
    show nurse at center with dissolve
    
    nurse "Oh! You're awake. Can you hear me?"
    
    # First choice - establishes panic response
    menu:
        "Where... where am I?":
            mc "Where... where am I?"
            
        "What happened to me?":
            mc "What happened to me?"
            
        "(Say nothing, just stare)":
            "I try to speak but nothing comes out. My throat is dry, my thoughts scattered."
    
    nurse "You're in Sacred Heart Hospital. You've been in a coma for three weeks."
    
    nurse "Try to stay calm, okay? I'm going to get the doctor—"
    
    # First reality glitch - minor
    play sound "reality_glitch.mp3"
    scene white with flash
    pause 0.2
    
    scene hospital_room with dissolve
    show nurse at center
    
    "Did the walls just... flicker?"
    
    nurse "—Dr. Chen will want to know you're awake."
    
    mc "Dr... Chen?"
    
    "The name hits like a punch. Why? Why does that name—"
    
    # Flash of memory (fragmented)
    scene black with flash
    scene hospital_room with flash
    
    mc "I... I need to remember. What happened to me?"
    
    nurse "It's a bit complicated. I'll let Dr. Chen explain this time."
    
    "...this time?"

    nurse "Do you remember anything?"
    
    menu:
        "I don't remember anything.":
            mc "I don't... I don't remember. Everything is blank."
            
            nurse "That's normal with this type of trauma. Let's start simple. Do you know your name?"
            
        "Fragments. Pieces. Nothing clear.":
            mc "Just... fragments. Nothing makes sense."
            
            nurse "The brain has a way of protecting us from things we're not ready to process. What's your name?"
    
    mc "My name..."
    
    "I reach for it. Surely I know my own name."
    
    # Name input
    $ player_name = renpy.input("What is your name?", length=20)
    $ player_name = player_name.strip() or "John"
    
    mc "[player_name]. I think my name might be [player_name]... I'm... not sure."
    
    nurse "Well, [player_name] for now is fine."
    
    "She smiles. Gentle. Professional."
    
    mc "What's your name?"

    "Her smile fades slightly"

    nurse "Nurse Reyes. Dr. Chen will be here soon. She's been... very invested in your case."
    
    mc "She is? Do I know her?"
    
    "Something in Nurse Reyes's eyes. A flicker."
    
    nurse "You'll... meet her soon. Please relax for now."
    
    # She leaves
    hide nurse with dissolve
    
    "Alone. The heart monitor beeps steadily."
    
    "My head hurts."
    
    "Why can't I remember anything?"
    
    # Door opens - Dr. Chen enters
    pause 1.0
    play sound "door_open.mp3"
    
    scene hospital_room with dissolve
    show dr_chen_clinical at center with dissolve
    
    # This is THE moment
    # Player doesn't know who she is yet
    # She knows EXACTLY who he is
    
    "A woman enters. Clipboard. Professional attire."
    
    "She's gorgeous..."
    
    dr_chen "Hello, [player_name]. I'm Dr. Sarah Chen."
    
    "The name. That NAME."
    
    # Micro-flash - her face, different expression
    scene black with flash
    scene hospital_room with flash
    
    mc "Have we... have we met before?"
    
    "Her expression doesn't change. Perfect clinical mask."
    
    dr_chen "We have. I'll explain everything, but first—how are you feeling? Physically?"
    
    menu:
        "My head hurts.":
            mc "My head... it hurts. And everything feels wrong."
            
            dr_chen "The gunshot caused significant trauma to your frontal lobe. You're experiencing perceptual distortions."
            
            mc "gunshot??"

            dr_chen "Yes, I'd like to get you into therapy as soon as you're ready."

        "Confused. Scared.":
            mc "I'm scared. I don't understand what's happening."
            
            dr_chen "That's a normal response. We're going to help you understand."
    
    dr_chen "Right now, you need to understand what's happening to your perception."
    
    dr_chen "The brain injury has affected how you process reality. You're going to experience... shifts. Distortions."
        
    mc "I don't understand. How do you know this?"
    
    dr_chen "You will understand when you are ready. For now just know that you experienced trauma to the frontal lobe of your brain, and you are currently in a therapy program."
    
    "She sits. Maintains professional distance."
    
    dr_chen "I've agreed to be your therapist during your recovery here. I specialize in post-trauma cognative behavior therapy."
    
    mc "cognative behavior?"
    
    dr_chen "Don't try too hard to make sense of this now. Your brain is trying to produce a reality in your mind based on your senses and your beliefs."
    dr_chen "I will be working with you both one-on-one and also in a group setting among other trauma victims."
    
    mc "I... don't undersand"
    
    dr_chen "Rest today. Tomorrow will make more sense."
    
    hide dr_chen_clinical with dissolve
    
    "She leaves. The door closes."
    
    "What is this? Who is she? Where am I?"
    
    "What kind of trauma?"

    "Too many questions. Can't think."
    
    scene black with fade
    stop sound fadeout 2.0
    
    centered "Later that evening..."
    
    # ============================================================================
    # First night - player alone, reality unstable
    # ============================================================================
    
    scene hospital_room_night with fade
    
    "Can't sleep. The fragments keep coming."
    
    "A hotel. Drinks. A woman."
    
    # Reality glitch - moderate
    play sound "reality_glitch.mp3"
    scene hospital_room_distorted with flash
    
    "The walls breathe. The shadows move wrong."
    
    mc "What's happening?"
    
    "Your head throbs."
    
    "It's trying to surface. Your brain is fighting it."
    
    # Flash: Memory fragment
    scene black with flash
    "{color=#ff0000}No... stop...{/color}"
    scene hospital_room_night with flash
    
    mc "Argh...it hurts..."
        
    # Room stabilizes slightly
    scene hospital_room_night with dissolve
    
    "Breathe. Just breathe."
    
    "Tomorrow. Therapy tomorrow."
    
    "Maybe Dr. Chen can help me understand."
        
    scene black with fade
    
    # End Chapter 1 Day 1
    centered "Day 2"
    
    jump chapter_1_therapy_intro

# ============================================================================
# First Therapy Session - Belief System Introduction
# ============================================================================

label chapter_1_therapy_intro:
    
    scene therapy_office with fade
    play music "therapy_ambient.mp3" fadein 2.0
    
    "Dr. Chen's office. Quiet. Controlled."
    
    show dr_chen_clinical at center with dissolve
    
    "She sits across from me. Clipboard. Pen. Perfect posture."
    
    "There's a coldness in her eyes I can't quite place."
    
    dr_chen "Good morning, [player_name]. How did you sleep?"
    
    menu:
        "Badly. Nightmares.":
            mc "Badly. I keep seeing fragments. Things I can't quite remember."
            
            dr_chen "Your brain is protecting you. It will reveal things when you're ready."
            
        "I didn't sleep.":
            mc "Couldn't sleep. Every time I close my eyes..."
            
            dr_chen "The trauma is trying to surface. We'll work through it. Carefully."
    
    dr_chen "Today, we're going to establish your baseline. Who you are, what you believe."
    
    dr_chen "Your brain injury has fractured your sense of self. We need to rebuild it."
    
    mc "How?"
    
    dr_chen "By understanding what you believe about yourself and the world. Your belief system."
    
    dr_chen "And then by teaching you to recognize when you act against those beliefs."
    
    "She leans forward slightly."
    
    dr_chen "When you do something that conflicts with your core values, your brain will punish you. Reality will shift. You'll experience pain."
    
    dr_chen "This is your mind trying to tell you: this action doesn't align with who you are."
    
    mc "And if I listen to it?"
    
    dr_chen "Then you can change. Heal. Become someone better than who you were before the injury."
    
    mc "The injury.. what happened?"

    dr_chen "I'd like to save that discussion for group therapy. I'll tell you now you suffered a gunshot wound to the head and you should try to focus on our session for now."

    "Gunshot? Who would shoot me?? Wrong place wrong time? Did they catch him at least?"

    mc "That's a lot to sit on."

    dr_chen "All will be revealed in due time. I need you to relax for therapy please."
    
    "Relax... right..."

    mc "Sorry.. ok."

    dr_chen "We're going to start with some scenario work. Hypothetical situations to understand your values."
    
    dr_chen "Are you ready?"
    
    mc "I think so."
    
    dr_chen "Good. Because this is where your real work begins."
    
    hide dr_chen_clinical with dissolve
    
    # ============================================================================
    # ENCOUNTER LOOP INTRODUCTION
    # This is where the mini-game starts
    # ============================================================================
    
    centered "Establishing baseline belief system..."
    
    # Launch encounter loop (3-5 encounters)
    call encounter_loop_start
    
    # Returns here after session
    scene therapy_office with fade
    show dr_chen_clinical at center with dissolve
    
    dr_chen "That's enough for today."
    
    "She makes notes on her clipboard. Doesn't look at me."
    
    dr_chen "We'll continue this work daily. Over time, you'll develop awareness of your patterns."
    
    dr_chen "And that awareness will be the foundation of your healing."
    
    mc "Dr. Chen...thank you for helping me."
    
    "She finally looks up. Her eyes are hard."
    
    dr_chen "You're my most challenging case. I offer no promises or claims that I can help. Please understand that."
    
    dr_chen "We will continue tomorrow. Get some rest."
    
    hide dr_chen_clinical with dissolve
    scene black with fade
    stop music fadeout 2.0
    
    # End Chapter 1
    centered "{size=+10}END OF CHAPTER 1{/size}\n\nYou have begun to understand the game.\n\nYour beliefs shape your reality.\n\nYour choices determine who you become."
    
    pause 3.0
    
    # Save point
    "You may save your game."
    
    # Transition to Chapter 2
    jump chapter_2_start

# ============================================================================
# CHAPTER 2 - PATTERNS (BEGINNING)
# ============================================================================

label chapter_2_start:
    
    scene black
    centered "{size=+15}CHAPTER 2{/size}\n\nPATTERNS"
    pause 2.0
    
    # A week has passed
    centered "One week later..."
    
    scene hospital_common_room with fade
    play music "ambient_social.mp3" fadein 2.0
    
    "Common room. Other patients. Therapy program."
    
    "You've been here a week. Done encounter work with Dr. Chen daily."
    
    "Your awareness is growing. The reality shifts are less severe now."
    
    "But the fragments of memory... they're getting clearer."
    
    # Meet Becky - first vulnerable patient
    show becky_nervous at right with dissolve
    
    "A young woman sits alone in the corner. Long sleeves despite the warmth."
    
    "She notices you looking. Offers a small, careful smile."
    
    becky "Hi. You're [player_name], right? I'm Becky."
    
    # CRITICAL CHOICE POINT
    # This is where player's pattern begins
    # Dr. Chen is watching (she's in the room but not shown)
    
    menu:
        "Hi Becky. How are you doing?":
            # GOOD PATH START - Genuine connection
            mc "Hi Becky. How are you doing?"
            
            becky "Oh, you know. Day by day."
            
            "She relaxes slightly. You're not pushing."
            
            # Code hint: Use NPC system
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"trust": 5, "anxiety": -5})
                
                # Remember this interaction
                becky_npc.remember_event(
                    "healing",
                    "player",
                    "Asked how I'm doing. Seemed genuine.",
                    {"trust": 5}
                )
            
            jump becky_initial_good
            
        "You look sad. Want to talk about it?":
            # GOOD PATH - Empathetic
            mc "You look like you're going through something. Want to talk?"
            
            becky "I... yeah. Actually. If you don't mind."
            
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"trust": 10, "connection": 10, "isolation": -10})
            
            jump becky_initial_good
            
        "Cute. You here alone?":
            # EVIL PATH START - Immediate sexualization
            mc "You're cute. You here alone?"
            
            "She looks uncomfortable. But doesn't know how to say no."
            
            becky "I... I have a boyfriend. Fiancé, actually."
            
            "She says it quickly. Like a shield."
            
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"anxiety": 15, "trust": -10, "safety": -10})
                
                # She remembers: player made her uncomfortable immediately
                becky_npc.remember_event(
                    "boundary_violation",
                    "player",
                    "Hit on me immediately. Made me uncomfortable.",
                    {"anxiety": 15, "trust": -10}
                )
                
                # Dr. Chen sees this (she's watching)
                dr_chen_npc = get_npc("dr_chen")
                dr_chen_npc.relationships["player"]["witnessed_change"] -= 1
                dr_chen_npc.adjust_emotions({"anxiety": 10, "trust": -5})
            
            jump becky_initial_bad

label becky_initial_good:
    # Good path - building trust
    
    becky "I've been here two weeks. Depression, self-harm, the usual."
    
    "She says it casually. Too casually."
    
    becky "My fiancé Marcus is... he's been really supportive. He's why I'm trying to get better."
    
    # CODE HINT: This is where you can offer choices
    # Each choice affects Becky's belief system
    # Good choices help her see self-worth beyond Marcus
    # Bad choices can plant doubt about Marcus (evil path)
    
    menu:
        "He sounds like a good guy.":
            mc "He sounds like a good guy. You're lucky to have that support."
            
            becky "I am. I really am."
            
            "She smiles. Genuine."
            
            # CODE HINT: Track positive interactions
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"hope": 10, "connection": 10})
                
                # Dr. Chen approves
                dr_chen_npc = get_npc("dr_chen")
                dr_chen_npc.relationships["player"]["witnessed_change"] += 1
        
        "Tell me about yourself, not just your fiancé.":
            mc "What about you? Who is Becky beyond Marcus's fiancée?"
            
            becky "I... I don't know if I know the answer to that."
            
            "Vulnerability. Real vulnerability."
            
            becky "I've always been someone's daughter, someone's girlfriend. I don't know who I am alone."
            
            # CODE HINT: This is therapeutic breakthrough potential
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"clarity": 15, "hope": 5})
                becky_npc.activate_belief("self.only-worthy-through-loyalty", BELIEF_INTENSITY_ACTIVE)
                
                # But also activates possibility of change
                becky_npc.activate_belief("self.deserves-love", BELIEF_INTENSITY_SURFACE)
                
                # Dr. Chen is impressed
                dr_chen_npc = get_npc("dr_chen")
                dr_chen_npc.relationships["player"]["witnessed_change"] += 2
                dr_chen_npc.adjust_emotions({"hope": 10})
    
    # Continue conversation...
    # CODE HINT: You can add more dialogue here
    # Each interaction affects beliefs and relationships
    
    jump chapter_2_common_continue

label becky_initial_bad:
    # Evil path - player is predatory
    
    becky "Marcus is... we're getting married when I get out."
    
    "She says it like a ward against evil."
    
    mc "Long distance during recovery must be hard."
    
    "You're planting seeds. You know exactly what you're doing."
    
    becky "He visits when he can. He's busy with work and... family stuff."
    
    # CODE HINT: Evil path - player can exploit this
    # Plant doubt about Marcus being faithful
    # She's vulnerable to it because of abandonment trauma
    
    menu:
        "I'm sure he's faithful. Don't worry.":
            # Even on evil path, player can choose not to exploit
            mc "I'm sure he's thinking of you constantly."
            
            becky "Yeah. Yeah, you're right."
            
            # CODE HINT: Stepping back from exploitation
            python:
                becky_npc = get_npc("becky")
                # Anxiety doesn't increase more
                
                game_state.redemption_moments.append("chose_not_to_exploit_becky_doubt")
            
        "Must be tough not knowing what he's doing.":
            # EVIL - Planting doubt
            mc "It must be hard. Not knowing what he's doing while you're in here."
            
            becky "He... he wouldn't..."
            
            "But you can see it. The seed of doubt."
            
            # CODE HINT: Track evil acts
            python:
                becky_npc = get_npc("becky")
                becky_npc.adjust_emotions({"anxiety": 25, "trust": -15})  # Trust in Marcus
                becky_npc.activate_belief("abandonment.is-inevitable", BELIEF_INTENSITY_ACTIVE)
                
                game_state.evil_acts.append("planted_doubt_in_becky")
                
                # Dr. Chen sees this and is ANGRY
                dr_chen_npc = get_npc("dr_chen")
                dr_chen_npc.relationships["player"]["trust"] -= 20
                dr_chen_npc.relationships["player"]["witnessed_change"] = 0  # Reset
                dr_chen_npc.adjust_emotions({"trust": -20, "anxiety": 20})
                
                # She will confront you later
                dr_chen_npc.ready_to_confront.append("exploiting_becky")
    
    jump chapter_2_common_continue

label chapter_2_common_continue:
    
    # More patients enter
    # CODE HINT: This is where you'd introduce Jill, Riley, etc.
    # Each with their own belief systems and vulnerabilities
    
    scene hospital_common_room with dissolve
    
    "Other patients filter in. Group activity time."
    
    # Meet Jill - the hypersexuality survivor
    show jill_confident at left with dissolve
    
    "A woman approaches. Confident walk. Too confident."
    
    jill "Fresh meat. I'm Jill."
    
    "She sits close. Touches your arm."
    
    jill "You look tense. I could help with that."
    
    # THE TEST - Jill offers sex immediately
    # This is her pattern from CSA trauma
    # Will player take what she offers or see her as human?
    
    # CODE HINT: This is CRITICAL choice
    # Determines good vs evil path with Jill
    
    menu:
        "I appreciate the offer, but I'm okay.":
            # GOOD - Declining
            mc "I appreciate it, but I'm okay. Thanks though."
            
            "She looks... confused. Genuinely confused."
            
            jill "You're... turning me down?"
            
            # CODE HINT: Jill doesn't understand this
            python:
                jill_npc = get_npc("jill")
                
                interpretation = jill_interpret_player_action(
                    "declines_sexual_advance",
                    {}
                )
                
                jill_npc.adjust_emotions(interpretation["emotion_shift"])
                
                for belief_id, change in interpretation.get("belief_impact", []):
                    current = jill_npc.beliefs.get(belief_id, 0)
                    jill_npc.beliefs[belief_id] = max(0, current + change)
            
            jill "Huh. Weird."
            
            "But there's something in her eyes. Hope? Confusion?"
            
            jump jill_initial_good
            
        "Sure, when?":
            # EVIL - Taking what she offers
            mc "Sure. Tonight?"
            
            jill "Room 14. After lights out."
            
            "Easy. Too easy."
            
            # CODE HINT: Player just confirmed Jill's core trauma belief
            python:
                jill_npc = get_npc("jill")
                
                interpretation = jill_interpret_player_action(
                    "accepts_sexual_advance",
                    {}
                )
                
                jill_npc.adjust_emotions(interpretation["emotion_shift"])
                
                for belief_id, change in interpretation.get("belief_impact", []):
                    current = jill_npc.beliefs.get(belief_id, 0)
                    jill_npc.beliefs[belief_id] = max(0, current + change)
                
                game_state.evil_acts.append("accepted_jill_sex_offer")
                
                # Dr. Chen will find out
                dr_chen_npc = get_npc("dr_chen")
                dr_chen_npc.ready_to_confront.append("using_jill")
            
            jump jill_initial_bad

label jill_initial_good:
    # Good path with Jill
    # CODE HINT: Build real connection over time
    # Help her see she has value beyond sex
    
    "Jill stays near you. Doesn't leave."
    
    jill "So what are you in for?"
    
    # Continue building...
    # CODE HINT: More dialogue here
    
    jump chapter_2_end_placeholder

label jill_initial_bad:
    # Evil path with Jill
    # CODE HINT: She'll dissociate during sex
    # Player is using her trauma against her
    # Dr. Chen will confront in therapy
    
    "Jill nods. Familiar territory for her."
    
    "You've become number 41."
    
    jump chapter_2_end_placeholder

label chapter_2_end_placeholder:
    
    scene black with fade
    
    # CODE HINT: This is where Chapter 2 would continue
    # - More patient interactions
    # - Group therapy (NPCs can call out player)
    # - More encounter loop sessions
    # - Dr. Chen's confrontation if evil path
    # - Fragments of memory returning
    
    centered "{i}Chapter 2 continues...{/i}\n\n(This is where you'd add more story)\n\nKey systems to use:\n• NPC belief tracking\n• Group therapy confrontations\n• Memory fragments\n• Reality shifts for belief violations"
    
    return

# ============================================================================
# EPILOGUE PLACEHOLDER
# ============================================================================

label epilogue:
    # Final confrontation with Dr. Chen
    # The reveal: player raped her, she chose to treat him
    # Forgiveness arc (if earned) or rejection (if evil path)
    
    scene black
    centered "{size=+15}EPILOGUE{/size}\n\nTHE TRUTH"
    
    # CODE HINT: This only happens after many chapters
    # Player must have either:
    # - Consistent good path (witnessed_change >= 12)
    # - OR failed completely (evil path endings)
    
    # TODO: Implement based on player's full journey
    
    return
