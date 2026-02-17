# Project: Introspection - Ren'Py Psychological Visual Novel

**Project Type:** Brownfield (existing codebase refinement)
**Analysis Date:** 2026-02-16

## Core Value

A psychological visual novel where players navigate emotional journeys through a belief-driven system. Players encounter real-world situations that trigger belief activations, emotional responses, and opportunities for introspection and growth through therapy mechanics.

## Problem Statement

The existing codebase has the foundational systems (belief system, emotion tracking, encounter routing, introspection mechanics) but needs:
- Bug fixes and mechanics refinement to make systems work reliably
- Dialogue steering capabilities to guide narrative based on player state
- Complete implementation of therapy/introspection mechanics
- Integration between systems (beliefs → emotions → encounters → dialogue)

## Target Users

Players interested in:
- Narrative-driven games with psychological depth
- Self-reflection and emotional exploration
- Interactive fiction with meaningful choices

## Existing Architecture

### Core Systems (game/core/)
- `0_config.rpy` - Game constants, phase definitions
- `1_game_state.rpy` - Player state class (GameState)
- `2_belief_system.rpy` - Belief activation, conflict resolution
- `3_npc_system.rpy` - NPC state class (NPCState)
- `encounter_router.rpy` - Encounter selection logic
- `introspection_system.rpy` - Introspection mechanics
- `reality_shifts.rpy` - Visual feedback system

### Data Layer (game/0_definitions.rpy)
- Belief definitions (positive, negative, conflict pairs)
- Emotion taxonomy (Brené Brown's Atlas of the Heart)
- Shift severity configurations

### Story Layer (game/story/)
- Script entry points and flow control
- Chapter scripts
- Therapy session scenes

### Content Layer (game/data/)
- NPC definitions
- Encounter scenarios

## Key Constraints

- **Engine:** Ren'Py 8.5.0
- **Language:** Python (embedded in Ren'Py)
- **No external dependencies:** Self-contained within Ren'Py
- **File loading order:** Alphabetical, relies on numeric prefixes for initialization order

## Current System Status

### Working Systems
- Basic GameState class with emotion tracking
- Belief definitions and conflict detection
- Emotion-belief mappings using Brené Brown taxonomy
- Basic encounter vault structure

### Known Issues/Incomplete
- Belief system not fully integrated with game flow
- Introspection mechanics are stubbed/incomplete
- Encounter router has logic but not fully connected
- Dialogue steering based on emotional state not implemented
- Therapy session mechanics need completion

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Belief-driven emotion model | Enables psychological realism and player reflection | Core mechanic established |
| Brené Brown emotion taxonomy | Research-backed, comprehensive emotion model | 20+ emotions mapped to beliefs |
| Encounter-based narrative | Allows state-driven story progression | Enables dialogue steering |

---

*Last updated: 2026-02-16 after project initialization*
