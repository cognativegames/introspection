init 20 python:
    beliefs["world.is-dangerous"] = {
        "id": "world.is-dangerous",
        "statement": "The world is dangerous and I must be on guard",
        "type": "negative",
        "domain": "safety",
        "deeper": ["self.is-vulnerable", "others.are-threatening"]
    }