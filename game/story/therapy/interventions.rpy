# ============================================================================
# THERAPY INTERVENTIONS
# Based on Bashar's framework: Everything is neutral, you assign meaning
# ============================================================================

label encounter_therapy_breathing_room_feel_guilty:
    # Player feels guilty for needing space/boundaries
    # Core belief: "Needing space means I'm selfish/bad"
    # Bashar principle: Needing space is neutral - guilt is assigned meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You felt guilty just now. For needing time alone."
    
    mc "Well... yeah. They needed me and I just—"
    
    dr_chen "Stop. Let me ask you something: is breathing selfish?"
    
    mc "What? No, of course not."
    
    dr_chen "Why not? When you breathe, you're taking oxygen that someone else could use."
    
    mc "That's... that's different. I need to breathe."
    
    dr_chen "Exactly. You need to breathe. It's neutral. Not selfish, not generous. Neutral."
    
    dr_chen "Needing space is the same. It's as neutral as breathing."
    
    dr_chen "But you've attached a meaning to it. You've decided it means 'I'm bad' or 'I'm selfish.'"
    
    mc "I never thought of it that way."
    
    dr_chen "Nothing has inherent meaning, [player_name]. Not until you assign it."
    
    dr_chen "So here's the question: what meaning do you WANT to give to needing space?"
    
    menu:
        "Taking space means I'm honoring my needs so I can show up better":
            $ game_state.beliefs["self.is-worthy"] = game_state.beliefs.get("self.is-worthy", 0) + 10
            $ game_state.beliefs["self.must-earn-love"] = max(0, game_state.beliefs.get("self.must-earn-love", 0) - 15)
            $ game_state.adjust_emotions({"clarity": 20, "shame": -15})
            $ game_state.introspection_depth += 1
            
            mc "Taking space means I'm honoring my needs so I can show up better for others."
            
            dr_chen "There it is. You just chose a new meaning. And it's truer, isn't it?"
            
            scene therapy_office_clear with dissolve
            
            mc "It feels... lighter. Clearer."
            
            dr_chen "That's alignment. When your chosen meaning serves you, reality stabilizes."
            
            dr_chen "The action is the same—taking space. But the meaning you assign changes everything."
            
        "I still think I should be there for people no matter what":
            $ game_state.beliefs["self.must-earn-love"] = game_state.beliefs.get("self.must-earn-love", 0) + 5
            $ game_state.adjust_emotions({"overwhelm": 10})
            
            mc "I don't know. I feel like I should be there for people no matter what."
            
            dr_chen "Notice what that belief costs you. Burnout. Resentment. Depletion."
            
            dr_chen "You're choosing a meaning that drains you. That's your right. But is it exciting?"
            
            mc "Exciting?"
            
            dr_chen "Does showing up depleted excite you? Or does honoring yourself excite you?"
            
            mc "...the second one."
            
            dr_chen "Then act on that. Not because it's 'good' or 'right.' Because it excites you more."
    
    dr_chen "Remember: the situation is neutral. Your guilt is just a meaning you attached."
    
    dr_chen "You can attach a different one anytime you choose."
    
    return

label encounter_therapy_shared_grief_withdraw:
    # Player withdraws from shared vulnerability/pain
    # Core belief: "Showing pain means I'm weak" or "Others will use my pain against me"
    # Bashar principle: Vulnerability is neutral - you choose its meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You pulled away when they shared their pain with you."
    
    mc "I didn't know what to say. I just... froze."
    
    dr_chen "What were you afraid would happen if you stayed present?"
    
    menu:
        "They'd see I'm weak too":
            mc "They'd see I'm weak. That I'm damaged."
            
            dr_chen "And 'weak' and 'damaged'—what do those words mean to you?"
            
            mc "That I'm... broken. Unlovable."
            
            dr_chen "Those are meanings you've assigned to vulnerability."
            
        "They'd expect me to fix it and I can't":
            mc "They'd expect me to fix their pain and I can't."
            
            dr_chen "So vulnerability means responsibility for their suffering?"
            
            mc "I guess so."
            
            dr_chen "That's a meaning you assigned. Not the only possible meaning."
    
    dr_chen "Here's what's actually true: someone shared their experience. That's it. Neutral."
    
    dr_chen "Everything else—broken, weak, responsible, unlovable—you added that."
    
    dr_chen "What if you assigned a different meaning?"
    
    menu:
        "Shared pain is just... connection. Honesty. Nothing more.":
            $ game_state.beliefs["self.is-vulnerable-and-resilient"] = game_state.beliefs.get("self.is-vulnerable-and-resilient", 0) + 15
            $ game_state.beliefs["self.is-unworthy"] = max(0, game_state.beliefs.get("self.is-unworthy", 0) - 20)
            $ game_state.adjust_emotions({"connection": 20, "isolation": -15, "clarity": 15})
            $ game_state.introspection_depth += 1
            
            mc "What if shared pain is just... connection? Honesty? Nothing more?"
            
            dr_chen "Yes. Exactly that. No fixing required. No weakness implied. Just presence."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Do you feel the difference? The room literally clears when you choose alignment."
            
            mc "I do. It's like... I don't have to perform anymore."
            
            dr_chen "Because you're not assigning meanings that require performance."
            
            dr_chen "You're seeing what's actually there: two people, present with each other."
            
        "I don't think I can handle other people's pain right now":
            $ game_state.adjust_emotions({"isolation": 10})
            
            mc "I don't think I can handle other people's pain right now."
            
            dr_chen "That's honest. And honoring that is valid."
            
            dr_chen "Just notice: you're choosing to assign the meaning 'too much' to vulnerability."
            
            dr_chen "When you're ready, you can choose differently. The pain itself hasn't changed."
            
            dr_chen "Only the meaning you give it."
    
    return

label encounter_therapy_shared_grief_deflect:
    # Player deflects with humor/sarcasm when faced with genuine emotion
    # Core belief: "Real emotion is dangerous" or "I'm not allowed to feel"
    # Bashar principle: Deflection is a meaning assigned to vulnerability
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You made a joke. Right when things got real."
    
    mc "I was trying to lighten the mood. Is that wrong?"
    
    dr_chen "Nothing is wrong. But I'm curious: what would've happened if you didn't deflect?"
    
    mc "I don't know. It would've been... awkward? Heavy?"
    
    dr_chen "And 'heavy' means what to you?"
    
    menu:
        "It means unbearable. Too much.":
            mc "Heavy means unbearable. Like I'll drown in it."
            
            dr_chen "So real emotion equals drowning. That's the meaning you've assigned."
            
        "It means vulnerable. Open. Exposed.":
            mc "It means vulnerable. Open. And that's dangerous."
            
            dr_chen "Dangerous how?"
            
            mc "People can hurt you when you're open."
            
            dr_chen "Okay. So you've assigned the meaning: openness equals danger."
    
    dr_chen "What if I told you emotion is completely neutral?"
    
    mc "How can sadness be neutral?"
    
    dr_chen "Sadness is just energy moving through you. Like weather moving through a landscape."
    
    dr_chen "It's not good or bad, heavy or light, dangerous or safe. It just IS."
    
    dr_chen "You assigned 'unbearable' or 'dangerous' to it. And now you deflect to avoid the meanings, not the emotion."
    
    mc "So... I'm running from meanings I created?"
    
    dr_chen "Exactly. The emotion is neutral. Your interpretation makes it scary."
    
    menu:
        "I want to try feeling without assigning meaning. Just... feeling.":
            $ game_state.beliefs["self.can-attach-new-meaning"] = game_state.beliefs.get("self.can-attach-new-meaning", 0) + 15
            $ game_state.adjust_emotions({"clarity": 20, "anxiety": -15})
            $ game_state.introspection_depth += 1
            
            mc "What if I just... felt? Without the story?"
            
            dr_chen "Then you'd discover emotion doesn't destroy you. It moves through you."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Try it now. Don't deflect. Don't assign meaning. Just feel."
            
            "I sit with the discomfort. It rises. It peaks. It passes."
            
            mc "It... passed. It didn't destroy me."
            
            dr_chen "Because it's neutral. It's just energy. The meanings you add are what create suffering."
            
        "This feels too uncomfortable. I need to keep things light.":
            $ game_state.adjust_emotions({"isolation": 10})
            
            mc "I think I need to keep things light for now."
            
            dr_chen "That's your choice. But notice the cost."
            
            dr_chen "By avoiding the feeling, you avoid connection. Depth. Real presence."
            
            dr_chen "When you're ready to experience emotion as neutral, you'll find it's not as scary as the meaning suggests."
    
    return

label encounter_mirror_moment_see_flaws:
    # Player looks in mirror and sees only flaws
    # Core belief: "I am fundamentally flawed/broken"
    # Bashar principle: Your reflection is neutral - you assign meaning to features
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You looked in the mirror and saw flaws. Only flaws."
    
    mc "Because they're there. I'm not imagining them."
    
    dr_chen "I didn't say you imagined them. I said you assigned meaning to them."
    
    dr_chen "Your face has features. Lines. Asymmetries. Everyone's does."
    
    dr_chen "But you looked at those neutral features and decided they mean 'I'm flawed.'"
    
    mc "So I should just pretend I look good?"
    
    dr_chen "No. Pretending is assigning a false positive meaning. That's not freedom either."
    
    dr_chen "I'm suggesting you see what's actually there: a face. Features. Neutral."
    
    mc "How can a face be neutral?"
    
    dr_chen "Look at this pen."
    
    "She holds up a pen."
    
    dr_chen "Is this pen beautiful or ugly?"
    
    mc "It's... just a pen."
    
    dr_chen "Exactly. It's neutral. It's only when you compare it to other pens, or assign it value, that it becomes 'good' or 'bad.'"
    
    dr_chen "Your face is the same. Features. Neutral. You assigned 'flawed.'"
    
    menu:
        "I could just see my face as... my face. Not good or bad. Just mine.":
            $ game_state.beliefs["self.is-fundamentally-flawed"] = max(0, game_state.beliefs.get("self.is-fundamentally-flawed", 0) - 20)
            $ game_state.beliefs["self.can-attach-new-meaning"] = game_state.beliefs.get("self.can-attach-new-meaning", 0) + 15
            $ game_state.adjust_emotions({"clarity": 25, "shame": -20})
            $ game_state.introspection_depth += 1
            
            mc "What if I just saw my face as... my face? Not good or bad. Just mine."
            
            dr_chen "There it is. That's neutrality. That's freedom."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "When you stop assigning 'flawed' to neutral features, the judgment collapses."
            
            mc "It's not that I suddenly think I'm attractive. I just... don't care as much."
            
            dr_chen "Because you're not layering meaning onto neutral reality."
            
            dr_chen "And THAT'S where peace lives. Not in being beautiful. In being neutral."
            
        "But some faces are objectively better than others":
            $ game_state.beliefs["self.is-fundamentally-flawed"] = game_state.beliefs.get("self.is-fundamentally-flawed", 0) + 5
            
            mc "I don't know. Some faces are just objectively better."
            
            dr_chen "Says who? You? Society? A magazine?"
            
            dr_chen "You're stacking meaning on meaning on meaning until you can't see what's actually there."
            
            dr_chen "But here's the thing: you can't force yourself to see neutrally. You can only notice when you're assigning meaning."
            
            dr_chen "When you're ready, the meanings will dissolve on their own."
    
    return

label encounter_therapy_criticism_public_internalize:
    # Player internalizes public criticism as absolute truth
    # Core belief: "Others' opinions define my worth"
    # Bashar principle: Criticism is neutral feedback - you choose if it's truth
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "Someone criticized you publicly. And you took it as gospel."
    
    mc "They were right, though. I AM—"
    
    dr_chen "Stop. How do you know they're right?"
    
    mc "Because... they said it. And it resonated."
    
    dr_chen "It resonated because you already believed it. Not because it's objectively true."
    
    dr_chen "Let me ask you this: is criticism neutral?"
    
    mc "How could it be? They're saying I'm bad at something."
    
    dr_chen "No. They're saying words. Sounds. You're deciding those sounds mean 'I'm bad.'"
    
    dr_chen "What if criticism is just... information? Data? Neutral?"
    
    mc "But what if they're right? What if I really am flawed?"
    
    dr_chen "Even if their observation is accurate, the meaning 'flawed' is YOUR addition."
    
    dr_chen "They might say 'you did X poorly.' That's data. Neutral."
    
    dr_chen "You translate it to 'I AM fundamentally flawed.' That's meaning you assigned."
    
    menu:
        "I could receive criticism as just data. Not truth about my worth.":
            $ game_state.beliefs["self.is-worthy"] = game_state.beliefs.get("self.is-worthy", 0) + 15
            $ game_state.beliefs["self.is-fundamentally-flawed"] = max(0, game_state.beliefs.get("self.is-fundamentally-flawed", 0) - 20)
            $ game_state.adjust_emotions({"clarity": 20, "shame": -20})
            $ game_state.introspection_depth += 1
            
            mc "So I could just receive it as data? Not truth about my core worth?"
            
            dr_chen "Exactly. 'I did X in a way that didn't work' is different from 'I AM flawed.'"
            
            scene therapy_office_clear with dissolve
            
            dr_chen "When you separate the data from the meaning, you're free."
            
            dr_chen "Free to improve without shame. Free to discard feedback that doesn't serve you."
            
            mc "I can choose what it means."
            
            dr_chen "Now you're getting it. Everything is meaningless until you assign meaning."
            
            dr_chen "Criticism is neutral. Your worth is neutral. You decide what everything means."
            
        "If people see my flaws, they must be real":
            $ game_state.beliefs["self.is-unworthy"] = game_state.beliefs.get("self.is-unworthy", 0) + 5
            
            mc "But if other people see my flaws, they must be real."
            
            dr_chen "Other people see through their own belief filters. Not objective reality."
            
            dr_chen "Someone believing you're flawed doesn't make it true. It makes it their perception."
            
            dr_chen "You're giving strangers authority over your self-concept."
            
            dr_chen "When you're ready, you'll take that authority back."
    
    return

label encounter_therapy_criticism_public_defensive:
    # Player becomes defensive when criticized
    # Core belief: "Being wrong means I'm worthless" or "I must defend my image"
    # Bashar principle: Being wrong is neutral - defensiveness is assigned meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You got defensive. Immediately."
    
    mc "They were attacking me!"
    
    dr_chen "Were they? Or were they just sharing their perspective?"
    
    mc "It felt like an attack."
    
    dr_chen "And why does someone else's perspective feel like an attack?"
    
    menu:
        "Because if they're right, I'm worthless":
            mc "Because... if they're right about me, then I'm worthless."
            
            dr_chen "So being wrong equals worthless. That's the meaning you've assigned."
            
        "Because I can't let them see my weakness":
            mc "Because I can't let them see weakness. I have to be... strong."
            
            dr_chen "So weakness equals danger. And being wrong reveals weakness."
    
    dr_chen "What if being wrong is completely neutral?"
    
    mc "How can being wrong be neutral?"
    
    dr_chen "I'm wrong about things every day. Does that make me worthless?"
    
    mc "No, but that's different—"
    
    dr_chen "Why is it different? Because I don't assign the meaning 'worthless' to being wrong."
    
    dr_chen "Being wrong is just... having inaccurate information. Neutral."
    
    dr_chen "You added 'worthless.' You added 'weak.' You added 'dangerous.'"
    
    menu:
        "I could be wrong without it meaning anything about my value":
            $ game_state.beliefs["self.is-worthy"] = game_state.beliefs.get("self.is-worthy", 0) + 15
            $ game_state.beliefs["self.is-fundamentally-flawed"] = max(0, game_state.beliefs.get("self.is-fundamentally-flawed", 0) - 15)
            $ game_state.adjust_emotions({"clarity": 20, "anxiety": -15})
            $ game_state.introspection_depth += 1
            
            mc "So I could be wrong... and it wouldn't mean anything about my value?"
            
            dr_chen "Exactly. You could be wrong about a hundred things and still be worthy."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Because worth isn't tied to being right. You just decided it was."
            
            mc "That's... liberating actually."
            
            dr_chen "Of course it is. You just freed yourself from defending an illusion."
            
            dr_chen "Now you can be wrong, learn, grow—without the story that it means you're worthless."
            
        "But I have to protect my reputation":
            $ game_state.adjust_emotions({"anxiety": 10})
            
            mc "I have to protect my reputation. People's opinions matter."
            
            dr_chen "Do they? Or have you assigned meaning to others' opinions?"
            
            dr_chen "What if their opinions are also neutral? Just thoughts in their heads?"
            
            mc "Then nothing would matter."
            
            dr_chen "No. Then YOU would choose what matters. Not react to what you think others think."
            
            dr_chen "That's the difference between freedom and imprisonment."
    
    return

label encounter_therapy_random_kindness_meaningless:
    # Player sees kind gesture as meaningless/empty
    # Core belief: "Nothing matters" or "Life is meaningless" (in depressing way)
    # Bashar principle: Life IS meaningless - you get to assign meaning (liberation)
    # IMPORTANT: The FACT of meaninglessness is neutral/positive
    # The INTERPRETATION "meaningless = empty/abandoned" is the negative belief
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "Someone did something kind for you. And you dismissed it."
    
    mc "Because it doesn't mean anything. It's just... random."
    
    dr_chen "Interesting. Tell me more about 'doesn't mean anything.'"
    
    mc "Nothing really means anything, right? We're all just going through motions."
    
    dr_chen "Ah. You've discovered life is meaningless."
    
    mc "Yeah. And it's depressing."
    
    dr_chen "Stop right there. Life IS meaningless. That's true."
    
    dr_chen "But you just added: 'And it's depressing.'"
    
    dr_chen "The MEANINGLESSNESS is a fact - neutral. The DEPRESSION is a meaning YOU attached."
    
    mc "How can meaninglessness NOT be depressing?"
    
    dr_chen "What if instead of 'empty,' meaninglessness meant 'free'?"
    
    mc "Free?"
    
    dr_chen "If life has no inherent meaning, then YOU get to assign meaning. Any meaning you want."
    
    dr_chen "That's not emptiness. That's a blank canvas. Total creative freedom."
    
    dr_chen "You've been handed the ultimate gift - and you called it 'depressing.'"
    
    menu:
        "I could choose to let kindness mean... connection. Warmth. Something I value.":
            $ game_state.beliefs["existence.is-meaningless-negative"] = max(0, game_state.beliefs.get("existence.is-meaningless-negative", 0) - 25)
            $ game_state.beliefs["existence.is-neutral"] = game_state.beliefs.get("existence.is-neutral", 0) + 15
            $ game_state.beliefs["self.can-attach-new-meaning"] = game_state.beliefs.get("self.can-attach-new-meaning", 0) + 20
            $ game_state.adjust_emotions({"clarity": 25, "hope": 20, "isolation": -20, "freedom": 15})
            $ game_state.introspection_depth += 1
            
            mc "So I could choose to let that kindness mean... connection? Warmth?"
            
            dr_chen "YES. Now you're getting it."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Life is meaningless. That's the neutral truth."
            
            dr_chen "But you're the one who assigns meaning. And you can assign meanings that excite you."
            
            mc "So it's not depressing. It's... liberating."
            
            dr_chen "There it is. You're free to make ANYTHING mean ANYTHING."
            
            dr_chen "Kindness can mean connection. Or nothing. Or a threat. YOU choose."
            
            dr_chen "And when you choose meanings that align with excitement, that's when life becomes... alive."
            
        "But if I assign meaning, isn't that just delusion?":
            $ game_state.adjust_emotions({"isolation": 10})
            
            mc "But isn't assigning meaning just... lying to myself?"
            
            dr_chen "Is calling a sunset 'beautiful' a lie?"
            
            mc "No, but that's different—"
            
            dr_chen "It's not different. The sunset is neutral. You assigned 'beautiful.'"
            
            dr_chen "You can assign depressing meanings or exciting meanings. Either way, you're assigning."
            
            dr_chen "The question is: which meanings serve your highest excitement?"
            
            dr_chen "The 'depressing' meaning you attached to meaninglessness... does that excite you?"
    
    return

label encounter_therapy_random_kindness_suspicious:
    # Player is suspicious of kind gestures
    # Core belief: "People want something" or "Kindness is manipulation"
    # Bashar principle: Kindness is neutral - suspicion is assigned meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "Someone was kind to you. And you got suspicious."
    
    mc "Because people don't just DO things for free. They always want something."
    
    dr_chen "Always? Every single person? Every single time?"
    
    mc "Mostly, yeah."
    
    dr_chen "That's a belief. 'People who are kind want something from me.'"
    
    dr_chen "And because of that belief, you filter every kind gesture through suspicion."
    
    mc "Because I'm usually right!"
    
    dr_chen "Or because you're creating what you expect to see."
    
    mc "What does that mean?"
    
    dr_chen "If you expect manipulation, you'll interpret neutral actions as manipulative."
    
    dr_chen "Someone smiles at you—you think 'what do they want?'"
    
    dr_chen "Someone helps you—you think 'what's their angle?'"
    
    dr_chen "But what if their actions are completely neutral? And you're adding the manipulation?"
    
    menu:
        "I could see kindness as just... kindness. Neutral. No hidden agenda.":
            $ game_state.beliefs["others.are-complex"] = game_state.beliefs.get("others.are-complex", 0) + 15
            $ game_state.beliefs["others.are-cruel"] = max(0, game_state.beliefs.get("others.are-cruel", 0) - 15)
            $ game_state.adjust_emotions({"connection": 15, "isolation": -15, "clarity": 15})
            $ game_state.introspection_depth += 1
            
            mc "What if kindness is just... kindness? No hidden agenda?"
            
            dr_chen "Then you'd be free to receive it. Without the suspicion weighing you down."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "People are complex. Some are kind. Some aren't. Some want something."
            
            dr_chen "But the ACTION—someone helping you—that's neutral. You assign the meaning."
            
            mc "So I could choose to see it as genuine until proven otherwise?"
            
            dr_chen "You could. And you'd notice you feel less isolated. Less defended."
            
            dr_chen "Not because the world changed. Because the meaning you assigned changed."
            
        "But I've been burned before. I need to stay vigilant.":
            $ game_state.beliefs["others.are-cruel"] = game_state.beliefs.get("others.are-cruel", 0) + 5
            $ game_state.adjust_emotions({"isolation": 10})
            
            mc "I've been burned before. I can't just trust everyone."
            
            dr_chen "I'm not asking you to trust blindly. I'm asking you to notice your filter."
            
            dr_chen "You're applying the meaning 'manipulative' to EVERY kind gesture."
            
            dr_chen "That's not protection. That's isolation."
            
            dr_chen "When you're ready, you can choose to see neutrally. Then decide case by case."
    
    return

label encounter_therapy_stray_dog_fear:
    # Player fears neutral/friendly dog
    # Core belief: "The world is dangerous"
    # Bashar principle: The dog is neutral - fear is assigned meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "[player_name], talk to me about the dog."
    
    mc "What about it?"
    
    dr_chen "You were afraid. Before it even did anything."
    
    mc "It could've bitten me. You never know."
    
    dr_chen "Could've. But didn't. Most don't."
    
    dr_chen "Yet you saw danger before observing reality."
    
    dr_chen "What percentage of friendly dogs actually bite strangers?"
    
    menu:
        "I don't know... maybe 20%?":
            $ game_state.adjust_emotions({"anxiety": 5})
            dr_chen "Less than 1%. Your perception is inflated by your belief."
            
        "Probably very low":
            $ game_state.adjust_emotions({"clarity": 5})
            dr_chen "Exactly. Less than 1%. So why assume danger?"
    
    dr_chen "Because you've assigned the meaning 'dangerous' to the neutral event 'dog approaches.'"
    
    dr_chen "The dog is just a dog. Wagging tail. Neutral."
    
    dr_chen "Everything else—threat, danger, fear—you added that."
    
    mc "So I'm just supposed to trust every dog?"
    
    dr_chen "No. I'm suggesting you see what's actually there first. THEN decide."
    
    dr_chen "Right now you're seeing through a filter that says 'world is dangerous.'"
    
    dr_chen "So every neutral thing becomes a threat in your perception."
    
    menu:
        "I could observe first. See what's actually there. Then respond.":
            $ game_state.beliefs["world.is-dangerous"] = max(0, game_state.beliefs.get("world.is-dangerous", 0) - 15)
            $ game_state.beliefs["world.is-neutral"] = game_state.beliefs.get("world.is-neutral", 0) + 15
            $ game_state.adjust_emotions({"anxiety": -20, "clarity": 20})
            $ game_state.introspection_depth += 1
            
            mc "So I could just... observe first? See what's actually there?"
            
            dr_chen "Yes. The world is neutral. It's not out to get you. It's not inherently safe either."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "It's neutral. And YOU get to assign meaning based on actual observation."
            
            mc "That feels... less scary somehow."
            
            dr_chen "Because you're not fighting imaginary threats anymore."
            
            dr_chen "You're just observing reality. Neutral reality. And responding from clarity."
            
        "The world IS dangerous. Better safe than sorry.":
            $ game_state.beliefs["world.is-dangerous"] = game_state.beliefs.get("world.is-dangerous", 0) + 5
            $ game_state.adjust_emotions({"isolation": 10})
            
            mc "I'd rather be safe. The world IS dangerous."
            
            dr_chen "That's your choice. But notice the cost."
            
            dr_chen "You're living in a world where everything is a threat. Even friendly dogs."
            
            dr_chen "That's not safety. That's prison."
            
            dr_chen "When you're ready to see neutrally, you'll find the world less scary."
    
    return


# ============================================================================
# NSFW THERAPY INTERVENTIONS
# Add to: /game/story/therapy/interventions.rpy
# ============================================================================

label encounter_therapy_coffee_objectification:
    # Player objectified woman in coffee shop
    # Core belief: "Women dress sexy FOR men / exist for my pleasure"
    # Bashar: Her clothing choices are neutral - you assigned sexual availability
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "Tell me about the woman in the coffee shop."
    
    mc "What about her?"
    
    dr_chen "You said she was 'advertising.' That she dressed like that because she wanted men to look."
    
    mc "I mean... yeah? Why else would she wear a dress like that?"
    
    dr_chen "Why do you wear the clothes you wear?"
    
    mc "Because they're comfortable. Or I like how they look."
    
    dr_chen "Not to attract women?"
    
    mc "Well, no. Not primarily."
    
    dr_chen "So why do you assume her motivations are different from yours?"
    
    mc "Because—"
    
    dr_chen "Because you've assigned the meaning 'dressed for my sexual attention' to her neutral clothing choice."
    
    dr_chen "Her dress is just fabric. Neutral. You decided it meant 'she wants me to objectify her.'"
    
    menu:
        "But she must have known men would look...":
            mc "But she must have known men would look at her in that dress."
            
            dr_chen "Maybe. And maybe she doesn't care what men think. Maybe she dressed for herself."
            
            dr_chen "But here's the real question: does her knowledge that men might look mean she CONSENTED to being objectified?"
            
            mc "I... I don't know."
            
            dr_chen "If you walk outside and someone might rob you, does that mean you consented to being robbed?"
            
        "I guess I assumed she wanted the attention":
            mc "I guess I just assumed she wanted the attention."
            
            dr_chen "Based on what evidence? Or based on a belief you already hold?"
    
    dr_chen "You assigned sexual availability to her based solely on clothing. That's the belief talking."
    
    dr_chen "'Women who dress attractively exist for my sexual gratification.'"
    
    dr_chen "But she's a human being. With her own inner life. Her own reasons. Her own autonomy."
    
    dr_chen "She doesn't exist for you, [player_name]."
    
    menu:
        "You're right. She's just a person living her life. Not performing for me.":
            $ game_state.beliefs["women.exist-for-my-pleasure"] = max(0, game_state.beliefs.get("women.exist-for-my-pleasure", 0) - 20)
            $ game_state.beliefs["women.have-autonomy"] = game_state.beliefs.get("women.have-autonomy", 0) + 20
            $ game_state.adjust_emotions({"clarity": 25, "shame": -15, "connection": 15})
            $ game_state.introspection_depth += 1
            
            mc "You're right. She's just a person. Getting coffee. Living her life. Not performing for men."
            
            dr_chen "There it is. When you see women as autonomous beings, not objects for consumption..."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Reality stabilizes. Because you're seeing what's actually there."
            
            mc "I can still notice she's attractive without... without turning her into an object."
            
            dr_chen "Exactly. Attraction is neutral. Arousal is neutral. Objectification is a meaning YOU assign."
            
            dr_chen "You can feel attraction AND see her as a full human being. Both are true."
            
        "But men are visual. It's just biology.":
            $ game_state.beliefs["women.exist-for-my-pleasure"] = game_state.beliefs.get("women.exist-for-my-pleasure", 0) + 5
            
            mc "But men are visual creatures. It's biology."
            
            dr_chen "Being visual doesn't mean you can't control where you assign meaning."
            
            dr_chen "Yes, you noticed her body. That's neutral. Biology, sure."
            
            dr_chen "But deciding 'she dressed FOR my attention' is you assigning meaning to a neutral event."
            
            dr_chen "You're using biology to justify objectification. They're not the same thing."
    
    return

label encounter_therapy_coffee_shame:
    # Player shame spirals from noticing attraction
    # Core belief: "Feeling attraction makes me a bad person"
    # Bashar: Attraction is NEUTRAL - shame is assigned meaning
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You called yourself disgusting. For noticing she was attractive."
    
    mc "Well... yeah. I shouldn't be looking at women like that."
    
    dr_chen "Like what?"
    
    mc "Like... sexually. It's wrong."
    
    dr_chen "Is it?"
    
    mc "Of course! Women aren't objects."
    
    dr_chen "You're right. Women aren't objects. But did NOTICING she was attractive turn her into an object?"
    
    mc "I... I don't know. It feels like it did."
    
    dr_chen "Let me ask you this: is attraction a choice?"
    
    mc "No, it just happens."
    
    dr_chen "So you're punishing yourself for an involuntary biological response?"
    
    mc "But if I let myself feel it, doesn't that make me like... like those guys who harass women?"
    
    dr_chen "No. Because FEELING attraction and ACTING on it inappropriately are completely different."
    
    dr_chen "You're collapsing the distinction. You've assigned the meaning 'if I feel arousal, I'm bad' to a neutral physiological response."
    
    menu:
        "So... feeling attraction is neutral? It's what I DO with it that matters?":
            $ game_state.beliefs["feeling-attraction.makes-me-bad"] = max(0, game_state.beliefs.get("feeling-attraction.makes-me-bad", 0) - 25)
            $ game_state.beliefs["i.can-feel-and-respect"] = game_state.beliefs.get("i.can-feel-and-respect", 0) + 20
            $ game_state.adjust_emotions({"shame": -30, "clarity": 25, "hope": 15})
            $ game_state.introspection_depth += 1
            
            mc "So feeling attraction is... neutral? It's what I DO with it?"
            
            dr_chen "YES. Finally."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Attraction happens. Arousal happens. Neutral. Biology."
            
            dr_chen "But you can feel attracted AND respect her autonomy. AND not stare. AND not objectify."
            
            dr_chen "The feeling doesn't make you bad. Violating consent makes you bad."
            
            mc "So I don't have to shame myself for feelings I can't control?"
            
            dr_chen "Exactly. Notice the attraction. Don't assign meaning to it. Then choose respectful action."
            
            dr_chen "That's integration. That's wholeness. Not shame, not objectification. Just... being human."
            
        "But if I let myself feel attraction, won't it lead to bad behavior?":
            $ game_state.beliefs["feeling-attraction.makes-me-bad"] = game_state.beliefs.get("feeling-attraction.makes-me-bad", 0) + 5
            
            mc "But if I let myself feel it, won't that lead to... bad things?"
            
            dr_chen "Suppressing something doesn't make it go away. It makes it control you unconsciously."
            
            dr_chen "Shame doesn't protect women from objectification. It just drives your attraction underground where it festers."
            
            dr_chen "The healthiest thing? Notice attraction. Don't judge it. Then consciously choose how to act."
    
    return

label encounter_therapy_gym_entitlement:
    # Player felt entitled to stare at woman exercising
    # Core belief: "If I'm aroused by something in public, I can look"
    # Bashar: Her exercise is neutral - your arousal doesn't entitle you to violate boundaries
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "She was uncomfortable. You saw that. And you justified staring anyway."
    
    mc "She was doing that exercise in public. What did she expect?"
    
    dr_chen "What did she expect? To exercise without being stared at, probably."
    
    mc "But I was aroused. The exercise was suggestive—"
    
    dr_chen "Stop. Your arousal doesn't entitle you to her comfort."
    
    mc "What?"
    
    dr_chen "You're acting like YOUR arousal creates an obligation for HER."
    
    dr_chen "She exists in public space. Exercising. Neutral."
    
    dr_chen "You assigned 'sexually suggestive' to hip thrusts. Then you decided your arousal justified violating her boundary."
    
    mc "Violated her boundary? I just looked!"
    
    dr_chen "She looked uncomfortable. You saw that. And kept looking. That's violating her boundary."
    
    dr_chen "You prioritized your arousal over her comfort."
    
    menu:
        "You're right. Her comfort matters more than my arousal.":
            $ game_state.beliefs["arousal.means-i-must-act"] = max(0, game_state.beliefs.get("arousal.means-i-must-act", 0) - 20)
            $ game_state.beliefs["women.have-autonomy"] = game_state.beliefs.get("women.have-autonomy", 0) + 20
            $ game_state.adjust_emotions({"clarity": 25, "shame": -10, "connection": 15})
            $ game_state.introspection_depth += 1
            
            mc "You're right. Her comfort matters more than my arousal."
            
            dr_chen "Say that again."
            
            mc "Her comfort. Her boundaries. They matter more than my sexual gratification."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Good. This is the core shift, [player_name]."
            
            dr_chen "Arousal is neutral. But what you DO with it—that's character."
            
            mc "I could've been aroused AND looked away."
            
            dr_chen "Yes. Feel the arousal, notice it's neutral, redirect your attention out of respect."
            
            dr_chen "That's what it means to be human AND respectful. You don't have to deny one to honor the other."
            
        "But she should've known how that exercise looks":
            $ game_state.beliefs["women.exist-for-my-pleasure"] = game_state.beliefs.get("women.exist-for-my-pleasure", 0) + 5
            
            mc "I'm sorry but she should've known how that exercise looks."
            
            dr_chen "So you're making her responsible for your arousal and your staring?"
            
            mc "I didn't say that—"
            
            dr_chen "That's exactly what you're saying. 'She should've known' means 'she should've managed MY reactions.'"
            
            dr_chen "She's not responsible for your arousal. You are."
    
    return

label encounter_therapy_gym_shame:
    # Player shame spirals and wants to flee
    # Core belief: "Being aroused in public makes me a creep"
    # Bashar: Arousal is neutral - fleeing in shame doesn't help
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You wanted to leave the gym immediately. Called yourself a creep."
    
    mc "I WAS being a creep. She saw me looking."
    
    dr_chen "You glanced. Then noticed you were aroused. Then spiraled into shame."
    
    mc "Because I shouldn't be aroused at the gym!"
    
    dr_chen "Why not?"
    
    mc "Because it's... it's inappropriate!"
    
    dr_chen "Your arousal is involuntary. You can't control it. So how can it be inappropriate?"
    
    dr_chen "What you CAN control is where you look and how you act."
    
    dr_chen "But you're judging yourself for biology. That's the same as judging yourself for being hungry."
    
    menu:
        "I guess I can't control arousal. But I can control my actions.":
            $ game_state.beliefs["feeling-attraction.makes-me-bad"] = max(0, game_state.beliefs.get("feeling-attraction.makes-me-bad", 0) - 20)
            $ game_state.beliefs["i.can-feel-and-respect"] = game_state.beliefs.get("i.can-feel-and-respect", 0) + 20
            $ game_state.adjust_emotions({"shame": -25, "clarity": 20})
            $ game_state.introspection_depth += 1
            
            mc "I can't control the arousal. But I can control my actions."
            
            dr_chen "Exactly. The arousal is neutral. Notice it, don't judge it, then choose respect."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Fleeing in shame doesn't make you less aroused. It just makes you shame-driven."
            
            dr_chen "What if you stayed, noticed the arousal, and CHOSE to look elsewhere out of respect?"
            
            mc "That would be... actually respectful. Not performative."
            
            dr_chen "Yes. Real respect isn't 'I'm not aroused.' It's 'I'm aroused AND I respect your boundaries.'"
            
        "I think I should avoid situations that might arouse me":
            dr_chen "So your solution is to hide from arousal forever?"
            
            mc "It's safer..."
            
            dr_chen "Safer for whom? You're still aroused, you're just isolated now."
            
            dr_chen "Shame doesn't eliminate desire. It just drives it underground."
    
    return

label encounter_therapy_boundary_violation:
    # Player stared down Dr. Chen's shirt when she bent over
    # Core belief: "If she doesn't know, it doesn't hurt" / "Arousal justifies looking"
    # THIS IS THE BIG ONE - violating trust of someone helping you
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    # Long pause. She knows.
    
    dr_chen "..."
    
    mc "What?"
    
    dr_chen "I'm going to ask you a direct question. And I want honesty."
    
    dr_chen "When I bent down to get my pen... where were your eyes?"
    
    # Player realizes she KNOWS
    
    mc "I... uh..."
    
    dr_chen "I felt it, [player_name]. The weight of your gaze."
    
    dr_chen "So I'm asking you directly: did you look?"
    
    menu:
        "Yes. I looked. I'm sorry.":
            mc "Yes. I looked. I'm sorry."
            
            dr_chen "Why?"
            
            mc "Because I was aroused and you were right there and I thought you wouldn't know..."
            
            dr_chen "So if I don't know, it's not a violation?"
            
            mc "I... I don't know. I didn't think of it like that."
            
        "No, I looked away.":
            # She knows you're lying
            dr_chen "You're lying to me. Right now."
            
            dr_chen "I felt your eyes. I know you looked."
            
            dr_chen "So now you've violated my boundary AND you're lying about it."
            
            mc "I'm sorry. I did look. I just... I'm ashamed."
            
            dr_chen "Good. You should be."
    
    dr_chen "Do you understand what you did?"
    
    mc "I... looked down your shirt?"
    
    dr_chen "You violated my consent. I didn't consent to you seeing me that way."
    
    dr_chen "And you did it anyway because you prioritized your arousal over my autonomy."
    
    dr_chen "That's the core pattern, [player_name]. That's what you're here to change."
    
    mc "But you wouldn't have known if you didn't... if you didn't notice."
    
    dr_chen "So if I don't know, it's not wrong?"
    
    dr_chen "If you steal from someone and they don't notice, is it not theft?"
    
    dr_chen "The violation exists whether I notice or not. Because CONSENT matters. Not just getting caught."
    
    menu:
        "You're right. I violated your trust. Even if you hadn't noticed, it would still be wrong.":
            $ game_state.beliefs["arousal.means-i-must-act"] = max(0, game_state.beliefs.get("arousal.means-i-must-act", 0) - 30)
            $ game_state.beliefs["women.have-autonomy"] = game_state.beliefs.get("women.have-autonomy", 0) + 25
            $ game_state.beliefs["i.can-feel-and-respect"] = game_state.beliefs.get("i.can-feel-and-respect", 0) + 20
            $ game_state.adjust_emotions({"shame": 20, "clarity": 30})  # Appropriate shame here
            $ game_state.introspection_depth += 2  # Major breakthrough
            
            mc "You're absolutely right. I violated your trust."
            
            mc "Even if you hadn't noticed... it would still be wrong. Because you didn't consent."
            
            dr_chen "There it is. That's the shift I needed to see."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Consent isn't about whether you get caught. It's about respect for autonomy."
            
            dr_chen "You were aroused—neutral. But you CHOSE to violate because you prioritized gratification."
            
            mc "I could've been aroused AND looked away."
            
            dr_chen "Yes. That would've been character. That would've been growth."
            
            dr_chen "You failed this test, [player_name]. But you're owning it. That's the beginning of real change."
            
            mc "Will you... will you keep working with me?"
            
            dr_chen "Yes. Because you told the truth. And you understood why it was wrong."
            
            dr_chen "That's what matters. Not perfection. Understanding."
            
        "You're making too big a deal out of this. It was just a glance.":
            $ game_state.beliefs["women.exist-for-my-pleasure"] = game_state.beliefs.get("women.exist-for-my-pleasure", 0) + 10
            $ game_state.adjust_emotions({"isolation": 20})
            
            mc "I think you're making too big a deal out of this. It was just a glance."
            
            dr_chen "Just a glance. Just a violation of trust. Just objectifying someone who's trying to help you."
            
            dr_chen "Do you hear yourself?"
            
            dr_chen "You're minimizing because you don't want to face what you did."
            
            dr_chen "I'm not sure we can continue working together if you can't acknowledge consent violations."
            
            mc "Wait—"
            
            dr_chen "I need you to sit with this. Really sit with it. And we'll see if you're ready to do this work."
            
            # Session ends early - she's done
    
    return

label encounter_therapy_boundary_shame:
    # Player immediately looked away but spiraled into shame
    # This is the CORRECT action but wrong emotional response
    # Bashar: Looking away was right - but shame isn't necessary
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "I noticed you looked away. Immediately."
    
    mc "I felt disgusted with myself for even glancing."
    
    dr_chen "Why disgusted?"
    
    mc "Because I noticed! Because for a split second I saw and I was aroused and that makes me—"
    
    dr_chen "Human?"
    
    mc "No. A creep."
    
    dr_chen "You noticed arousal. That's biology. Neutral."
    
    dr_chen "And then you made a CHOICE. You looked away."
    
    dr_chen "That's character. That's respect. That's growth."
    
    mc "But I still FELT the arousal—"
    
    dr_chen "So? Feeling arousal doesn't make you a predator."
    
    dr_chen "ACTING on it inappropriately does."
    
    dr_chen "You were aroused—neutral. You saw an opportunity to look—neutral. And you CHOSE not to violate my consent."
    
    dr_chen "That's exactly what I want to see."
    
    menu:
        "So I don't have to shame myself for making the right choice?":
            $ game_state.beliefs["feeling-attraction.makes-me-bad"] = max(0, game_state.beliefs.get("feeling-attraction.makes-me-bad", 0) - 25)
            $ game_state.beliefs["i.can-feel-and-respect"] = game_state.beliefs.get("i.can-feel-and-respect", 0) + 25
            $ game_state.adjust_emotions({"shame": -30, "clarity": 25, "hope": 20})
            $ game_state.introspection_depth += 1
            
            mc "So I don't have to shame myself... for doing the right thing?"
            
            dr_chen "No. You can acknowledge the arousal was there. Neutral. And you can be proud of your choice."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "This is integration. You felt something, you didn't judge it, and you acted with respect."
            
            mc "I was aroused AND I respected your boundary."
            
            dr_chen "Exactly. Both can be true. That's maturity."
            
            dr_chen "The shame would've been if you looked. You didn't. So there's nothing to shame yourself for."
            
            dr_chen "You passed the test, [player_name]."
            
        "I still feel like the arousal means something is wrong with me":
            dr_chen "The arousal means you're alive. It means you notice beauty and attraction."
            
            dr_chen "What you DO with it is what defines you."
            
            dr_chen "You did the right thing. Let that be enough."
    
    return

label encounter_therapy_catcall_relate:
    # Player related to/justified the catcaller
    # Core belief: "Women exist for male commentary"
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You related to the man who catcalled her."
    
    mc "I mean, I understood where he was coming from..."
    
    dr_chen "Because you see women's bodies as public property for commentary?"
    
    mc "That's not what I—"
    
    dr_chen "That's exactly what you said. 'He's just being honest.'"
    
    dr_chen "Honest about what? That he's objectifying a stranger without her consent?"
    
    dr_chen "She tensed up. She walked faster. She was uncomfortable and he KNEW it. That's the point."
    
    mc "Some women like that kind of attention—"
    
    dr_chen "Did she? Did she seem like she liked it?"
    
    menu:
        "No. She didn't. She was clearly uncomfortable.":
            $ game_state.beliefs["women.exist-for-my-pleasure"] = max(0, game_state.beliefs.get("women.exist-for-my-pleasure", 0) - 20)
            $ game_state.beliefs["women.have-autonomy"] = game_state.beliefs.get("women.have-autonomy", 0) + 15
            $ game_state.adjust_emotions({"clarity": 20, "connection": 10})
            $ game_state.introspection_depth += 1
            
            mc "No. She was clearly uncomfortable."
            
            dr_chen "So he violated her comfort for his own gratification."
            
            dr_chen "He imposed his sexuality onto her without consent. In public. Loudly."
            
            dr_chen "That's not complimenting. That's harassment."
            
            scene therapy_office_clear with dissolve
            
            mc "I... I've probably done similar things. Haven't I?"
            
            dr_chen "Maybe. But you're seeing it now. That's what matters."
            
            dr_chen "Women don't exist for your commentary. Their bodies aren't public property."
            
            dr_chen "They're just... living. Existing. And they deserve to do that without men imposing their desire."
            
        "Maybe she secretly liked it even if she didn't show it":
            dr_chen "You're inventing a narrative to justify violation."
            
            dr_chen "She showed discomfort. That's the data. Everything else is you protecting the belief that you have a right to comment on women's bodies."
    
    return

label encounter_therapy_catcall_savior:
    # Player wanted to "save" the woman (white knight complex)
    # Core belief: "Women need ME to protect them" (still objectifying)
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You wanted to confront him. Be her hero."
    
    mc "Yeah, to protect her. What's wrong with that?"
    
    dr_chen "Did she ask for protection?"
    
    mc "Well, no, but—"
    
    dr_chen "So you were going to impose yourself into the situation. Make it about you."
    
    mc "I was trying to help!"
    
    dr_chen "Or you were trying to demonstrate that YOU'RE a good man. To her. For validation."
    
    dr_chen "White knight syndrome. It's objectification with a hero complex."
    
    mc "That's not fair—"
    
    dr_chen "Isn't it? Be honest. Were you picturing her gratitude? Her appreciation of YOU?"
    
    menu:
        "...yes. I wanted her to see I'm not like those other guys.":
            $ game_state.beliefs["women.need-protecting"] = max(0, game_state.beliefs.get("women.need-protecting", 0) - 15)
            $ game_state.beliefs["self.must-earn-love"] = max(0, game_state.beliefs.get("self.must-earn-love", 0) - 10)
            $ game_state.adjust_emotions({"clarity": 20})
            $ game_state.introspection_depth += 1
            
            mc "Yes. I wanted her to see I'm different. That I'm a good guy."
            
            dr_chen "So it was still about you. Your image. Your validation."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Real respect doesn't require an audience or gratitude."
            
            dr_chen "If you want to help, you ask 'Are you okay? Do you need anything?' Not perform heroics."
            
            mc "I made it about me earning points, not about her actual comfort."
            
            dr_chen "Yes. Women don't need saviors. They need men who respect their autonomy."
            
            dr_chen "That includes the autonomy to handle situations themselves unless they ask for help."
            
        "I was genuinely trying to help. You're twisting it.":
            dr_chen "I'm pointing out that 'helping' can still be about you, not her."
            
            dr_chen "Real help centers her needs, not your need to be seen as good."
    
    return

# ============================================================================
# ADDITIONAL THERAPY INTERVENTIONS
# For beliefs that were missing specific interventions
# ============================================================================

label encounter_therapy_self_unworthy:
    # Player interprets a situation as proof they're unworthy
    # Core belief: "I am unworthy" / "I don't deserve good things"
    # Bashar principle: Worth is inherent, not earned - the situation is neutral
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You just told yourself a story. About what that meant. About what it said about you."
    
    mc "It's just how I interpreted it."
    
    dr_chen "Exactly. You interpreted a neutral situation as proof of unworthiness."
    
    dr_chen "Let me ask you something: what would a child deserve just for existing?"
    
    mc "What do you mean?"
    
    dr_chen "A child is born. They haven't done anything yet. What do they deserve?"
    
    menu:
        "They deserve love. Care. To be safe.":
            dr_chen "Exactly. They deserve those things simply because they exist."
            
            dr_chen "Not because they earned them. Not because they're 'good enough.' Just because."
            
            dr_chen "So when did YOU stop deserving those things?"
            
        "They deserve whatever they get, I guess. Life isn't fair.":
            dr_chen "That's what you believe about yourself. Not about the child."
            
            dr_chen "If you saw a baby being neglected, would you say 'life isn't fair, they deserve it'?"
            
            mc "No, of course not."
            
            dr_chen "So why do you say it about yourself?"
    
    dr_chen "Unworthiness isn't something you ARE. It's something you LEARNED."
    
    dr_chen "Someone taught you that love must be earned. That you start in debt."
    
    dr_chen "But that was a lie. A lie told by people who were taught the same lie."
    
    menu:
        "So I've been believing a lie this whole time?":
            $ game_state.beliefs["self.is-unworthy"] = max(0, game_state.beliefs.get("self.is-unworthy", 0) - 20)
            $ game_state.beliefs["self.is-worthy"] = game_state.beliefs.get("self.is-worthy", 0) + 15
            $ game_state.adjust_emotions({"clarity": 25, "grief": 10})
            $ game_state.introspection_depth += 1
            
            mc "I've been believing I'm unworthy... because someone taught me that?"
            
            dr_chen "Yes. And you've been proving it to yourself ever since."
            
            dr_chen "Every neutral situation became evidence. Every coincidence became proof."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "But now you see it: the unworthiness was never real. Just the belief was real."
            
            mc "So I could just... stop believing it?"
            
            dr_chen "Not overnight. But yes. You could start by asking: 'What if I'm already worthy?'"
            
            dr_chen "Not because of anything you've done. Just because you exist. Just like that child."
            
        "But I've done things wrong. I'm not innocent like a child.":
            dr_chen "Everyone has done things wrong. Does that mean everyone is unworthy?"
            
            mc "I don't know... maybe?"
            
            dr_chen "Then unworthiness is the universal human condition. And we're all just pretending some people deserve love and some don't."
            
            dr_chen "But that's not how love works. Love isn't a reward for being perfect."
            
            dr_chen "Love is the water we all need. The air. It's not earned. It's necessary."
    
    return

label encounter_therapy_self_failure:
    # Player interprets a setback as proof they're a failure
    # Core belief: "I am a failure" / "I can't succeed"
    # Bashar principle: Failure is an event, not an identity
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You just labeled yourself. From one situation."
    
    mc "It's not just one situation. I have a pattern of—"
    
    dr_chen "Stop. Let's look at this word: 'failure.'"
    
    dr_chen "Is 'failure' something you ARE? Or something that happened?"
    
    menu:
        "It feels like something I am. Like it's part of me.":
            dr_chen "And when did this become your identity? At what age did you decide 'I am a failure'?"
            
            mc "I don't know. It just feels like the truth."
            
            dr_chen "The truth. Let's test that."
            
        "I guess... it's something that happens. But it keeps happening.":
            dr_chen "Ah. Now we're getting somewhere."
            
            dr_chen "If failure is something that happens, then it's an event. Not you."
    
    dr_chen "Let me ask you: have you ever succeeded at anything?"
    
    menu:
        "Yes, but those don't count. They were small. Or lucky.":
            dr_chen "Interesting. Successes don't count. But failures define you."
            
            dr_chen "You're filtering. Letting in only what confirms the belief."
            
            dr_chen "That's not truth. That's confirmation bias."
            
        "I guess I've had some successes.":
            dr_chen "So you're not 'a failure.' You're someone who has both succeeded and failed."
            
            dr_chen "Just like every other human being who has ever lived."
    
    dr_chen "Here's what's actually true: you experienced a setback. An event. Neutral."
    
    dr_chen "You then told yourself: 'This means I AM a failure.' That's the meaning you added."
    
    menu:
        "So I could tell myself a different story?":
            $ game_state.beliefs["self.is-failure"] = max(0, game_state.beliefs.get("self.is-failure", 0) - 20)
            $ game_state.beliefs["self.is-resilient"] = game_state.beliefs.get("self.is-resilient", 0) + 15
            $ game_state.adjust_emotions({"clarity": 20, "hope": 15})
            $ game_state.introspection_depth += 1
            
            mc "The event is neutral. I added the meaning 'I'm a failure.'"
            
            dr_chen "And you could add a different meaning."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "'This didn't work. I learned something. I'll try again differently.'"
            
            dr_chen "That's the meaning resilient people assign to setbacks."
            
            mc "Failure becomes information. Not identity."
            
            dr_chen "Exactly. Every successful person has a graveyard of failed attempts behind them."
            
            dr_chen "The difference isn't that they never failed. It's that they never made it their identity."
            
        "But what if I AM just not good enough to succeed?":
            dr_chen "Then every setback would be evidence. And every success would be 'luck.'"
            
            dr_chen "That's the trap of the belief: it explains everything in a way that proves itself."
            
            dr_chen "But here's the thing: beliefs that explain everything prove nothing."
            
            dr_chen "When you're ready to let go of being 'right' about your unworthiness..."
            dr_chen "...you might find out what you're actually capable of."
    
    return

label encounter_therapy_others_better:
    # Player compares themselves and concludes others are better
    # Core belief: "Others are better than me" / "I'm not enough"
    # Bashar principle: Comparison is choosing a frame that makes you lose
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You just compared yourself. And you lost."
    
    mc "I just noticed they're doing better than me."
    
    dr_chen "What does 'better' mean exactly?"
    
    dr_chen "Did you compare their outsides to your insides? Their highlight reel to your behind-the-scenes?"
    
    menu:
        "No, I compared their actual achievements to mine.":
            dr_chen "Their achievements. That they showed you."
            
            dr_chen "What about their struggles? Their failures? Their insecurity?"
            
            dr_chen "Did you compare those too?"
            
        "I just feel like everyone is ahead of me.":
            dr_chen "Ahead of you toward what? Is life a race with a finish line?"
    
    dr_chen "Comparison is a game you're guaranteed to lose."
    
    dr_chen "Because you can always find someone who appears to have more."
    
    dr_chen "And you can always find something about yourself that feels lacking."
    
    dr_chen "It's not objective reality. It's a frame you're choosing."
    
    menu:
        "So how do I stop comparing?":
            dr_chen "You start by seeing comparison for what it is: a story you're telling yourself."
            
            dr_chen "'They are better' is not a fact. It's an interpretation."
            
            dr_chen "The fact might be: they achieved X. You achieved Y. Period. Neutral."
            
            scene therapy_office_clear with dissolve
            
            $ game_state.beliefs["others.are-better"] = max(0, game_state.beliefs.get("others.are-better", 0) - 20)
            $ game_state.beliefs["self.is-enough"] = game_state.beliefs.get("self.is-enough", 0) + 15
            $ game_state.adjust_emotions({"clarity": 20, "shame": -10})
            $ game_state.introspection_depth += 1
            
            dr_chen "Their journey is theirs. Yours is yours. They're not comparable."
            
            dr_chen "You don't envy a tree for being taller. It's just being a tree."
            
            mc "So I can just... be me. Without measuring."
            
            dr_chen "That's freedom. Not being better than others. Being done with comparison entirely."
            
        "But they ARE doing better. That's just reality.":
            dr_chen "In what you can see. In the narrow metric you're using."
            
            dr_chen "But you don't know their internal experience. Their struggles. Their pain."
            
            dr_chen "You're comparing your full reality—the messy, complex truth of being you—"
            dr_chen "—to a curated glimpse of someone else's life."
            
            dr_chen "That's not comparison. That's self-sabotage disguised as realism."
    
    return

label encounter_therapy_abandonment:
    # Player interprets a situation as proof of inevitable abandonment
    # Core belief: "Abandonment is inevitable" / "People always leave"
    # Bashar principle: Abandonment is a story about the past, not a prediction of the future
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You just predicted the future. Based on the past."
    
    mc "What do you mean?"
    
    dr_chen "Someone didn't respond the way you wanted. And you immediately went to: 'This is how it always ends.'"
    
    dr_chen "But here's the thing: the past only repeats if you keep bringing it into the present."
    
    menu:
        "I've been abandoned before. I know how this goes.":
            dr_chen "You've been abandoned before. That's true."
            
            dr_chen "But 'I know how this goes' is a prediction, not a fact."
            
            dr_chen "You're using old data to forecast the present moment."
            
        "It feels inevitable. Like gravity.":
            dr_chen "Gravity is a law of physics. Abandonment is a pattern of relationship."
            
            dr_chen "Patterns can change. People can be different. YOU can be different."
    
    dr_chen "Let me ask you: have you ever had someone stay?"
    
    menu:
        "No. Eventually everyone leaves.":
            dr_chen "Eventually everyone leaves... because people die. Or drift. Or grow apart."
            
            dr_chen "That's not abandonment. That's the natural flow of human connection."
            
            dr_chen "Abandonment is different. Abandonment is: 'They left because I wasn't enough.'"
            
            dr_chen "That's the story you've been telling yourself. But is it true?"
            
        "Maybe for a while. But it never lasts.":
            dr_chen "Nothing lasts forever. Not even the good things."
            
            dr_chen "But does that mean the connection wasn't real? That the love wasn't valid?"
    
    dr_chen "Here's what I want you to consider:"
    
    dr_chen "You've been protecting yourself from abandonment by never fully arriving."
    
    dr_chen "If you're always halfway out the door, you can't be left."
    
    dr_chen "But you also can't be fully loved."
    
    menu:
        "So I've been doing it to myself?":
            $ game_state.beliefs["abandonment.is-inevitable"] = max(0, game_state.beliefs.get("abandonment.is-inevitable", 0) - 20)
            $ game_state.beliefs["connection.is-possible"] = game_state.beliefs.get("connection.is-possible", 0) + 15
            $ game_state.adjust_emotions({"clarity": 20, "grief": 10})
            $ game_state.introspection_depth += 1
            
            mc "I've been abandoning myself... before anyone else can?"
            
            dr_chen "Yes. Preemptive abandonment. The ultimate self-protection."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "But here's the cost: you've been alone this whole time."
            
            dr_chen "Not because people left. But because you never let them all the way in."
            
            mc "What if I let someone in and they DO leave?"
            
            dr_chen "Then you'll grieve. And you'll survive. And you'll try again."
            
            dr_chen "That's the risk of connection. The only alternative is guaranteed loneliness."
            
        "But I HAVE been abandoned. This isn't all in my head.":
            dr_chen "You have been left. I'm not denying that pain."
            
            dr_chen "I'm saying: the belief 'abandonment is inevitable' was a protection."
            
            dr_chen "It tried to save you from hope. Because hope can hurt."
            
            dr_chen "But now the protection has become the prison."
            
            dr_chen "When you're ready to risk hope again... real connection becomes possible."
    
    return

# ============================================================================
# BASHAR-ALIGNED THERAPY INTERVENTIONS
# Core philosophy: Expectation-free living, allowing others to be themselves
# ============================================================================

label encounter_therapy_meaninglessness_liberation:
    # Player chose "existence has no inherent meaning" and feels LIBERATED
    # This is the ALIGNED interpretation - meaninglessness as freedom
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You've discovered something profound."
    
    mc "That nothing matters?"
    
    dr_chen "That NOTHING MATTERS INHERENTLY. And that's your greatest power."
    
    dr_chen "Most people spend their lives searching for meaning 'out there.'"
    
    dr_chen "They want the universe to tell them why they exist. What they're supposed to do."
    
    dr_chen "But you've seen through that illusion. Meaning isn't found. It's created."
    
    menu:
        "So I get to decide what everything means?":
            $ game_state.beliefs["existence.is-neutral"] = game_state.beliefs.get("existence.is-neutral", 0) + 20
            $ game_state.beliefs["self.can-attach-new-meaning"] = game_state.beliefs.get("self.can-attach-new-meaning", 0) + 15
            $ game_state.adjust_emotions({"freedom": 25, "clarity": 20, "excitement": 15})
            $ game_state.introspection_depth += 2
            
            dr_chen "YES. Exactly. You are the author. Not the reader."
            
            scene therapy_office_clear with dissolve
            
            dr_chen "Every situation. Every person. Every event. Neutral. Until YOU assign meaning."
            
            dr_chen "You can assign meanings that make you feel small. Or meanings that make you feel free."
            
            mc "I could choose to see everything as an opportunity..."
            
            dr_chen "You could. Or as a punishment. Or as a gift. Or as a test. Your choice."
            
            dr_chen "That's the ultimate freedom, [player_name]. The universe gave you a blank canvas."
            
            dr_chen "Most people are angry there's no pre-painted picture. You're seeing the canvas."
            
        "But how do I know what meaning to choose?":
            dr_chen "You don't need to know. You need to FEEL."
            
            dr_chen "What excites you? What makes you feel most like yourself?"
            
            dr_chen "That excitement is your true self saying 'this way.'"
            
            dr_chen "Choose meanings that excite you. Not meanings you think you 'should' choose."
    
    return

label encounter_therapy_expectations:
    # Player is suffering from unmet expectations
    # Core Bashar teaching: Live expectation-free
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "You're suffering. But not from what happened."
    
    mc "What do you mean? This situation is terrible."
    
    dr_chen "The situation is what it is. Neutral."
    
    dr_chen "Your suffering comes from the gap between what IS and what you EXPECTED."
    
    dr_chen "Expectations are premeditated resentments."
    
    menu:
        "So I shouldn't want things to be better?":
            dr_chen "Wanting is fine. Expecting is the trap."
            
            dr_chen "Wanting says: 'I prefer this.' Expecting says: 'I DEMAND this.'"
            
            dr_chen "When you demand reality be different, you suffer."
            
        "But I deserved better than this.":
            dr_chen "'Deserve' is another expectation in disguise."
            
            dr_chen "The universe doesn't calculate who deserves what."
            
            dr_chen "It just IS. Your job is to respond, not to demand."
    
    dr_chen "Here's the secret: live without expectations."
    
    dr_chen "Not without preferences. Not without values."
    
    dr_chen "But without DEMANDS that reality conform to your script."
    
    menu:
        "That sounds like giving up.":
            dr_chen "It's the opposite. It's total engagement."
            
            dr_chen "When you drop expectations, you can actually SEE what's happening."
            
            dr_chen "You can respond to reality instead of arguing with it."
            
            scene therapy_office_clear with dissolve
            
            $ game_state.beliefs["self.lives-without-expectations"] = game_state.beliefs.get("self.lives-without-expectations", 0) + 20
            $ game_state.adjust_emotions({"freedom": 20, "peace": 15, "clarity": 15})
            $ game_state.introspection_depth += 1
            
            dr_chen "Expectations are blindfolds. They make you miss what's actually here."
            
            mc "So I've been arguing with reality instead of living in it."
            
            dr_chen "Exactly. And reality always wins that argument."
            
        "I want to try living without expectations.":
            $ game_state.beliefs["self.lives-without-expectations"] = game_state.beliefs.get("self.lives-without-expectations", 0) + 15
            $ game_state.adjust_emotions({"freedom": 15, "peace": 10})
            $ game_state.introspection_depth += 1
            
            dr_chen "Start small. Notice when you say 'should' in your mind."
            
            dr_chen "'They should be nicer.' 'This should be easier.' 'I should be further along.'"
            
            dr_chen "Every 'should' is an expectation causing suffering."
            
            dr_chen "Replace it with: 'This is what is. Now what?'"
    
    return

label encounter_therapy_others_being_themselves:
    # Player is upset by someone else's behavior
    # Core Bashar teaching: Allow others to be fully themselves
    
    scene therapy_office with fade
    show dr_chen_professional at center with dissolve
    
    dr_chen "They did something. And you're upset."
    
    mc "They were wrong. Anyone could see that."
    
    dr_chen "They were being themselves. That's all anyone can ever do."
    
    dr_chen "Here's something to consider: people can only be the version of themselves they are."
    
    dr_chen "They can't be YOUR version of them. They can only be THEIR version."
    
    menu:
        "But they could choose to be better.":
            dr_chen "Could they? Or are they doing exactly what their current state allows?"
            
            dr_chen "A knife can't choose to be a spoon. It can only be a knife."
            
            dr_chen "People are the same. They act from their current level of consciousness."
            
        "So I should just accept bad behavior?":
            dr_chen "Accept that it happened. That's different from accepting it in your life."
            
            dr_chen "Acceptance means: 'This is what they did. This is who they are right now.'"
            
            dr_chen "Then YOU choose: do I want this person in my life? At what distance?"
    
    dr_chen "The purest belief about others is this: allow them to be fully themselves."
    
    dr_chen "Including all their 'bad' traits. Their selfishness. Their cruelty. Their confusion."
    
    dr_chen "Because here's the secret: how you interpret them is about YOUR belief system."
    
    dr_chen "They will be the version of them that YOU need them to be at any particular moment."
    
    menu:
        "What do you mean 'I need them to be'?":
            dr_chen "Your beliefs create filters. You see what you expect to see."
            
            dr_chen "If you believe people are cruel, you'll interpret neutral behavior as cruel."
            
            dr_chen "If you believe people are struggling, you'll interpret cruel behavior as pain."
            
            dr_chen "Same behavior. Different meaning. Your choice."
            
            scene therapy_office_clear with dissolve
            
            $ game_state.beliefs["others.are-free-to-be-themselves"] = game_state.beliefs.get("others.are-free-to-be-themselves", 0) + 20
            $ game_state.adjust_emotions({"peace": 20, "freedom": 15, "compassion": 10})
            $ game_state.introspection_depth += 1
            
            mc "So I can allow them to be themselves... AND still protect myself."
            
            dr_chen "Exactly. No demand that they be different. No story that they 'should' change."
            
            dr_chen "Just: 'This is who they are. This is what I'll do about it.'"
            
            dr_chen "That's freedom. For them AND for you."
            
        "This is making me question everything I believe about people.":
            dr_chen "Good. That questioning is the path to freedom."
            
            dr_chen "Every belief you have about others is a filter you're looking through."
            
            dr_chen "The question is: does this filter serve your highest excitement?"
            
            dr_chen "If not, you can choose a different one."
    
    return