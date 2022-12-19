import xlsxwriter as xl
import random

wb = xl.Workbook('wind-dataset(2).xlsx')
sheet = wb.add_worksheet()

row = col = 0
sensitivity = 0.25

column_names = ['X-ac', 'X-bc', 'z', 'z0', 'R-r', 'C-t', 'VD-ac', 'VD-bc']

data = [500, 200, 60, 0.3, 20, 0.88, 0.0208, 0.1116]

for item in column_names:
    sheet.write(row, col, item)
    col += 1

while row <= 50:
    col = 0
    row += 1

    for item in data:
        ul = random.random() * sensitivity
        ll = random.random() * -sensitivity
        sheet.write(row, col, item * (1 + ul + ll))
        col += 1

wb.close()
