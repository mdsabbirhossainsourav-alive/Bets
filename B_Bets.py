n,m = map(int, input().split())
participants = []
for i in range(m):
    li,ri,ti,ci = map(int, input().split())
    participants.append((li,ri,ti,ci))
total_profit = 0
for section in range(1,n+1):
    best_time = float('inf')
    best_profit = 0
    best_index = float('inf')
    for idx, (li,ri,ti,ci) in enumerate(participants):
        if li <= section <= ri: 
            if ti < best_time or (ti == best_time and idx < best_index):
                best_time = ti
                best_profit = ci
                best_index = idx
    total_profit += best_profit
print(total_profit)
