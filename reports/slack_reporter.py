import os
import requests

def get_slack_bot_token():
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.secrets', 'slack_bot_token.txt')
    with open(token_path) as f:
        return f.read().strip()

def post_slack_thread_reply(channel, thread_ts, text):
    token = get_slack_bot_token()
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "channel": channel,
        "thread_ts": thread_ts,
        "text": text,
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()
