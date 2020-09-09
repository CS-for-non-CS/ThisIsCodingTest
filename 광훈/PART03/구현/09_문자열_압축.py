def solution(s):
    # 결과값 초기화
    result = len(s)

    # i : 나누는 기준 길이
    # 단어 길이의 반을 넘어가면 나누는 의미가 없음
    for i in range(1, len(s) // 2 + 1):
        # 그룹 내 단어 수
        cur_num = 1
        # 현재 단어
        cur_char = s[:i]
        # 총 길이
        cur_len = 0

        # 단어를 잘라가며 검사
        for j in range(i, len(s), i):
            # 같으면 그룹 내 단어 수 1 증가
            if cur_char == s[j:j+i]:
                cur_num += 1
            else:
                # 그룹 크기가 1보다 클 경우
                if cur_num != 1:
                    # 글자 앞에 붙는 숫자 길이 더해주기
                    cur_len += len(str(cur_num))
                cur_len += i
                cur_num = 1
                cur_char = s[j:j+i]

        # 마지막 단어 추가
        if cur_num != 1:
            cur_len += len(str(cur_num))
        cur_len += len(cur_char)

        result = min(result, cur_len)

    return result
