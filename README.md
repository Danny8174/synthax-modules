
# Synthax: AI-Native Programming Language (Phase 2)

Welcome to the Synthax Phase 2 Modules repository â€” a collection of core tools, AI extensions, and interface utilities designed for the world's first **AI-native programming language**.

---

## Overview

Synthax is built for human-readability and machine-cooperation. These modules allow users to write, run, and extend `.synth` code with voice, assistants, and persistent tools.

---

## Features Included

### 1. `synthax_core.py`
- Core interpreter for `.synth` code
- Native support for `log`, `set`, `wait`, `askAI`, `explain`, `predict`

### 2. `interpreter.py`
- Entry point script for running Synthax files or code strings

### 3. `synthax_assistant.py`
- Natural language â†’ Synthax code generator (AI-powered)
- Converts plain instructions into structured `.synth` logic

### 4. `user_tools.py`
- Save, load, export `.synth` programs
- File operations for offline use

### 5. `index.html`
- Web-based runner with voice support
- Includes Synthax CLI emulator
- Uses Web Speech API for voice â†’ Synthax transcription

---

## Quick Start

1. Clone the repo  
```bash
git clone https://github.com/Danny8174/synthax-modules.git
cd synthax-modules
```

2. Run Synthax interpreter
```bash
python3 interpreter.py
```

3. Use `index.html` in a browser (for frontend + voice demo)

---

## Sample Code

```synth
log "Hello from Synthax!"
wait 2
askAI "Summarise the concept of emergence in 2 lines."
```

---

## Contributing

Want to add a feature, plugin, or tool?  
Open an issue or fork and PR.

---

## License

MIT â€” use freely, fork creatively, contribute proudly.

---

> Created by Daniel Barry Stephenson | [github.com/Danny8174](https://github.com/Danny8174)
