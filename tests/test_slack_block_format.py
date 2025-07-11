import unittest
from reports.slack_reporter import get_slack_bot_token
import requests
import re

def parse_slack_message_url(url: str):
    m = re.search(r'/archives/([A-Z0-9]+)/p(\d{16})', url)
    if not m:
        raise ValueError('URL에서 channel_id와 ts를 추출할 수 없습니다.')
    channel_id = m.group(1)
    ts_raw = m.group(2)
    ts = f"{ts_raw[:10]}.{ts_raw[10:]}"
    return channel_id, ts

class TestSlackBlockFormat(unittest.TestCase):
    def test_send_block_message(self):
        url = "https://supajaiscool.slack.com/archives/D03KB4XFQRG/p1752135101513329"
        channel, thread_ts = parse_slack_message_url(url)
        token = get_slack_bot_token()
        api_url = "https://slack.com/api/chat.postMessage"
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
        blocks = [
    {"type": "section", "text": {"type": "mrkdwn", "text": "*Google Play 앱 리뷰 현황 보고*"}},
    {"type": "section", "text": {"type": "mrkdwn", "text": "> 인용구 예시"}},
    {"type": "section", "text": {"type": "mrkdwn", "text": "*리뷰 리스트:*\n• 홍길동 (5점)\n• 김철수 (4점)"}}
]
        data = {
            "channel": channel,
            "thread_ts": thread_ts,
            "blocks": blocks,
            "text": "Google Play 앱 리뷰 현황 보고"
        }
        resp = requests.post(api_url, headers=headers, json=data)
        print(resp.json())
        self.assertTrue(resp.json().get("ok"))

if __name__ == "__main__":
    unittest.main()
