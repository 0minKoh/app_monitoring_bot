# Google Play 리뷰 수집 기능 구현 (fetch 함수는 실제 API 연동 시 구현)

import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.secrets', 'google_play_service_account_key.json')
SCOPES = ['https://www.googleapis.com/auth/androidpublisher']

def fetch_google_play_reviews(app_id, max_results=1000):
    """
    Google Play Developer API를 통해 앱 리뷰를 수집합니다.
    반환: [{author, rating, text} ...]
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('androidpublisher', 'v3', credentials=credentials)
    reviews_resource = service.reviews()
    result = []
    token = None
    fetched = 0
    while fetched < max_results:
        req = reviews_resource.list(packageName=app_id, maxResults=100, token=token)
        resp = req.execute()
        print("[DEBUG] API 응답 Response: ", json.dumps(resp, indent=2))
        for review in resp.get('reviews', []):
            # comments 리스트가 비어있는 경우를 대비해 확인합니다.
            if not review.get('comments'):
                continue

            user_comment = review['comments'][0]['userComment']
            user = review.get('authorName', '익명')
            rating = user_comment.get('starRating', 0)
            text = user_comment.get('text', '')
            result.append({'author': user, 'rating': rating, 'text': text})
            fetched += 1
            if fetched >= max_results:
                break
        token = resp.get('tokenPagination', {}).get('nextPageToken')
        if not token:
            break
    return result

class GooglePlayReviewCollector:
    def __init__(self, app_id):
        self.app_id = app_id

    def collect_reviews(self):
        return fetch_google_play_reviews(self.app_id)
