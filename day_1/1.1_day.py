
# 1.1_day_input.sql
with open("day_1/1.1_day_input.sql", "r") as file:
    data = file.readlines()

res = []
seq = []
for e in data:
    if e == "\n":
        res.append(seq)
        seq = []
        continue
    seq.append(int(e.replace("\n", "")))
res.append(seq)

sum_list = []
for e in res:
    sum_list.append(sum(e))

print(max(sum_list))