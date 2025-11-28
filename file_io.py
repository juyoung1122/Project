
FILE_NAME = "reviews.txt"

def save_reviews(data):
    """리스트 데이터를 텍스트 파일에 저장합니다."""
    try:
        
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            for movie, review in data:
               
                f.write(f"{movie}|{review}\n") 
        print(f"✅ {len(data)}개의 영화 평점이 '{FILE_NAME}'에 저장되었습니다.")
    except Exception as e:
        print(f"❌ 파일 저장 중 오류 발생: {e}")

def load_reviews():
    """텍스트 파일에서 데이터를 읽어와 리스트로 반환합니다."""
    loaded_data = []
    try:
        
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            for line in f:
                
                movie, review = line.strip().split('|', 1)                 loaded_data.append([movie, review])
        print(f"✅ '{FILE_NAME}'에서 {len(loaded_data)}개의 평점을 불러왔습니다.")
    except FileNotFoundError:
        print(f"⚠️ '{FILE_NAME}' 파일이 없습니다. 새롭게 시작합니다.")
    except Exception as e:
        print(f"❌ 파일 불러오기 중 오류 발생: {e}")
        
    return loaded_data
