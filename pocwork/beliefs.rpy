init 10 python:
    beliefs = {}

    # SELF-WORTH CONFLICT CLUSTER
    
    beliefs["self.is-worthy"] = {
        "id": "self.is-worthy",
        "statement": "I am worthy of love and kindness",
        "type": "positive",
        "domain": "self-worth",
        "conflicts_with": ["self.is-unworthy", "self.must-earn-love", "self.is-fundamentally-flawed"]
    }
    
    beliefs["self.is-unworthy"] = {
        "id": "self.is-unworthy",
        "statement": "I am unworthy of love or good things",
        "type": "negative",
        "domain": "self-worth",
        "absurdity": "high",
        "conflicts_with": ["self.is-worthy", "self.is-capable"],
        "resolution": "self.is-worthy"
    }
    
    beliefs["self.must-earn-love"] = {
        "id": "self.must-earn-love",
        "statement": "I must earn love through achievement or sacrifice",
        "type": "negative",
        "domain": "self-worth",
        "absurdity": "moderate",
        "conflicts_with": ["self.is-worthy", "existence.is-unconditional"],
        "resolution": "self.is-worthy",
        "synthesis": "self.is-worthy-and-striving"  # Can be worthy AND want to grow
    }
    
    # SYNTHESIS BELIEF - transcends the conflict
    beliefs["self.is-worthy-and-striving"] = {
        "id": "self.is-worthy-and-striving",
        "statement": "I am worthy as I am, and I can still choose to grow",
        "type": "positive",
        "domain": "self-worth",
        "note": "Transcends the conflict between unconditional worth and achievement"
    }
    
    # CAPABILITY CONFLICT CLUSTER
    
    beliefs["self.is-capable"] = {
        "id": "self.is-capable",
        "statement": "I am capable of handling challenges",
        "type": "positive",
        "domain": "self-efficacy",
        "conflicts_with": ["self.is-failure", "self.is-fundamentally-flawed"]
    }
    
    beliefs["self.is-failure"] = {
        "id": "self.is-failure",
        "statement": "I am a failure at everything that matters",
        "type": "negative",
        "domain": "self-efficacy",
        "absurdity": "extreme",
        "conflicts_with": ["self.is-capable", "self.is-resilient"],
        "resolution": "self.is-capable",
        "deeper": ["self.is-fundamentally-flawed"]  # This belief supports the failure belief
    }
    
    # WORLDVIEW CONFLICT CLUSTER
    
    beliefs["world.is-safe"] = {
        "id": "world.is-safe",
        "statement": "The world is generally safe and supportive",
        "type": "positive",
        "domain": "world-view",
        "conflicts_with": ["world.is-dangerous", "world.is-hostile"]
    }
    
    beliefs["world.is-dangerous"] = {
        "id": "world.is-dangerous",
        "statement": "The world is fundamentally dangerous and threatening",
        "type": "negative",
        "domain": "world-view",
        "absurdity": "moderate",
        "conflicts_with": ["world.is-safe", "world.is-neutral"],
        "resolution": "world.is-neutral",
        "synthesis": "world.is-complex"
    }
    
    beliefs["world.is-neutral"] = {
        "id": "world.is-neutral",
        "statement": "The world is neutral; it has both danger and safety",
        "type": "positive",
        "domain": "world-view",
        "conflicts_with": ["world.is-hostile"]
    }
    
    # SYNTHESIS - transcends safe vs dangerous
    beliefs["world.is-complex"] = {
        "id": "world.is-complex",
        "statement": "The world contains both beauty and danger, and I can navigate both",
        "type": "positive",
        "domain": "world-view",
        "note": "Acknowledges danger without being consumed by fear"
    }
    
    # RELATIONSHIP CONFLICT CLUSTER
    
    beliefs["others.are-friendly"] = {
        "id": "others.are-friendly",
        "statement": "Most people are generally kind and well-meaning",
        "type": "positive",
        "domain": "relationships",
        "conflicts_with": ["others.are-cruel", "others.are-threatening"]
    }
    
    beliefs["others.are-cruel"] = {
        "id": "others.are-cruel",
        "statement": "People are fundamentally cruel and will hurt me",
        "type": "negative",
        "domain": "relationships",
        "absurdity": "high",
        "conflicts_with": ["others.are-friendly"],
        "resolution": "others.are-complex",
        "deeper": ["self.is-unworthy"]  # "I attract cruelty because I'm unworthy"
    }
    
    beliefs["others.are-threatening"] = {
        "id": "others.are-threatening",
        "statement": "Other people are threats to my safety",
        "type": "negative",
        "domain": "relationships",
        "absurdity": "moderate",
        "conflicts_with": ["others.are-friendly"],
        "resolution": "others.are-complex"
    }
    
    beliefs["others.are-complex"] = {
        "id": "others.are-complex",
        "statement": "People are complex; some are kind, some aren't, and I can discern the difference",
        "type": "positive",
        "domain": "relationships",
        "note": "Realistic view that allows for both trust and boundaries"
    }
    
    # EXISTENCE CONFLICT CLUSTER
    
    beliefs["existence.is-meaningful"] = {
        "id": "existence.is-meaningful",
        "statement": "Life has inherent meaning and purpose",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": ["existence.is-meaningless"]
    }
    
    beliefs["existence.is-meaningless"] = {
        "id": "existence.is-meaningless",
        "statement": "Life is fundamentally meaningless and empty",
        "type": "negative",
        "domain": "existential",
        "absurdity": "extreme",
        "conflicts_with": ["existence.is-meaningful", "self.can-attach-new-meaning"],
        "resolution": "self.can-attach-new-meaning",
        "deeper": ["self.is-unworthy", "world.is-hostile"]
    }
    
    beliefs["self.can-attach-new-meaning"] = {
        "id": "self.can-attach-new-meaning",
        "statement": "I can create meaning through my choices and connections",
        "type": "positive",
        "domain": "existential",
        "conflicts_with": [],  # Doesn't conflict - it transcends the meaning debate
        "note": "Synthesis of meaningless vs meaningful - personal agency over meaning"
    }
    
    # VULNERABILITY CONFLICT
    
    beliefs["self.is-vulnerable"] = {
        "id": "self.is-vulnerable",
        "statement": "I am vulnerable and can be hurt",
        "type": "neutral",  # Not inherently negative!
        "domain": "self-awareness",
        "conflicts_with": ["self.is-invulnerable"],
        "note": "Can coexist with resilience - vulnerability ≠ weakness"
    }
    
    beliefs["self.is-resilient"] = {
        "id": "self.is-resilient",
        "statement": "I can recover from setbacks and pain",
        "type": "positive",
        "domain": "self-efficacy",
        "conflicts_with": ["self.is-fundamentally-flawed"],
        "synthesis_with": "self.is-vulnerable",  # Can be both vulnerable AND resilient
        "synthesis": "self.is-vulnerable-and-resilient"
    }
    
    beliefs["self.is-vulnerable-and-resilient"] = {
        "id": "self.is-vulnerable-and-resilient",
        "statement": "I can be hurt, and I can heal. Both are true.",
        "type": "positive",
        "domain": "integration",
        "note": "The integration of vulnerability and strength"
    }

# COMMON CONFLICT PATTERNS TO MODEL

# Pattern 1: Self-worth conditional vs unconditional
# Conflict: "I must earn love" vs "I am worthy as I am"
# Synthesis: "I am worthy and I can still grow"

# Pattern 2: World as hostile vs safe
# Conflict: "World is dangerous" vs "World is safe"
# Synthesis: "World is complex - I can handle both"

# Pattern 3: People as threats vs friends
# Conflict: "Others are cruel" vs "Others are kind"
# Synthesis: "People are complex - I can discern"

# Pattern 4: Life as meaningless vs meaningful
# Conflict: "Nothing matters" vs "Everything matters"
# Synthesis: "I create meaning through choice"

# Pattern 5: Self as broken vs capable
# Conflict: "I'm fundamentally flawed" vs "I'm capable"
# Resolution: Examine the "flawed" belief, replace with "I'm human and learning"