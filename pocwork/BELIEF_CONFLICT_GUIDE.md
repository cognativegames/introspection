# BELIEF CONFLICT SYSTEM GUIDE

## The Core Insight

**Suffering comes from conflicting beliefs, not from single beliefs.**

Example:
- Believing "I'm unworthy" alone = sad, but stable
- Believing "I'm unworthy" AND "I deserve love" = PAINFUL CONFLICT

This is cognitive dissonance - the psychological discomfort from holding contradictory beliefs.

---

## How Conflicts Work

### 1. Belief Definition (in belief files)

```python
beliefs["self.is-worthy"] = {
    "id": "self.is-worthy",
    "statement": "I am worthy of love and kindness",
    "type": "positive",
    "conflicts_with": ["self.is-unworthy", "self.must-earn-love"],
    "resolution": None  # This is the resolved state
}

beliefs["self.is-unworthy"] = {
    "id": "self.is-unworthy",
    "statement": "I am unworthy of love or good things",
    "type": "negative",
    "conflicts_with": ["self.is-worthy", "self.is-capable"],
    "resolution": "self.is-worthy"  # This resolves to worthy
}
```

### 2. Conflict Detection (automatic)

When beliefs are activated, the system:
1. Checks `conflicts_with` field
2. Sees if conflicting belief is also active (≥ SURFACE)
3. Calculates severity based on intensities
4. Applies emotional consequences

```python
# Player activates "I'm worthy" at ACTIVE level
game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)

# But they already have "I'm unworthy" at CORE level
# System detects: CONFLICT!
# Severity = min(ACTIVE, CORE) = ACTIVE
# Distress = 15 points anxiety, 12 overwhelm, -10 clarity
```

### 3. Emotional Consequences

**Conflict Distress by Severity:**

| Severity | Anxiety | Overwhelm | Clarity Loss |
|----------|---------|-----------|--------------|
| SURFACE  | +8      | +6        | -5           |
| ACTIVE   | +15     | +12       | -9           |
| CORE     | +25     | +20       | -15          |

**Multiple conflicts stack** (up to caps)

---

## Conflict Patterns

### Pattern 1: Self-Worth Conflict
**Common setup:**
- Player has "I'm unworthy" from past trauma (CORE)
- Therapy/encounters activate "I'm worthy" (ACTIVE)
- **CONFLICT**: Both active at once

**Emotional result:**
- High anxiety (wanting to believe worthy, but can't)
- Overwhelm (two truths fighting)
- Low clarity (which is real?)

**Resolution paths:**
1. Examine "unworthy" belief → resolve → accept "worthy"
2. Examine both → transcend to synthesis
3. Ignore → distress persists

### Pattern 2: World-View Conflict
**Common setup:**
- "World is dangerous" (CORE - from trauma)
- "World is safe" (SURFACE - new experience)
- **CONFLICT**

**Why this happens:**
One positive experience doesn't immediately erase years of danger

**Resolution:**
Often synthesis: "World is complex - I can handle both"

### Pattern 3: Capability Conflict
**Common setup:**
- "I'm a failure" (ACTIVE - recent setback)
- "I'm capable" (ACTIVE - also true sometimes)
- **CONFLICT**

**This is realistic:**
People ARE capable in some areas and struggle in others

**Resolution:**
Nuanced belief: "I'm capable in X, learning in Y"

---

## When Conflicts Appear

### Automatic Triggers:
1. **After interpretation choice** - `apply_conflict_consequences()` called
2. **If total distress > 10** - Conflict shown to player
3. **If severity ≥ ACTIVE** - Full conflict sequence offered

### Manual Triggers:
```renpy
# Check if conflict exists
python:
    conflicts = game_state.detect_belief_conflicts()
    if conflicts:
        # Do something

# Force conflict display
call show_belief_conflict

# Go straight to resolution
call introspect_conflict
```

---

## Player Experience Flow

### Low Introspection Depth (0-2):
Player is **unaware** of conflicts
- Conflicts create distress (anxiety, overwhelm)
- Player doesn't know why they feel bad
- No resolution offered yet
- **Just suffers the cognitive dissonance**

### Medium Depth (3-4):
Player **notices** conflicts
- "Part of me believes X, but I also believe Y"
- Can observe the contradiction
- Offered chance to examine
- May not resolve yet

### High Depth (5+):
Player **works with** conflicts
- Sees conflicts as information
- Can choose which belief to keep
- Can find synthesis
- May see conflict warnings before choices

---

## Implementing Conflicts in Your Beliefs

### Step 1: Identify Conflict Pairs

Common conflicts:
- Worthy ↔ Unworthy
- Capable ↔ Failure
- Safe ↔ Dangerous
- Friendly ↔ Cruel
- Meaningful ↔ Meaningless
- Vulnerable ↔ Invulnerable

### Step 2: Add `conflicts_with` Field

```python
beliefs["my-belief"] = {
    "id": "my-belief",
    "statement": "...",
    "conflicts_with": ["belief-id-1", "belief-id-2"],
    # ... other fields
}
```

**Rules:**
- Add conflicts to BOTH beliefs (A conflicts B, B conflicts A)
- List ALL significant conflicts
- Conflicts can be across domains

### Step 3: Add Resolution Path (for negatives)

```python
beliefs["negative-belief"] = {
    "id": "negative-belief",
    "statement": "...",
    "type": "negative",
    "conflicts_with": ["positive-belief"],
    "resolution": "positive-belief"  # What replaces this
}
```

### Step 4: Add Synthesis (optional, advanced)

```python
beliefs["binary-belief-a"] = {
    "id": "binary-belief-a",
    "conflicts_with": ["binary-belief-b"],
    "synthesis": "integrated-belief"  # Third option
}

beliefs["binary-belief-b"] = {
    "id": "binary-belief-b",
    "conflicts_with": ["binary-belief-a"],
    "synthesis": "integrated-belief"  # Same synthesis
}

beliefs["integrated-belief"] = {
    "id": "integrated-belief",
    "statement": "I can hold both truths in balance",
    "type": "positive",
    "note": "Transcends the binary"
}
```

---

## Conflict Resolution Options

### Option 1: Choose One Belief
Player picks which feels more true, other is examined/resolved

```renpy
"Belief A feels true. Belief B is the lie."
    $ game_state.resolve_belief("belief-b")
    $ game_state.beliefs["belief-a"] = BELIEF_INTENSITY_CORE
```

**Emotional effect:** Clarity +20, anxiety -15

### Option 2: Transcend via Synthesis
Player finds a third belief that includes both truths

```renpy
"What if both have truth in them?"
    $ game_state.resolve_belief("belief-a")
    $ game_state.resolve_belief("belief-b")
    $ game_state.activate_belief("synthesis-belief", BELIEF_INTENSITY_ACTIVE)
```

**Emotional effect:** Clarity +30, hope +25, huge reduction in distress

### Option 3: Neither is True
Player sees both as constructs

```renpy
"Neither feels completely true."
    $ game_state.beliefs["belief-a"] = BELIEF_INTENSITY_EXAMINED
    $ game_state.beliefs["belief-b"] = BELIEF_INTENSITY_EXAMINED
```

**Emotional effect:** Clarity +20, introspection_depth +2

### Option 4: Not Ready Yet
Conflict persists but intensity may reduce

```renpy
"I can't tell yet. This is too confusing."
    # Beliefs marked as EXAMINED but not resolved
    # Distress continues but player is aware
```

---

## Design Considerations

### What Makes a Good Conflict?

**DO create conflicts that:**
✓ Reflect real psychological tensions
✓ Have clear emotional stakes
✓ Offer multiple resolution paths
✓ Feel personal and resonant

**DON'T create conflicts that:**
✗ Are just semantic differences
✗ Have obvious "right" answers
✗ Lack emotional impact
✗ Can't be resolved or synthesized

### Example: Good Conflict
```
"I must be perfect to be loved" 
    vs 
"I am worthy as I am"

- Clear tension
- Emotionally charged
- Multiple resolutions possible
- Relatable
```

### Example: Poor Conflict
```
"Apples are fruit"
    vs
"Oranges are fruit"

- No real conflict
- No emotional stakes
- Not personal
```

---

## Integration with Encounter Loop

### In Encounter Files:

```python
encounters["example"] = {
    "interpretations": [
        {
            "display": "I'm worthy of kindness",
            "activates": ["self.is-worthy"],
            # This will auto-conflict with "self.is-unworthy" if active
        },
        {
            "display": "I don't deserve this",
            "activates": ["self.is-unworthy"],
            # This will auto-conflict with "self.is-worthy" if active
        }
    ]
}
```

### In show_interpretation_consequence:

```renpy
# Conflicts automatically detected after beliefs activated
call show_interpretation_consequence
    # Calls apply_conflict_consequences()
    # Shows conflicts if distress > 10
    # Offers resolution if severe enough
```

### In Introspection:

```renpy
call introspect_conflict
    # Shows most severe conflict
    # Offers resolution paths
    # Applies emotional healing if resolved
```

---

## Advanced: Nested Conflicts

Some beliefs support other beliefs (the `deeper` field):

```python
beliefs["self.is-failure"] = {
    "deeper": ["self.is-fundamentally-flawed"]
}
```

When player resolves "failure," you can:

```renpy
python:
    # Check if deeper beliefs should also be questioned
    failed_belief = beliefs["self.is-failure"]
    
    if "deeper" in failed_belief:
        for deeper_id in failed_belief["deeper"]:
            if game_state.beliefs.get(deeper_id, 0) >= BELIEF_INTENSITY_ACTIVE:
                # Offer to examine this too
                renpy.say(None, f"This makes you wonder about: {beliefs[deeper_id]['statement']}")
```

This creates **cascading insight** - resolving one belief reveals deeper ones.

---

## Testing Conflicts

### Debug Commands:

```python
# Show all active conflicts
conflicts = game_state.detect_belief_conflicts()
for b1, b2, severity in conflicts:
    print(f"CONFLICT: {b1} vs {b2} (severity: {severity})")

# Check specific conflict
will_conflict = will_create_conflict(["self.is-worthy"])
print(f"Will create conflict: {will_conflict}")

# Force a conflict for testing
game_state.activate_belief("self.is-worthy", BELIEF_INTENSITY_ACTIVE)
game_state.activate_belief("self.is-unworthy", BELIEF_INTENSITY_CORE)
call show_belief_conflict
```

### What to Test:

- [ ] Do conflicts appear when expected?
- [ ] Is distress amount appropriate?
- [ ] Can player resolve via all paths?
- [ ] Does synthesis feel earned?
- [ ] Do emotions shift appropriately?
- [ ] Can player ignore if not ready?

---

## Common Questions

**Q: Should every belief have conflicts?**
A: No. Only beliefs that oppose each other. "I like apples" doesn't conflict with "I like oranges"

**Q: Can positive beliefs conflict?**
A: Rarely. Usually it's negative vs positive or extreme vs moderate. But yes, if they're mutually exclusive.

**Q: How many conflicts per belief?**
A: 1-3 is good. More than that gets overwhelming.

**Q: Should conflicts always be resolvable?**
A: No. Some tensions are permanent (vulnerable AND resilient). That's synthesis, not resolution.

**Q: What if player never resolves conflicts?**
A: They suffer high anxiety/overwhelm. Game can adapt by offering grounding encounters. Don't force it.

**Q: Can conflicts re-emerge after resolution?**
A: Yes! Old beliefs can reactivate under stress. That's realistic. Mark them as EXAMINED not DORMANT.

---

## Summary

Conflicts are the **heart of the therapeutic journey**:

1. Player develops negative beliefs (often CORE)
2. New experiences activate positive beliefs (SURFACE/ACTIVE)
3. **CONFLICT** creates distress
4. Player must **examine and choose**
5. Resolution brings **clarity and healing**

This models real therapy:
- Old patterns vs new insights
- Cognitive dissonance as growth opportunity
- Integration as the goal

The suffering isn't from having negative beliefs.
**It's from believing two contradictory things at once.**
