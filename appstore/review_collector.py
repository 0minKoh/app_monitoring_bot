# App Store Connect 리뷰 수집 기능 (API 연동)
# 실제 API 연동은 JWT 인증 필요


import os
import time
import jwt
import requests

# App Store Connect API 인증 정보
ISSUER_ID = 'a537d894-286a-4b9e-ae12-6e5202dd3f0d'
KEY_ID = '85T8597SMF'
PRIVATE_KEY_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.secrets', 'AuthKey_85T8597SMF.p8')

def _generate_jwt_token():
    with open(PRIVATE_KEY_PATH, 'r') as f:
        private_key = f.read()
    now = int(time.time())
    payload = {
        'iss': ISSUER_ID,
        'iat': now,
        'exp': now + 20 * 60,
        'aud': 'appstoreconnect-v1'
    }
    headers = {
        'alg': 'ES256',
        'kid': KEY_ID,
        'typ': 'JWT'
    }
    token = jwt.encode(payload, private_key, algorithm='ES256', headers=headers)
    return token

def fetch_appstore_reviews(app_id, max_results=1000, country='KOR'):
    """
    App Store Connect API를 통해 앱 리뷰를 수집합니다.
    반환: [{author, rating, text, date} ...]
    """
    token = _generate_jwt_token()
    url = f'https://api.appstoreconnect.apple.com/v1/apps/{app_id}/customerReviews'
    headers = {'Authorization': f'Bearer {token}'}
    params = {'limit': 200, 'filter[territory]': country}
    result = []
    next_url = url
    while next_url and len(result) < max_results:
        resp = requests.get(next_url, headers=headers, params=params if next_url == url else None)
        if resp.status_code != 200:
            print('API 오류:', resp.text)
            break
        data = resp.json()
        for item in data.get('data', []):
            attr = item.get('attributes', {})
            result.append({
                'author': attr.get('reviewerNickname', '익명'),
                'rating': attr.get('rating', 0),
                'text': attr.get('body', ''),
                'date': attr.get('createdDate', '')
            })
            if len(result) >= max_results:
                break
        next_url = data.get('links', {}).get('next')
    return result

class AppStoreReviewCollector:
    def __init__(self, app_id):
        self.app_id = app_id

    def collect_reviews(self, return_raw=False):
        if not return_raw:
            return fetch_appstore_reviews(self.app_id)
        # 원본 API 응답을 반환
        token = _generate_jwt_token()
        url = f'https://api.appstoreconnect.apple.com/v1/apps/{self.app_id}/customerReviews'
        headers = {'Authorization': f'Bearer {token}'}
        params = {'limit': 200, 'filter[territory]': 'KOR'}
        resp = requests.get(url, headers=headers, params=params)
        return resp.json()
