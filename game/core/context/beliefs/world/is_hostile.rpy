init 20 python:
    beliefs["world.is-hostile"] = {
        "id": "world.is-hostile",
        "statement": "The world is hostile and completely against me.",
        "type": "negative",
        "domain": "safety",
        "deeper": ["existence.is-meaningless"],
        "resolution": "world.is-neutral"
    }