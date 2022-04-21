import pandas as pd
from datetime import datetime

def getDate(x):
    date = datetime.fromisoformat(" ".join(x.split(" ")[:-1]))
    return date





print ('**********************************************')
a = pd.read_excel (r'Peca_swipe.xls')
df = a.sort_values(by=['DateTime'])
#print (df[df["DateTime"] == "2022-03-25 19:17:46 Friday"])
for i,r in df.iterrows():
    if (r['Addr'] in  "Prod. Exit-Exit") or (r['Addr'] in  "Main Entry-Exit"):
        dateTimeExit = r['DateTime']
        doorExit = r['Addr']
        dayExit = dateTimeExit.split(" ")[-1]
        dateExit = getDate(dateTimeExit)
        
        for x,p in df.iterrows():
        #if (len(df.index)-1) > int(i):
            # doorIn = df.loc[[int(i)+1],'Addr'].values[0]
            doorIn = p['Addr']
            if "-In" in doorIn:
                out = False
                #dateTimeIn = df.loc[[int(i)+1],['DateTime']].values[0]
                dateTimeIn = p['DateTime']
                dayIn = dateTimeIn[0].split(" ")[-1]
                dateIn = getDate(dateTimeIn)
                if dateExit < dateIn:
                    print (dateExit,doorExit )
                    print (dateIn, doorIn)
                    out = dateIn - dateExit
                    print ( out)
                    print ("\n")
            if out :
                break            

            
        #break
#print (len(df.index))
#print(df.loc[[111],"Addr"])