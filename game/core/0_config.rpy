# ============================================================================
# CORE CONFIGURATION
# All game constants and configuration values
# ============================================================================

# Game phases
define GAME_PHASE_STORY = 0
define GAME_PHASE_ENCOUNTER = 1
define GAME_PHASE_INTERPRET = 2
define GAME_PHASE_CONSEQUENCE = 3
define GAME_PHASE_INTROSPECT = 4
define GAME_PHASE_RESOLUTION = 5
define GAME_PHASE_REFLECTION = 6

# Belief intensity levels
define BELIEF_INTENSITY_DORMANT = 0
define BELIEF_INTENSITY_SURFACE = 1
define BELIEF_INTENSITY_ACTIVE = 2
define BELIEF_INTENSITY_CORE = 3
define BELIEF_INTENSITY_EXAMINED = 4
define BELIEF_INTENSITY_RESOLVED = 5

# Transitions
define fade = Fade(0.5, 0.0, 0.5)
define dissolve = Dissolve(0.5)
define quick_fade = Fade(0.2, 0.0, 0.2)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")