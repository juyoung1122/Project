from dataclasses import dataclass

@dataclass
class Review:
    """
    하나의 영화 평점 항목을 나타내는 데이터 구조 (클래스).
    Movie: 영화 제목
    Review: 한 줄 평 내용
    """
    movie: str
    review: str

    def to_file_format(self):
        """파일에 저장하기 위한 형식으로 반환 (예: 인셉션|시간이 멈추는 명작)"""
        return f"{self.movie}|{self.review}\n"
