# TasteGraph Agent Pipeline






## 🚀 Quick Start (For Judges)

You can run this pipeline locally in under a minute using either Python or Docker.


### Option 1: Local Python Setup

```bash
# Clone the repository
git clone [https://github.com/rcortez056-spec/tastegraph-agent-pipeline.git](https://github.com/rcortez056-spec/tastegraph-agent-pipeline.git)
cd tastegraph-agent-pipeline

# Install dependencies
pip install -r requirements.txt

# Run the app locally
python main.py
## Project Overview
TasteGraph is a production-grade autonomous agent pipeline designed to leverage cultural intelligence data for advanced preference modeling and recommendation workflows.

## Tech Stack
* **Backend:** Python, Flask
* **Deployment:** Containerized and hosted on Google Cloud Run
* **Integration:** Qloo API for cultural data and recommendations

## Architecture & Workflow
The system exposes a secure API endpoint (`/api/recommend`) that processes incoming payloads, securely retrieves the `QLOO_API_KEY` from environment variables, and queries the Qloo API with robust error handling and timeout protections.
