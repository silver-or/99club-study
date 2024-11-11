def solution(arr):
    answer = arr
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    return answer

'''
def no_continuous(s):
    result = []
    for c in s:
        if len(result) == 0 or result[-1] != c:
            result.append(c)

    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
'''