from datetime import datetime


def writetext(quantity,total):
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) # บวกเป็น พ.ศ.
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data.txt'
	with open(filename,'a', encoding='utf-8') as file: #'w' = ทุกครั้งที่มีการบันทึก จะเป็นการเขียนไฟล์ใหม่ , 'a' = append ค่าเข้าไปในไฟล์ที่มีอยู่แล้ว
		file.write('\n'+'วัน-เวลา: {} ทุเรียน: {} กก. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total)) # , = ใส่ , ทุก 3 หลัก # .2f = ตัดให้เหลือ 2 ตำแหน่ง

# writetext(90,9000)
# writetext(91,9100)
# writetext(92,9200)
# writetext(93,9300)
