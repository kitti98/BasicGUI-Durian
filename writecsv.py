import csv

# ฟังชั่น csv ต้องมีทั้งฟังชั่น write กับ read
def writecsv(data):
    # แบบนี้ data = ['Time',10,500]
    with open('data.csv','a',newline='',encoding='utf-8') as file: # ใส่ newline='' เพื่อไม่ให้ขึ้นต้นด้วยบรรทัดว่าง
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('Success')

# d = ['2022-04-03 00:29:30',50,5000]
# writecsv(d)

def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        # print(list(fr))
        data = list(fr)
    return data

def sumdata():
    # ฟังชั่นนี้ใช้สำหรับรวมค่าที่ได้จาก csv แล้วสรุปออกมาเป็น 2 อย่าง
    result = readcsv()
    sumlist_quan = []
    sumlist_total = []
    for d in result:
        sumlist_quan.append(float(d[1]))
        sumlist_total.append(float(d[2]))
    sumquan = sum(sumlist_quan)
    sumtotal = sum(sumlist_total)
    return (sumquan, sumtotal)

result = sumdata()
print(result)

# sumlist_quan = []
# for d in result:
#     sumlist_quan.append(float(d[1]))
# print(sumlist_quan, sum(sumlist_quan))

# sumlist_quan2 = [float(d[1]) for d in result]
# print(sumlist_quan2 , sum(sumlist_quan2))

# sumquan = sum([float(d[1]) for d in result])
# print(sumquan)
