# INTROSPECTION - Refactored Project Structure

## Overview
This is a complete refactoring of your RenPy game following best practices. The code has been reorganized for clarity, maintainability, and scalability.

## Key Changes Made

### 1. Eliminated Init Priority Issues
- **Before**: Classes defined at `init 10`, methods monkey-patched at `init 20`
- **After**: All classes and methods defined together in single files with default `init python:`
- **Why**: Eliminates race conditions and "function not defined" errors

### 2. Consolidated Class Definitions
- **Before**: GameState class split across 10+ files
- **After**: Single file with all methods inline
- **Files affected**:
  - `core/game_state.rpy` - Complete GameState class
  - `core/encounter_router.rpy` - Complete EncounterRouter class

### 3. Clear Separation of Concerns
```
game/
├── core/           # Game mechanics and systems
├── data/           # Static data and definitions
├── story/          # Narrative content
├── screens/        # UI and interface
└── assets/         # Media files
```

### 4. Removed Redundancy
- Eliminated duplicate belief systems
- Consolidated character definitions
- Merged scattered utility functions

## New Directory Structure

### `/core/` - Game Mechanics
- `config.rpy` - All constants (GAME_PHASE_*, BELIEF_INTENSITY_*, etc.)
- `game_state.rpy` - GameState class with all methods
- `encounter_router.rpy` - EncounterRouter class
- `belief_system.rpy` - Belief mechanics and labels
- `forgiveness_system.rpy` - Forgiveness/redemption mechanics
- `introspection_system.rpy` - Introspection mechanics
- `reality_shifts.rpy` - Reality shift system

### `/data/` - Static Data
- `variables.rpy` - All game variables and defaults
- `characters.rpy` - All character definitions
- `encounters/` - Encounter definitions
  - `_index.rpy` - Encounter registry (populate with your encounters)
  - `stranger_smile.rpy`, `dog_park.rpy`, etc.
- `beliefs/` - Belief definitions (to be populated)

### `/story/` - Narrative Content
- `script.rpy` - Main game flow and entry point
- `chapter_00.rpy` - Prologue
- `chapter_01.rpy` - Chapter 1
- `therapy/` - Therapy session mechanics

### `/screens/` - UI
- `main_screens.rpy` - Main UI screens
- `debug_hud.rpy` - Debug overlay

### `/assets/` - Media Files
- `audio/` - Sound and music
- `images/` - Graphics
- `fonts/` - Typography

## How to Use

### Starting the Game
1. The entry point is `label start` in `story/script.rpy`
2. Game state is automatically initialized
3. Flow goes: start → prologue → chapters

### Adding New Content

#### New Encounter
1. Create file in `data/encounters/your_encounter.rpy`
2. Define encounter dict with proper structure
3. Add to encounters registry in `data/encounters/_index.rpy`

#### New Belief
1. Create file in `data/beliefs/belief_name.rpy`
2. Define belief with proper structure
3. Add to beliefs registry

#### New Chapter
1. Create `story/chapter_XX.rpy`
2. Add label `chapter_XX`
3. Add jump logic in `story/script.rpy`

### Best Practices

#### DO:
- Put all class methods directly in the class definition
- Use `define` for constants
- Use `default` for variables
- Keep related code in the same file
- Use clear, descriptive names

#### DON'T:
- Use init priorities unless absolutely necessary
- Monkey-patch methods onto classes
- Split class definitions across files
- Duplicate functionality
- Use global functions when methods make more sense

## Fixed Issues

### Race Condition Bugs
- ✅ Constants now loaded before classes
- ✅ Classes fully defined before use
- ✅ No more "function not defined" errors

### Organization Issues
- ✅ Clear file hierarchy
- ✅ Consistent naming conventions
- ✅ Logical grouping of related code
- ✅ No more scattered concerns

### Code Quality
- ✅ Classes defined in single files
- ✅ Methods included in class definitions
- ✅ Proper separation of concerns
- ✅ Eliminated redundancy

## Next Steps

### Immediate
1. Review the refactored structure
2. Test game startup and basic flow
3. Populate missing content (encounters, beliefs)

### Scaling the Game
1. Add new chapters in `story/` directory
2. Add new encounters in `data/encounters/`
3. Add new belief definitions in `data/beliefs/`
4. Extend GameState class methods as needed

### Adding Features
- **New character**: Add to `data/characters.rpy`
- **New game phase**: Add constant to `core/config.rpy`
- **New system**: Create new file in `core/`
- **New screen**: Add to `screens/`

## File Naming Conventions
- Snake_case for files: `my_file.rpy`
- Clear descriptive names: `belief_system.rpy` not `beliefs.rpy`
- Prefix with category: `chapter_01.rpy`, not just `01.rpy`

## Code Style
- Classes: PascalCase (`GameState`, `EncounterRouter`)
- Methods: snake_case (`activate_belief`, `select_encounter`)
- Constants: UPPER_SNAKE_CASE (`GAME_PHASE_STORY`)
- Variables: snake_case (`game_state`, `player_name`)

## Debugging
The debug HUD is still available in `screens/debug_hud.rpy`. Use it to:
- Monitor game state
- Track beliefs
- Check emotions
- View relationships

## Questions?
The structure is now intuitive and follows RenPy best practices. Each file has a clear purpose, and the organization makes it obvious where to put new content.

Happy coding!
