import datetime
d1 = datetime.datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")
d2 = datetime.datetime.strptime(input(),"%Y-%m-%d %H:%M:%S")
print(int(abs(d2-d1).total_seconds()))

#from datetime import datetime
#d1 = datetime.fromisoformat(input())  # без шаблона
#d2 = datetime.fromisoformat(input())
#print(int(abs((d2 - d1).total_seconds())))