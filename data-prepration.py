import json

with open ('snapp-comments-lists.py', 'r', encoding="utf-8") as f:
    rf = f.read()
with open ('snapp-comments-csv.csv', 'a+', encoding="utf-8") as f:
    spl = rf.split(",")
    f.write(str(",\n".join([",".join(spl[i:i+6]) for i in range(0,len(spl),6)])))