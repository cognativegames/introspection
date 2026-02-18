label therapy_session_1:
    # This integrates with your GameState belief system in /core/context/beliefs/
    
    scene therapy_room with fade
    show therapist_normal at center with dissolve
    
    therapist "Good morning, [player_name]. How did you sleep?"
    
    therapist "Today we're going to do something that might seem strange, but I promise it has a purpose."
    
    therapist "I'm going to describe some scenarios to you. Hypothetical situations. And I want you to tell me how you'd respond."
    
    mc "What's this for?"
    
    therapist "You don't remember who you were before the injury. But your values, your beliefs about the world... those are still in there somewhere."
    
    therapist "We're going to help you find them, and then we're going to build a framework around them."
    
    mc "Okay. I'm ready."
    
    therapist "Let's start with something simple."
    
    # SCENARIO 1: Self-worth
    therapist "Imagine you're at a party. Someone criticizes you in front of everyone. Says something hurtful about who you are."
    
    therapist "What's your immediate reaction?"
    
    menu:
        "They're right. I am fundamentally flawed.":
            $ game_state.activate_belief("self.is-fundamentally-flawed", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.is-unworthy", BELIEF_INTENSITY_SURFACE)
            
            mc "They're probably right. I must have done something to deserve that."
            
            therapist "So when someone criticizes you, you automatically assume it's true?"
            
            mc "Usually, yes."
            
            therapist "That's a belief we'll want to examine closely. The idea that you're fundamentally flawed."
            
        "They're being cruel, but maybe there's some truth to it.":
            $ game_state.activate_belief("self.is-vulnerable", BELIEF_INTENSITY_SURFACE)
            $ game_state.activate_belief("others.are-cruel", BELIEF_INTENSITY_SURFACE)
            
            mc "I'd feel hurt. Maybe defensive. Wonder if they're seeing something I don't."
            
            therapist "You're open to criticism but it affects you emotionally. You believe you're vulnerable."
            
        "That's their problem, not mine. I know my worth.":
            $ game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.is-resilient", BELIEF_INTENSITY_SURFACE)
            
            mc "I'd be annoyed, but I wouldn't internalize it. People project their issues onto others all the time."
            
            therapist "Interesting. You have a strong sense of self-worth that doesn't collapse under criticism."
            
            mc "I've learned that what people say about me usually says more about them."
            
            therapist "That's a healthy belief. A protective one."
    
    # SCENARIO 2: World view
    therapist "Next scenario. You're walking alone at night and see someone approaching. What do you think?"
    
    menu:
        "They might hurt me. The world is dangerous.":
            $ game_state.activate_belief("world.is-dangerous", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("others.are-threatening", BELIEF_INTENSITY_SURFACE)
            
            mc "I'm on alert immediately. Calculating escape routes. Preparing for threat."
            
            therapist "You see the world as fundamentally dangerous. Others as potential threats."
            
            mc "Better safe than sorry."
            
            therapist "That belief protects you, but it also isolates you. We'll explore that."
            
        "They're probably just going about their business.":
            $ game_state.activate_belief("world.is-neutral", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("others.are-friendly", BELIEF_INTENSITY_SURFACE)
            
            mc "Most people are just living their lives. Not everyone is a threat."
            
            therapist "You see the world as relatively neutral. People as generally benign."
            
            mc "Most of the time, yeah."
            
        "I don't know. It depends.":
            $ game_state.activate_belief("world.is-neutral", BELIEF_INTENSITY_SURFACE)
            
            mc "I'd assess the situation. How they're walking, body language, context."
            
            therapist "You're pragmatic. You don't assume danger or safety—you evaluate."
    
    # SCENARIO 3: Meaning and existence
    therapist "Last one for today. Why do you think you're here? What makes life meaningful?"
    
    menu:
        "Nothing, really. Existence is meaningless.":
            $ game_state.activate_belief("existence.is-meaningless", BELIEF_INTENSITY_ACTIVE)
            
            mc "We're just... here. There's no grand purpose. We're born, we live, we die."
            
            therapist "You believe existence has no inherent meaning."
            
            mc "Does it?"
            
            therapist "That's for you to decide. But that belief—if held too tightly—can lead to hopelessness."
            
        "Life has whatever meaning I give it.":
            $ game_state.activate_belief("self.can-attach-new-meaning", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("existence.is-unconditional", BELIEF_INTENSITY_SURFACE)
            
            mc "There's no universal meaning, but I can create my own. Find what matters to me."
            
            therapist "You believe you have agency over meaning. That's powerful."
            
            mc "It's the only thing that makes sense to me."
            
        "I'm here to help others. To make things better.":
            $ game_state.activate_belief("self.can-attach-positive-meaning", BELIEF_INTENSITY_ACTIVE)
            $ game_state.activate_belief("self.is-capable", BELIEF_INTENSITY_SURFACE)
            
            mc "I think we're meant to ease suffering. To leave things better than we found them."
            
            therapist "A belief in service. In contribution. That gives you direction."
    
    # Wrap up session 1
    therapist "These are your foundational beliefs, [player_name]. The core of how you see yourself, others, and the world."
    
    therapist "Over the next few sessions, we'll refine them. Examine them. See which ones serve you and which ones hold you back."
    
    therapist "But here's what you need to understand: when you act in alignment with these beliefs, reality will feel stable. Solid."
    
    # Visual demonstration - world becomes clearer
    play sound "soft_harmonic.mp3"
    show therapist_normal_clear with dissolve
    scene therapy_room_clear with dissolve
    
    "The room sharpens. Everything becomes more vivid, more real."
    
    mc "It's clearer. Everything is clearer."
    
    therapist "Yes. Because you're building structure. Your mind has something to anchor to."
    
    therapist "But when you act *against* your beliefs—when you betray your own values—you'll feel it. Immediately."
    
    therapist "The world will shift. You'll experience pain. Disorientation."
    
    # Minor glitch demonstration
    play sound "reality_glitch.mp3"
    show therapist_normal_blur with dissolve
    
    "The room wavers slightly."
    
    therapist "Like that. Your brain telling you: this doesn't align. This isn't who you are."
    
    # Stabilize
    play sound "soft_harmonic.mp3"
    show therapist_normal_clear with dissolve
    scene therapy_room_clear with dissolve
    
    therapist "So the path forward is this: Know your beliefs. Act in alignment with them."
    
    therapist "And when you slip—when you make mistakes—pause. Reflect. Introspect."
    
    mc "And if I want to change a belief?"
    
    therapist "Then you examine it. Really examine it. See if it serves you. And if it doesn't..."
    
    therapist "You can consciously choose to resolve it. To replace it with something healthier."
    
    therapist "But that takes time. Awareness. Honesty with yourself."
    
    mc "This is a lot."
    
    therapist "It is. But you're already doing it. Every choice you just made came from somewhere deep inside you."
    
    therapist "We're just making the implicit explicit."
    
    # End therapy session 1
    scene black with fade
    
    return
