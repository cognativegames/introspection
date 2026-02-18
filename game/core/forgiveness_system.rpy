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
    
    therapist "I've been thinking a lot about what happened between us."
    
    # Player may feel defensive - reality might flicker if they're not ready
    if player_state["awareness_level"] < 7:
        play sound "soft_glitch.mp3"
        "Your head twinges. Guilt? Fear? You're not sure."
    
    therapist "When you [evil_act_committed], it hurt. Deeply. I want you to know that. I'm not going to pretend it didn't happen or that it was okay."
    
    menu:
        "I know. I'm sorry.":
            $ player_state["redemption_moments"].append(f"apologized_to_{character_name}")
            $ forgiveness_arcs["requirements"]["genuine_remorse_shown"] += 1
            
            mc "I know. I'm sorry, Sarah. I was... I was wrong."
            
            therapist "Thank you for saying that. And I believe you mean it. I've watched you these past weeks. I've seen you trying."
            
        "I don't know what you want me to say.":
            $ player_state["awareness_level"] -= 1
            
            mc "I don't know what you want me to say. It happened. I can't change it."
            
            therapist "I'm not asking you to change the past. I'm trying to talk about the future."
            
        "(Say nothing)":
            "You stay quiet. Sometimes words feel inadequate."
            
            therapist "It's okay. You don't have to say anything right now."
    
    therapist "I spent a long time being angry at you. Replaying it over and over. Imagining all the things I wished I'd said or done differently."
    
    therapist "And you know what I realized?"
    
    mc "What?"
    
    therapist "That anger was poisoning me more than what you did. I was letting what happened define me. Control me. Keep me trapped."
    
    show sarah_gentle at center with dissolve
    
    therapist "So I've decided to forgive you."
    
    # This might shock the player - reality stabilizes briefly
    play sound "soft_harmonic.mp3"
    $ reality_stability = min(10, reality_stability + 1)
    
    mc "You... what?"
    
    therapist "I forgive you. Not because what you did was okay—it wasn't. Not because you've earned it or because enough time has passed. But because *I* need to let this go."
    
    therapist "Carrying hatred doesn't hurt you, [player_name]. It hurts *me*. And I'm tired of hurting."
    
    menu:
        "I don't deserve your forgiveness.":
            mc "I don't deserve your forgiveness. Not after what I did."
            
            therapist "Maybe not. But forgiveness isn't about what you deserve. It's about what I need to heal."
            
            therapist "And here's the thing I want you to understand: forgiving you doesn't mean I'm okay with what happened. It doesn't mean we go back to how things were."
            
        "Thank you.":
            mc "Thank you. I... I don't know what to say."
            
            therapist "You don't have to say anything. Just... try to be better. For yourself, not for me."
            
        "Why are you telling me this?":
            mc "Why are you telling me this?"
            
            therapist "Because I think you need to hear it. And because I think you're carrying something heavier than what you did to me."
    
    therapist "Can I ask you something?"
    
    mc "Sure."
    
    therapist "When you hurt me, when you used my trauma against me... where did that come from?"
    
    # Critical moment - player must confront their own pain
    menu:
        "I don't know. I just... did it.":
            therapist "I don't believe that. Nobody just does something like that for no reason."
            
        "I was hurt too. A long time ago.":
            $ player_state["awareness_level"] += 2
            $ player_state["redemption_moments"].append("acknowledged_own_trauma")
            
            mc "I was hurt too. A long time ago. By someone I trusted."
            
            therapist "And you've been carrying that ever since?"
            
            mc "I guess so. I didn't even realize until now."
            
            therapist "That's what hurt people do, [player_name]. We hurt others. We recreate our pain in different forms, with different faces."
            
        "Because I'm a monster.":
            $ player_state["awareness_level"] += 1
            
            mc "Because I'm a monster. That's what you want to hear, right?"
            
            therapist "No. That's what *you* believe. And that belief is making you act like one."
    
    show sarah_compassionate at center with dissolve
    
    therapist "Listen to me carefully, because this is important: You are not defined by the worst thing you've ever done."
    
    therapist "I know what it's like to hate yourself. To think you're broken beyond repair. I carried that for years after... after what happened to me."
    
    therapist "But healing taught me something: we get to choose who we are going forward. Not who we were. Not what was done to us. Not what we did in our pain."
    
    therapist "*Who we choose to be.*"
    
    # Visual effect - reality becomes very stable, clear
    play sound "soft_harmonic.mp3"
    scene character_room_clear with dissolve
    show sarah_clear at center with dissolve
    
    $ reality_stability = min(10, reality_stability + 2)
    
    "The room sharpens. Everything becomes crystalline, vivid. Sarah's eyes are kind. Tired, but kind."
    
    therapist "If I can forgive you, [player_name]... can you forgive whoever hurt you?"
    
    # THE CRITICAL QUESTION
    # This is where the player might break through their own pain
    menu:
        "I... I don't know if I can.":
            mc "I don't know if I can. What they did... it changed me."
            
            therapist "It did change you. But it doesn't have to control you. Not anymore."
            
            therapist "Forgiving them doesn't mean what they did was okay. It means you're not going to let it keep poisoning you."
            
        "Maybe. If you can forgive me... maybe I can try.":
            $ player_state["awareness_level"] += 3
            $ player_state["redemption_moments"].append("considered_forgiving_own_abuser")
            $ reality_stability = min(10, reality_stability + 2)
            
            mc "Maybe. If you can forgive me... maybe I can try."
            
            therapist "That's all any of us can do. Try. One day at a time. One choice at a time."
            
            play sound "soft_harmonic.mp3"
            "Something inside you shifts. Not reality this time. Something deeper. A knot you didn't know you were carrying begins to loosen."
            
        "I want to. I'm just so angry.":
            mc "I want to. I'm just... I'm so angry. All the time. And I don't know how to stop."
            
            therapist "Then start with forgiving yourself. For being angry. For being hurt. For not knowing how to process it."
            
            therapist "Anger is just pain that doesn't know where to go. Give it permission to exist, and then... let it start to heal."
    
    therapist "I'm not going to tell you we're okay, [player_name]. I'm not going to say we can be what we were before you hurt me."
    
    therapist "But I am going to tell you this: I see you trying. I see you becoming aware. And that matters."
    
    therapist "So here's what forgiveness looks like for me: I release you from the narrative that you're a monster. You're a person who did a monstrous thing. Those are different."
    
    therapist "And I set a boundary: if you hurt me again, I'm done. Forgiveness isn't a free pass to keep causing harm. It's a gift, not an invitation."
    
    therapist "Can you respect that?"
    
    menu:
        "Yes. I can. I will.":
            $ char_state["trust"] = 4  # Not full trust, but foundation for rebuilding
            $ char_state["boundaries_established"] = True
            $ player_state["redemption_moments"].append(f"accepted_boundaries_{character_name}")
            
            mc "Yes. I can. I will."
            
            therapist "Then we can try again. Slowly. Carefully. As different people than we were before."
            
        "I don't know if I can promise that.":
            $ char_state["boundaries_established"] = True
            
            mc "I don't know if I can promise that. I'm still... figuring myself out."
            
            therapist "That's honest. I appreciate that more than a promise you're not sure you can keep."
            
            therapist "The boundary stands either way. But thank you for not lying to me."
    
    therapist "One more thing."
    
    mc "Yes?"
    
    therapist "Whatever you decide to do with this—with my forgiveness, with your own pain, with who you want to become—make sure it's your choice. Not because you think you owe me. Not because you're trying to prove something."
    
    therapist "Choose to heal because *you* deserve to be free from this. Just like I deserved to be free from hating you."
    
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