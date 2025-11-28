
reviews = []

def add_review(movie_title, review_text):
    """새 영화 평점을 리스트에 추가합니다."""
    reviews.append([movie_title, review_text])
    print(f"✅ 영화 '{movie_title}'의 평점이 추가되었습니다.")

def view_reviews():
    """현재 리스트에 있는 모든 평점을 출력합니다."""
    if not reviews:
        print("등록된 영화 평점이 없습니다.")
        return
        
    print("\n--- 🎬 전체 영화 평점 목록 ---")
    for i, review in enumerate(reviews):
        print(f"{i+1}. 제목: {review[0]} / 평점: {review[1]}")
    print("------------------------------")
