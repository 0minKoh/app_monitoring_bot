# Google Play 리뷰 수집 기능 구현 (fetch 함수는 실제 API 연동 시 구현)
def fetch_google_play_reviews(app_id):
    # 실제 구현에서는 Google Play API 또는 비공식 라이브러리 사용
    # 테스트에서는 mocking
    return []

class GooglePlayReviewCollector:
    def __init__(self, app_id):
        self.app_id = app_id

    def collect_reviews(self):
        return fetch_google_play_reviews(self.app_id)
