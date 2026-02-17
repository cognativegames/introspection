# INTROSPECTION - DEBUG/AWARENESS HUD
# Shows player state, NPC emotions, active beliefs, and conflicts
# Can be toggled on/off, or shown when introspection_depth is high enough

# Configuration
define config.developer = True  # Set to False for release

# Toggle variables
default show_debug_hud = False
default show_awareness_hud = False
default show_awareness_ui = False

# Keybind to toggle HUD
init python:
    def ToggleHUD():
        global show_debug_hud
        show_debug_hud = not show_debug_hud
        renpy.restart_interaction()

    config.keymap['toggle_debug'] = ['K']
    config.underlay.append(renpy.Keymap(toggle_debug=ToggleHUD))

# ============================================================================
# MAIN HUD SCREEN
# ============================================================================

screen introspection_hud():
    """
    Main HUD - shows when debug is on OR when player has high awareness
    """
    
    # Only show if enabled
    python:
        should_show = show_debug_hud or (
            game_state and (
                game_state.introspection_depth >= 3 or 
                game_state.is_self_awareness_unlocked()
            )
        )
    
    if should_show:
        
        # Dark overlay frame
        frame:
            xalign 0.02
            yalign 0.02
            xsize 400
            background Solid("#000000aa")
            padding (10, 10)
            
            vbox:
                spacing 5
                
                # Header
                text "INTROSPECTION HUD" size 18 color "#00ff00" bold True
                text "(Press K to toggle)" size 12 color "#888888"
                
                null height 5
                
                # Player State Section
                text "=== PLAYER STATE ===" size 14 color "#ffff00"
                
                if game_state:
                    # Emotions - grouped by category
                    text "EMOTIONS:" size 12 color "#ffffff" bold True
                    
                    python:
                        # Group emotions by family
                        emotion_groups = {}
                        for emotion_name, value in game_state.emotions.items():
                            group = game_state.get_emotion_group(emotion_name)
                            if group not in emotion_groups:
                                emotion_groups[group] = []
                            emotion_groups[group].append((emotion_name, value))
                        
                        # Sort each group's emotions by value
                        for group_name in emotion_groups:
                            emotion_groups[group_name].sort(key=lambda x: x[1], reverse=True)
                        
                        # Sort groups by highest emotion value
                        sorted_groups = sorted(emotion_groups.items(), 
                            key=lambda x: max(v for _, v in x[1]), reverse=True)
                    
                    # Display by group (top 4 groups)
                    for group_name, emotions_list in sorted_groups[:4]:
                        # Show group name
                        $ group_display = group_name.replace("_", " ").title() if group_name else "Other"
                        text f"{group_display}:" size 10 color "#ffff88" italic True
                        
                        # Show emotions in this group (already sorted)
                        for emotion, value in emotions_list[:3]:  # Top 3 per group
                            if value >= 2:  # Only show significant emotions (20% of 10)
                                $ color = get_emotion_color(value)
                                hbox:
                                    spacing 5
                                    text f"  {emotion}:" size 11 color "#aaaaaa" xsize 90
                                    bar value value range 10 xsize 120 xalign 0.0
                                    text f"{value}" size 11 color color xsize 35
                        
                        null height 3
                    
                    # Active Beliefs
                    text "ACTIVE BELIEFS:" size 12 color "#ffffff" bold True
                    
                    python:
                        active_beliefs = [(b_id, intensity) for b_id, intensity in game_state.beliefs.items() 
                                            if intensity >= BELIEF_INTENSITY_SURFACE]
                        active_beliefs.sort(key=lambda x: x[1], reverse=True)
                    
                    if active_beliefs:
                        for belief_id, intensity in active_beliefs[:5]:  # Top 5
                            if belief_id in beliefs:
                                $ belief_type = beliefs[belief_id].get("type", "neutral")
                                $ color = "#ff8888" if belief_type == "negative" else "#88ff88" if belief_type == "positive" else "#8888ff"
                                
                                hbox:
                                    text f"({get_intensity_name(intensity)})" size 10 color "#888888" xsize 80
                                    text f"{beliefs[belief_id]['statement'][:30]}..." size 10 color color
                    else:
                        text "None active yet" size 11 color "#666666" italic True
                    
                    null height 5
                    
                    # Conflicts
                    python:
                        conflicts = game_state.detect_belief_conflicts()
                    
                    if conflicts:
                        text "CONFLICTS:" size 12 color "#ff0000" bold True
                        
                        for b1, b2, severity in conflicts[:3]:  # Top 3
                            if b1 in beliefs and b2 in beliefs:
                                text f"• {beliefs[b1]['statement'][:25]}... VS {beliefs[b2]['statement'][:25]}..." size 9 color "#ffaaaa"
                    
                    null height 5
                    
                    # Meta stats
                    text "PROGRESS:" size 12 color "#ffffff" bold True
                    text f"Introspection Depth: {game_state.introspection_depth}" size 11 color "#aaaaaa"
                    text f"Chapter: {game_state.chapter}" size 11 color "#aaaaaa"
                    text f"Phase: {get_phase_name(game_state.phase)}" size 11 color "#aaaaaa"

# ============================================================================
# NPC MONITORING SCREEN
# Shows emotions and beliefs of NPCs you've interacted with
# ============================================================================

screen npc_monitor():
    """
    Shows state of NPCs player has met
    Useful for debugging NPC reactions
    """
    
    if show_debug_hud:
        
        frame:
            xalign 0.98
            yalign 0.02
            xsize 400
            background Solid("#000000aa")
            padding (10, 10)
            
            viewport:
                ysize 800
                scrollbars "vertical"
                mousewheel True
                
                vbox:
                    spacing 10
                    
                    text "=== NPC STATES ===" size 18 color "#00ff00" bold True
                    
                    null height 5
                    
                    # Show each NPC
                    python:
                        monitored_npcs = ["dr_chen", "becky", "jill"]  # Add more as needed
                    
                    for npc_id in monitored_npcs:
                        if npc_id in npc_states:
                            $ npc = npc_states[npc_id]
                            
                            # NPC Name
                            text npc.name.upper() size 14 color "#ffff00" bold True
                            
                            # Relationship with player
                            python:
                                rel = npc.get_relationship_with("player")
                            
                            text f"Trust: {rel.get('trust', 0)}" size 11 color "#aaaaaa"
                            text f"Witnessed Change: {rel.get('witnessed_change', 0)}" size 11 color "#aaaaaa"
                            
                            # Top emotions
                            python:
                                top_emotions = sorted(npc.emotions.items(), key=lambda x: x[1], reverse=True)[:3]
                            
                            hbox:
                                spacing 10
                                for emotion, value in top_emotions:
                                    text f"{emotion}: {value}" size 10 color get_emotion_color(value)
                            
                            # Active beliefs
                            python:
                                npc_active_beliefs = [(b, i) for b, i in npc.beliefs.items() if i >= BELIEF_INTENSITY_ACTIVE]
                            
                            if npc_active_beliefs:
                                text f"Beliefs: {len(npc_active_beliefs)} active" size 10 color "#888888"
                            
                            # Recent memories
                            if npc.memories:
                                $ recent = npc.memories[-1]
                                text f"Last memory: {recent['type']}" size 9 color "#666666" italic True
                            
                            null height 10

# ============================================================================
# COMPACT AWARENESS INDICATOR
# Shows only when player has awareness, minimal UI
# ============================================================================

screen awareness_indicator():
    """
    Minimal indicator that shows when player has high introspection depth
    Just shows conflicts and dominant emotion
    """
    
    if game_state and game_state.introspection_depth >= 4 and not show_debug_hud:
        
        frame:
            xalign 0.5
            yalign 0.95
            background Solid("#00000088")
            padding (15, 8)
            
            hbox:
                spacing 20
                
                # Dominant emotion
                python:
                    dominant = game_state.get_dominant_emotion()
                
                if dominant:
                    text f"Feeling: {dominant.title()}" size 14 color get_emotion_color(game_state.emotions[dominant])
                
                # Active conflicts indicator
                python:
                    conflicts = game_state.detect_belief_conflicts()
                
                if conflicts:
                    text "⚠ Internal Conflict" size 14 color "#ff8888" bold True
                
                # Introspection depth
                for i in range(game_state.introspection_depth):
                    text "●" size 16 color "#00ffff"

# ============================================================================
# SELF-AWARENESS TOGGLE
# Static icon that appears when self-awareness >= 70%
# ============================================================================

screen self_awareness_toggle():
    """
    Shows an icon when self-awareness is unlocked (>= 70%)
    Clicking it toggles the full awareness UI
    """
    
    # Only show when self-awareness is unlocked
    if game_state and game_state.is_self_awareness_unlocked():
        
        # Static icon in bottom-right corner
        imagebutton:
            xalign 0.98
            yalign 0.98
            idle "gui/window_icon.png"  # Use game's window icon or a custom one
            hover "gui/window_icon.png"
            action ToggleVariable("show_awareness_ui")
            tooltip "Self-Awareness: %d%%" % game_state.get_self_awareness_percentage()
        
        # Show awareness UI when toggled on
        if show_awareness_ui:
            frame:
                xalign 0.95
                yalign 0.85
                xsize 300
                background Solid("#000000aa")
                padding (15, 10)
                
                vbox:
                    spacing 5
                    
                    text "SELF-AWARENESS" size 14 color "#00ffff" bold True
                    
                    python:
                        awareness_pct = game_state.get_self_awareness_percentage()
                        awareness_val = game_state.calculate_self_awareness()
                    
                    # Progress bar
                    bar value awareness_val range 10 xsize 200
                    
                    text "%d%%" % awareness_pct size 12 color "#00ffff"
                    
                    null height 5
                    
                    # Show active beliefs summary
                    text "Active Beliefs:" size 11 color "#aaaaaa"
                    
                    python:
                        active = [(b, i) for b, i in game_state.beliefs.items() 
                                  if i >= BELIEF_INTENSITY_SURFACE]
                    
                    if active:
                        for bid, intensity in active[:3]:
                            if bid in beliefs:
                                $ btype = beliefs[bid].get("type", "neutral")
                                $ color = "#ff8888" if btype == "negative" else "#88ff88" if btype == "positive" else "#8888ff"
                                text "• %s" % beliefs[bid]["statement"][:30] size 10 color color
                    else:
                        text "None yet" size 10 color "#666666" italic True
                    
                    null height 10
                    
                    text "Click icon to close" size 9 color "#666666" italic True

# ============================================================================
# EMOTION INSPECTOR - Hover to see Brené Brown definition
# ============================================================================

screen emotion_inspector():
    """
    Shows emotion definitions on hover
    Educates player about emotions
    """
    
    if show_debug_hud and game_state:
        
        frame:
            xalign 0.02
            yalign 0.70
            xsize 400
            background Solid("#000000aa")
            padding (10, 10)
            
            vbox:
                spacing 5
                
                text "EMOTION GUIDE" size 14 color "#ffff00" bold True
                text "(Brené Brown's Atlas)" size 10 color "#888888" italic True
                
                null height 5
                
                # Show top 3 active emotions with definitions
                python:
                    top_emotions = sorted(game_state.emotions.items(), 
                        key=lambda x: x[1], reverse=True)[:3]
                
                for emotion, value in top_emotions:
                    if value >= 2:  # 20% of 10 scale
                        $ definition = game_state.get_emotion_definition(emotion)
                        $ related = game_state.get_related_beliefs(emotion)
                        
                        # Emotion name and value
                        hbox:
                            text emotion.upper() size 12 color get_emotion_color(value) bold True
                            text f" ({value})" size 11 color "#888888"
                        
                        # Definition
                        text definition size 9 color "#cccccc" italic True
                        
                        # Related beliefs (if any)
                        if related:
                            text f"→ Linked beliefs: {', '.join(related[:2])}" size 8 color "#888888"
                        
                        null height 8

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

init python:
    def get_emotion_color(value):
        """Return color based on emotion intensity (0-10 scale)"""
        if value >= 7:
            return "#ff0000"  # Red - very high
        elif value >= 5:
            return "#ffaa00"  # Orange - high
        elif value >= 3:
            return "#ffff00"  # Yellow - moderate
        else:
            return "#00ff00"  # Green - low
    
    def get_intensity_name(intensity):
        """Convert intensity number to name"""
        names = {
            0: "DORMANT",
            1: "SURFACE",
            2: "ACTIVE",
            3: "CORE",
            4: "EXAMINED",
            5: "RESOLVED"
        }
        return names.get(intensity, "UNKNOWN")
    
    def get_phase_name(phase):
        """Convert phase number to name"""
        names = {
            0: "STORY",
            1: "ENCOUNTER",
            2: "INTERPRET",
            3: "CONSEQUENCE",
            4: "INTROSPECT",
            5: "RESOLUTION",
            6: "REFLECTION"
        }
        return names.get(phase, "UNKNOWN")

# ============================================================================
# BELIEF TREE VISUALIZER
# Shows player's belief tree with conflicts highlighted
# ============================================================================

screen belief_tree():
    """
    Visual tree of beliefs
    Press T to toggle
    """
    
    if show_debug_hud:
        
        frame:
            xalign 0.5
            yalign 0.5
            xsize 800
            ysize 600
            background Solid("#000000dd")
            padding (20, 20)
            
            vbox:
                text "BELIEF TREE" size 24 color "#00ff00" bold True
                text "(Organized by domain)" size 12 color "#888888"
                
                null height 10
                
                viewport:
                    ysize 500
                    scrollbars "vertical"
                    mousewheel True
                    
                    vbox:
                        spacing 15
                        
                        # Group beliefs by domain
                        python:
                            beliefs_by_domain = {}
                            
                            for belief_id, intensity in game_state.beliefs.items():
                                if intensity > 0 and belief_id in beliefs:
                                    domain = beliefs[belief_id].get("domain", "unknown")
                                    
                                    if domain not in beliefs_by_domain:
                                        beliefs_by_domain[domain] = []
                                    
                                    beliefs_by_domain[domain].append((belief_id, intensity))
                        
                        # Display each domain
                        for domain, belief_list in beliefs_by_domain.items():
                            text domain.upper().replace("-", " ") size 16 color "#ffff00" bold True
                            
                            for belief_id, intensity in belief_list:
                                $ belief = beliefs[belief_id]
                                $ belief_type = belief.get("type", "neutral")
                                $ color = "#ff8888" if belief_type == "negative" else "#88ff88" if belief_type == "positive" else "#8888ff"
                                
                                # Check if in conflict
                                python:
                                    in_conflict = False
                                    conflicts = game_state.detect_belief_conflicts()
                                    for c1, c2, sev in conflicts:
                                        if belief_id == c1 or belief_id == c2:
                                            in_conflict = True
                                            break
                                
                                hbox:
                                    spacing 10
                                    
                                    if in_conflict:
                                        text "⚠" size 16 color "#ff0000"
                                    
                                    text f"({get_intensity_name(intensity)})" size 11 color "#666666" xsize 100
                                    text belief["statement"] size 12 color color
                            
                            null height 10

# ============================================================================
# AUTO-SHOW HUD IN SCREENS
# ============================================================================

# Add to default screens that are always shown
init python:
    #config.overlay_screens.append("introspection_hud")
    config.overlay_screens.append("npc_monitor")
    config.overlay_screens.append("awareness_indicator")
    config.overlay_screens.append("emotion_inspector")
    config.overlay_screens.append("self_awareness_toggle")
    
# ============================================================================
# QUICK REFERENCE - KEYBINDS
# ============================================================================

# K = Toggle full debug HUD
# T = Toggle belief tree (when debug is on)
# Press during gameplay to see internal state

# For release version, set show_debug_hud based on settings menu
# Or unlock as player gains introspection_depth
