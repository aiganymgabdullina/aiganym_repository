#1 esep
print("1 esep")
with open("shop_logs.txt", "w") as f:
    f.write("2026-02-01;user_1;LOGIN\n")
    f.write("2026-02-01;user_2;LOGIN\n")
    f.write("2026-02-01;user_1;BUY;120\n")
    f.write("2026-02-01;user_3;LOGIN\n")
    f.write("2026-02-01;user_2;BUY;300\n")
    f.write("2026-02-01;user_1;BUY;50\n")
    f.write("2026-02-01;user_2;LOGOUT\n")
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
    chek=total_sum / total_buys
else:
    chek=0
report = open("report.txt","w",encoding="utf-8")
report.write("Уникальных пользователей:"+ str(len(unique_users))+"\n")
report.write("Всего покупок:"+ str(total_buys)+"\n")
report.write("Общая сумма:"+ str(total_sum)+"\n")
report.write("Самый активный покупатель:"+max_user+"\n")
report.write("Средний чек:"+ str(chek) +"\n")
report.close()
print("Отчет успешно создан!")


#2 esep
print("2 esep")
import csv
with open("employees.csv", "w", encoding="utf-8") as f:
    f.write("name,department,salary\n")
    f.write("Ali,IT,500000\n")
    f.write("Dana,HR,300000\n")
    f.write("Arman,IT,600000\n")
    f.write("Aruzhan,Marketing,400000\n")
    f.write("Dias,IT,450000\n")

employees = []
departments = {}
total_salary = 0
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"]
        department = row["department"]
        salary = int(row["salary"])
        employee = {"name": name, "department": department,"salary": salary}
        employees.append(employee)
        total_salary += salary
        if department not in departments:
            departments[department] = []
        departments[department].append(employee)

average_salary = total_salary/len(employees)

department_averages ={}
for d in departments:
    d_total = 0
    for e in departments[d]:
        d_total += e["salary"]
    d_average = d_total /len(departments[d])
    department_averages[d] = d_average

highest_department = max(department_averages, key = department_averages.get)
highest_emp = max(employees, key = lambda x: x["salary"])
hight_salary_employees = []
for emp in employees:
    if emp["salary"] > average_salary:
        hight_salary_employees.append(emp)

with open("hight_salary.csv", "w") as f:
    a = csv.DictWriter(f, fieldnames=["name", "department", "salary"])
    a.writeheader()
    a.writerows(hight_salary_employees)
print("Отчет успешно создан!")

#3 esep
print("3 esep")
import json
with open("orders.json", "w") as f:
    f.write("""
[
  {
    "order_id": 1,
    "user": "Ali",
    "items": ["phone", "case"],
    "total": 300000
  },
  {
    "order_id": 2,
    "user": "Dana",
    "items": ["laptop"],
    "total": 800000
  },
  {
    "order_id": 3,
    "user": "Ali",
    "items": ["mouse", "keyboard"],
    "total": 70000
  }
]
""")
with open("orders.json", "r") as f:
    orders = json.load(f)
total_revenue = 0
user_orders = {}
item_counts = {}
most_expensive_order = 0
top_user = ""
total_items_sold = 0
for order in orders:
    user = order["user"]
    total = order["total"]
    items = order["items"]
    total_revenue += total
    if user not in user_orders:
        user_orders[user] = 0
    user_orders[user] += 1
    if total > most_expensive_order:
        most_expensive_order = total
        top_user = user
    total_items_sold += len(items)
    for item in items:
        if item not in item_counts:
            item_counts[item] = 0
        item_counts[item] += 1
most_popular_item = max(item_counts, key=item_counts.get)


with open("summary.json", "w") as f:
    f.write("{\n")
    f.write(f'  "total_revenue": {total_revenue},\n')
    f.write(f'  "top_user": "{top_user}",\n')
    f.write(f'  "most_popular_item": "{most_popular_item}",\n')
    f.write(f'  "total_orders": {len(orders)}\n')
    f.write("}")
print("Отчет успешно создан!")
