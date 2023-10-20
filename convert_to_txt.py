import pandas as pd

exel_file_name = 'tms_data.xlsx'
df = pd.read_excel(exel_file_name)

f = open("tms_data_txt", 'w')

now = -1
for i in range(4,df.shape[0],2):
    t = str(df.iloc[i])[22:33]
    t= "".join(t.split('.'))
    t= "".join(t.split(':'))
    t = str(int(t)-2747907)
    if (int(t) != now):
        n = t+" "+str(df.iloc[i])[36:].split(" ")[0]+"\n"
        f.write(str(n))
        now = int(t)

