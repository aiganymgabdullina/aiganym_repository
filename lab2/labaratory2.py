
file = open("shop_logs.txt", "r")
unique_users = set()
total_buys = 0
total_sum = 0
user_spending = {}
for line in file:
    parts = line.strip().split(";")

user_id = parts[1]

action = parts[2]
unique_users.add(user_id)
if action == "BUY":
    total_buys += 1
    amount = int(parts[3])
    total_sum += amount
    if user_id not in user_spending:
        user_spending[user_id] = amount
    else:
        user_spending[user_id] += amount
file.close()
f=open("shop_logs.txt","r")
unique_users= set()
total_buys=0
total_sum=0
user_spending={}
for line in f:
    line=line.strip()
    if not line:
        continue
    parts = line.split(";")
    if len(parts)<3:
        continue
    user_id = parts[1]
    action = parts[2]
    unique_users.add(user_id)
    if action == "BUY":
        if len(parts)<4:
            continue
        n= int(parts[3])
        total_buys+=1
        total_sum+=n
        if user_id not in user_spending:
            user_spending[user_id] = n
        else:
            user_spending[user_id] += n
f.close()
max_user= ""
max_spend=0

for user in user_spending:
    if user_spending[user] > max_spend:
        max_spend=user_spending[user]
        max_user=user
if total_buys >0:
    u=total_sum / total_buys
else:
    u=0
report = open("report.txt","w",encoding="utf-8")
report.write("Уникальных пользователей:"+ str(len(unique_users))+"\n")
report.write("Всего покупок:"+ str(total_buys)+"\n")
report.write("Общая сумма:"+ str(total_sum)+"\n")
report.write("Самый активный покупатель:"+max_user+"\n")
report.write("Средний чек:"+ str(u) +"\n")
report.close()
print("Отчет успешно создан!")
