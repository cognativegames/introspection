# MIGRATION GUIDE

## Quick Start

1. **Backup your old project** (you already have it in game.zip)
2. **Copy this refactored folder** to your RenPy projects directory
3. **Test the game** - run it and verify it works
4. **Review changes** - read README.md for full details

## What Was Fixed

### Critical Bug Fixes
✅ Eliminated all init 10/init 20 race conditions
✅ Fixed "function not defined" errors
✅ Consolidated split class definitions
✅ Removed monkey-patching anti-pattern

### Organizational Improvements
✅ Clear directory structure
✅ Logical file grouping
✅ Consistent naming conventions
✅ Single source of truth for each concern

## File Mapping

### Old → New Locations

**Core Systems:**
- `core/constants.rpy` → `core/config.rpy` (renamed, no init priority)
- `core/models/GameState/GameState.rpy` + `methods/*.rpy` → `core/game_state.rpy` (consolidated)
- `core/models/EncounterRouter/EncounterRouter.rpy` + `methods/*.rpy` → `core/encounter_router.rpy` (consolidated)
- `core/beliefs.rpy` → `core/belief_system.rpy` (cleaned up)
- `core/forgiveness.rpy` → `core/forgiveness_system.rpy`
- `core/introspection.rpy` → `core/introspection_system.rpy`
- `core/reality_shifts.rpy` → `core/reality_shifts.rpy`

**Data:**
- `data/variables.rpy` → `data/variables.rpy` (updated)
- `data/characters/*.rpy` → `data/characters.rpy` (consolidated)
- `core/context/encounters/*.rpy` → `data/encounters/*.rpy` (moved)
- NEW: `data/beliefs/belief_data.rpy` (template for belief definitions)

**Story:**
- `story/main_script.rpy` → `story/script.rpy` (renamed)
- `story/chapter00/prologue.rpy` → `story/chapter_00.rpy` (flattened)
- `story/chapter01/chapter_01_complete.rpy` → `story/chapter_01.rpy` (flattened)
- `story/therapy/*` → `story/therapy/*` (preserved)

**UI:**
- `ui/screens.rpy` → `screens/main_screens.rpy`
- `core/debug_hud.rpy` → `screens/debug_hud.rpy` (moved)

## Key Changes to Review

### 1. GameState Class
The class is now fully defined in one file (`core/game_state.rpy`) with all methods inline.

**Old way (DON'T do this):**
```python
# In GameState.rpy
init 10 python:
    class GameState:
        def __init__(self):
            # ...

# In methods/activate_belief.rpy  
init 20 python:
    def activate_belief(self, belief_id):
        # ...
    GameState.activate_belief = activate_belief  # Monkey-patching!
```

**New way (DO this):**
```python
# All in core/game_state.rpy
init python:
    class GameState:
        def __init__(self):
            # ...
        
        def activate_belief(self, belief_id):
            # Method defined right in the class!
```

### 2. Constants
All constants are now defined with `define` instead of in `init python:` blocks.

**Old way:**
```python
init python:
    GAME_PHASE_STORY = 0
```

**New way:**
```python
define GAME_PHASE_STORY = 0
```

### 3. Encounters
Encounters are now in `data/encounters/` and use `init python:` instead of `init 20 python:`

All init priorities have been removed - they were unnecessary and causing problems.

## Testing Checklist

1. ✓ Game starts without errors
2. ✓ GameState initializes correctly
3. ✓ Constants are accessible
4. ✓ Beliefs system works
5. ✓ Encounters can be selected
6. ✓ Story flow is intact
7. ✓ Debug HUD displays

## Next Steps

1. **Populate Content:**
   - Add belief definitions to `data/beliefs/belief_data.rpy`
   - Add encounter definitions to `data/encounters/`
   - Complete character initialization in `data/characters.rpy`

2. **Extend Story:**
   - Add new chapters in `story/`
   - Extend therapy sessions in `story/therapy/`

3. **Add Features:**
   - New game mechanics go in `core/`
   - New screens go in `screens/`
   - New data goes in `data/`

## Need Help?

The structure is now intuitive and follows RenPy best practices. If you're unsure where something goes:

- **Is it game logic/mechanics?** → `core/`
- **Is it static data/definitions?** → `data/`
- **Is it story/narrative content?** → `story/`
- **Is it UI/display related?** → `screens/`
- **Is it media (images/audio)?** → `assets/`

## Benefits of New Structure

1. **No More Race Conditions** - Everything loads in the right order
2. **Easy to Navigate** - Clear hierarchy and organization
3. **Scalable** - Easy to add new content without confusion
4. **Maintainable** - Related code is grouped together
5. **Debuggable** - Clear separation of concerns
6. **Professional** - Follows industry best practices

Enjoy your refactored codebase!
