# 유저의 점수를 리스트 형태로 입력 받음
scores = list(map(int,input()))
# 점수의 길이를 구하여 반 나누기
N = len(scores)
# 짝수만 주어진다고 하지만, 홀수 인 경우도 가능함
# 내장 함수 기능사용, 리스트 인덱싱의 start 이상 end 미만 이용
if not N % 2:
    before = sum(scores[:N//2])
    after = sum(scores[N//2:])
else:
    before = sum(scores[:N//2])
    after = sum(scores[N//2+1:])
# 값 비교 후 결과 print
if before == after:
    print("LUCKY")
else:
    print("READY")