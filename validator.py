# validator.py
def is_valid_input(text, max_length=50, min_length=1):
    """
    입력된 문자열이 최소/최대 길이를 만족하는지 확인합니다.
    (예: 영화 제목이나 한 줄 평이 너무 길거나 비어있는지 확인)
    """
    if not (min_length <= len(text) <= max_length):
        print(f"❌ 오류: 입력은 {min_length}자 이상, {max_length}자 이하여야 합니다.")
        return False
    return True

def get_validated_input(prompt, max_len=50):
    """유효성 검사를 통과할 때까지 입력을 반복해서 받는 함수."""
    while True:
        user_input = input(prompt).strip()
        if is_valid_input(user_input, max_length=max_len):
            return user_input
