# AI Brand Assistant

**Version:** 1.0  
**Author:** Mehrdad Khorsand  
**Built with:** FastAPI, Python, OpenAI-compatible AI Gateway, Tailwind CSS  
**Status:** Working Prototype

---

## Overview

AI Brand Assistant is a full-stack web application that generates a complete brand starter kit from a simple business description.

Enter a description like *"A cozy, organic coffee shop in Tehran targeting young professionals"*, and in 20–30 seconds you get:

- **A generated logo concept** (AI image generation)
- **3 brand name suggestions**
- **3 taglines**
- **A ready-to-post social media caption**
- **A 5-color brand palette** (with hex codes)
- **A font pairing recommendation**
- **A target audience profile**

The tool supports both **English and Persian** input, automatically matching the output language to the input.

---

## Features

| Feature | Description |
| :--- | :--- |
| **Text Generation** | Brand names, taglines, social copy, audience profile |
| **Image Generation** | AI-generated logo concept based on the top brand name |
| **Structured Output** | All data returned as clean JSON via the API |
| **Persian & English** | Full bilingual support with automatic language detection |
| **Modern UI** | Clean, responsive interface built with Tailwind CSS |
| **Copy & Download** | Copy any text with one click, download the full kit as JSON |

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.14, FastAPI, Uvicorn |
| **AI Client** | OpenAI Python SDK (OpenAI-compatible) |
| **AI Gateway** | AvalAI (Iran-accessible, OpenAI-compatible) |
| **Text Model** | GPT-4o (or equivalent) |
| **Image Model** | `gpt-image-2.5-flare` (via AvalAI) |
| **Frontend** | HTML5, Tailwind CSS (via CDN), vanilla JavaScript |
| **Dev Tools** | Cursor, Claude, VS Code |
| **Environment** | Docker-ready, `.env`-based configuration |

---

## Architecture
