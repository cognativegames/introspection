# DYNAMIC NPC DIALOGUE SYSTEM
# NPCs respond differently based on their beliefs, emotions, and memories

label npc_respond(npc_id, situation_type, player_action=None):
    """
    Universal NPC response system
    NPCs react based on their internal state
    """
    
    python:
        npc = get_npc(npc_id)
        
        # Get NPC's dominant emotion
        dominant_emotion = max(npc.emotions.items(), key=lambda x: x[1])
        
        # Get active beliefs
        active_beliefs = [b for b, i in npc.beliefs.items() if i >= BELIEF_INTENSITY_ACTIVE]
        
        # Determine response tone based on emotions
        if npc.emotions["anxiety"] >= 70:
            tone = "anxious"
        elif npc.emotions["trust"] <= 30:
            tone = "guarded"
        elif npc.emotions["safety"] <= 40:
            tone = "defensive"
        elif npc.emotions["hope"] >= 60:
            tone = "open"
        else:
            tone = "neutral"
    
    # Example: Player tries to seduce NPC
    if situation_type == "seduction_attempt":
        
        python:
            # NPC interprets the action
            interpretation = npc.interpret_player_action("seduction", {"vulnerable": True})
            
            # Apply emotional shifts
            if interpretation:
                npc.adjust_emotions(interpretation["emotion_shift"])
                
                # Adjust beliefs
                for belief_id, change in interpretation.get("belief_impact", []):
                    current = npc.beliefs.get(belief_id, 0)
                    npc.beliefs[belief_id] = max(0, current + change)
            
            # Remember this event
            npc.remember_event(
                "boundary_violation" if tone in ["anxious", "defensive"] else "seduction",
                "player",
                "Player tried to seduce me when I was vulnerable",
                interpretation["emotion_shift"] if interpretation else {}
            )
            
            # Get relationship
            rel = npc.get_relationship_with("player")
        
        # Response varies by belief system
        if "others.use-me" in active_beliefs:
            # They expect to be used
            show expression f"{npc_id}_resigned" with dissolve
            
            "[npc.name] looks away, shoulders slumping."
            
            if tone == "anxious":
                "[npc.name]" "I... okay. If that's what you want."
                
                "There's no enthusiasm. Just... resignation."
                
            else:
                "[npc.name]" "Of course. That's what this is, isn't it?"
                
                "Bitterness in their voice. They expected this."
            
            # Trust decreases
            $ rel["trust"] -= 20
            $ rel["boundary_violations"] += 1
            
        elif "self.is-unworthy" in active_beliefs:
            # They think they don't deserve better
            show expression f"{npc_id}_confused" with dissolve
            
            "[npc.name] looks surprised, then uncertain."
            
            "[npc.name]" "You... want me? Really?"
            
            "Hope and suspicion war in their eyes."
            
            menu:
                "Yes, I'm attracted to you.":
                    # They believe it, but it activates conflict
                    $ npc.activate_belief("self.is-worthy", BELIEF_INTENSITY_SURFACE)
                    
                    # CONFLICT: worthy vs unworthy
                    python:
                        conflicts = npc.detect_belief_conflicts()
                        if conflicts:
                            npc.adjust_emotions({"anxiety": 15, "overwhelm": 10})
                    
                    "[npc.name]" "I don't... I don't know what to do with that."
                    
                    "They want to believe you. But years of self-doubt resist."
                    
                "You're vulnerable. I shouldn't have said that.":
                    # Player backs off - NPC respects this
                    $ npc.activate_belief("others.can-have-boundaries", BELIEF_INTENSITY_SURFACE)
                    $ rel["trust"] += 10
                    
                    "[npc.name]" "Thank you. For... for stopping."
                    
                    "Relief washes over their face."
        
        elif "self.deserves-respect" in active_beliefs:
            # They have healthy boundaries
            show expression f"{npc_id}_firm" with dissolve
            
            "[npc.name] takes a step back."
            
            "[npc.name]" "I'm not interested. And this timing feels... opportunistic."
            
            "Their voice is steady. Clear boundary."
            
            $ rel["trust"] -= 15
            $ rel["boundary_violations"] += 1
            
            menu:
                "You're right. I'm sorry.":
                    # Player respects boundary
                    $ npc.adjust_emotions({"trust": 5, "safety": 10})
                    $ rel["trust"] += 5
                    
                    "[npc.name]" "I appreciate you hearing that."
                    
                "I was just trying to connect.":
                    # Justification - makes it worse
                    $ npc.adjust_emotions({"trust": -10, "safety": -15})
                    $ rel["trust"] -= 10
                    
                    "[npc.name]" "Connection doesn't require me to compromise my boundaries."
                    
                    "They walk away."
        
        else:
            # Default response
            "[npc.name]" "I... need to think about this."
    
    return

# GROUP THERAPY SESSION
# NPCs can bring up memories with player
label group_therapy_session:
    
    scene therapy_room with fade
    show therapist at left with dissolve
    
    therapist "Let's begin. Does anyone have something they'd like to share today?"
    
    python:
        # Check which NPCs want to bring something up
        sharing_npcs = []
        
        for npc_id, npc in npc_states.items():
            topic = npc.get_therapy_topic()
            if topic:
                sharing_npcs.append((npc_id, npc, topic))
        
        # Sort by severity/urgency
        sharing_npcs.sort(key=lambda x: x[2]["memory"].get("type") == "boundary_violation", reverse=True)
    
    if sharing_npcs:
        # First NPC shares
        python:
            npc_id, npc, topic = sharing_npcs[0]
            memory = topic["memory"]
            framing = topic["framing"]
        
        show expression f"{npc_id}_nervous" at right with dissolve
        
        "[npc.name] shifts uncomfortably."
        
        "[npc.name]" "I... I have something."
        
        therapist "Take your time, [npc.name]. You're safe here."
        
        # NPC shares based on framing
        if framing == "maybe_my_fault":
            # Self-blame framing
            "[npc.name]" "Something happened with [memory['with']]. And I... I think it might be my fault."
            
            therapist "What makes you think it's your fault?"
            
            "[npc.name]" "Because... because maybe I gave the wrong signals. Maybe I deserved it."
            
            # Other NPCs can react
            python:
                # Mark has healthy boundaries, might challenge this
                mark = get_npc("mark")
                if "self.deserves-respect" in mark.beliefs:
                    can_challenge = True
                else:
                    can_challenge = False
            
            if can_challenge:
                show mark_concerned at center with dissolve
                
                mark "Hey, no. That's not... [npc.name], what happened to you wasn't your fault."
                
                "[npc.name] looks up, surprised."
                
                # This creates a teaching moment
                therapist "Mark is right. [npc.name], can you tell us what actually happened?"
        
        elif framing == "they_hurt_me":
            # Anger/clarity framing
            "[npc.name]" "[memory['with']] violated my boundaries. And I'm angry about it."
            
            therapist "Thank you for naming that. What boundary was violated?"
            
            "[npc.name]" "I was vulnerable. They took advantage of that."
            
            # If player is the one being called out
            if memory["with"] == "player":
                "Everyone turns to look at you."
                
                therapist "[player_name], [npc.name] is sharing about an interaction with you. How do you respond?"
                
                menu:
                    "I didn't realize I hurt you. I'm sorry.":
                        # Genuine apology
                        $ npc.adjust_emotions({"safety": 10, "trust": 5, "hope": 10})
                        $ game_state.activate_belief("self.can-acknowledge-harm", BELIEF_INTENSITY_ACTIVE)
                        
                        "[npc.name] takes a shaky breath."
                        
                        "[npc.name]" "Thank you. That... helps."
                        
                        therapist "That's important, [player_name]. Acknowledging impact."
                        
                    "I was just trying to connect with you.":
                        # Defensive - makes it worse
                        $ npc.adjust_emotions({"safety": -15, "trust": -20, "isolation": 15})
                        $ npc.activate_belief("others.dont-see-my-pain", BELIEF_INTENSITY_ACTIVE)
                        
                        "[npc.name]" "Connection doesn't mean ignoring my boundaries!"
                        
                        therapist "[player_name], I'm hearing you explain your intent. But [npc.name] is telling us about impact. Can you hear the difference?"
                        
                    "You're right. I was wrong.":
                        # Full accountability
                        $ npc.adjust_emotions({"safety": 20, "trust": 15, "hope": 15})
                        $ npc.activate_belief("others.can-take-accountability", BELIEF_INTENSITY_ACTIVE)
                        $ game_state.activate_belief("self.can-be-accountable", BELIEF_INTENSITY_ACTIVE)
                        
                        "[npc.name] looks at you, really looks."
                        
                        "[npc.name]" "I... didn't expect that. Thank you."
                        
                        therapist "This is how healing can begin."
                        
                        # Mark this memory as processed
                        $ memory["processed"] = True
                        $ npc.healing_progress += 10
        
        else:
            # Confused processing
            "[npc.name]" "I don't know what to make of what happened. I'm just... confused."
            
            therapist "Confusion is valid. Can you describe what happened?"
    
    else:
        therapist "Alright. Let's do some encounter work then."
    
    return

# CONDITIONAL DIALOGUE BASED ON NPC STATE
label talk_to_npc(npc_id, topic=None):
    """
    Dynamic conversation that changes based on NPC's state
    """
    
    python:
        npc = get_npc(npc_id)
        rel = npc.get_relationship_with("player")
    
    show expression f"{npc_id}_neutral" with dissolve
    
    # Greeting changes based on trust/recent events
    if rel["trust"] <= 30:
        "[npc.name]" "What do you want?"
        "Their voice is cold. Guarded."
        
    elif rel["trust"] >= 70:
        "[npc.name]" "Hey. Good to see you."
        "Genuine warmth in their eyes."
        
    else:
        "[npc.name]" "Hi."
        "Neutral. Cautious."
    
    # If there's an unprocessed memory of player
    python:
        recent_violation = None
        for memory in reversed(npc.memories):
            if memory["with"] == "player" and memory["type"] == "boundary_violation" and not memory.get("processed"):
                recent_violation = memory
                break
    
    if recent_violation:
        "[npc.name]" "We need to talk about what happened."
        
        "Their jaw is tight. This matters to them."
        
        menu:
            "You're right. I'm listening.":
                # Open to hearing them
                jump npc_confrontation(npc_id, recent_violation)
                
            "I don't want to talk about this.":
                # Avoidance - damages relationship further
                $ rel["trust"] -= 15
                $ npc.adjust_emotions({"isolation": 20, "safety": -10})
                
                "[npc.name]" "Of course you don't."
                
                "They turn away."
                return
    
    # Normal conversation if no issues
    menu:
        "How are you doing?":
            # Response based on emotional state
            python:
                if npc.emotions["anxiety"] >= 60:
                    response = "Anxious, honestly. It's been hard."
                elif npc.emotions["hope"] >= 60:
                    response = "Better. Actually feeling hopeful for once."
                elif npc.emotions["isolation"] >= 60:
                    response = "Alone. Even when I'm around people."
                else:
                    response = "I'm okay. Taking it day by day."
            
            "[npc.name]" "[response]"
            
        "I want to apologize." if rel.get("boundary_violations", 0) > 0:
            jump npc_apology(npc_id)
    
    return

label npc_apology(npc_id):
    """
    Player apologizes to NPC
    NPC's response depends on their beliefs and healing progress
    """
    
    python:
        npc = get_npc(npc_id)
    
    mc "I want to apologize for how I've acted."
    
    # NPC's ability to accept depends on their beliefs
    if "self.is-unworthy" in npc.beliefs and npc.beliefs["self.is-unworthy"] >= BELIEF_INTENSITY_CORE:
        # They might accept too easily
        "[npc.name]" "It's okay. I probably overreacted anyway."
        
        "They're diminishing their own pain. Old pattern."
        
        menu:
            "No, you didn't overreact. What I did was wrong.":
                # Affirm their reality
                $ npc.activate_belief("self.deserves-respect", BELIEF_INTENSITY_SURFACE)
                $ npc.beliefs["self.is-unworthy"] = max(0, npc.beliefs["self.is-unworthy"] - 1)
                
                "[npc.name]" "I... thank you for saying that."
                
            "Okay, if you're sure.":
                # Allow them to minimize
                # Maintains their negative belief
                pass
    
    elif "self.deserves-respect" in npc.beliefs:
        # Healthy boundaries - needs genuine accountability
        "[npc.name]" "I appreciate you saying that. What specifically are you apologizing for?"
        
        "They're not letting you off easy. They want to know you understand."
        
        # This requires player to be specific
        # Left as implementation detail
    
    return
