# Phase 1: Belief & Emotion Core - Context

**Gathered:** 2026-02-16
**Status:** Ready for planning

<domain>
## Phase Boundary

Fix and complete core belief system and emotion mechanics. Beliefs drive emotions AND dialogue options. All subsequent systems (encounters, therapy, dialogue) depend on this working correctly.

</domain>

<decisions>
## Implementation Decisions

### Belief Mechanics

- **Activation:** Beliefs activate through both dialogue choices AND player actions
- **Conflict handling:** Conflicts don't need separate UI - negative beliefs ARE the conflict. When contradictory beliefs are active, emotions spike (anxiety, fear, overwhelm, cluster-specific)
- **Intensity display:** Narrative reflection with physical/emotional markers (heart race, nausea, sweaty palms, positive tingles, relief)
- **Self-awareness calculation:** Inverse of negative belief intensity sum - fewer/lower negative beliefs = higher self-awareness
- **Self-awareness effects:** Unlocks at 70% threshold, affects both dialogue AND UI
- **Belief resolution:** Player can accept positive (rewards) or negative (continue suffering, story steers). Therapy sessions replayable with variations based on state (AVN groundhog day model)
- **Therapy unlock:** Day-by-day milestones

### Emotion Display

- **NPC emotions:** Conveyed through image variants (expression changes) + dialogue hints ("looks sad", "giggles"). Narrative controls HOW NPC expresses emotion
- **Player emotions:** Conveyed through narration, UI (only when self-awareness >70%), visual effects (flash, red blink, blur, transitions)
- **Scale:** 0-10 range
- **Update timing:** Immediate after belief change in therapy/introspection
- **Emotion derivation:** Values calculated FROM belief scores, not set independently. Dormant beliefs limit dialogue but don't affect emotion until conflict triggers

### Reality Shift Effects

- **Prominence:** Simplified, primarily early story when player is recreating base reality
- **Severity:** Calculated from belief type (dormant vs active) and player awareness
- **Effects:** Screen effects (blur, color shift) + sprite changes + audio cues
- **Manual override:** Can be set explicitly in dialogue if needed

### Player Feedback

- **Debug HUD:** Full debug showing all belief values, emotions, conflicts, self-awareness
- **Player-facing UI:** Toggle with static icon in corner, icon appears only when self-awareness >70%
- **Self-awareness threshold:** 70% unlocks the state display UI

</decisions>

<specifics>
## Specific Ideas

- "All negative beliefs are conceptually conflicting beliefs by design" - energy through positive beliefs = excitement/hope, through negative = anxiety/fear
- Therapy sessions similar to harem AVN - play same day over until milestone
- Groundhog day model for solo/group therapy sessions
- Self-awareness calculation helps player "see" their emotions better

</specifics>

<deferred>
## Deferred Ideas

- None - all discussion stayed within Phase 1 scope

</deferred>

---

*Phase: 01-belief-emotion-core*
*Context gathered: 2026-02-16*
