import unittest
from appstore.review_collector import AppStoreReviewCollector

class TestAppStoreReviewCollector(unittest.TestCase):
    def test_real_api_review_count(self):
        collector = AppStoreReviewCollector(app_id='6742638932')
        reviews = collector.collect_reviews()
        print(f"App Store 리뷰 개수: {len(reviews)}")
        if reviews:
            print("가장 최근 리뷰:", reviews[0])

if __name__ == '__main__':
    unittest.main()
