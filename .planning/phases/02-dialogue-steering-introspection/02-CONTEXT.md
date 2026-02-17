# Phase 2: Dialogue Steering & Introspection - Context

**Gathered:** 2026-02-17
**Status:** Ready for planning

<domain>
## Phase Boundary

Implement encounter routing based on player state and complete the introspection/therapy mechanics. Encounters are therapy sessions where therapist (Dr. Chen) offers scenarios to help player transform negative beliefs into positive ones. Goal: coach player toward healthier belief system through NSFW AVN experiences with accountability.

</domain>

<decisions>
## Implementation Decisions

### Encounter Routing
- **Logic:** Hybrid of story progression + character state (emotions, beliefs)
- **Access:** Player cannot access encounters directly - therapist (Dr. Chen) offers them
- **Selection:** Therapist selects based on player's current negative beliefs and emotional state
- **Belief-tier:** Encounters mapped to belief tiers - player progresses through tiers

### Introspection Triggers
- **When offered:** After 2+ negative interpretations
- **What shows:** Both beliefs AND emotions
- **Player options:**
  - Examine and resolve belief (drop negative, assign positive → emotions shift immediately)
  - Decline introspection → "living in denial" → enhanced negative emotions (loneliness, emptiness, detachment)
- **Narrative:** Feelings are indicators of beliefs. Introspection asks: "What must I believe is true about myself for me to feel this way?"

### Therapy Structure
- **Session model:** Day-by-day
- **Groundhog day:** Replay same day until milestone achieved
- **Therapist role:** Dr. Chen offers encounters, provides reflection after choices
- **Belief change:** Immediate - resolving negative belief instantly shifts related emotions
- **Progression:** Player drops negative belief → assigns positive belief → emotions align with new belief

### Encounter Vault
- **Clusters:** Best first approach - start focused (self-worth, relationships, capability), scale to all 6 later
- **Content:** Dynamic - adapts based on current belief states
- **Variety:** 3+ scenarios per active cluster minimum
- **Visual presentation:** Hybrid - narrated with dialog, visuals from player character's imagination. Visuals change based on beliefs (e.g., dog appears friendly or aggressive based on belief state). All encounters are neutral - player's beliefs trigger emotions.
- **NSFW:** Full explicit, zero censorship. "Evil path" arcs hold player extremely accountable - guilt, shame, remorse when manipulating NPCs

</decisions>

<specifics>
## Specific Ideas

- NSFW AVN with therapy overlay - player imagines scenarios, processes through Dr. Chen
- Goal: subtly coach player away from NSFW toward healthier beliefs
- Visual changes based on belief state - same scene appears different based on player's internal state
- "Evil path" consequences - player feels extreme negative emotions when acting against positive beliefs

</specifics>

<deferred>
## Deferred Ideas

- Expansion to all 6 belief clusters (start with 3)
- Specific encounter scenarios (to be created during implementation)
- Visual asset requirements for dynamic imagery

</deferred>

---

*Phase: 02-dialogue-steering-introspection*
*Context gathered: 2026-02-17*
