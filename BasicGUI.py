from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import csv

#########################################

def timestamp(thai=True):
	stamp = datetime.now()
	if thai == True:
		stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	return stamp

def writetext(quantity,total):
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename,'a', encoding='utf-8') as file: #'w' = ทุกครั้งที่มีการบันทึก จะเป็นการเขียนไฟล์ใหม่ , 'a' = append ค่าเข้าไปในไฟล์ที่มีอยู่แล้ว
		file.write('\n'+'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total)) # , = ใส่ , ทุก 3 หลัก # .2f = ตัดให้เหลือ 2 ตำแหน่ง

def writecsv(data):
    # แบบนี้ data = ['Time',10,500]
    with open('data.csv','a',newline='',encoding='utf-8') as file: # ใส่ newline='' เพื่อไม่ให้ขึ้นต้นด้วยบรรทัดว่าง
        fw = csv.writer(file) # fw = file writer
        fw.writerow(data)
    print('Success')

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

#########################################
GUI = Tk()
GUI.geometry('700x850')
GUI.title('Durian v.0.0.1')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file)
IMG.pack(pady=20)

L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .place(x,y) , .grid(row=0,column=0)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน (กิโลกรัม)',font=('Angsana New',20))
L2.pack() # .place(x,y) , .grid(row=0,column=0)

v_quantity = StringVar() #ตำแหน่งตัวแปรที่ใช้เก็บข้อมูลของช่องกรอก
E1 = ttk.Entry(GUI,textvariable=v_quantity,font=('impact',30))
E1.pack()


def Cal(event=None):
	quantity = v_quantity.get()
	price = 100
	print('จำนวน', float(quantity) * price)
	Total = float(quantity) * price
	
	# # stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	
	# stamp = datetime.now()
	# stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
	# stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')

	# # ฟังชั่นบันทึกข้อมูลลงไฟล์ txt
	# filename = 'data.txt'
	# with open(filename,'a', encoding='utf-8') as file: #'w' = ทุกครั้งที่มีการบันทึก จะเป็นการเขียนไฟล์ใหม่ , 'a' = append ค่าเข้าไปในไฟล์ที่มีอยู่แล้ว
	# 	file.write('\n'+'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,Total)) # , = ใส่ , ทุก 3 หลัก # .2f = ตัดให้เหลือ 2 ตำแหน่ง
	
	# writetext(quantity,Total)
	data = [timestamp(),quantity,Total]
	writecsv(data)

	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,Total)
	messagebox.showinfo(title,text)

	v_quantity.set('') # clear data
	E1.focus()

B1 = ttk.Button(GUI,text='คำนวณ',command=Cal)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Cal)

def SummaryData(event):
	# pop up
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = 'จำนวนที่ขายได้ทั้งหมด: {} กก.\nยอดขาย: {:,.2f} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)

GUI.bind('<F1>',SummaryData)
GUI.bind('<F2>',SummaryData)

E1.focus() # ให้ cursor ไปยังตำแหน่งของ E1
GUI.mainloop()