# Cortex — Terminal-Based AI Assistant Powered by Gemini

<div align="center">

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**A Minimal CLI Interface for Interacting with Google's Gemini Models**

_AI in your terminal. Fast, simple, no fluff._

</div>

---

## What is Cortex?

Cortex is a lightweight command-line AI assistant that lets you interact with Google’s Gemini models directly from your terminal. It strips away unnecessary UI and focuses on fast, clean, and controlled interactions with an LLM.

Designed as a backend-focused learning project, Cortex emphasizes:

- **Direct API interaction** (no wrappers, no magic — just clean requests)
- **Secure environment handling** (`.env`, no leaked secrets)
- **CLI-first UX** (argparse, flags, structured output)
- **Graceful failure handling** (quota errors, API instability)
- **Token usage visibility** (prompt + response cost awareness)

---

## Tech Stack

| Layer                      | Technology                     | Why                                    |
| -------------------------- | ------------------------------ | -------------------------------------- |
| **Core Language**          | Python 3.12                    | Fast iteration, strong ecosystem       |
| **LLM API**                | Google Gemini (`google-genai`) | Free-tier access, fast inference       |
| **CLI Parsing**            | argparse                       | Built-in, lightweight, no dependencies |
| **Environment Management** | python-dotenv                  | Secure API key handling                |

---

## Security as First Principles

- API keys stored in `.env`, never hardcoded
- `.env` excluded via `.gitignore`
- No secrets logged to terminal
- Fail-fast behavior when API key is missing
- Graceful degradation when API fails (no crashes)

---

## Quick Start

### Prerequisites

- Python 3.12+
- Google Gemini API key

---

### Setup

```bash
# Clone
git clone https://github.com/your-username/cortex.git
cd cortex

# Install dependencies
uv sync
```
---

## Author

**[@nickemma](https://github.com/nickemma)** — Building production-grade distributed systems, infrastructure, and backend platforms from first principles.

💼 Open to distributed systems, infrastructure, and backend engineering roles at companies building serious systems.

 <div align="center">
 <a href="https://www.linkedin.com/in/techieemma/"><img src="https://img.shields.io/badge/linkedin-%23f78a38.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
 <a href="https://twitter.com/techieemma"><img src="https://img.shields.io/badge/Twitter-%23f78a38.svg?style=for-the-badge&logo=Twitter&logoColor=white" alt="Twitter"></a>
 <a href="https://github.com/nickemma/"><img src="https://img.shields.io/badge/github-%23f78a38.svg?style=for-the-badge&logo=github&logoColor=white" alt="Github"></a>
 <a href="https://techieemma.medium.com/"><img src="https://img.shields.io/badge/Medium-%23f78a38.svg?style=for-the-badge&logo=Medium&logoColor=white" alt="Medium"></a>
 <a href="mailto:nicholasemmanuel321@gmail.com"><img src="https://img.shields.io/badge/Gmail-f78a38?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"></a>
 </div>

---

<div align="center">

**Building Systems, Building Faith — One Commit at a Time**
