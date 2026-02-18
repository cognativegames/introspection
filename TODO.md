# INTROSPECTION - GitHub Issue Tickets

---

## EPIC 1: CORE SYSTEMS & ENGINE (Milestone 1)

### Issue #1: Set Up RenPy Project Structure
**Labels:** `setup`, `infrastructure`, `priority-critical`  
**Effort:** 2 hours  
**Dependencies:** None

**Description:**
Initialize the RenPy project with proper directory structure for scripts, images, audio, and game data.

**Acceptance Criteria:**
- [ ] RenPy project created and launches successfully
- [ ] Directory structure matches specification in README:
  - `/game/scripts/` for story files
  - `/game/scripts/mechanics/` for system files
  - `/game/characters/` for character definitions
  - `/game/images/` with subfolders
  - `/game/audio/` with subfolders
- [ ] Git repository initialized
- [ ] .gitignore configured for RenPy
- [ ] README.md added to project root
- [ ] Test scene runs successfully

---

### Issue #2: Implement Belief System Core Classes
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #1

**Description:**
Create the BeliefSystem Python class that manages core beliefs, surface beliefs, and on-mind beliefs for both player and NPCs.

**Acceptance Criteria:**
- [ ] `BeliefSystem` class created in `/game/scripts/mechanics/belief_system.rpy`
- [ ] Methods implemented:
  - `add_core_belief(belief_id, statement, strength)`
  - `add_surface_belief(belief_id, statement, source)`
  - `set_on_mind(belief_id, source)`
  - `clear_on_mind(belief_id)`
  - `get_active_beliefs()`
  - `introspect(depth)`
- [ ] Belief modification depth system working (1-3 depths)
- [ ] Unit tests pass for all methods
- [ ] Example belief added and retrieved successfully
- [ ] Documentation comments added to all methods

**Technical Notes:**
```python
# Should support structure like:
belief_system.add_core_belief(
    "values_honesty_over_feelings",
    "I believe honesty is more important than protecting feelings",
    strength=8
)
```

---

### Issue #3: Implement Drug System Core Classes
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #2

**Description:**
Create drug classes (Alcohol, Cannabis, Antidepressants, Antipsychotics) with decorator functions for HIGH and COMEDOWN states.

**Acceptance Criteria:**
- [ ] Base `Drug` class created with:
  - Tolerance tracking
  - Timing system (onset, peak, duration, comedown)
  - `apply_high()` decorator method
  - `apply_comedown()` decorator method
- [ ] `Alcohol` class fully implemented with effects
- [ ] `Cannabis` class fully implemented with effects
- [ ] `AlcoholCannabis` (crossfaded) class implemented
- [ ] `Antidepressant` class fully implemented
- [ ] `Antipsychotic` class fully implemented
- [ ] `DrugManager` class handles active drugs and combinations
- [ ] Drug effects properly modify player_state
- [ ] Tolerance increases with each use
- [ ] Test: Take alcohol, verify belief system narrows
- [ ] Test: Take cannabis, verify introspection depth increases
- [ ] Test: Crossfaded state produces expected effects

---

### Issue #4: Implement Reality Shift System
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 10 hours  
**Dependencies:** #2

**Description:**
Create the reality shift system that triggers visual/physical effects when player acts against beliefs or uses drugs.

**Acceptance Criteria:**
- [ ] `shift_severity` dictionary defined with all 5 levels
- [ ] `trigger_reality_shift(severity, reason)` label created
- [ ] Visual effects implemented for each severity:
  - Catastrophic: Complete breakdown scenes
  - Severe: Major distortion effects
  - Moderate: Flicker/shimmer effects
  - Minor: Subtle detail changes
  - Harmony: Clarity enhancement
- [ ] Physical pain response text for each level
- [ ] Duration pause system working
- [ ] Audio cues play for each shift type
- [ ] Introspection prompt offered for severe/catastrophic
- [ ] `reality_stability` stat properly tracked (0-10)
- [ ] Test: Violate core belief, trigger appropriate shift
- [ ] Test: Act in alignment, trigger harmony state

---

### Issue #5: Implement Introspection Mechanic
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #2, #4

**Description:**
Create the introspection scene/label that pauses gameplay and allows player to examine beliefs and process emotions.

**Acceptance Criteria:**
- [ ] `introspect(reason)` label created
- [ ] Introspection space scene/background created (placeholder ok)
- [ ] System determines which belief was violated
- [ ] Displays violated belief to player
- [ ] Shows "The Critical Question" text
- [ ] Offers multiple interpretations (menu choices)
- [ ] Player awareness increases based on choice quality
- [ ] Option to apologize after introspection
- [ ] Option to commit to doing better
- [ ] Option to continue harmful path (with consequences)
- [ ] Introspection can stabilize reality if genuine
- [ ] Can worsen reality if player refuses to engage
- [ ] Test: Trigger after belief violation, complete flow

---

### Issue #6: Implement State Management & Save System
**Labels:** `feature`, `infrastructure`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #2, #3

**Description:**
Create comprehensive state management for player_state, npc_states, and implement save/load functionality.

**Acceptance Criteria:**
- [ ] `player_state` dictionary defined with all fields from README
- [ ] `npc_states` dictionary structure defined
- [ ] All states properly initialize on new game
- [ ] Save system stores all state variables
- [ ] Load system restores all state variables
- [ ] Auto-save triggers defined:
  - After major choices
  - End of scenes
  - Before reality shifts
  - Before introspection
  - After drug use
- [ ] Manual save/load works from menu
- [ ] Multiple save slots supported (minimum 10)
- [ ] Save file metadata (timestamp, chapter, playtime)
- [ ] Test: Save mid-game, load, verify state intact

---

### Issue #7: Implement Choice Tracking System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 5 hours  
**Dependencies:** #6

**Description:**
Create system to track all meaningful player choices with consequences (immediate, mid-term, revelation).

**Acceptance Criteria:**
- [ ] `choice_record` data structure defined
- [ ] System records each major choice with:
  - choice_id
  - chapter
  - character_involved
  - choice_text
  - alignment (good/evil/neutral)
  - belief_alignment (true/false)
  - consequences (immediate/mid-term/revelation)
- [ ] Choice history accessible for debugging
- [ ] Choices properly saved/loaded
- [ ] Function to query choices by character
- [ ] Function to query choices by alignment
- [ ] Test: Make 5 choices, verify all recorded correctly

---

### Issue #8: Implement Belief-Action Alignment Checker
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #2, #4, #5

**Description:**
Create `check_belief_alignment()` label that runs before major choices to determine if action aligns with core beliefs.

**Acceptance Criteria:**
- [ ] `check_belief_alignment(action_belief, action_description)` label created
- [ ] Calculates alignment score based on core beliefs
- [ ] Determines if action is aligned or not
- [ ] Triggers positive feeling text if aligned
- [ ] Triggers reality shift if not aligned
- [ ] Shift severity based on degree of misalignment
- [ ] Reality stability modified appropriately
- [ ] Can trigger harmony state for perfect alignment
- [ ] Test: Aligned action produces positive result
- [ ] Test: Misaligned action triggers shift and pain

---

### Issue #9: Implement NPC Belief System & Reaction Engine
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 10 hours  
**Dependencies:** #2, #6

**Description:**
Create system for NPCs to have their own belief systems and react to player based on those beliefs.

**Acceptance Criteria:**
- [ ] Each NPC can have own `BeliefSystem` instance
- [ ] NPC belief systems stored in `npc_states`
- [ ] Function to check if player action aligns with NPC beliefs
- [ ] Function to calculate NPC emotional response
- [ ] Trust modification based on alignment
- [ ] Dialogue options filtered by NPC belief system
- [ ] NPCs can have beliefs reinforced or challenged
- [ ] Openness stat determines receptivity to new ideas
- [ ] Test: Player action aligns with NPC belief, trust increases
- [ ] Test: Player action violates NPC belief, trust decreases

---

### Issue #10: Implement Forgiveness System
**Labels:** `feature`, `core-mechanic`, `priority-medium`  
**Effort:** 8 hours  
**Dependencies:** #9

**Description:**
Create the forgiveness arc system where NPCs can forgive player after evil acts if conditions are met.

**Acceptance Criteria:**
- [ ] Forgiveness requirements calculated:
  - NPC trauma_healing >= 7
  - NPC witnessed_change >= 5
  - Forgiveness_timer expired
  - Player awareness_level >= 6
  - Player genuine_remorse_shown >= 3
- [ ] `forgiveness_scene(character_name, evil_act)` template created
- [ ] Boundaries established system implemented
- [ ] One-chance-only system (can't violate again)
- [ ] Forgiveness stabilizes reality temporarily
- [ ] Player can accept or reject forgiveness
- [ ] Accepting forgiveness unlocks redemption path
- [ ] Test: Meet all requirements, trigger forgiveness scene

---

### Issue #11: Create Character Definition System
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 4 hours  
**Dependencies:** #1

**Description:**
Define all characters in RenPy with proper character objects and color coding.

**Acceptance Criteria:**
- [ ] All 13 characters defined in `/game/characters/definitions.rpy`
- [ ] Character objects created:
  - Becky, Maria, Jasmine, Jill
  - Dr. Sarah Chen, Nurse Reyes, Detective Rivera
  - Marcus, Daniel, Carlos
  - Father James, The Watcher, Thomas
- [ ] Color coding applied to each character
- [ ] Character image tags set up (placeholder images ok)
- [ ] Test: Each character can speak dialogue
- [ ] Character names display correctly

---

### Issue #12: Implement Group Therapy Session System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #2, #5, #9

**Description:**
Create group therapy hub where 3 introspections happen per session, player can volunteer or observe, NPCs witness and react.

**Acceptance Criteria:**
- [ ] `group_therapy_session()` label created
- [ ] Session allows exactly 3 introspections
- [ ] Player can raise hand to volunteer
- [ ] NPCs can volunteer (AI determines who)
- [ ] Introspection depth increases over time (week 1: surface, week 5: deep)
- [ ] Witnesses tracked for each introspection
- [ ] Witness reactions calculated based on beliefs
- [ ] Beliefs reinforced or challenged appropriately
- [ ] New dialogue options unlocked based on what was shared
- [ ] Callback system: characters reference previous sessions
- [ ] Group reputation stat tracked
- [ ] Violating confidentiality has severe consequences
- [ ] Test: Complete session, player volunteers
- [ ] Test: Complete session, observe only
- [ ] Test: Character references previous session later

---

## EPIC 2: CHAPTER 1 - AWAKENING (Milestone 2)

### Issue #13: Write Chapter 1 Complete Dialogue
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 16 hours  
**Dependencies:** #1, #11

**Description:**
Write all dialogue for Chapter 1 (Hospital Awakening) including dramatic reality shifts, name choice, and character introductions.

**Acceptance Criteria:**
- [ ] Complete script file: `/game/scripts/chapter_01_awakening.rpy`
- [ ] Opening: Wake up scene with amnesia
- [ ] Dramatic reality shifts: giraffe, jungle, underwater, void
- [ ] Name input prompt integrated
- [ ] Nurse Reyes introduction dialogue
- [ ] Dr. Chen introduction dialogue
- [ ] Reality shift explanations woven in naturally
- [ ] Player choices affect panic_level and awareness_level
- [ ] Foreshadowing of suicide attempt subtly included
- [ ] Chapter ends with player alone, contemplating
- [ ] Minimum 3000 words of dialogue
- [ ] Proofread and polished
- [ ] Test: Play through Chapter 1 start to finish

---

### Issue #14: Create Chapter 1 Placeholder Art
**Labels:** `art`, `placeholder`, `priority-high`  
**Effort:** 8 hours  
**Dependencies:** #13

**Description:**
Create or source placeholder images for all Chapter 1 scenes and characters.

**Acceptance Criteria:**
- [ ] Hospital room background (normal version)
- [ ] Hospital room backgrounds for shifts:
  - Jungle hospital
  - Underwater hospital
  - Void/dreamspace
  - Evening lighting version
  - Night version
- [ ] Nurse Reyes character sprites:
  - Normal human
  - Giraffe variant (dramatic shift)
  - Mermaid variant (dramatic shift)
  - Subtle variants (hair length, clothing)
- [ ] Dr. Chen character sprites:
  - Normal (with glasses)
  - Normal variant (subtle differences)
- [ ] Introspection space background (abstract)
- [ ] All images at proper resolution for RenPy
- [ ] Images compressed appropriately
- [ ] Test: All images display in-game

---

### Issue #15: Implement Chapter 1 Reality Shift Sequences
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #4, #13, #14

**Description:**
Implement the dramatic reality shift sequences in Chapter 1 with proper audio/visual effects.

**Acceptance Criteria:**
- [ ] First shift: Hospital → Jungle with giraffe nurse
- [ ] Second shift: Jungle → Underwater with mermaid nurse
- [ ] Third shift: Underwater → Stable hospital (slightly different)
- [ ] Each shift has:
  - Flash/transition effect
  - Screen shake (if appropriate)
  - Audio glitch sound
  - Pause for player to register
- [ ] Player reactions written for each shift
- [ ] Panic level increases with each shift
- [ ] Awareness can increase if player tries to cope
- [ ] Stability gradually improves by end of chapter
- [ ] Test: Experience all three shifts in sequence

---

### Issue #16: Create Chapter 1 Audio Assets
**Labels:** `audio`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #13

**Description:**
Source or create audio assets for Chapter 1 (heartbeat, reality glitches, ambience).

**Acceptance Criteria:**
- [ ] Heartbeat monitor sound (looping)
- [ ] Reality glitch sound effect (harsh)
- [ ] Reality glitch sound effect (soft)
- [ ] Hospital ambience (subtle)
- [ ] Door open sound
- [ ] Soft harmonic sound (for stability moments)
- [ ] Background music for Chapter 1 (ambient, unsettling)
- [ ] All audio files in proper format (ogg preferred)
- [ ] Audio levels balanced
- [ ] Test: All sounds play correctly in-game

---

### Issue #17: Implement Player Name Input & State Initialization
**Labels:** `feature`, `priority-high`  
**Effort:** 3 hours  
**Dependencies:** #6, #13

**Description:**
Implement the name input prompt and initialize all player_state variables for new game.

**Acceptance Criteria:**
- [ ] Name input prompt appears at correct moment
- [ ] Player can enter custom name
- [ ] Default name "Alex" if blank
- [ ] Name stored in `player_name` variable
- [ ] Name used in dialogue correctly
- [ ] All `player_state` variables initialized:
  - awareness_level = 0
  - panic_level = 5
  - reality_stability = 0
  - core_beliefs = {}
  - etc. (all from README)
- [ ] `player_state["name_chosen"] = True` set
- [ ] Test: Enter name, verify it appears in dialogue
- [ ] Test: Leave blank, verify default name used

---

### Issue #18: Implement Chapter 1 Endings & Transitions
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 2 hours  
**Dependencies:** #13

**Description:**
Create the ending sequence for Chapter 1 and transition to Chapter 2.

**Acceptance Criteria:**
- [ ] Final scene: Player alone at night
- [ ] Introspective narration about what happened
- [ ] Hint at the suicide question ("or why I put it there myself")
- [ ] Peaceful shift moment (stars in window)
- [ ] Fade to black
- [ ] "End of Chapter 1" title card (optional)
- [ ] Smooth transition to Chapter 2 start
- [ ] Auto-save triggers
- [ ] Test: Complete Chapter 1, transition to Chapter 2

---

### Issue #19: Chapter 1 Playtesting & Iteration
**Labels:** `testing`, `priority-high`  
**Effort:** 4 hours  
**Dependencies:** #13, #14, #15, #16, #17, #18

**Description:**
Playtest Chapter 1 completely, gather feedback, iterate on pacing and clarity.

**Acceptance Criteria:**
- [ ] Minimum 3 playtesters complete Chapter 1
- [ ] Feedback documented for:
  - Pacing (too fast/slow?)
  - Clarity (confusing moments?)
  - Emotional impact (scary? intriguing?)
  - Technical issues (bugs, typos)
- [ ] Issues prioritized and addressed
- [ ] Typos fixed
- [ ] Pacing adjusted if needed
- [ ] Re-test after changes
- [ ] Chapter 1 ready for integration

---

## EPIC 3: CHAPTERS 2-3 - GROUP THERAPY & BELIEF BUILDING (Milestone 3)

### Issue #20: Design Therapy Scenario Questions
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #2

**Description:**
Design 10-15 hypothetical scenario questions that will build player's core belief system in therapy sessions.

**Acceptance Criteria:**
- [ ] Minimum 10 scenarios covering belief pairs:
  - Honesty vs Kindness
  - Self-Sacrifice vs Self-Preservation
  - Justice vs Mercy
  - Control vs Surrender
  - Individual vs Community
  - Abundance vs Scarcity
  - Worth vs Performance
  - Trust vs Caution
  - Logic vs Emotion
  - Structure vs Flexibility
- [ ] Each scenario has:
  - Setup description
  - 3-4 choice options
  - Belief values assigned to each choice
  - Dr. Chen follow-up dialogue
- [ ] Scenarios are emotionally engaging
- [ ] No "obviously right" answers
- [ ] Scenarios documented in design doc
- [ ] Review with sensitivity reader

---

### Issue #21: Implement Therapy Session 1 (One-on-One)
**Labels:** `feature`, `content`, `priority-critical`  
**Effort:** 10 hours  
**Dependencies:** #2, #11, #20

**Description:**
Create the first one-on-one therapy session where player answers scenarios and builds core beliefs.

**Acceptance Criteria:**
- [ ] `therapy_session_1()` label created
- [ ] Therapy room background (placeholder ok)
- [ ] Dr. Chen sprite shown
- [ ] Introduction to belief-building exercise
- [ ] Minimum 5 scenarios presented
- [ ] Player choices populate `core_beliefs` dictionary correctly
- [ ] Belief strengths assigned (1-10) based on choice
- [ ] Dr. Chen reflects player's choices back to them
- [ ] Visual demonstration of reality stabilizing
- [ ] reality_stability increases to ~3-4 by end
- [ ] Chapter 2 auto-save at end of session
- [ ] Test: Complete session, verify beliefs stored correctly

---

### Issue #22: Implement Group Therapy Sessions (Weeks 1-2)
**Labels:** `feature`, `content`, `priority-critical`  
**Effort:** 16 hours  
**Dependencies:** #12, #11, #20

**Description:**
Create 3-4 early group therapy sessions with surface-level sharing and group dynamic establishment.

**Acceptance Criteria:**
- [ ] `group_therapy_week_1_day_1()` through `day_3()` labels created
- [ ] All 4 female patients attend
- [ ] Dr. Chen facilitates
- [ ] Each session has 3 introspections
- [ ] Week 1 topics are surface-level:
  - "Why I'm here"
  - "What I'm anxious about"
  - "One thing I want to change"
- [ ] Player can choose to volunteer or observe
- [ ] NPC volunteer logic implemented (varies by character comfort)
- [ ] Witness reactions calculated and stored
- [ ] Group reputation begins tracking
- [ ] Characters reference each other's shares in next session
- [ ] Relationships begin forming based on shared topics
- [ ] Test: Complete 3 sessions, verify progression

---

### Issue #23: Write Character Background Shares (Progressive Revelation)
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** Character arcs defined

**Description:**
Write the progressive revelations each character makes in group therapy from surface to deep.

**Acceptance Criteria:**
- [ ] Becky's progression:
  - Week 1: "I'm depressed, I self-harm sometimes"
  - Week 2: "My boyfriend Marcus is everything to me"
  - Week 3: "I'm terrified of abandonment"
  - Week 4: "My parents neglected me as a child"
  - Week 5: "I don't know who I am without someone to be devoted to"
- [ ] Maria's progression documented (5 weeks)
- [ ] Jasmine's progression documented (5 weeks)
- [ ] Jill's progression documented (5 weeks)
- [ ] Each share has:
  - Emotional authenticity
  - Appropriate depth for week
  - Witness reaction potential
  - Callback opportunities
- [ ] Dr. Chen's facilitation responses written
- [ ] Test: Read all progressions, verify arc makes sense

---

### Issue #24: Implement Group Therapy Sessions (Weeks 3-5)
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 20 hours  
**Dependencies:** #22, #23

**Description:**
Create mid-to-deep group therapy sessions where real trauma begins emerging and bonds deepen.

**Acceptance Criteria:**
- [ ] Week 3 sessions (3 days) created
- [ ] Week 4 sessions (3 days) created
- [ ] Week 5 sessions (3 days) created
- [ ] Total: 9 additional group sessions
- [ ] Topics deepen appropriately:
  - Week 3: Origins of current behaviors
  - Week 4: Core trauma reveals begin
  - Week 5: Deep vulnerability, processing help
- [ ] Player can share own struggles (polygamy guilt, etc.)
- [ ] Group reactions to player shares affect relationships
- [ ] Major revelations unlock private dialogue options
- [ ] Characters reference group shares in 1-on-1 encounters
- [ ] "You said in group that..." callback system working
- [ ] Trust levels affected by group interactions
- [ ] Test: Complete all week 3-5 sessions
- [ ] Test: Player shares, verify NPCs react correctly

---

### Issue #25: Implement Witness Reaction & Belief Change System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 10 hours  
**Dependencies:** #9, #12

**Description:**
Create system where NPCs who witness introspections have beliefs reinforced or challenged, affecting future interactions.

**Acceptance Criteria:**
- [ ] `process_witness_reaction()` function created
- [ ] For each witness, calculate:
  - Does introspection align with their beliefs?
  - Are they open to new perspectives?
  - How does this affect trust/relationship?
- [ ] If aligned: Belief reinforced, trust increases
- [ ] If challenging + high openness: Consider new perspective, growth
- [ ] If challenging + low openness: Defensive, trust decreases
- [ ] New dialogue options unlocked based on reactions
- [ ] Examples:
  - "I heard what you said in group about..."
  - "When you shared that, it made me think..."
  - "I don't agree with what you said, but..."
- [ ] Test: Share something controversial, verify mixed reactions
- [ ] Test: Share something supportive, verify positive reactions

---

### Issue #26: Create Therapy Room & Group Room Backgrounds
**Labels:** `art`, `priority-medium`  
**Effort:** 6 hours  
**Dependencies:** #14

**Description:**
Create backgrounds for one-on-one therapy room and group therapy room.

**Acceptance Criteria:**
- [ ] One-on-one therapy room:
  - Professional but warm
  - Couch, chairs, desk
  - Diplomas, plants
  - Clear and stable version
  - Blurred/distorted version (for low stability)
- [ ] Group therapy room:
  - Circle of chairs
  - Institutional but comfortable
  - Multiple character positions possible
  - Natural lighting
- [ ] Both rooms in day and evening lighting
- [ ] Placeholder quality acceptable, will refine later
- [ ] Test: Both backgrounds display correctly

---

### Issue #27: Implement Medication Choice Scene
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #3, #21

**Description:**
Create scene where Dr. Chen offers antidepressants/antipsychotics as requirement for release, player must choose.

**Acceptance Criteria:**
- [ ] Scene triggers at end of Chapter 2
- [ ] Dr. Chen explains:
  - Facility policy for release
  - Need to be "stabilized"
  - Medication will help with reality shifts
  - But will affect introspection capacity
- [ ] Player choice:
  - Accept medication → Faster release, limited introspection
  - Refuse medication → Stay longer, full access to healing
- [ ] Choice affects game state:
  - `player_state["on_medication"] = True/False`
  - `player_state["release_timeline"]` set
- [ ] If accepted, drug system activates antidepressants
- [ ] Explanation of trade-offs clear but not preachy
- [ ] Test: Both paths lead to functioning game

---

### Issue #28: Implement Detective Rivera First Interview
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 6 hours  
**Dependencies:** #11

**Description:**
Create first interview scene with Detective Rivera investigating the shooting.

**Acceptance Criteria:**
- [ ] Scene triggers in Chapter 3
- [ ] Detective Rivera character sprite
- [ ] Professional but probing dialogue
- [ ] Questions about:
  - What do you remember?
  - Do you have enemies?
  - Any recent conflicts?
  - Relationship history?
- [ ] Player can answer honestly or evasively
- [ ] Detective takes notes, subtle hints of suspicion
- [ ] Foreshadowing: "Interesting. Most people remember *something*"
- [ ] Her guilt about missing signs with partner subtly shown
- [ ] Sets up ongoing investigation subplot
- [ ] Test: Complete interview, verify it flows naturally

---

### Issue #29: Create Chapter 2-3 Transitions & Pacing
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #21, #22, #24

**Description:**
Create smooth transitions between therapy sessions and establish proper pacing for Chapters 2-3.

**Acceptance Criteria:**
- [ ] Time passage indicators:
  - "Three days later..."
  - "After another week of sessions..."
  - Calendar/day counter (optional)
- [ ] Variation between sessions (not repetitive)
- [ ] Some sessions can be summarized:
  - "The next two sessions covered similar ground..."
- [ ] Important sessions played in full
- [ ] Player has downtime between sessions
- [ ] Can explore facility, talk to characters
- [ ] Pacing feels natural, not rushed
- [ ] Clear progression week-to-week
- [ ] Test: Play Chapters 2-3, pacing feels good

---

### Issue #30: Chapters 2-3 Playtesting & Iteration
**Labels:** `testing`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** All Chapter 2-3 issues complete

**Description:**
Playtest Chapters 2-3 completely, focusing on belief system building and group therapy mechanics.

**Acceptance Criteria:**
- [ ] Minimum 3 playtesters complete Chapters 2-3
- [ ] Feedback on:
  - Is belief system building clear?
  - Is group therapy engaging or tedious?
  - Do character progressions feel authentic?
  - Are choices meaningful?
  - Any confusion about mechanics?
- [ ] Issues documented and prioritized
- [ ] Pacing adjusted if needed
- [ ] Repetitive elements trimmed
- [ ] Add variety if sessions feel same-y
- [ ] Test again after changes
- [ ] Chapters 2-3 ready for integration

---

## EPIC 4: CHAPTERS 4-7 - CHARACTER ARCS (Milestone 4)

### Issue #31: Write Becky's Complete Character Arc (Chapter 4)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Becky's arc including good path, evil path, and all variations.

**Acceptance Criteria:**
- [ ] Introduction scene establishing relationship
- [ ] Good path scenes:
  - Supporting her loyalty
  - Helping her process attachment trauma
  - Self-worth building conversations
  - Her healing progression
  - Healthy relationship with Marcus outcome
- [ ] Evil path scenes:
  - Planting doubt about Marcus
  - Intercepting letters/messages
  - Seduction during vulnerability
  - Exploitation of fear
- [ ] Neutral path options (player inconsistent)
- [ ] Private conversations referencing group therapy
- [ ] Self-harm trigger warnings and sensitive handling
- [ ] Minimum 5000 words of dialogue
- [ ] Multiple branch points (minimum 10 major choices)
- [ ] Test: Play through both paths completely

---

### Issue #32: Write Maria's Complete Character Arc (Chapter 5)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Maria's arc including addiction, recovery, and brother storyline.

**Acceptance Criteria:**
- [ ] Introduction establishing her functional alcoholism
- [ ] Good path scenes:
  - Supporting through withdrawals
  - Processing survivor's guilt
  - Confronting pattern with mother
  - Sobriety milestones
  - Kidney donation outcome
- [ ] Evil path scenes:
  - Supplying alcohol "for tapering"
  - Using intoxication for sex
  - Hiding information about Carlos
  - Keeping her dependent
- [ ] Withdrawal scenes (realistic, intense)
- [ ] Relapse possibility in both paths
- [ ] Carlos introduction (good vs evil path versions)
- [ ] Minimum 5000 words of dialogue
- [ ] Addiction portrayed authentically, not glamorized
- [ ] Test: Both paths feel impactful

---

### Issue #33: Write Jasmine's Complete Character Arc (Chapter 6)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Jasmine's arc including drug addiction, grief for Lily, and Daniel/Marcus reunion.

**Acceptance Criteria:**
- [ ] Introduction showing addiction severity
- [ ] Good path scenes:
  - Sitting with her during withdrawals
  - Learning about Lily gradually
  - Helping her say Lily's name
  - Supporting trauma therapy
  - Daniel and Marcus reunion
- [ ] Evil path scenes:
  - Supplying drugs "to prevent hard withdrawals"
  - Sexual exploitation during dependency
  - Hiding settlement and brake failure info
  - Marcus seeing her strung out
- [ ] Withdrawal scenes (medical accuracy)
- [ ] Overdose scene (evil path, survives)
- [ ] Grief processing (Lily's memory honored)
- [ ] Minimum 5000 words of dialogue
- [ ] Sensitive handling of child death
- [ ] Test: Both emotional impacts land

---

### Issue #34: Write Jill's Complete Character Arc (Chapter 7)
**Labels:** `content`, `writing`, `priority-critical`, `sensitive-content`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Jill's arc including CSA trauma, hypersexuality, and Sophie reunion.

**Acceptance Criteria:**
- [ ] Introduction showing hypersexual behavior
- [ ] Good path scenes:
  - Recognizing trauma not choice
  - Declining her propositions (first time valued without sex)
  - Processing consent vs compulsion
  - Building self-worth separate from sexuality
  - Sophie reunion and shared healing
- [ ] Evil path scenes:
  - Sleeping with her "because she wants it"
  - Using trauma patterns
  - Framing sex as therapy
  - Reinforcing harmful beliefs
- [ ] CSA revelation handled with extreme care:
  - Never shown, only discussed
  - Age-appropriate language
  - Focus on healing not details
- [ ] Sophie's testimony and abuser imprisonment
- [ ] Minimum 5000 words of dialogue
- [ ] Sensitivity reader REQUIRED before implementation
- [ ] Test: Therapeutic value without re-traumatization

---

### Issue #35: Implement Evil Act Tracking & Consequences
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 8 hours  
**Dependencies:** #7, #31-34

**Description:**
Create system to track evil acts and accumulate consequences that manifest in Chapter 10.

**Acceptance Criteria:**
- [ ] `player_state["evil_acts"]` array populated with:
  - Character harmed
  - Type of harm
  - Severity
  - Chapter committed
  - Hidden consequences (revealed post-revelation)
- [ ] Evil act triggers:
  - Reality shift (severity based on act)
  - Introspection opportunity
  - Trust decrease
  - Relationship damage
- [ ] Consequences stored but not revealed yet:
  - Becky: Father's death while cheating
  - Maria: Carlos's kidney failure
  - Jasmine: Marcus traumatized
  - Jill: Missed healing with Sophie
- [ ] Evil path flag set if evil_acts.length >= 5
- [ ] Test: Commit evil act, verify tracking and consequences

---

### Issue #36: Implement Good Path Rewards & Relationship Building
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 10 hours  
**Dependencies:** #9, #31-34

**Description:**
Create positive reinforcement system for good path choices including deepening relationships and healing progression.

**Acceptance Criteria:**
- [ ] Trust system increases with good choices
- [ ] Relationship milestones tracked:
  - Friendship (trust 5)
  - Close friendship (trust 7)
  - Deep trust (trust 9)
  - Romance possible (trust 9 + mutual attraction)
- [ ] Each milestone unlocks:
  - New dialogue options
  - Deeper conversations
  - Physical affection options (hugs, etc.)
  - Romance scenes (if applicable)
- [ ] Characters thank player for help
- [ ] Reality stability increases with good acts
- [ ] "Helper's high" positive reinforcement
- [ ] Good path flag set if mostly good choices
- [ ] Test: Good path feels rewarding, not just "less bad"

---

### Issue #37: Create NSFW Scenes (Good Path)
**Labels:** `content`, `nsfw`, `priority-medium`  
**Effort:** 16 hours  
**Dependencies:** #36, Character arc completion

**Description:**
Write adult/sexual content for good path romance options with focus on emotional connection and mutual vulnerability.

**Acceptance Criteria:**
- [ ] Romance scenes for each of 4 patients (good path)
- [ ] Scenes require:
  - Trust >= 9
  - Mutual attraction established
  - No exploitation occurred
  - Genuine emotional connection
- [ ] Content characteristics:
  - Emotionally intimate
  - Mutual vulnerability
  - Celebration of healing
  - Consensual and enthusiastic
  - Character-specific (not generic)
- [ ] Proper age gates and warnings
- [ ] Player can decline (doesn't break relationship)
- [ ] Test: Scenes feel earned, not gratuitous

---

### Issue #38: Create NSFW Scenes (Evil Path)
**Labels:** `content`, `nsfw`, `priority-medium`  
**Effort:** 12 hours  
**Dependencies:** #35, Character arc completion

**Description:**
Write adult/sexual content for evil path that emphasizes exploitation, emptiness, and unhealthy dynamics.

**Acceptance Criteria:**
- [ ] Exploitation scenes for each of 4 patients (evil path)
- [ ] Content characteristics:
  - Hollow, mechanical
  - Power imbalance clear
  - Character dissociated/disconnected
  - Player should feel empty after
  - Questionable consent
  - No emotional intimacy
- [ ] Scenes trigger:
  - Shame (if player has any awareness)
  - Reality shift (moderate to severe)
  - Relationship damage
- [ ] Player can still back out (redemption possible)
- [ ] Proper warnings
- [ ] Test: Scenes feel appropriately uncomfortable

---

### Issue #39: Implement Polygamy/Honesty System
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 8 hours  
**Dependencies:** #36

**Description:**
Create system where player can pursue multiple relationships IF they're honest, vs infidelity if they hide it.

**Acceptance Criteria:**
- [ ] Player can initiate romance with multiple characters
- [ ] If pursuing multiple, dialogue option appears:
  - "I need to be honest with you about something..."
  - Can reveal other relationship(s)
- [ ] Honesty path:
  - Characters discuss polyamory
  - Some accept, some don't (based on beliefs)
  - Boundaries established
  - Trust maintained if honest
  - Ethical non-monogamy possible
- [ ] Dishonesty/infidelity path:
  - Characters discover eventually
  - Massive trust betrayal
  - Reality shift (severe)
  - Relationships destroyed
  - Feeds into evil path
- [ ] Group therapy scene where guilt surfaces
- [ ] Test: Honest polyamory works, cheating has consequences

---

### Issue #40: Create Character-Specific Backgrounds & Sprites
**Labels:** `art`, `priority-high`  
**Effort:** 40 hours  
**Dependencies:** Character designs finalized

**Description:**
Create character sprites and personal room backgrounds for all main characters.

**Acceptance Criteria:**
- [ ] Character sprites (all expressions) for:
  - Becky (neutral, happy, sad, anxious, crying, intimate)
  - Maria (neutral, professional, drunk, withdrawing, happy, intimate)
  - Jasmine (neutral, exhausted, high, sober, grieving, intimate)
  - Jill (neutral, defensive, sexual, vulnerable, healing, intimate)
  - Dr. Chen (professional, warm, concerned, approving)
  - Nurse Reyes (neutral, caring, stern, suspicious)
  - Detective Rivera (professional, probing, sympathetic)
- [ ] Personal room backgrounds:
  - Becky's room (cute, personal photos)
  - Maria's room (organized, minimalist)
  - Jasmine's room (sparse, medication visible)
  - Jill's room (provocative decor, armor)
- [ ] ComfyUI rendering with best consistency possible
- [ ] Multiple variants for reality stability levels
- [ ] Test: All sprites and backgrounds display properly

---

## EPIC 5: CHAPTERS 8-11 - REVELATION & RESOLUTION (Milestone 5)

### Issue #41: Write Chapter 8 - Convergence
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 16 hours  
**Dependencies:** Chapters 4-7 complete

**Description:**
Write Chapter 8 where storylines intersect, consequences manifest, and player senses something bigger approaching.

**Acceptance Criteria:**
- [ ] Multiple character storylines intersect
- [ ] Detective investigation intensifies
- [ ] The Watcher appearances increase
- [ ] Flashback fragments begin appearing
- [ ] Player begins questioning: "Who was I before?"
- [ ] Reality shifts frequency based on path:
  - Good path: Mostly stable
  - Evil path: Increasing chaos
- [ ] Foreshadowing of revelation:
  - "Why can't I remember who shot me?"
  - "What if I already know the answer?"
- [ ] Build tension without revealing yet
- [ ] Minimum 4000 words
- [ ] Test: Creates anticipation for revelation

---

### Issue #42: Write Chapter 9 - The Revelation
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** #41, Full character arcs

**Description:**
Write the revelation sequence where player discovers the suicide attempt and their predatory past.

**Acceptance Criteria:**
- [ ] Revelation triggers after Chapter 8
- [ ] Memory flood sequence:
  - Past predatory behavior shown (implications, not details)
  - Realizing the pattern of hurting women
  - Moment of self-awareness and horror
  - Suicide attempt decision (not shown, revealed)
  - Waking up: "A second chance"
- [ ] Parallel drawn to current behavior:
  - Good path: "I chose differently this time"
  - Evil path: "I repeated the exact same pattern"
- [ ] Detective Rivera reveals findings
- [ ] Reality shift based on path:
  - Good path: Perfect clarity (10/10)
  - Evil path: Complete breakdown (0/10)
- [ ] The Watcher's final pre-resolution appearance
- [ ] Minimum 5000 words
- [ ] Extremely emotionally impactful
- [ ] Test: Players report strong emotional response

---

### Issue #43: Write Chapter 10 - Good Path Consequences
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 16 hours  
**Dependencies:** #42

**Description:**
Write all good path outcomes where male characters arrive, reunions happen, healing is celebrated.

**Acceptance Criteria:**
- [ ] Marcus arrives for Becky reunion
- [ ] Daniel and Marcus(son) arrive for Jasmine
- [ ] Carlos arrives for Maria
- [ ] Sophie reveals abuser imprisoned for Jill
- [ ] Each reunion scene:
  - Emotional and authentic
  - Thanks player for their role
  - Shows ripple effect of healing
  - Celebrates character growth
- [ ] Patient outcomes:
  - Becky: Married, names daughter after therapist
  - Maria: Sober, saved Carlos, runs treatment center
  - Jasmine: Reunited with family, honoring Lily
  - Jill: Running CSA support group with Sophie
- [ ] Player sees they broke the cycle
- [ ] Can forgive past self
- [ ] Can forgive original abuser (optional)
- [ ] Minimum 6000 words total
- [ ] Test: Feels genuinely uplifting

---

### Issue #44: Write Chapter 10 - Evil Path Consequences
**Labels:** `content`, `writing`, `priority-critical`, `dark-content`  
**Effort:** 16 hours  
**Dependencies:** #42

**Description:**
Write all evil path devastating consequences where truth about player's actions revealed and damage shown.

**Acceptance Criteria:**
- [ ] Marcus arrives, reveals truth about letters
- [ ] Becky learns father died while she was cheating
- [ ] Becky's suicide attempt (survives, player watches)
- [ ] Carlos arrives dying, Maria learns she could have saved him
- [ ] Daniel and Marcus arrive, Marcus traumatized
- [ ] Sophie confronts player: "You're no different than he was"
- [ ] Each consequence scene:
  - Devastating but not gratuitous
  - Shows real human cost
  - Characters either break or forgive
  - Player sees themselves as monster
- [ ] Detective arrests player (implied charges)
- [ ] Reality completely unstable
- [ ] Player alone, facing what they've done
- [ ] Minimum 6000 words total
- [ ] Test: Players report feeling genuine horror/shame

---

### Issue #45: Write Forgiveness Scenes (Evil Path Redemption)
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #10, #44

**Description:**
Write forgiveness scenes where mature characters can forgive player despite evil acts, teaching about breaking cycles.

**Acceptance Criteria:**
- [ ] Forgiveness scenes for each character (if requirements met)
- [ ] Based on template in code artifact
- [ ] Each scene includes:
  - Acknowledgment of harm
  - Explanation: forgiveness is for their healing
  - Clear boundaries established
  - "Can you forgive who hurt you?"
  - Offer of redemption path
- [ ] Player can accept or reject forgiveness
- [ ] Accepting begins redemption arc
- [ ] Reality stabilizes if genuine acceptance
- [ ] Dr. Chen's final teaching scene
- [ ] Minimum 4000 words total
- [ ] Test: Emotionally powerful, not preachy

---

### Issue #46: Write Chapter 11 - Good Path Epilogues
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #43

**Description:**
Write multiple ending variations for good path based on romance choices and player decisions.

**Acceptance Criteria:**
- [ ] Endings for each romance option:
  - Becky ending
  - Maria ending
  - Jasmine ending
  - Jill ending
  - Dr. Chen ending (post-treatment)
  - Nurse Reyes ending
  - Polyamory ending (if pursued honestly)
- [ ] Solo ending (player healed but single)
- [ ] Each ending includes:
  - Time jump (months/year later)
  - Character thriving montage
  - Player's new purpose
  - The Watcher fully formed, smiling
  - Final message about breaking cycles
- [ ] Endings are 1500-2000 words each
- [ ] Each feels satisfying and earned
- [ ] Credits roll integration
- [ ] Test: Players report satisfaction

---

### Issue #47: Write Chapter 11 - Evil Path Ending
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 8 hours  
**Dependencies:** #44, #45

**Description:**
Write the evil path ending where player faces complete consequences, with option to try again or give up.

**Acceptance Criteria:**
- [ ] Player in psych ward or prison
- [ ] Alone, reality unstable
- [ ] Montage of destroyed lives
- [ ] The Watcher fades to nothing, crying
- [ ] Dr. Chen final visit:
  - "You had a second chance"
  - "You chose the same pattern"
  - "But even now, you could choose to heal"
  - "Do you want to?"
- [ ] Final choice:
  - Try again (New Game+ option)
  - Give up (Game over)
- [ ] Final message about choice
- [ ] Credits roll (somber music)
- [ ] Minimum 2000 words
- [ ] Test: Impactful but offers hope

---

### Issue #48: Implement The Watcher System
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 10 hours  
**Dependencies:** #11

**Description:**
Create The Watcher spirit manifestation that appears during moral choices and reacts to player's path.

**Acceptance Criteria:**
- [ ] The Watcher character sprite:
  - Young boy (8-12) made of light/shadow
  - Ethereal, not quite solid
  - Multiple states: bright, dim, fading, crying, smiling
- [ ] Appears only during:
  - Major moral choices
  - Introspection moments
  - Reality shifts (severe)
  - Revelation
  - Epilogue
- [ ] Never in NSFW scenes
- [ ] Brightness/solidity based on player alignment:
  - Good acts: Brighter, more solid
  - Evil acts: Dimmer, more shadow
- [ ] No dialogue until final scenes
- [ ] Good path: Becomes fully formed, speaks, smiles
- [ ] Evil path: Fades completely, final tear
- [ ] Test: Appears at correct moments, visual progression clear

---

### Issue #49: Implement Male Support Characters
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 8 hours  
**Dependencies:** #11, Character arcs

**Description:**
Implement Marcus, Daniel, Carlos as characters with their post-revelation appearances and dialogue.

**Acceptance Criteria:**
- [ ] Character definitions for Marcus, Daniel, Carlos
- [ ] Character sprites (placeholder ok)
- [ ] Marcus dialogue:
  - Good path: Grateful, loving toward Becky
  - Evil path: Forgiving of Becky, silent fury at player
- [ ] Daniel dialogue:
  - Good path: Thanks player
  - Evil path: Grace toward Jasmine, anger at player
- [ ] Carlos dialogue:
  - Good path: Recovery, gratitude
  - Evil path: Dying, forgiving, devastating grace
- [ ] Each shows healthy masculinity model
- [ ] Test: Characters appear in correct paths

---

### Issue #50: Create Ending Cinematics & Credits
**Labels:** `feature`, `art`, `priority-medium`  
**Effort:** 12 hours  
**Dependencies:** All endings written

**Description:**
Create visual sequences for each ending including montages and credits.

**Acceptance Criteria:**
- [ ] Good path montages:
  - Characters thriving (still images ok)
  - Time passage indicated
  - Happiness and healing shown
- [ ] Evil path montages:
  - Consequences shown (still images)
  - Somber tone
  - Emptiness conveyed
- [ ] Credits sequence:
  - All contributors listed
  - Mental health resources included
  - "This is not therapy" disclaimer
  - Crisis hotlines
- [ ] Music for each ending type
- [ ] "The End" or "Try Again?" screens
- [ ] Test: All endings play correctly

---

## EPIC 6: ART & AUDIO (Milestone 6)

### Issue #51: Create All Character Portraits (Final Art Pass)
**Labels:** `art`, `priority-high`  
**Effort:** 60 hours  
**Dependencies:** All chapters complete, ComfyUI workflow refined

**Description:**
Create final, most consistent possible character portraits for all characters in all needed expressions.

**Acceptance Criteria:**
- [ ] All 13 characters with full expression sets
- [ ] Best possible consistency from ComfyUI
- [ ] Reality shift variants for key characters
- [ ] NSFW variants for romance characters
- [ ] Total estimated: 150+ unique images
- [ ] Consistent art style maintained
- [ ] High resolution (1080p minimum)
- [ ] Properly compressed
- [ ] Organized in folders
- [ ] Test: All images load correctly

---

### Issue #52: Create All Background Art (Final Art Pass)
**Labels:** `art`, `priority-high`  
**Effort:** 40 hours  
**Dependencies:** All chapters complete

**Description:**
Create or source final background art for all locations including reality shift variants.

**Acceptance Criteria:**
- [ ] Hospital room (+variants)
- [ ] Therapy office (+variants)
- [ ] Group therapy room
- [ ] Assisted living common area
- [ ] All 4 patient bedrooms
- [ ] Player bedroom
- [ ] Outdoor area
- [ ] Introspection space
- [ ] Detective's office
- [ ] Ending scene backgrounds
- [ ] Reality shift variants for each
- [ ] Day/evening/night variants as needed
- [ ] Estimated: 50+ backgrounds
- [ ] Test: All backgrounds display correctly

---

### Issue #53: Create Visual Effects for Reality Shifts
**Labels:** `art`, `vfx`, `priority-medium`  
**Effort:** 16 hours  
**Dependencies:** #4

**Description:**
Create visual effect overlays and transitions for reality shifts at all severity levels.

**Acceptance Criteria:**
- [ ] Catastrophic shift effects:
  - Screen break/shatter
  - Impossible geometry overlays
  - Void textures
  - Particle effects
- [ ] Severe shift effects:
  - Major distortion waves
  - Color inversion flashes
  - Transformation sequences
- [ ] Moderate shift effects:
  - Flicker/shimmer overlays
  - Color shift filters
  - Subtle distortions
- [ ] Minor shift effects:
  - Brief glitch effects
  - Subtle color changes
- [ ] Harmony effects:
  - Clarity enhance
  - Soft glow
  - Vibrant saturation
- [ ] All effects as image overlays or RenPy transforms
- [ ] Test: All effects play smoothly

---

### Issue #54: Compose Main Theme & Chapter Themes
**Labels:** `audio`, `music`, `priority-high`  
**Effort:** 40 hours  
**Dependencies:** Tone of game established

**Description:**
Compose or source main theme music and chapter-specific themes.

**Acceptance Criteria:**
- [ ] Main menu theme (mysterious, melancholic)
- [ ] Chapter 1 theme (unsettling, medical)
- [ ] Therapy theme (calm, introspective)
- [ ] Good path theme (hopeful, warm)
- [ ] Evil path theme (dark, tense)
- [ ] Romance themes (intimate, emotional)
- [ ] Revelation theme (dramatic, intense)
- [ ] Good ending theme (uplifting)
- [ ] Evil ending theme (somber, heavy)
- [ ] All tracks loopable
- [ ] 3-5 minutes each minimum
- [ ] OGG format
- [ ] Volume balanced
- [ ] Test: All music plays correctly, enhances mood

---

### Issue #55: Create Sound Effects Library
**Labels:** `audio`, `sfx`, `priority-medium`  
**Effort:** 12 hours  
**Dependencies:** None

**Description:**
Create or source all sound effects needed throughout game.

**Acceptance Criteria:**
- [ ] Reality shift sounds (all severities)
- [ ] Heartbeat monitor
- [ ] Hospital ambience
- [ ] Door sounds
- [ ] Footsteps
- [ ] UI sounds (click, hover, etc.)
- [ ] Phone/message notification
- [ ] Harmony chime
- [ ] Brain zap sound (antidepressant withdrawal)
- [ ] Ambient sounds (rain, birds, etc.)
- [ ] All SFX in OGG format
- [ ] Volume normalized
- [ ] Test: All sounds play at appropriate moments

---

### Issue #56: Create UI Graphics & Custom Screens
**Labels:** `art`, `ui`, `priority-medium`  
**Effort:** 20 hours  
**Dependencies:** RenPy screens designed

**Description:**
Create custom UI graphics for menus, dialogue boxes, and game-specific screens.

**Acceptance Criteria:**
- [ ] Custom dialogue box
- [ ] Custom choice menu
- [ ] Introspection screen UI
- [ ] Group therapy seating chart (visual)
- [ ] Belief system display screen
- [ ] Drug effects status display
- [ ] Reality stability indicator
- [ ] Relationship/trust meters (optional)
- [ ] Save/load screen graphics
- [ ] Settings screen graphics
- [ ] Main menu graphics
- [ ] All graphics match aesthetic
- [ ] Test: All UI elements display correctly

---

## EPIC 7: POLISH & RELEASE (Milestone 7)

### Issue #57: Implement Comprehensive Save/Load Testing
**Labels:** `testing`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** All content complete

**Description:**
Test save/load functionality extensively across all game states and chapters.

**Acceptance Criteria:**
- [ ] Test saving/loading in every chapter
- [ ] Test saving during:
  - Dialogue
  - Choices
  - Reality shifts
  - Introspection
  - Drug effects active
  - NSFW scenes
- [ ] Verify all state variables save correctly
- [ ] Verify all state variables load correctly
- [ ] Test multiple save slots
- [ ] Test save file corruption handling
- [ ] Test auto-save functionality
- [ ] Document any save-breaking changes
- [ ] Fix all critical save/load bugs

---

### Issue #58: Full QA Pass - Good Path
**Labels:** `testing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** All content complete

**Description:**
Complete playthrough of entire game on good path, documenting all bugs and issues.

**Acceptance Criteria:**
- [ ] Full playthrough from start to credits (good path)
- [ ] Test all major choice variations
- [ ] Document all bugs found
- [ ] Document all typos found
- [ ] Document pacing issues
- [ ] Document unclear moments
- [ ] Verify all good outcomes trigger correctly
- [ ] Verify male character appearances work
- [ ] Verify romance scenes unlock properly
- [ ] Verify endings accessible
- [ ] Minimum 3 complete playthroughs
- [ ] All critical bugs fixed before release

---

### Issue #59: Full QA Pass - Evil Path
**Labels:** `testing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** All content complete

**Description:**
Complete playthrough of entire game on evil path, documenting all bugs and issues.

**Acceptance Criteria:**
- [ ] Full playthrough from start to credits (evil path)
- [ ] Test all major evil choice variations
- [ ] Document all bugs found
- [ ] Verify all devastating consequences trigger
- [ ] Verify reality degradation works
- [ ] Verify evil ending accessible
- [ ] Verify forgiveness scenes trigger when appropriate
- [ ] Test redemption path possibility
- [ ] Minimum 3 complete playthroughs
- [ ] All critical bugs fixed before release

---

### Issue #60: Writing Polish Pass
**Labels:** `content`, `polish`, `priority-high`  
**Effort:** 30 hours  
**Dependencies:** All writing complete

**Description:**
Professional editing pass on all dialogue and narration for clarity, consistency, and impact.

**Acceptance Criteria:**
- [ ] Proofread entire script
- [ ] Fix all typos and grammar errors
- [ ] Verify character voice consistency
- [ ] Improve unclear moments
- [ ] Tighten wordy sections
- [ ] Enhance emotional beats
- [ ] Verify The Critical Question appears consistently
- [ ] Verify foreshadowing works
- [ ] Check for plot holes
- [ ] Verify character arc consistency
- [ ] Professional editor review (if budget allows)
- [ ] Second proofread pass

---

### Issue #61: Sensitivity Reader Review
**Labels:** `testing`, `priority-critical`  
**Effort:** 16 hours + reader time  
**Dependencies:** All writing complete

**Description:**
Have mental health professionals and sensitivity readers review content for therapeutic accuracy and potential harm.

**Acceptance Criteria:**
- [ ] Mental health professional reviews:
  - Therapy scenes
  - Introspection mechanics
  - Drug effects
  - Suicide content
  - Trauma handling
- [ ] CSA survivor reviews Jill's arc
- [ ] Addiction specialist reviews Maria/Jasmine arcs
- [ ] Self-harm expertise reviews Becky's arc
- [ ] All feedback documented
- [ ] Critical issues addressed
- [ ] Content warnings updated based on feedback
- [ ] Therapeutic resources updated

---

### Issue #62: Performance Optimization
**Labels:** `technical`, `optimization`, `priority-medium`  
**Effort:** 12 hours  
**Dependencies:** All content implemented

**Description:**
Optimize game performance for smooth playback on target hardware.

**Acceptance Criteria:**
- [ ] Image loading optimization:
  - Proper preloading
  - Lazy loading for NSFW
  - Image compression without quality loss
- [ ] Audio optimization:
  - Proper looping
  - Volume normalization
  - Format optimization
- [ ] Script optimization:
  - Remove redundant code
  - Optimize state checks
  - Clean up unused variables
- [ ] Test on minimum spec hardware
- [ ] Achieve 60fps in dialogue scenes
- [ ] Load times under 5 seconds
- [ ] Save times under 2 seconds

---

### Issue #63: Accessibility Features
**Labels:** `feature`, `accessibility`, `priority-medium`  
**Effort:** 10 hours  
**Dependencies:** All content complete

**Description:**
Implement accessibility features for wider player access.

**Acceptance Criteria:**
- [ ] Text size options (small/medium/large)
- [ ] Font options (serif/sans-serif/dyslexia-friendly)
- [ ] High contrast mode
- [ ] Screen reader compatibility (basic)
- [ ] Colorblind mode considerations
- [ ] Skip options for:
  - NSFW content
  - Specific trigger content
  - Reality shift sequences (if triggering)
- [ ] Content warning customization
- [ ] Auto-advance text option
- [ ] Test with accessibility tools

---

### Issue #64: Create Marketing Materials
**Labels:** `marketing`, `priority-high`  
**Effort:** 20 hours  
**Dependencies:** Game near complete

**Description:**
Create all marketing materials for launch including trailer, screenshots, and copy.

**Acceptance Criteria:**
- [ ] Game trailer (2-3 minutes):
  - Showcases core concept
  - Shows gameplay
  - Highlights uniqueness
  - Includes content warnings
  - Music and voiceover
- [ ] Screenshot collection (20+):
  - Variety of scenes
  - Show different characters
  - Show UI
  - Show key moments
  - No major spoilers
- [ ] Marketing copy:
  - Short description (100 words)
  - Long description (500 words)
  - Feature list
  - Taglines
- [ ] Key art / Cover image
- [ ] Logo design
- [ ] Test marketing with target audience

---

### Issue #65: Steam Page Setup
**Labels:** `distribution`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #64

**Description:**
Set up Steam store page with all required assets and information.

**Acceptance Criteria:**
- [ ] Steam Partner account created
- [ ] App registered
- [ ] Store page filled out:
  - Title and subtitle
  - Short and long descriptions
  - Feature list
  - System requirements
  - Age rating applied
  - Content warnings
  - Screenshots uploaded
  - Trailer uploaded
  - Key art uploaded
- [ ] Tags applied appropriately
- [ ] Price point set
- [ ] Release date set
- [ ] Review build uploaded
- [ ] Test: Store page visible and looks good

---

### Issue #66: Itch.io Page Setup
**Labels:** `distribution`, `priority-high`  
**Effort:** 4 hours  
**Dependencies:** #64

**Description:**
Set up Itch.io page as alternative/early access platform.

**Acceptance Criteria:**
- [ ] Itch.io account created
- [ ] Game page created
- [ ] Description and screenshots added
- [ ] Trailer embedded
- [ ] Pricing set (or free demo version)
- [ ] Tags applied
- [ ] Content warnings clear
- [ ] Download builds uploaded
- [ ] Test: Page looks good, downloads work

---

### Issue #67: Patreon Setup & Community Building
**Labels:** `marketing`, `community`, `priority-medium`  
**Effort:** 8 hours  
**Dependencies:** None (can start early)

**Description:**
Set up Patreon for ongoing support and community building during development.

**Acceptance Criteria:**
- [ ] Patreon account created
- [ ] Tier structure defined:
  - $5: Dev updates, early access to news
  - $10: Early access to builds
  - $25: Input on content, name in credits
- [ ] Page description written
- [ ] Reward fulfillment plan
- [ ] Regular update schedule committed to
- [ ] Discord server set up (optional)
- [ ] First post welcoming patrons
- [ ] Link from game to Patreon

---

### Issue #68: Beta Testing Program
**Labels:** `testing`, `priority-high`  
**Effort:** 40 hours (+ tester time)  
**Dependencies:** Game feature-complete

**Description:**
Run structured beta testing program with external testers before release.

**Acceptance Criteria:**
- [ ] Recruit 10-20 beta testers
- [ ] Diverse tester backgrounds
- [ ] Test builds distributed
- [ ] Feedback survey created:
  - Technical issues?
  - Pacing issues?
  - Story clarity?
  - Emotional impact?
  - Therapeutic value?# INTROSPECTION - GitHub Issue Tickets

---

## EPIC 1: CORE SYSTEMS & ENGINE (Milestone 1)

### Issue #1: Set Up RenPy Project Structure
**Labels:** `setup`, `infrastructure`, `priority-critical`  
**Effort:** 2 hours  
**Dependencies:** None

**Description:**
Initialize the RenPy project with proper directory structure for scripts, images, audio, and game data.

**Acceptance Criteria:**
- [ ] RenPy project created and launches successfully
- [ ] Directory structure matches specification in README:
  - `/game/scripts/` for story files
  - `/game/scripts/mechanics/` for system files
  - `/game/characters/` for character definitions
  - `/game/images/` with subfolders
  - `/game/audio/` with subfolders
- [ ] Git repository initialized
- [ ] .gitignore configured for RenPy
- [ ] README.md added to project root
- [ ] Test scene runs successfully

---

### Issue #2: Implement Belief System Core Classes
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #1

**Description:**
Create the BeliefSystem Python class that manages core beliefs, surface beliefs, and on-mind beliefs for both player and NPCs.

**Acceptance Criteria:**
- [ ] `BeliefSystem` class created in `/game/scripts/mechanics/belief_system.rpy`
- [ ] Methods implemented:
  - `add_core_belief(belief_id, statement, strength)`
  - `add_surface_belief(belief_id, statement, source)`
  - `set_on_mind(belief_id, source)`
  - `clear_on_mind(belief_id)`
  - `get_active_beliefs()`
  - `introspect(depth)`
- [ ] Belief modification depth system working (1-3 depths)
- [ ] Unit tests pass for all methods
- [ ] Example belief added and retrieved successfully
- [ ] Documentation comments added to all methods

**Technical Notes:**
```python
# Should support structure like:
belief_system.add_core_belief(
    "values_honesty_over_feelings",
    "I believe honesty is more important than protecting feelings",
    strength=8
)
```

---

### Issue #3: Implement Drug System Core Classes
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #2

**Description:**
Create drug classes (Alcohol, Cannabis, Antidepressants, Antipsychotics) with decorator functions for HIGH and COMEDOWN states.

**Acceptance Criteria:**
- [ ] Base `Drug` class created with:
  - Tolerance tracking
  - Timing system (onset, peak, duration, comedown)
  - `apply_high()` decorator method
  - `apply_comedown()` decorator method
- [ ] `Alcohol` class fully implemented with effects
- [ ] `Cannabis` class fully implemented with effects
- [ ] `AlcoholCannabis` (crossfaded) class implemented
- [ ] `Antidepressant` class fully implemented
- [ ] `Antipsychotic` class fully implemented
- [ ] `DrugManager` class handles active drugs and combinations
- [ ] Drug effects properly modify player_state
- [ ] Tolerance increases with each use
- [ ] Test: Take alcohol, verify belief system narrows
- [ ] Test: Take cannabis, verify introspection depth increases
- [ ] Test: Crossfaded state produces expected effects

---

### Issue #4: Implement Reality Shift System
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 10 hours  
**Dependencies:** #2

**Description:**
Create the reality shift system that triggers visual/physical effects when player acts against beliefs or uses drugs.

**Acceptance Criteria:**
- [ ] `shift_severity` dictionary defined with all 5 levels
- [ ] `trigger_reality_shift(severity, reason)` label created
- [ ] Visual effects implemented for each severity:
  - Catastrophic: Complete breakdown scenes
  - Severe: Major distortion effects
  - Moderate: Flicker/shimmer effects
  - Minor: Subtle detail changes
  - Harmony: Clarity enhancement
- [ ] Physical pain response text for each level
- [ ] Duration pause system working
- [ ] Audio cues play for each shift type
- [ ] Introspection prompt offered for severe/catastrophic
- [ ] `reality_stability` stat properly tracked (0-10)
- [ ] Test: Violate core belief, trigger appropriate shift
- [ ] Test: Act in alignment, trigger harmony state

---

### Issue #5: Implement Introspection Mechanic
**Labels:** `feature`, `core-mechanic`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #2, #4

**Description:**
Create the introspection scene/label that pauses gameplay and allows player to examine beliefs and process emotions.

**Acceptance Criteria:**
- [ ] `introspect(reason)` label created
- [ ] Introspection space scene/background created (placeholder ok)
- [ ] System determines which belief was violated
- [ ] Displays violated belief to player
- [ ] Shows "The Critical Question" text
- [ ] Offers multiple interpretations (menu choices)
- [ ] Player awareness increases based on choice quality
- [ ] Option to apologize after introspection
- [ ] Option to commit to doing better
- [ ] Option to continue harmful path (with consequences)
- [ ] Introspection can stabilize reality if genuine
- [ ] Can worsen reality if player refuses to engage
- [ ] Test: Trigger after belief violation, complete flow

---

### Issue #6: Implement State Management & Save System
**Labels:** `feature`, `infrastructure`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #2, #3

**Description:**
Create comprehensive state management for player_state, npc_states, and implement save/load functionality.

**Acceptance Criteria:**
- [ ] `player_state` dictionary defined with all fields from README
- [ ] `npc_states` dictionary structure defined
- [ ] All states properly initialize on new game
- [ ] Save system stores all state variables
- [ ] Load system restores all state variables
- [ ] Auto-save triggers defined:
  - After major choices
  - End of scenes
  - Before reality shifts
  - Before introspection
  - After drug use
- [ ] Manual save/load works from menu
- [ ] Multiple save slots supported (minimum 10)
- [ ] Save file metadata (timestamp, chapter, playtime)
- [ ] Test: Save mid-game, load, verify state intact

---

### Issue #7: Implement Choice Tracking System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 5 hours  
**Dependencies:** #6

**Description:**
Create system to track all meaningful player choices with consequences (immediate, mid-term, revelation).

**Acceptance Criteria:**
- [ ] `choice_record` data structure defined
- [ ] System records each major choice with:
  - choice_id
  - chapter
  - character_involved
  - choice_text
  - alignment (good/evil/neutral)
  - belief_alignment (true/false)
  - consequences (immediate/mid-term/revelation)
- [ ] Choice history accessible for debugging
- [ ] Choices properly saved/loaded
- [ ] Function to query choices by character
- [ ] Function to query choices by alignment
- [ ] Test: Make 5 choices, verify all recorded correctly

---

### Issue #8: Implement Belief-Action Alignment Checker
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #2, #4, #5

**Description:**
Create `check_belief_alignment()` label that runs before major choices to determine if action aligns with core beliefs.

**Acceptance Criteria:**
- [ ] `check_belief_alignment(action_belief, action_description)` label created
- [ ] Calculates alignment score based on core beliefs
- [ ] Determines if action is aligned or not
- [ ] Triggers positive feeling text if aligned
- [ ] Triggers reality shift if not aligned
- [ ] Shift severity based on degree of misalignment
- [ ] Reality stability modified appropriately
- [ ] Can trigger harmony state for perfect alignment
- [ ] Test: Aligned action produces positive result
- [ ] Test: Misaligned action triggers shift and pain

---

### Issue #9: Implement NPC Belief System & Reaction Engine
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 10 hours  
**Dependencies:** #2, #6

**Description:**
Create system for NPCs to have their own belief systems and react to player based on those beliefs.

**Acceptance Criteria:**
- [ ] Each NPC can have own `BeliefSystem` instance
- [ ] NPC belief systems stored in `npc_states`
- [ ] Function to check if player action aligns with NPC beliefs
- [ ] Function to calculate NPC emotional response
- [ ] Trust modification based on alignment
- [ ] Dialogue options filtered by NPC belief system
- [ ] NPCs can have beliefs reinforced or challenged
- [ ] Openness stat determines receptivity to new ideas
- [ ] Test: Player action aligns with NPC belief, trust increases
- [ ] Test: Player action violates NPC belief, trust decreases

---

### Issue #10: Implement Forgiveness System
**Labels:** `feature`, `core-mechanic`, `priority-medium`  
**Effort:** 8 hours  
**Dependencies:** #9

**Description:**
Create the forgiveness arc system where NPCs can forgive player after evil acts if conditions are met.

**Acceptance Criteria:**
- [ ] Forgiveness requirements calculated:
  - NPC trauma_healing >= 7
  - NPC witnessed_change >= 5
  - Forgiveness_timer expired
  - Player awareness_level >= 6
  - Player genuine_remorse_shown >= 3
- [ ] `forgiveness_scene(character_name, evil_act)` template created
- [ ] Boundaries established system implemented
- [ ] One-chance-only system (can't violate again)
- [ ] Forgiveness stabilizes reality temporarily
- [ ] Player can accept or reject forgiveness
- [ ] Accepting forgiveness unlocks redemption path
- [ ] Test: Meet all requirements, trigger forgiveness scene

---

### Issue #11: Create Character Definition System
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 4 hours  
**Dependencies:** #1

**Description:**
Define all characters in RenPy with proper character objects and color coding.

**Acceptance Criteria:**
- [ ] All 13 characters defined in `/game/characters/definitions.rpy`
- [ ] Character objects created:
  - Becky, Maria, Jasmine, Jill
  - Dr. Sarah Chen, Nurse Reyes, Detective Rivera
  - Marcus, Daniel, Carlos
  - Father James, The Watcher, Thomas
- [ ] Color coding applied to each character
- [ ] Character image tags set up (placeholder images ok)
- [ ] Test: Each character can speak dialogue
- [ ] Character names display correctly

---

### Issue #12: Implement Group Therapy Session System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** #2, #5, #9

**Description:**
Create group therapy hub where 3 introspections happen per session, player can volunteer or observe, NPCs witness and react.

**Acceptance Criteria:**
- [ ] `group_therapy_session()` label created
- [ ] Session allows exactly 3 introspections
- [ ] Player can raise hand to volunteer
- [ ] NPCs can volunteer (AI determines who)
- [ ] Introspection depth increases over time (week 1: surface, week 5: deep)
- [ ] Witnesses tracked for each introspection
- [ ] Witness reactions calculated based on beliefs
- [ ] Beliefs reinforced or challenged appropriately
- [ ] New dialogue options unlocked based on what was shared
- [ ] Callback system: characters reference previous sessions
- [ ] Group reputation stat tracked
- [ ] Violating confidentiality has severe consequences
- [ ] Test: Complete session, player volunteers
- [ ] Test: Complete session, observe only
- [ ] Test: Character references previous session later

---

## EPIC 2: CHAPTER 1 - AWAKENING (Milestone 2)

### Issue #13: Write Chapter 1 Complete Dialogue
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 16 hours  
**Dependencies:** #1, #11

**Description:**
Write all dialogue for Chapter 1 (Hospital Awakening) including dramatic reality shifts, name choice, and character introductions.

**Acceptance Criteria:**
- [ ] Complete script file: `/game/scripts/chapter_01_awakening.rpy`
- [ ] Opening: Wake up scene with amnesia
- [ ] Dramatic reality shifts: giraffe, jungle, underwater, void
- [ ] Name input prompt integrated
- [ ] Nurse Reyes introduction dialogue
- [ ] Dr. Chen introduction dialogue
- [ ] Reality shift explanations woven in naturally
- [ ] Player choices affect panic_level and awareness_level
- [ ] Foreshadowing of suicide attempt subtly included
- [ ] Chapter ends with player alone, contemplating
- [ ] Minimum 3000 words of dialogue
- [ ] Proofread and polished
- [ ] Test: Play through Chapter 1 start to finish

---

### Issue #14: Create Chapter 1 Placeholder Art
**Labels:** `art`, `placeholder`, `priority-high`  
**Effort:** 8 hours  
**Dependencies:** #13

**Description:**
Create or source placeholder images for all Chapter 1 scenes and characters.

**Acceptance Criteria:**
- [ ] Hospital room background (normal version)
- [ ] Hospital room backgrounds for shifts:
  - Jungle hospital
  - Underwater hospital
  - Void/dreamspace
  - Evening lighting version
  - Night version
- [ ] Nurse Reyes character sprites:
  - Normal human
  - Giraffe variant (dramatic shift)
  - Mermaid variant (dramatic shift)
  - Subtle variants (hair length, clothing)
- [ ] Dr. Chen character sprites:
  - Normal (with glasses)
  - Normal variant (subtle differences)
- [ ] Introspection space background (abstract)
- [ ] All images at proper resolution for RenPy
- [ ] Images compressed appropriately
- [ ] Test: All images display in-game

---

### Issue #15: Implement Chapter 1 Reality Shift Sequences
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** #4, #13, #14

**Description:**
Implement the dramatic reality shift sequences in Chapter 1 with proper audio/visual effects.

**Acceptance Criteria:**
- [ ] First shift: Hospital → Jungle with giraffe nurse
- [ ] Second shift: Jungle → Underwater with mermaid nurse
- [ ] Third shift: Underwater → Stable hospital (slightly different)
- [ ] Each shift has:
  - Flash/transition effect
  - Screen shake (if appropriate)
  - Audio glitch sound
  - Pause for player to register
- [ ] Player reactions written for each shift
- [ ] Panic level increases with each shift
- [ ] Awareness can increase if player tries to cope
- [ ] Stability gradually improves by end of chapter
- [ ] Test: Experience all three shifts in sequence

---

### Issue #16: Create Chapter 1 Audio Assets
**Labels:** `audio`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #13

**Description:**
Source or create audio assets for Chapter 1 (heartbeat, reality glitches, ambience).

**Acceptance Criteria:**
- [ ] Heartbeat monitor sound (looping)
- [ ] Reality glitch sound effect (harsh)
- [ ] Reality glitch sound effect (soft)
- [ ] Hospital ambience (subtle)
- [ ] Door open sound
- [ ] Soft harmonic sound (for stability moments)
- [ ] Background music for Chapter 1 (ambient, unsettling)
- [ ] All audio files in proper format (ogg preferred)
- [ ] Audio levels balanced
- [ ] Test: All sounds play correctly in-game

---

### Issue #17: Implement Player Name Input & State Initialization
**Labels:** `feature`, `priority-high`  
**Effort:** 3 hours  
**Dependencies:** #6, #13

**Description:**
Implement the name input prompt and initialize all player_state variables for new game.

**Acceptance Criteria:**
- [ ] Name input prompt appears at correct moment
- [ ] Player can enter custom name
- [ ] Default name "Alex" if blank
- [ ] Name stored in `player_name` variable
- [ ] Name used in dialogue correctly
- [ ] All `player_state` variables initialized:
  - awareness_level = 0
  - panic_level = 5
  - reality_stability = 0
  - core_beliefs = {}
  - etc. (all from README)
- [ ] `player_state["name_chosen"] = True` set
- [ ] Test: Enter name, verify it appears in dialogue
- [ ] Test: Leave blank, verify default name used

---

### Issue #18: Implement Chapter 1 Endings & Transitions
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 2 hours  
**Dependencies:** #13

**Description:**
Create the ending sequence for Chapter 1 and transition to Chapter 2.

**Acceptance Criteria:**
- [ ] Final scene: Player alone at night
- [ ] Introspective narration about what happened
- [ ] Hint at the suicide question ("or why I put it there myself")
- [ ] Peaceful shift moment (stars in window)
- [ ] Fade to black
- [ ] "End of Chapter 1" title card (optional)
- [ ] Smooth transition to Chapter 2 start
- [ ] Auto-save triggers
- [ ] Test: Complete Chapter 1, transition to Chapter 2

---

### Issue #19: Chapter 1 Playtesting & Iteration
**Labels:** `testing`, `priority-high`  
**Effort:** 4 hours  
**Dependencies:** #13, #14, #15, #16, #17, #18

**Description:**
Playtest Chapter 1 completely, gather feedback, iterate on pacing and clarity.

**Acceptance Criteria:**
- [ ] Minimum 3 playtesters complete Chapter 1
- [ ] Feedback documented for:
  - Pacing (too fast/slow?)
  - Clarity (confusing moments?)
  - Emotional impact (scary? intriguing?)
  - Technical issues (bugs, typos)
- [ ] Issues prioritized and addressed
- [ ] Typos fixed
- [ ] Pacing adjusted if needed
- [ ] Re-test after changes
- [ ] Chapter 1 ready for integration

---

## EPIC 3: CHAPTERS 2-3 - GROUP THERAPY & BELIEF BUILDING (Milestone 3)

### Issue #20: Design Therapy Scenario Questions
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 8 hours  
**Dependencies:** #2

**Description:**
Design 10-15 hypothetical scenario questions that will build player's core belief system in therapy sessions.

**Acceptance Criteria:**
- [ ] Minimum 10 scenarios covering belief pairs:
  - Honesty vs Kindness
  - Self-Sacrifice vs Self-Preservation
  - Justice vs Mercy
  - Control vs Surrender
  - Individual vs Community
  - Abundance vs Scarcity
  - Worth vs Performance
  - Trust vs Caution
  - Logic vs Emotion
  - Structure vs Flexibility
- [ ] Each scenario has:
  - Setup description
  - 3-4 choice options
  - Belief values assigned to each choice
  - Dr. Chen follow-up dialogue
- [ ] Scenarios are emotionally engaging
- [ ] No "obviously right" answers
- [ ] Scenarios documented in design doc
- [ ] Review with sensitivity reader

---

### Issue #21: Implement Therapy Session 1 (One-on-One)
**Labels:** `feature`, `content`, `priority-critical`  
**Effort:** 10 hours  
**Dependencies:** #2, #11, #20

**Description:**
Create the first one-on-one therapy session where player answers scenarios and builds core beliefs.

**Acceptance Criteria:**
- [ ] `therapy_session_1()` label created
- [ ] Therapy room background (placeholder ok)
- [ ] Dr. Chen sprite shown
- [ ] Introduction to belief-building exercise
- [ ] Minimum 5 scenarios presented
- [ ] Player choices populate `core_beliefs` dictionary correctly
- [ ] Belief strengths assigned (1-10) based on choice
- [ ] Dr. Chen reflects player's choices back to them
- [ ] Visual demonstration of reality stabilizing
- [ ] reality_stability increases to ~3-4 by end
- [ ] Chapter 2 auto-save at end of session
- [ ] Test: Complete session, verify beliefs stored correctly

---

### Issue #22: Implement Group Therapy Sessions (Weeks 1-2)
**Labels:** `feature`, `content`, `priority-critical`  
**Effort:** 16 hours  
**Dependencies:** #12, #11, #20

**Description:**
Create 3-4 early group therapy sessions with surface-level sharing and group dynamic establishment.

**Acceptance Criteria:**
- [ ] `group_therapy_week_1_day_1()` through `day_3()` labels created
- [ ] All 4 female patients attend
- [ ] Dr. Chen facilitates
- [ ] Each session has 3 introspections
- [ ] Week 1 topics are surface-level:
  - "Why I'm here"
  - "What I'm anxious about"
  - "One thing I want to change"
- [ ] Player can choose to volunteer or observe
- [ ] NPC volunteer logic implemented (varies by character comfort)
- [ ] Witness reactions calculated and stored
- [ ] Group reputation begins tracking
- [ ] Characters reference each other's shares in next session
- [ ] Relationships begin forming based on shared topics
- [ ] Test: Complete 3 sessions, verify progression

---

### Issue #23: Write Character Background Shares (Progressive Revelation)
**Labels:** `content`, `writing`, `priority-high`  
**Effort:** 12 hours  
**Dependencies:** Character arcs defined

**Description:**
Write the progressive revelations each character makes in group therapy from surface to deep.

**Acceptance Criteria:**
- [ ] Becky's progression:
  - Week 1: "I'm depressed, I self-harm sometimes"
  - Week 2: "My boyfriend Marcus is everything to me"
  - Week 3: "I'm terrified of abandonment"
  - Week 4: "My parents neglected me as a child"
  - Week 5: "I don't know who I am without someone to be devoted to"
- [ ] Maria's progression documented (5 weeks)
- [ ] Jasmine's progression documented (5 weeks)
- [ ] Jill's progression documented (5 weeks)
- [ ] Each share has:
  - Emotional authenticity
  - Appropriate depth for week
  - Witness reaction potential
  - Callback opportunities
- [ ] Dr. Chen's facilitation responses written
- [ ] Test: Read all progressions, verify arc makes sense

---

### Issue #24: Implement Group Therapy Sessions (Weeks 3-5)
**Labels:** `feature`, `content`, `priority-high`  
**Effort:** 20 hours  
**Dependencies:** #22, #23

**Description:**
Create mid-to-deep group therapy sessions where real trauma begins emerging and bonds deepen.

**Acceptance Criteria:**
- [ ] Week 3 sessions (3 days) created
- [ ] Week 4 sessions (3 days) created
- [ ] Week 5 sessions (3 days) created
- [ ] Total: 9 additional group sessions
- [ ] Topics deepen appropriately:
  - Week 3: Origins of current behaviors
  - Week 4: Core trauma reveals begin
  - Week 5: Deep vulnerability, processing help
- [ ] Player can share own struggles (polygamy guilt, etc.)
- [ ] Group reactions to player shares affect relationships
- [ ] Major revelations unlock private dialogue options
- [ ] Characters reference group shares in 1-on-1 encounters
- [ ] "You said in group that..." callback system working
- [ ] Trust levels affected by group interactions
- [ ] Test: Complete all week 3-5 sessions
- [ ] Test: Player shares, verify NPCs react correctly

---

### Issue #25: Implement Witness Reaction & Belief Change System
**Labels:** `feature`, `core-mechanic`, `priority-high`  
**Effort:** 10 hours  
**Dependencies:** #9, #12

**Description:**
Create system where NPCs who witness introspections have beliefs reinforced or challenged, affecting future interactions.

**Acceptance Criteria:**
- [ ] `process_witness_reaction()` function created
- [ ] For each witness, calculate:
  - Does introspection align with their beliefs?
  - Are they open to new perspectives?
  - How does this affect trust/relationship?
- [ ] If aligned: Belief reinforced, trust increases
- [ ] If challenging + high openness: Consider new perspective, growth
- [ ] If challenging + low openness: Defensive, trust decreases
- [ ] New dialogue options unlocked based on reactions
- [ ] Examples:
  - "I heard what you said in group about..."
  - "When you shared that, it made me think..."
  - "I don't agree with what you said, but..."
- [ ] Test: Share something controversial, verify mixed reactions
- [ ] Test: Share something supportive, verify positive reactions

---

### Issue #26: Create Therapy Room & Group Room Backgrounds
**Labels:** `art`, `priority-medium`  
**Effort:** 6 hours  
**Dependencies:** #14

**Description:**
Create backgrounds for one-on-one therapy room and group therapy room.

**Acceptance Criteria:**
- [ ] One-on-one therapy room:
  - Professional but warm
  - Couch, chairs, desk
  - Diplomas, plants
  - Clear and stable version
  - Blurred/distorted version (for low stability)
- [ ] Group therapy room:
  - Circle of chairs
  - Institutional but comfortable
  - Multiple character positions possible
  - Natural lighting
- [ ] Both rooms in day and evening lighting
- [ ] Placeholder quality acceptable, will refine later
- [ ] Test: Both backgrounds display correctly

---

### Issue #27: Implement Medication Choice Scene
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #3, #21

**Description:**
Create scene where Dr. Chen offers antidepressants/antipsychotics as requirement for release, player must choose.

**Acceptance Criteria:**
- [ ] Scene triggers at end of Chapter 2
- [ ] Dr. Chen explains:
  - Facility policy for release
  - Need to be "stabilized"
  - Medication will help with reality shifts
  - But will affect introspection capacity
- [ ] Player choice:
  - Accept medication → Faster release, limited introspection
  - Refuse medication → Stay longer, full access to healing
- [ ] Choice affects game state:
  - `player_state["on_medication"] = True/False`
  - `player_state["release_timeline"]` set
- [ ] If accepted, drug system activates antidepressants
- [ ] Explanation of trade-offs clear but not preachy
- [ ] Test: Both paths lead to functioning game

---

### Issue #28: Implement Detective Rivera First Interview
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 6 hours  
**Dependencies:** #11

**Description:**
Create first interview scene with Detective Rivera investigating the shooting.

**Acceptance Criteria:**
- [ ] Scene triggers in Chapter 3
- [ ] Detective Rivera character sprite
- [ ] Professional but probing dialogue
- [ ] Questions about:
  - What do you remember?
  - Do you have enemies?
  - Any recent conflicts?
  - Relationship history?
- [ ] Player can answer honestly or evasively
- [ ] Detective takes notes, subtle hints of suspicion
- [ ] Foreshadowing: "Interesting. Most people remember *something*"
- [ ] Her guilt about missing signs with partner subtly shown
- [ ] Sets up ongoing investigation subplot
- [ ] Test: Complete interview, verify it flows naturally

---

### Issue #29: Create Chapter 2-3 Transitions & Pacing
**Labels:** `feature`, `content`, `priority-medium`  
**Effort:** 4 hours  
**Dependencies:** #21, #22, #24

**Description:**
Create smooth transitions between therapy sessions and establish proper pacing for Chapters 2-3.

**Acceptance Criteria:**
- [ ] Time passage indicators:
  - "Three days later..."
  - "After another week of sessions..."
  - Calendar/day counter (optional)
- [ ] Variation between sessions (not repetitive)
- [ ] Some sessions can be summarized:
  - "The next two sessions covered similar ground..."
- [ ] Important sessions played in full
- [ ] Player has downtime between sessions
- [ ] Can explore facility, talk to characters
- [ ] Pacing feels natural, not rushed
- [ ] Clear progression week-to-week
- [ ] Test: Play Chapters 2-3, pacing feels good

---

### Issue #30: Chapters 2-3 Playtesting & Iteration
**Labels:** `testing`, `priority-high`  
**Effort:** 6 hours  
**Dependencies:** All Chapter 2-3 issues complete

**Description:**
Playtest Chapters 2-3 completely, focusing on belief system building and group therapy mechanics.

**Acceptance Criteria:**
- [ ] Minimum 3 playtesters complete Chapters 2-3
- [ ] Feedback on:
  - Is belief system building clear?
  - Is group therapy engaging or tedious?
  - Do character progressions feel authentic?
  - Are choices meaningful?
  - Any confusion about mechanics?
- [ ] Issues documented and prioritized
- [ ] Pacing adjusted if needed
- [ ] Repetitive elements trimmed
- [ ] Add variety if sessions feel same-y
- [ ] Test again after changes
- [ ] Chapters 2-3 ready for integration

---

## EPIC 4: CHAPTERS 4-7 - CHARACTER ARCS (Milestone 4)

### Issue #31: Write Becky's Complete Character Arc (Chapter 4)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Becky's arc including good path, evil path, and all variations.

**Acceptance Criteria:**
- [ ] Introduction scene establishing relationship
- [ ] Good path scenes:
  - Supporting her loyalty
  - Helping her process attachment trauma
  - Self-worth building conversations
  - Her healing progression
  - Healthy relationship with Marcus outcome
- [ ] Evil path scenes:
  - Planting doubt about Marcus
  - Intercepting letters/messages
  - Seduction during vulnerability
  - Exploitation of fear
- [ ] Neutral path options (player inconsistent)
- [ ] Private conversations referencing group therapy
- [ ] Self-harm trigger warnings and sensitive handling
- [ ] Minimum 5000 words of dialogue
- [ ] Multiple branch points (minimum 10 major choices)
- [ ] Test: Play through both paths completely

---

### Issue #32: Write Maria's Complete Character Arc (Chapter 5)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Maria's arc including addiction, recovery, and brother storyline.

**Acceptance Criteria:**
- [ ] Introduction establishing her functional alcoholism
- [ ] Good path scenes:
  - Supporting through withdrawals
  - Processing survivor's guilt
  - Confronting pattern with mother
  - Sobriety milestones
  - Kidney donation outcome
- [ ] Evil path scenes:
  - Supplying alcohol "for tapering"
  - Using intoxication for sex
  - Hiding information about Carlos
  - Keeping her dependent
- [ ] Withdrawal scenes (realistic, intense)
- [ ] Relapse possibility in both paths
- [ ] Carlos introduction (good vs evil path versions)
- [ ] Minimum 5000 words of dialogue
- [ ] Addiction portrayed authentically, not glamorized
- [ ] Test: Both paths feel impactful

---

### Issue #33: Write Jasmine's Complete Character Arc (Chapter 6)
**Labels:** `content`, `writing`, `priority-critical`  
**Effort:** 20 hours  
**Dependencies:** Character arcs document

**Description:**
Write complete dialogue and scenes for Jasmine's arc including drug addiction, grief for Lily, and Daniel/Marcus reunion.

**Acceptance Criteria