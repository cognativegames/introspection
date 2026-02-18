# External Integrations

**Analysis Date:** 2026-02-16

## No External Integrations

This project is a self-contained Ren'Py visual novel with no external API calls, cloud services, or third-party integrations.

## Local-Only Systems

**Data Storage:**
- Save files: `game/saves/` - Local filesystem
- Persistent data: `game/saves/persistent` - Ren'Py native save system

**Assets:**
- Images: `game/assets/` - Local image files
- Audio: `game/audio/` - Local audio files (if present)

## Development Tools

**ComfyUI Integration (for character generation):**
- Workflow files in `.comfyui/` - Local JSON configs
- Output: Character pose sets (JSON + renders)
- Not connected to any external service during runtime

**Version Control:**
- Git - Local version control
- GitHub - Remote hosting (`.github/workflows/build.yml`)

## Environment Configuration

**No environment variables required:**
- No `.env` files present
- No API keys needed
- No external service credentials

**Game Configuration:**
- All config in `game/core/0_config.rpy`
- Belief definitions in `game/0_definitions.rpy`

## Runtime Environment

**Platform:**
- Desktop - Windows/Mac/Linux via Ren'Py
- Web build possible via Ren'Py

**No network calls during gameplay:**
- No analytics
- No telemetry
- No content delivery network (CDN)
- Fully offline-capable

---

*Integration audit: 2026-02-16*
