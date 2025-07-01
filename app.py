from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from bson.json_util import dumps
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["webhook_events"]

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Webhook received:", data)

    event_type = request.headers.get('X-GitHub-Event')

    if event_type == "push" and 'head_commit' in data:
        doc = {
            "author": data['head_commit']['author']['name'],
            "to_branch": data['ref'].split('/')[-1],
            "timestamp": data['head_commit']['timestamp'],
            "event_type": "push"
        }
        collection.insert_one(doc)
        return jsonify({"message": "Push event stored!"}), 200

    elif event_type == "issues" and 'issue' in data:
        doc = {
            "author": data['issue']['user']['login'],
            "title": data['issue']['title'],
            "body": data['issue']['body'],
            "timestamp": data['issue']['created_at'],
            "issue_number": data['issue']['number'],
            "event_type": "issues"
        }
        collection.insert_one(doc)
        return jsonify({"message": "Issue event stored!"}), 200

    elif event_type == "pull_request" and 'pull_request' in data:
        doc = {
            "author": data['pull_request']['user']['login'],
            "title": data['pull_request']['title'],
            "body": data['pull_request']['body'],
            "timestamp": data['pull_request']['created_at'],
            "pr_number": data['pull_request']['number'],
            "event_type": "pull_request"
        }
        collection.insert_one(doc)
        return jsonify({"message": "Pull request event stored!"}), 200

    return jsonify({"message": "Unhandled event"}), 400

@app.route('/events', methods=['GET'])
def get_events():
    event_type = request.args.get('type')  # Example: /events?type=push

    if event_type:
        events = collection.find({"event_type": event_type}).sort("timestamp", -1).limit(20)
    else:
        events = collection.find().sort("timestamp", -1).limit(20)

    return dumps(events), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
