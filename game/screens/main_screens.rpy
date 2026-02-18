# Introspection - UI Screens
# ./game/screens.rpy

# ============================================
# EMOTIONAL HUD
# ============================================

screen emotional_hud():
    """Display emotional state in corner"""
    
    zorder 100
    
    frame:
        xalign 0.98
        yalign 0.02
        xsize 200
        background "#000000cc"
        padding (15, 10)
        
        vbox:
            spacing 8
            
            text "Emotional State" size 18 color "#ffffff" xalign 0.5
            
            # Show top 3 emotions
            python:
                sorted_emotions = sorted(game.emotions.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)[:3]
            
            for emotion, value in sorted_emotions:
                hbox:
                    spacing 8
                    
                    text "[emotion.title()]" size 14 min_width 80 color "#cccccc"
                    
                    bar value value range 100 xsize 80 ysize 10 left_bar "#4ecdc4" right_bar "#333333"

# ============================================
# BELIEF NOTIFICATION
# ============================================

screen belief_notification(belief_text, belief_type):
    """Show when beliefs activate"""
    
    zorder 200
    
    frame:
        xalign 0.5
        yalign 0.15
        background "#000000dd"
        padding (25, 15)
        
        hbox:
            spacing 15
            
            if belief_type == "positive":
                text "✨" size 28
            else:
                text "⚠️" size 28
            
            vbox:
                spacing 5
                text "Belief Activated" size 14 color "#999999"
                text "[belief_text]" size 18 italic True color "#ffffff"
    
    # Auto-hide after 2 seconds
    timer 2.0 action Hide("belief_notification")

# ============================================
# INTROSPECTION PROMPT
# ============================================

screen introspection_prompt():
    """Offer introspection"""
    
    modal True
    zorder 300
    
    # Dim background
    add "#00000080"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        background "#1a1a2e"
        padding (40, 30)
        
        vbox:
            spacing 25
            
            text "Something feels... off." size 26 xalign 0.5 color "#9370db"
            
            text ("You notice tension in your chest.\n" + "The world doesn't quite make sense right now.") size 18 xalign 0.5 color "#cccccc"
            
            null height 10
            
            text "Do you want to look deeper?" size 20 xalign 0.5 color "#4ecdc4"
            
            null height 15
            
            hbox:
                spacing 30
                xalign 0.5
                
                textbutton "Explore this feeling":
                    action Jump("begin_introspection")
                    xsize 250
                    ysize 50
                    text_size 18
                
                textbutton "Not right now":
                    action Jump("encounter_loop")
                    xsize 250
                    ysize 50
                    text_size 18

# ============================================
# SIMPLE CHOICE MENU (Optional Enhancement)
# ============================================

screen choice_menu(items):
    """Enhanced choice menu"""
    
    style_prefix "choice"
    
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 15
        
        for i in items:
            textbutton i.caption:
                action i.action
                xsize 600

# ============================================
# BASIC STYLES (if you don't have them)
# ============================================

style choice_vbox:
    spacing 10

style choice_button:
    background "#1a1a2e"
    hover_background "#4ecdc4"
    padding (20, 15)
    xsize 600

style choice_button_text:
    size 18
    color "#ffffff"
    hover_color "#000000"
    xalign 0.5