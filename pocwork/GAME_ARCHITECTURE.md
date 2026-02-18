# INTROSPECTION - COMPLETE GAME ARCHITECTURE

## Core Philosophy
**Everyone uses the same engine: Player, NPCs, and their interactions all run on beliefs → emotions → behavior**

---

## WHAT YOU HAVE NOW

### 1. Belief System ✓
**Location**: `/core/context/beliefs/`

- Structured belief definitions
- Positive, negative, and neutral beliefs
- Conflict definitions
- Resolution and synthesis paths
- Shared by player AND NPCs

### 2. Game State ✓
**Location**: `/core/models/GameState/`

- Tracks player's beliefs (id → intensity)
- Tracks emotions (0-100 scale)
- Relationships with NPCs
- Introspection depth
- Belief history
- Achievement system

### 3. NPC System ✓ (NEW)
**Location**: Your game + npc_system.rpy

- Each NPC has same structure as player
- Own beliefs, emotions, memories
- Interpret player actions through their lens
- Remember events
- Decide what to share in therapy

### 4. Encounter Loop ✓
**Location**: encounter_loop_system.rpy

- Emotion-driven scenario selection
- Interpretation → belief activation → consequences
- Conflict detection
- Introspection opportunities
- Resolution pathways

### 5. Conflict System ✓
**Location**: belief_conflict_system.rpy

- Auto-detects contradictory beliefs
- Applies emotional distress
- Offers resolution paths
- Synthesis for transcendence
- Works for player AND NPCs

### 6. Dynamic Dialogue ✓ (NEW)
**Location**: npc_dialogue_system.rpy

- NPC responses based on emotional state
- Conditional dialogue options
- Memory-driven confrontations
- Group therapy system
- Apology and accountability mechanics

---

## WHAT'S LEFT TO BUILD

### 1. Content Creation (BIGGEST TASK)

**Story Chapters**
- [ ] Chapter 1: Hospital awakening (you have this)
- [ ] Chapter 2-5: Main story beats
- [ ] Character introductions
- [ ] Major plot events
- [ ] Climax and resolution

**Encounter Library**
- [ ] 30-50 encounters covering all belief domains
- [ ] Mix of difficulty levels (simple → complex)
- [ ] Tag appropriately (calming, stressful, etc.)
- [ ] Test all interpretation paths

**Therapy Sessions**
- [ ] 5-10 structured therapy sessions
- [ ] Initial belief establishment
- [ ] Mid-game check-ins
- [ ] Final integration session

**Group Therapy Scenes**
- [ ] 8-12 group sessions
- [ ] NPC story arcs
- [ ] Player accountability moments
- [ ] Healing and growth beats

**NPC Definitions**
- [ ] 5-8 major NPCs with full backstories
- [ ] Starting beliefs for each
- [ ] Trauma histories
- [ ] Growth arcs
- [ ] Relationships with each other

### 2. Visual Assets

**Backgrounds**
- [ ] Hospital rooms (multiple variations for reality shifts)
- [ ] Therapy office
- [ ] Introspection spaces (abstract, clear, conflicted, deep)
- [ ] Story locations (home, café, park, etc.)
- [ ] Reality distortion versions

**Character Sprites**
- [ ] Player character (optional, can be first-person)
- [ ] Dr. Chen (therapist)
- [ ] 5-8 NPCs (multiple expressions each)
  - Neutral, happy, sad, angry, anxious, defensive, open, etc.

**UI Elements**
- [ ] Belief/emotion display screens
- [ ] Conflict visualization
- [ ] Memory/journal interface
- [ ] Achievement notifications

**Visual Effects**
- [ ] Reality shift effects (glitch, flash, distortion)
- [ ] Clarity effects (harmonic, clear, stable)
- [ ] Conflict visualization (split screen, dissonance)
- [ ] Healing moments (light, integration)

### 3. Audio

**Music**
- [ ] Main theme
- [ ] Therapy/introspection ambient
- [ ] Deep introspection
- [ ] Story scenes (neutral)
- [ ] Tense moments
- [ ] Resolution/healing moments

**Sound Effects**
- [ ] Reality glitch sounds (multiple levels)
- [ ] Soft harmonic (clarity)
- [ ] Dissonance (conflict)
- [ ] Resolution chime
- [ ] Heartbeat (anxiety)
- [ ] Gentle sounds (calm)

### 4. Polish & Integration

**UI/UX**
- [ ] Main menu
- [ ] Settings screen
- [ ] Save/load system
- [ ] Skip/rollback configuration
- [ ] Accessibility options (text size, contrast, etc.)

**Tutorial/Onboarding**
- [ ] Explain belief system to player
- [ ] Teach introspection mechanics
- [ ] Introduce conflict system gradually
- [ ] Tooltip system for complex concepts

**Transitions**
- [ ] Smooth chapter transitions
- [ ] Story ↔ encounter loop integration
- [ ] Time passage indicators
- [ ] Emotional state transitions

### 5. Systems Integration

**Achievement System**
- [ ] Define achievements
  - "Resolved first core belief"
  - "Helped NPC in therapy"
  - "Took accountability"
  - "Found synthesis"
  - etc.
- [ ] Hook into existing check_achievements()

**Journal/Memory System**
- [ ] Player can review their belief history
- [ ] See resolved vs active beliefs
- [ ] Review key memories/events
- [ ] Track relationship status with NPCs

**Endings System**
- [ ] Multiple endings based on:
  - Beliefs resolved
  - Relationships healed
  - Introspection depth
  - Actions taken
- [ ] 3-5 distinct endings

### 6. Testing & Balancing

**Belief Balance**
- [ ] Test all conflict pairs
- [ ] Ensure resolution paths work
- [ ] Verify synthesis beliefs feel earned
- [ ] Check intensity progression feels right

**Emotional Balance**
- [ ] Emotion shifts feel proportional
- [ ] Overwhelm doesn't spike too easily
- [ ] Anxiety manageable
- [ ] Hope/clarity achievable

**Encounter Balance**
- [ ] Distribution across belief domains
- [ ] Difficulty curve appropriate
- [ ] Not too many/few of each tag
- [ ] Router selects appropriately

**NPC Balance**
- [ ] Each NPC has distinct belief profile
- [ ] Growth arcs feel authentic
- [ ] Reactions are consistent with beliefs
- [ ] Therapy moments land emotionally

---

## REUSABLE ENGINE COMPONENTS

### What's Universal:

1. **Belief Activation**
   ```python
   entity.activate_belief(belief_id, intensity)
   ```
   Works for player, all NPCs, same code

2. **Emotion Management**
   ```python
   entity.adjust_emotions({emotion: change})
   ```
   Same for everyone

3. **Conflict Detection**
   ```python
   entity.detect_belief_conflicts()
   ```
   Same algorithm for all

4. **Interpretation**
   ```python
   entity.interpret_action(action_type, context)
   ```
   Each entity filters through their beliefs

5. **Memory**
   ```python
   entity.remember_event(type, other, description, impact)
   ```
   Everyone stores memories the same way

### What's Specific:

1. **Encounter Selection** - Only for encounter loop
2. **Therapy Topics** - Only NPCs decide to share
3. **Story Choices** - Only player makes these
4. **Dialogue Generation** - Based on NPC state but manually written

---

## DEVELOPMENT PRIORITY

### Phase 1: Core Content (NOW)
1. Define 5-8 major NPCs with beliefs
2. Write 20 core encounters
3. Outline main story chapters
4. Create basic visual placeholders

### Phase 2: Integration
5. Wire story to encounter loop
6. Implement group therapy system
7. Add NPC dialogue variations
8. Test belief/conflict flow

### Phase 3: Expansion
9. Add remaining encounters (30-50 total)
10. Flesh out all NPCs
11. Write all story chapters
12. Create all variations

### Phase 4: Polish
13. Professional art
14. Music/sound
15. UI/UX refinement
16. Testing and balancing

### Phase 5: Finishing
17. Endings
18. Achievements
19. Accessibility
20. Release prep

---

## WHAT YOU'RE MISSING (Technical)

### Small Gaps:

1. **Reality Shift Visual System**
   - Need actual scene definitions for shifts
   - Currently just labels, need backgrounds

2. **Overlay/Visual Effects**
   - `conflict_overlay`, `clarity_overlay` etc.
   - Can be simple colored screens initially

3. **Character Display Names**
   - Map npc_id to display names
   - Handle pronouns

4. **Scene Backgrounds**
   - Link encounter scenes to actual .png files
   - Create fallbacks

5. **Music/Sound Hooks**
   - Actual audio files
   - Volume controls

### Medium Gaps:

1. **Save/Load Integration**
   - Ensure all state persists correctly
   - Test belief/emotion persistence

2. **Gallery/Journal UI**
   - Screen definitions for reviewing history
   - Belief tree visualization

3. **Skip/Rollback Handling**
   - Some scenes shouldn't be rollback-able
   - Encounter choices should be final

4. **Tutorial System**
   - Gradual introduction of concepts
   - Help screens

### No Gaps:

1. Core engine - Complete ✓
2. Belief system - Complete ✓
3. NPC system - Complete ✓
4. Conflict detection - Complete ✓
5. Dialogue framework - Complete ✓

---

## ESTIMATED WORK REMAINING

### Programming: ~10-15%
- Small integrations
- UI screens
- Polish and testing

### Content Writing: ~60-70%
- Story dialogue
- Encounter descriptions
- NPC characterization
- Therapy sessions

### Art/Audio: ~20-30%
- Character sprites
- Backgrounds
- UI elements
- Music/SFX

---

## CRITICAL PATH

**To get to "playable alpha":**

1. ✓ Core systems (DONE)
2. Define 5 NPCs with beliefs
3. Write 15 core encounters
4. Write Chapter 1 + 2 story
5. Create 3 group therapy scenes
6. Basic placeholder art
7. Wire it all together
8. Test one complete playthrough

**That's probably 40-60 hours of work from where you are now.**

After that, it's expansion:
- More encounters
- More chapters
- More NPCs
- Better art
- Music
- Polish

---

## WHAT I CAN HELP WITH NEXT

1. **NPC Definitions** - Help create 5-8 NPCs with:
   - Background/trauma
   - Starting beliefs
   - Growth arcs
   - Relationships

2. **Encounter Templates** - Create 20-30 encounters:
   - Covering all belief domains
   - Various difficulty levels
   - Proper tags

3. **Story Outline** - Structure the narrative:
   - Chapter breakdown
   - Key plot points
   - Integration with encounter loop
   - Ending variations

4. **Integration Code** - Wire together:
   - Story → encounters → therapy loop
   - NPC appearance triggers
   - Memory callbacks

5. **Testing Framework** - Help create:
   - Belief progression tests
   - Emotional balance checks
   - Encounter distribution
   - NPC behavior verification

**What do you want to tackle first?**
