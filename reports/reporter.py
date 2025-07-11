def format_appstore_report(reviews, mention_channel=False):
    # App Store 리뷰가 있는 평점만 보여주는 포맷
    if reviews is None or not reviews:
        msg = "[App Store 앱 리뷰 현황 보고]\n리뷰가 있는 평점: 0개"
        if mention_channel:
            msg = "<!channel>\n" + msg
        return msg
    if len(reviews) >= 1000:
        msg = "[App Store 앱 리뷰 현황 보고]\n리뷰 GET API 한계 도달 (1000개 이상)"
        if mention_channel:
            msg = "<!channel>\n" + msg
        return msg
    reviews_with_text = [r for r in reviews if r.get('text') and r.get('text').strip()]
    msg = f"[App Store 앱 리뷰 현황 보고]\n리뷰가 있는 평점: {len(reviews_with_text)}개"
    if reviews_with_text:
        r = reviews_with_text[0]
        msg += f"\n가장 최근 리뷰: {r['author']} ({r['rating']}점)"
    if mention_channel:
        msg = "<!channel>\n" + msg
    return msg
def format_google_play_report(reviews, mention_channel=False):
    # 리뷰가 있는 평점만 보여주는 포맷 (최종)
    if reviews is None or not reviews:
        msg = "[Google Play 앱 리뷰 현황 보고]\n리뷰가 있는 평점: 0개"
        if mention_channel:
            msg = "<!channel>\n" + msg
        return msg
    if len(reviews) >= 1000:
        msg = "[Google Play 앱 리뷰 현황 보고]\n리뷰 GET API 한계 도달 (1000개 이상)"
        if mention_channel:
            msg = "<!channel>\n" + msg
        return msg
    reviews_with_text = [r for r in reviews if r.get('text') and r.get('text').strip()]
    msg = f"[Google Play 앱 리뷰 현황 보고]\n리뷰가 있는 평점: {len(reviews_with_text)}개"
    if reviews_with_text:
        r = reviews_with_text[0]
        msg += f"\n가장 최근 리뷰: {r['author']} ({r['rating']}점)"
    if mention_channel:
        msg = "<!channel>\n" + msg
    return msg
