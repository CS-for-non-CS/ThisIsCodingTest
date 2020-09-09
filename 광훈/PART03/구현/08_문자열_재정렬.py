word = input()

# 알파벳 개수 세기 위한 리스트 선언
alphabets = [0] * 26

# 더한 숫자 총합
# 숫자가 없을 경우를 체크하기 위해 -1로 초기화
number = -1

for char in word:
    # 아스키 코드 이용해서 알파벳인지 체크
    if ord('A') <= ord(char) <= ord('Z'):
        alphabets[ord(char) - ord('A')] += 1
    else:
        # 숫자가 1개 이상일 경우 0으로 바꿈
        if number < 0:
            number = 0
        number += int(char)

result = ''

# 알파벳 순서대로 붙이기
for index, alphabet in enumerate(alphabets):
    result += chr(ord('A') + index) * alphabet

# 숫자 붙이기
if number >= 0:
    result += str(number)

print(result)
