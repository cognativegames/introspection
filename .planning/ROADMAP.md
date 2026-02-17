# Roadmap: Introspection - Ren'Py Psychological Visual Novel

**Version:** 1.0
**Date:** 2026-02-16

## Overview

**Total Phases:** 3 | **Total Requirements:** 23 | **Project Type:** Brownfield Refinement

| # | Phase | Goal | Requirements | Success Criteria |
|---|-------|------|--------------|------------------|
| 1 | Belief & Emotion Core | Fix and complete core belief system and emotion mechanics | BELIEF-01 to BELIEF-05, EMOT-01 to EMOT-04, REAL-01 to REAL-04 | 9 criteria |
| 2 | Dialogue Steering & Introspection | Implement encounter routing and therapy mechanics | ENCO-01 to ENCO-05, INTRO-01 to INTRO-05 | 10 criteria |
| 3 | Game Flow Integration | Connect systems into playable narrative flow | FLOW-01 to FLOW-04 | 4 criteria |

---

## Phase Details

### Phase 1: Belief & Emotion Core

**Goal:** Fix and complete the core belief system and emotion mechanics to create a solid foundation for the game.

**Requirements:**
- BELIEF-01: Belief activation from player choices
- BELIEF-02: Belief conflict detection
- BELIEF-03: Conflict consequence application
- BELIEF-04: Belief resolution flow
- BELIEF-05: Belief intensity tracking
- EMOT-01: Emotion initialization
- EMOT-02: Emotion adjustment
- EMOT-03: Emotion-belief feedback
- EMOT-04: Dominant emotion display
- REAL-01: Shift triggers
- REAL-02: Severity levels
- REAL-03: Visual effects
- REAL-04: Harmony state

**Success Criteria:**
1. Player can make interpretation choices in encounters that activate beliefs
2. Contradictory beliefs are detected and severity is calculated correctly
3. Active conflicts trigger emotional distress (anxiety, overwhelm increases)
4. Reality shifts trigger at appropriate thresholds (minor: 3+, moderate: 5+, severe: 7+)
5. Player can examine and resolve belief conflicts through introspection flow
6. All 20+ emotions initialize to baseline values from Brené Brown taxonomy
7. adjust_emotions() correctly modifies emotions with bounds (0-100)
8. High emotion states surface relevant belief feedback
9. Harmony state triggers when acting in alignment with core beliefs

**Dependencies:**
- None (foundational)

---

### Phase 2: Dialogue Steering & Introspection

**Goal:** Implement encounter routing based on player state and complete the introspection/therapy mechanics.

**Requirements:**
- ENCO-01: Encounter router integration
- ENCO-02: Anxiety-based routing
- ENCO-03: Belief-based routing
- ENCO-04: Interpretation choices
- ENCO-05: Encounter vault population
- INTRO-01: Introspection trigger
- INTRO-02: Conflict visualization
- INTRO-03: Belief examination flow
- INTRO-04: Belief synthesis
- INTRO-05: Therapy session integration

**Success Criteria:**
1. Encounter router selects appropriate encounters based on anxiety level (>70 triggers calming)
2. Active negative beliefs trigger encounters that address those specific beliefs
3. Each encounter offers 2-3 interpretation choices affecting player state
4. Introspection offered after 2+ negative interpretations OR high distress (anxiety/overwhelm >70)
5. Conflict visualization shows both beliefs with clear choice options
6. Belief examination flow allows player to choose which belief to keep
7. Synthesis options appear when neither belief feels true
8. Dr. Chen therapy sessions properly connect to belief system
9. Encounter vault has minimum 3 scenarios per belief cluster
10. Interpretation streak tracking works (positive/negative counts)

**Dependencies:**
- Phase 1 (belief and emotion systems must work first)

---

### Phase 3: Game Flow Integration

**Goal:** Connect all systems into a cohesive, playable narrative flow.

**Requirements:**
- FLOW-01: Chapter to encounter flow
- FLOW-02: Encounter to resolution
- FLOW-03: Save/load state persistence
- FLOW-04: Debug tools

**Success Criteria:**
1. Story chapters (ch00, ch01) transition smoothly to encounter system
2. After encounter resolution, game returns to story with updated belief/emotion state
3. GameState persists correctly across Ren'Py save/load
4. Debug HUD displays: current beliefs with intensity, emotion values, active conflicts
5. Main menu and game screens functional
6. Prologue flows into first chapter

**Dependencies:**
- Phase 1 and Phase 2 (all systems must be functional)

---

## Execution Notes

- **Phase 1 is critical path** - All subsequent phases depend on working belief/emotion core
- **Iterative testing recommended** - Test each requirement individually before moving on
- **Debug tools essential** - Implement debug HUD early to verify system behavior
- **Belief system is the anchor** - Everything (emotions, encounters, dialogue) flows from beliefs
