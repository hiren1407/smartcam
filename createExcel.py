from datetime import date
import xlrd

from xlutils.copy import copy
import xlsxwriter

# wb = xlsxwriter.Workbook("attenDance.xlsx")
# dailyUpdate = wb.add_worksheet('dailyUpdate')
wb  = xlrd.open_workbook('attenDance1.xlsx',on_demand = True)
rb = copy(wb)
dailyUpdate = rb.get_sheet(0)
dailyUpdate1 = wb.sheet_by_index(0)
#dailyUpdate.write(0,0,'Roll No')
#dailyUpdate.write(0,1,'Name')
##rb.save('attenDance.xls')
# # # # dailyUpdate.write(4,3,'')

# # # # # worksheet.write(0,0,'Roll No')
# # # # # worksheet.write('B1','Name')
# # # # print(workbook.sheetnames)

def addName(fid,name):
	# rollnoS = "A" + str(rollno)
	dailyUpdate.write(fid,0,fid)
	dailyUpdate.write(fid,1,fid)
	# worksheet.write('B'+rollno,name)
	# print(rollno)
	rb.save('attenDance1.xlsx')
	
# # 	# print(d1)


#addName(4,'hiren')

def updateAttendance(fid,attendance):
	today = date.today()
	currentDate = today.strftime("%d/%m/%y")
	cols = dailyUpdate1.ncols
	# print(cols)
	# print(currentDate)
	lastDate = dailyUpdate1.cell_value(0, cols-1)
	if (lastDate != currentDate):
		dailyUpdate.write(0,cols,currentDate)
		dailyUpdate.write(fid,cols,attendance)

	else:
		dailyUpdate.write(fid,cols-1,attendance)
	rb.save('attenDance1.xlsx')

	#print(lastDate)
	# dailyUpdate.write()
#updateAttendance(4,'P')


# # # book = xlwt.Workbook(encoding="utf-8")




# # # dailyUpdate = book.add_sheet("dailyUpdate")
# wb.close()