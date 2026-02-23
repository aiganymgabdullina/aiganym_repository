#1 esep
print("1 esep")
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

