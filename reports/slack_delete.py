import requests
import os

def get_slack_bot_token():
    token_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.secrets', 'slack_bot_token.txt')
    with open(token_path) as f:
        return f.read().strip()


import re

def parse_slack_message_url(url: str):
    """
    Slack 메시지 URL에서 channel_id와 ts를 추출합니다.
    """
    m = re.search(r'/archives/([A-Z0-9]+)/p(\d{16})', url)
    if not m:
        raise ValueError('URL에서 channel_id와 ts를 추출할 수 없습니다.')
    channel_id = m.group(1)
    ts_raw = m.group(2)
    ts = f"{ts_raw[:10]}.{ts_raw[10:]}"
    return channel_id, ts

def delete_slack_message_by_url(url: str):
    channel_id, ts = parse_slack_message_url(url)
    token = get_slack_bot_token()
    api_url = "https://slack.com/api/chat.delete"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "channel": channel_id,
        "ts": ts,
    }
    response = requests.post(api_url, headers=headers, data=data)
    return response.json()

if __name__ == "__main__":
    url = "https://supajaiscool.slack.com/archives/C0802303F8U/p1752133971063679?thread_ts=1752113397.669759&cid=C0802303F8U"
    resp = delete_slack_message_by_url(url)
    print("삭제 응답:", resp)
