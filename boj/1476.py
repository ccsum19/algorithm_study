#날짜 계산

e, s, m = map(int, input().split())
date = 1

while (date - e) % 15 or (date - s) % 28 or (date - m) % 19:
    date += 1

print(date)