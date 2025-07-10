def format_google_play_report(reviews):
    # 리뷰가 있는 평점만 보여주는 포맷
    if not reviews:
        return "(Google Play) 앱 리뷰 현황 보고\n- 리뷰가 있는 평점 0개"
    # 텍스트가 실제로 존재하는 리뷰만 카운트 (공백, None 제외)
    reviews_with_text = [r for r in reviews if r.get('text') and r.get('text').strip()]
    lines = ["(Google Play) 앱 리뷰 현황 보고"]
    lines.append(f"- 리뷰가 있는 평점 {len(reviews_with_text)}개")
    if reviews_with_text:
        r = reviews_with_text[0]  # 가장 최근 리뷰 1개만 표시
        lines.append(f"  - {r['author']} ({r['rating']}점)")
    return '\n'.join(lines)
