# TasteGraph Agent Pipeline

An autonomous agent pipeline that queries the Qloo API to deliver recommendation insights[cite: 1]. Hosted live on Google Cloud Run with continuous delivery from GitHub.

---

## 🚀 Quick Start (For Judges)

You can run this pipeline locally in under a minute using Python or Docker[cite: 6].

### Option 1: Local Python Setup

```bash
# Clone the repository
git clone [https://github.com/rcortez056-spec/tastegraph-agent-pipeline.git](https://github.com/rcortez056-spec/tastegraph-agent-pipeline.git)
cd tastegraph-agent-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the app locally
python main.py

🛠️ Tech Stack
Backend: Python / Flask / Gunicorn

Hosting: Google Cloud Run

Integration: Qloo Hackathon v2 API
