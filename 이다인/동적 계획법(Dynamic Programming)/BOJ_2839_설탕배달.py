'''
1. 문제 요약
- n킬로그램을 3킬로그램 봉지와 5킬로그램 봉지로 나눌 때, 봉지의 최소 개수

2. 아이디어
- 봉지의 최소 개수이므로 5킬로그램 봉지를 최대한 많이 사용
- n이 5의 배수가 아니라면 5킬로그램 봉지 수를 1씩 줄여가면서 나머지를 3킬로그램 봉지로 채움
- 위의 과정을 거친 후, 5킬로그램 봉지 수가 0이 될 때 까지 n이 3으로 나누어지지 않는다면 정확하게 n킬로그램을 만들 수 없으므로 -1 출력
'''

n = int(input())

five = n // 5
three = 0
n %= 5

while (five >= 0):
    if (n % 3 == 0):
        three = n // 3
        print(five + three)
        exit()
    n += 5
    five -= 1

print(-1)