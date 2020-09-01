month, day = input().split()
month = int(month)
day = int(day)

period = 0

if month > 1:
    period += 31
if month > 2:
    period += 28
if month > 3:
    period += 31
if month > 4:
    period += 30
if month > 5:
    period += 31
if month > 6:
    period += 30
if month > 7:
    period += 31
if month > 8:
    period += 31
if month > 9:
    period += 30
if month > 10:
    period += 31
if month > 11:
    period += 30
period += day

idx = period % 7

ans = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(ans[idx])