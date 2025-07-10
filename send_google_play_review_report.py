from google_play.review_collector import GooglePlayReviewCollector
from reports.reporter import format_google_play_report
from reports.slack_reporter import post_slack_thread_reply

# 환경설정: 실제 값으로 교체하거나 환경변수로 관리 가능
APP_ID = 'com.supaja.hero'
CHANNEL_ID = 'C0802303F8U'
THREAD_TS = '1752113397.669759'

if __name__ == '__main__':
    collector = GooglePlayReviewCollector(app_id=APP_ID)
    reviews = collector.collect_reviews()
    # mention_channel=True로 하면 <!channel> 멘션 포함
    message = format_google_play_report(reviews, mention_channel=True)
    resp = post_slack_thread_reply(CHANNEL_ID, THREAD_TS, message)
    print('Slack 응답:', resp)
