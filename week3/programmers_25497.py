import sys

N = int(sys.stdin.readline())
skills = sys.stdin.readline().strip()
cnt = 0
s_count = 0
l_count = 0

for skill in skills:
    if skill.isdigit():
        cnt += 1  # 숫자인 경우 바로 카운트
    elif skill == 'S':
        s_count += 1  # S 카운트 증가
    elif skill == 'K':
        if s_count > 0:  # S가 먼저 나왔으면 SK 쌍 카운트
            s_count -= 1
            cnt += 1
        else:
            break  # 조건이 맞지 않으면 종료
    elif skill == 'L':
        l_count += 1  # L 카운트 증가
    elif skill == 'R':
        if l_count > 0:  # L이 먼저 나왔으면 LR 쌍 카운트
            l_count -= 1
            cnt += 1
        else:
            break  # 조건이 맞지 않으면 종료

print(cnt)
