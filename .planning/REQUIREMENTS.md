# Requirements: Introspection - Ren'Py Psychological Visual Novel

**Version:** 1.0
**Date:** 2026-02-16

## v1 Requirements

### Belief System Core

- [ ] **BELIEF-01**: Belief activation from player choices - When player makes interpretation in encounter, relevant beliefs should activate based on the interpretation type
- [ ] **BELIEF-02**: Belief conflict detection - System must detect when contradictory beliefs are both active and calculate severity
- [ ] **BELIEF-03**: Conflict consequence application - Active conflicts should trigger emotional distress (anxiety, overwhelm) and reality shifts
- [ ] **BELIEF-04**: Belief resolution flow - Player should be able to examine and resolve conflicts through introspection
- [ ] **BELIEF-05**: Belief intensity tracking - Track belief states: DORMANT (0), SURFACE (1), ACTIVE (3), CORE (5), EXAMINED (2), RESOLVED (4)

### Emotion System

- [ ] **EMOT-01**: Emotion initialization - All 20+ emotions from Brené Brown taxonomy should initialize to baseline values
- [ ] **EMOT-02**: Emotion adjustment - GameState.adjust_emotions() should modify emotions with bounds (0-100)
- [ ] **EMOT-03**: Emotion-belief feedback - System should surface which beliefs might be active based on current emotions
- [ ] **EMOT-04**: Dominant emotion display - UI should show player's dominant current emotion

### Encounter & Dialogue Steering

- [ ] **ENCO-01**: Encounter router integration - Router should select encounters based on player's emotional state and belief activations
- [ ] **ENCO-02**: Anxiety-based routing - High anxiety (>70) should trigger calming encounters
- [ ] **ENCO-03**: Belief-based routing - Active negative beliefs should trigger encounters that address those beliefs
- [ ] **ENCO-04**: Interpretation choices - Each encounter should offer positive/negative/neutral interpretations that affect beliefs
- [ ] **ENCO-05**: Encounter vault population - Populate encounter vault with sufficient scenarios for each belief cluster

### Introspection & Therapy Mechanics

- [ ] **INTRO-01**: Introspection trigger - Player should be offered introspection after 2+ negative interpretations OR high emotional distress
- [ ] **INTRO-02**: Conflict visualization - Show active belief conflicts with severity and let player choose response
- [ ] **INTRO-03**: Belief examination flow - Player can choose which belief to keep and examine the conflicting one
- [ ] **INTRO-04**: Belief synthesis - When neither belief feels true, offer synthesis options that transcend the conflict
- [ ] **INTRO-05**: Therapy session integration - Dr. Chen therapy sessions should be connected to belief system

### Reality Shifts

- [ ] **REAL-01**: Shift triggers - Reality shifts should trigger based on belief conflicts and acting against beliefs
- [ ] **REAL-02**: Severity levels - Support minor, moderate, severe, and catastrophic shifts
- [ ] **REAL-03**: Visual effects - Appropriate visual feedback for each severity level
- [ ] **REAL-04**: Harmony state - Positive alignment should trigger stability/harmony states

### Game Flow Integration

- [ ] **FLOW-01**: Chapter to encounter flow - Story chapters should transition to encounter system
- [ ] **FLOW-02**: Encounter to resolution - After encounter resolution, return to story with updated state
- [ ] **FLOW-03**: Save/load state persistence - GameState should persist correctly across saves
- [ ] **FLOW-04**: Debug tools - Debug HUD should show current beliefs, emotions, and game state

## v2 Requirements (Deferred)

- Multiple NPCs with independent belief/emotion systems
- Forgiveness arc mechanics
- Achievement system completion
- Multiple story chapters with branching

## Out of Scope

- **AI-generated dialogue**: Using pre-written dialogue only
- **Multiplayer/social features**: Single-player experience only
- **Mobile-specific UI**: Desktop-focused for initial release
- **Audio/music system**: Focus on narrative mechanics first

---

## Traceability

| Requirement | Phase | Priority |
|------------|-------|----------|
| BELIEF-01 through BELIEF-05 | Phase 1 | Critical |
| EMOT-01 through EMOT-04 | Phase 1 | Critical |
| ENCO-01 through ENCO-05 | Phase 2 | High |
| INTRO-01 through INTRO-05 | Phase 2 | High |
| REAL-01 through REAL-04 | Phase 1 | High |
| FLOW-01 through FLOW-04 | Phase 3 | Medium |
