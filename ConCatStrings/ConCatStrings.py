'''
Created on 22/01/2015

@author: Juan.Insuasti
'''

import xlrd
from xlwt import Workbook


if __name__ == '__main__':
    
    workbookA = xlrd.open_workbook('a.xlsx') 
    workbookB = xlrd.open_workbook('b.xlsx')
    
    worksheetA = workbookA.sheet_by_name('Sheet1')
    worksheetB = workbookB.sheet_by_name('Sheet1')
    
    workbookC = Workbook()
    sheet1 = workbookC.add_sheet('hoja1')
    
    rowa = worksheetA.nrows - 1
    rowb = worksheetB.nrows - 1 
    
    x_rowa = 0
   
    pos = 0
    
    while x_rowa <= rowa:
        cella = worksheetA.cell_value(x_rowa,0)
        x_rowb = 0
        while x_rowb <= rowb:
            cellb = worksheetB.cell_value(x_rowb,0)
            sheet1.write(pos,0,cella + cellb)
            pos += 1
            x_rowb += 1
        
        x_rowa += 1
    
    workbookC.save('result.xls')

