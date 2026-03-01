# VTRecon

<p align="center">
  <b>Modular VirusTotal CLI for Threat Intelligence & Reputation Analysis</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue.svg" />
  <img src="https://img.shields.io/badge/Version-0.1.0-informational.svg" />
  <img src="https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.svg" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange.svg" />
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-lightgrey.svg" />
</p>

---

## Overview

VTRecon is a modular VirusTotal CLI tool for automated threat intelligence and reputation analysis. It streamlines hash, URL, and file lookups with structured terminal output and API automation. Built for efficiency and extensibility, VTRecon is designed to evolve into a full-featured graphical threat analysis platform.

---

## Core Capabilities

- Asynchronous VirusTotal API integration
- Hash reputation lookups
- Structured terminal output
- Lightweight and modular design
- Built for future GUI integration

---

## Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/VTRecon.git
cd VTRecon
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run VTRecon:

```bash
python main.py
```

On first execution:
- You will be prompted to enter your VirusTotal API key.
- The key will be stored locally in `VirusTotalAPI.txt`.
- You will then be prompted to enter a hash for analysis.

---

## Example Output

```
Results for <hash_value>:
{'harmless': 65, 'malicious': 3, 'suspicious': 1, 'undetected': 12}
```

---


The CLI implementation acts as the foundation for a scalable threat intelligence framework.

---

## Roadmap

- [ ] URL scanning support
- [ ] File upload scanning
- [ ] Batch processing mode
- [ ] JSON output flag
- [ ] Argparse-based CLI flags
- [ ] Environment variable API support
- [ ] Config file support
- [ ] Logging system
- [ ] GUI interface (Tkinter / PyQt / Web-based)
- [ ] Plugin architecture

---

## Security Considerations

For production use, storing API keys in plaintext is not recommended.

Preferred approach:

```bash
export VT_API_KEY=your_api_key_here
```

Future versions will support environment variable authentication.

---

## Versioning

VTRecon follows semantic versioning:

```
MAJOR.MINOR.PATCH
```

Current Version: `0.1.0`

---

## Contributing

Contributions, feature requests, and security improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## License

This project is licensed under the GNU General Public License v2.0.

---

## Disclaimer

VTRecon is intended for educational and authorized security research purposes only. Users are responsible for complying with VirusTotal’s terms of service and applicable laws.
