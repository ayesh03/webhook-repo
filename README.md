# Webhook Receiver for GitHub Events

This project is a Flask-based webhook receiver that listens to GitHub events (Push, Pull Request, Issue) and stores them in a MongoDB database. The UI fetches the latest events every 15 seconds and displays them in a minimal format.

---

##  Features

- Receives GitHub Webhooks from `action-repo`
- Handles:
  - `push` events
  - `pull_request` events
  - `issues` events
- Stores only required fields in MongoDB
- UI displays events in:
  - Push: `{author} pushed to {to_branch} on {timestamp}`
  - Pull Request: `{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}`
  - (Bonus) Merge: `{author} merged branch {from_branch} to {to_branch} on {timestamp}`
- Events are filtered by type (All, Push, Pull Request, Issues)

---

##  Tech Stack

- Python Flask
- MongoDB
- HTML + JavaScript (Vanilla) for frontend
- GitHub Webhooks

---

##  MongoDB Schema

Each webhook event is stored as a document in MongoDB under `webhook_db.webhook_events`:

```json
{
  "author": "ayesh03",
  "title": "Test PR",
  "body": "Testing pull request event",
  "timestamp": "2025-07-01T04:13:44Z",
  "pr_number": 5,
  "event_type": "pull_request"
}
