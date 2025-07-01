#  Webhook Receiver for GitHub Events

This project is a **Flask-based webhook receiver** that listens to GitHub events from a separate repository (`action-repo`) and stores them in **MongoDB**. It also includes a minimal **frontend UI** that polls every 15 seconds to show the latest GitHub events (Push, Pull Request, Issue, and optionally Merge).

---

##  Features

-  Receives GitHub webhooks from [`action-repo`](https://github.com/ayesh03/action-repo)
-  Handles the following event types:
  - `push`
  - `pull_request`
  - `issues`
-  Stores essential data in MongoDB
-  Frontend UI:
  - Polls backend every 15 seconds
  - Filters by event type (All, Push, Pull Request, Issues)
  - Renders data in minimal format

---

##  Webhook Event Formats

- **Push:**
{author} pushed to {to_branch} on {timestamp}

markdown


- **Pull Request:**
{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}

markdown
Copy code

- **Merge (Bonus):**
{author} merged branch {from_branch} to {to_branch} on {timestamp}

yaml
Copy code

---

##  MongoDB Schema

All events are stored in the `webhook_db.webhook_events` collection:

```json
{
"author": "ayesh03",
"title": "Test PR",
"body": "Testing pull request event",
"timestamp": "2025-07-01T04:13:44Z",
"pr_number": 5,
"event_type": "pull_request"
}
 Tech Stack
 Python (Flask)

 MongoDB (local)

 HTML + JavaScript (Vanilla)

 GitHub Webhooks

 UI Preview
The UI fetches updates from the backend every 15 seconds and shows them in real time.

 Screenshot 1 – All Events

 Screenshot 2 – Push Events

 Screenshot 3 – Pull Request Events

 Screenshot 4 – Issue Events

 Setup Instructions
Clone this repo:

bash
Copy code
git clone https://github.com/ayesh03/webhook-repo.git
cd webhook-repo
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Start MongoDB (make sure it’s running on localhost:27017)

Run Flask app:

bash

python app.py

Open in browser:
http://127.0.0.1:5000

Webhook setup:

Go to action-repo

Settings → Webhooks → Add new

Payload URL: https://1c07-203-192-253-152.ngrok-free.app/webhook

Content type: application/json

Select events: Push, Pull request, Issues

 Folder Structure

webhook-repo/

├── templates/
│   └── index.html
├── issue_event.png
├── pull_event.png
├── push_event.png
├── all_event.png
├── app.py
├── README.md
└── requirements.txt


