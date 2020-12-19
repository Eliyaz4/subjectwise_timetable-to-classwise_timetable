import pandas as pd
import numpy as np
rows,cols=9,6
data1=pd.read_excel("egni.xlsx","Page 1")
data2=pd.read_excel("egni.xlsx","Page 2")
data3=pd.read_excel("egni.xlsx","Page 3")
data4=pd.read_excel("egni.xlsx","Page 4")
data5=pd.read_excel("egni.xlsx","Page 5")
maths=data1.as_matrix()
science=data2.as_matrix()
english=data3.as_matrix()
kanada=data4.as_matrix()
hindi=data5.as_matrix()
m=[["-------"]*cols]*rows
six=np.array(m)
seven=np.array(m)
eigth=np.array(m)
ninth=np.array(m)
tenth=np.array(m)
for i in range(1,10):
	for j in range(1,7):
			if(maths[i][j]=="6th"):
				six[i-1][j-1]="maths"
			if(maths[i][j]=="7th"):
				seven[i-1][j-1]="maths"
			if(maths[i][j]=="8th"):
				eigth[i-1][j-1]="maths"
			if(maths[i][j]=="9th"):
				ninth[i-1][j-1]="maths"
			if(maths[i][j]=="10th"):
				tenth[i-1][j-1]="maths"
for i in range(1,10):
	for j in range(1,7):
			if(science[i][j]=="6th"):
				six[i-1][j-1]="science"
			if(science[i][j]=="7th"):
				seven[i-1][j-1]="science"
			if(science[i][j]=="8th"):
				eigth[i-1][j-1]="science"
			if(science[i][j]=="9th"):
				ninth[i-1][j-1]="science"
			if(science[i][j]=="10th"):
				tenth[i-1][j-1]="science"
for i in range(1,10):
	for j in range(1,7):
			if(english[i][j]=="6th"):
				six[i-1][j-1]="english"
			if(english[i][j]=="7th"):
				seven[i-1][j-1]="english"
			if(english[i][j]=="8th"):
				eigth[i-1][j-1]="english"
			if(english[i][j]=="9th"):
				ninth[i-1][j-1]="english"
			if(english[i][j]=="10th"):
				tenth[i-1][j-1]="english"
for i in range(1,10):
	for j in range(1,7):
			if(kanada[i][j]=="6th"):
				six[i-1][j-1]="kanada"
			if(kanada[i][j]=="7th"):
				seven[i-1][j-1]="kanada"
			if(kanada[i][j]=="8th"):
				eigth[i-1][j-1]="kanada"
			if(kanada[i][j]=="9th"):
				ninth[i-1][j-1]="kanada"
			if(kanada[i][j]=="10th"):
				tenth[i-1][j-1]="kanada"
for i in range(1,10):
	for j in range(1,7):
			if(hindi[i][j]=="6th"):
				six[i-1][j-1]="hindi"
			if(hindi[i][j]=="7th"):
				seven[i-1][j-1]="hindi"
			if(hindi[i][j]=="8th"):
				eigth[i-1][j-1]="hindi"
			if(hindi[i][j]=="9th"):
				ninth[i-1][j-1]="hindi"
			if(hindi[i][j]=="10th"):
				tenth[i-1][j-1]="hindi"
six=pd.DataFrame(six,columns=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],index=["8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM"])
six.to_csv("Sixth_class.csv")
seven=pd.DataFrame(seven,columns=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],index=["8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM"])
seven.to_csv("Seventh_class.csv")
eigth=pd.DataFrame(eigth,columns=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],index=["8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM"])
eigth.to_csv("Eigth_class.csv")
ninth=pd.DataFrame(ninth,columns=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],index=["8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM"])
ninth.to_csv("Ninth_class.csv")
tenth=pd.DataFrame(tenth,columns=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],index=["8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM"])
tenth.to_csv("Tenth_class.csv")





