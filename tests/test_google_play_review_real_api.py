import unittest
from google_play.review_collector import GooglePlayReviewCollector

class TestGooglePlayReviewRealAPI(unittest.TestCase):
    def test_real_api_collect(self):
        collector = GooglePlayReviewCollector(app_id='com.supaja.hero')
        reviews = collector.collect_reviews()
        print(f"리뷰 개수: {len(reviews)}")
        for r in reviews[:5]:
            print(r)
        self.assertIsInstance(reviews, list)
        self.assertTrue(all('author' in r and 'rating' in r and 'text' in r for r in reviews))

if __name__ == '__main__':
    unittest.main()
