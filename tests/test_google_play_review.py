import unittest
from unittest.mock import patch
from google_play.review_collector import GooglePlayReviewCollector
from reports.reporter import format_google_play_report

class TestGooglePlayReviewCollector(unittest.TestCase):
    @patch('google_play.review_collector.fetch_google_play_reviews')
    def test_review_report_format(self, mock_fetch):
        # 샘플 데이터: (작성자, 평점, 리뷰)
        mock_fetch.return_value = [
            {'author': 'Jg Lee', 'rating': 3, 'text': '괜찮아요'},
            {'author': 'TG Happy', 'rating': 2, 'text': '별로에요'},
            {'author': '권오형', 'rating': 5, 'text': '좋아요'},
            {'author': '익명', 'rating': 5, 'text': ''},
            {'author': '익명2', 'rating': 4, 'text': ''},
            {'author': '익명3', 'rating': 5, 'text': ''},
            {'author': '익명4', 'rating': 5, 'text': ''},
        ]
        collector = GooglePlayReviewCollector(app_id='com.example.app')
        reviews = collector.collect_reviews()
        report = format_google_play_report(reviews)
        expected = """(Google Play) 앱 리뷰 현황 보고
- 평점 7개
  - 평균 4.143 (4.1)
- 리뷰가 있는 평점 3개
  - Jg Lee (3점)
  - TG Happy (2점)
  - 권오형 (5점)
"""
        self.assertEqual(report.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
