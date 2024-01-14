import xlrd
"打开指定目录下的一个excel表格,formatting_info=True表示读取各种格式信息"
get_excel= xlrd.open_workbook(r"C:\Users\gxw\.vscode\python\list1.xlsx")
print(get_excel)
#获取工作簿中的所有表格，以列表形式返回表格名称
all_excel = get_excel.sheet_names()
print("所有的表格名称:",all_excel)
# 获取工作簿中的一个工作表
get_indexsheet = get_excel.sheets()[0]#通过索引获取
print("表格的索引",get_indexsheet)
get_namesheet = get_excel.sheet_by_name("人员信息统计表")#通过名称获取
print("表格的索引",get_namesheet)
#获取该sheet表中的有效行数
nrows = get_namesheet.nrows
print("表格中的有效行数",nrows)
#获取该sheet表中的有效列数
ncols = get_namesheet.ncols
print("表格中的有效列数",ncols)
# 获取整行或者整列的内容
rows = get_namesheet.row_values(0) #获取第一行的内容
cols = get_namesheet.col_values(1) #获取第二列的内容
print("第一行的内容%s,第二列的内容%s"%(rows,cols))
# 获取单元格内容
con = get_namesheet.cell_value(1,1)#获取第二行，第二列的内容
print("获取单元格的内容：",con)
# 获取单元格数据类型
datatype = get_namesheet.cell(1,1).ctype #ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(datatype)