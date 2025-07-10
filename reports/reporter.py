def format_google_play_report(reviews):
    if not reviews:
        return "(Google Play) 앱 리뷰 현황 보고\n- 평점 0개\n  - 평균 0.000 (0.0)\n- 리뷰가 있는 평점 0개"
    ratings = [r['rating'] for r in reviews]
    avg = sum(ratings) / len(ratings)
    avg_round = round(avg, 1)
    reviews_with_text = [r for r in reviews if r.get('text')]
    lines = ["(Google Play) 앱 리뷰 현황 보고"]
    lines.append(f"- 평점 {len(ratings)}개\n  - 평균 {avg:.3f} ({avg_round})")
    lines.append(f"- 리뷰가 있는 평점 {len(reviews_with_text)}개")
    for r in reviews_with_text:
        lines.append(f"  - {r['author']} ({r['rating']}점)")
    return '\n'.join(lines)
