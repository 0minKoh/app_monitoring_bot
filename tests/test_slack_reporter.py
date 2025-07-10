import unittest
from reports.slack_reporter import post_slack_thread_reply

class TestSlackReporter(unittest.TestCase):
    def test_post_slack_thread_reply(self):
        channel = "C0802303F8U"
        thread_ts = "1752113397.669759"
        text = "(Google Play) 앱 리뷰 현황 보고\n- 평점 34개\n  - 평균 4.9\n- 리뷰가 있는 평점 5개\n  - 홍길동 (5점)\n  - 김철수 (4점)"
        resp = post_slack_thread_reply(channel, thread_ts, text)
        print(resp)
        self.assertTrue(resp.get("ok"))

if __name__ == '__main__':
    unittest.main()
