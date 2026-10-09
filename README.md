# TasteGraph Agent Pipeline

## Project Overview
TasteGraph is a production-grade autonomous agent pipeline designed to leverage cultural intelligence data for advanced preference modeling and recommendation workflows.

## Tech Stack
* **Backend:** Python, Flask
* **Deployment:** Containerized and hosted on Google Cloud Run
* **Integration:** Qloo API for cultural data and recommendations

## Architecture & Workflow
The system exposes a secure API endpoint (`/api/recommend`) that processes incoming payloads, securely retrieves the `QLOO_API_KEY` from environment variables, and queries the Qloo API with robust error handling and timeout protections.
