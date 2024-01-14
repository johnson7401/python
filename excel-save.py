from pandas import DataFrame

data = { 'name': ['zs', 'ls', 'ww'], 'age': [11, 12, 13], 'gender': ['man', 'man', 'woman']}
df = DataFrame(data)
df.to_excel(r"C:\Users\gxw\.vscode\python\list2.xls")