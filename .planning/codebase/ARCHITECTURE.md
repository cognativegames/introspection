# Architecture

**Analysis Date:** 2026-02-16

## Pattern Overview

**Overall:** Unified Entity System with Belief-Driven Psychology

**Key Characteristics:**
- Player and ALL NPCs use identical state management (beliefs, emotions, memories)
- Beliefs drive emotions, emotions drive behavior
- Conflict detection between contradictory beliefs
- Reality shifts visualize internal psychological states

## Layers

### Core Engine Layer
- Purpose: State management and game logic
- Location: `game/core/`
- Files:
  - `0_config.rpy` - Game constants, phase definitions
  - `1_game_state.rpy` - Player state class (GameState)
  - `2_belief_system.rpy` - Belief activation, conflict resolution
  - `3_npc_system.rpy` - NPC state class (NPCState)
  - `encounter_router.rpy` - Encounter selection logic

### Data Layer
- Purpose: Definitions and static data
- Location: `game/0_definitions.rpy`
- Contains:
  - Belief definitions (positive, negative, conflict pairs)
  - Emotion taxonomy (Brené Brown's Atlas of the Heart)
  - Shift severity configurations

### Story Layer
- Purpose: Narrative content and scenes
- Location: `game/story/`
- Files:
  - `script.rpy` - Entry point and flow control
  - `chapter_00.rpy`, `chapter_01.rpy` - Story chapters
  - `therapy/` - Therapy session scenes

### Content Layer
- Purpose: Game content (characters, encounters)
- Location: `game/data/`
- Directories:
  - `characters/` - NPC definitions
  - `encounters/` - Encounter scenarios
  - `npc_data.rpy` - NPC initialization

## Data Flow

**Core Flow:**
```
1. Story Chapter → Triggers encounter loop
2. Encounter Router → Selects scenario based on emotions/beliefs
3. Player Interpretation → Activates beliefs
4. Belief Activation → Triggers emotional response
5. Conflict Detection → If contradictory beliefs active
6. Reality Shift → Visual feedback of internal state
7. Introspection → Optional deep examination
8. Resolution → Beliefs modified, emotions adjusted
9. Return to Story → Continue narrative
```

**State Management:**
- Single `game_state` instance (global)
- Multiple `NPCState` instances in `npc_states{}` dictionary
- Belief intensity scale: 0 (DORMANT) → 5 (RESOLVED)
- Emotion scale: 0-100

## Key Abstractions

### GameState Class
- Purpose: Player's complete internal state
- Location: `game/core/1_game_state.rpy`
- Key methods:
  - `activate_belief(belief_id, intensity)` - Add/modify belief
  - `detect_belief_conflicts()` - Find contradictory beliefs
  - `apply_conflict_consequences()` - Calculate distress
  - `adjust_emotions(changes)` - Modify emotional state

### NPCState Class
- Purpose: Mirror of player state for NPCs
- Location: `game/core/3_npc_system.rpy`
- Same methods as GameState plus:
  - `interpret_player_action()` - How NPC views player
  - `remember_event()` - Store interactions
  - `get_therapy_topic()` - What to share in group

### EncounterRouter Class
- Purpose: Select appropriate encounters
- Location: `game/core/encounter_router.rpy`
- Selection criteria:
  - High anxiety → calming encounters
  - Deep introspection → complex encounters
  - Active negative beliefs → targeted encounters

## Entry Points

**Main Entry:**
- Location: `game/story/script.rpy`
- Label: `label start:`
- Initializes game_state and NPCs, jumps to prologue

**Chapter Flow:**
- `label main_game_flow:` - Routes to correct chapter
- Chapter labels: `chapter_01`, `chapter_02`, etc.

## Error Handling

**Approach:**
- Try/except blocks in Python code
- Ren'Py's built-in rollback for story choices
- Fallback default values in state initialization

**Debug Tools:**
- `game/screens/debug_hud.rpy` - Debug overlay

---

*Architecture analysis: 2026-02-16*
