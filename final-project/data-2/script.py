import xlsxwriter as xl
import random

wb = xl.Workbook('data.xlsx')
sheet = wb.add_worksheet()

row = col = 0
moe = 0.25


vars = ["TURBINE", "maximum-capacity", "capacity-factor", "annual-power-output", "revenue", "installation-cost", "maintenance-cost", "total-cost"]

turbine = 1
mc = 1500
cf = 0.2
apo= mc*cf
revenue = apo * 0.12
ic = 200000
mc = apo * 0.10
tc = (ic / 20) + mc

data = [turbine, mc, cf,  apo, revenue, ic, mc, tc]
# column_names = ['X-ac', 'X-bc', 'z', 'z0', 'R-r', 'C-t', 'VD-ac', 'VD-bc']
# data = [500, 200, 60, 0.3, 20, 0.88, 0.0208, 0.1116]

for item in vars:
    sheet.write(row, col, item)
    col += 1

while row <= 50:
    col = 0
    row += 1
    turbine += 1   


    for item in data:
        #max-capacity, capacity factor
        if item == data[1] or item == data[2]:
            ul = random.random() * moe
            ll = random.random() * -moe
            item = item * (1 + ul + ll)
            sheet.write(row, col, item)
        
        #everything else
        else:
            sheet.write(row, col, item)
        col += 1

wb.close()
