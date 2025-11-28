# main.py
import review_manager
import file_io

def display_menu():
    print("\n--- 🍿 영화 한 줄 평 관리 ---")
    print("1. 새 평점 추가")
    print("2. 전체 평점 보기")
    print("3. 평점 저장 (파일로)")
    print("4. 평점 불러오기 (파일에서)")
    print("5. 종료")
    print("----------------------------")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("메뉴를 선택하세요 (1-5): ")

        if choice == '1':
            movie = input("영화 제목: ")
            review = input("한 줄 평: ")
            review_manager.add_review(movie, review)
        elif choice == '2':
            review_manager.view_reviews()
        elif choice == '3':
            file_io.save_reviews(review_manager.reviews)
        elif choice == '4':
            # 파일에서 불러온 후, 현재 리스트에 덮어쓰기
            review_manager.reviews = file_io.load_reviews()
        elif choice == '5':
            print("프로그램을 종료합니다. 감사합니다!")
            break
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")
