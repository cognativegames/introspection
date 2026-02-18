# Technology Stack

**Analysis Date:** 2026-02-16

## Language & Engine

**Primary:**
- Ren'Py 8.5.0 - Visual novel game engine
- Python (embedded in Ren'Py) - Game logic and state management

**Secondary:**
- Ren'Py Script (.rpy) - Game script files
- Ren'Py Bytecode (.rpyc) - Compiled scripts

## Game Engine

**Core:**
- Ren'Py 8.5.0 - Visual novel framework
  - Scene management
  - Character display
  - Transition effects
  - Save/load system

**Build:**
- Ren'Py Launcher - Development environment
- Ren'Py Compiler - Compiles .rpy to .rpyc

## Key Dependencies

**Ren'Py Built-ins:**
- `Fade`, `Dissolve` - Transition effects
- `renpy.call()` - Label invocation
- `renpy.scene()` - Scene management
- `renpy.jump()` - Flow control

**Python Standard Library (embedded):**
- `random` - Encounter selection
- `json` - Data serialization

## Project Configuration

**Game Config:**
- `game/` - Main game directory
- `.rpy` files loaded alphabetically at startup
- `0_definitions.rpy`, `1_game_state.rpy`, `2_belief_system.rpy` use prefix ordering

**Entry Point:**
- `game/story/script.rpy` - Contains `label start:` entry point

## No External Dependencies

This project has:
- No npm/node dependencies
- No external Python packages (PyPI)
- No cloud services
- No external APIs

All functionality is self-contained within Ren'Py and Python standard library.

---

*Stack analysis: 2026-02-16*
