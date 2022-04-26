import pandas as pd
from datetime import datetime
from tabulate import tabulate

def getDate(x):
    date = datetime.fromisoformat(" ".join(x.split(" ")[:-1]))
    return date




def calculate (file):
    print ('**********************************************')
    a = pd.read_excel (file)
    df = a.sort_values(by=['DateTime'])
    inout =[]
    #print (df[df["DateTime"] == "2022-03-25 19:17:46 Friday"])
    for i,r in df.iterrows():
        if (r['Addr'] in  "Prod. Exit-Exit") or (r['Addr'] in  "Main Entry-Exit"):
            dateTimeExit = r['DateTime']
            doorExit = r['Addr']
            #dayExit = dateTimeExit.split(" ")[-1]
            dateExit = getDate(dateTimeExit)
            name = r['User Name']
            for x,p in df.iterrows():
            #if (len(df.index)-1) > int(i):
                # doorIn = df.loc[[int(i)+1],'Addr'].values[0]
                doorIn = p['Addr']
                if "-In" in doorIn:
                    out = False
                    #dateTimeIn = df.loc[[int(i)+1],['DateTime']].values[0]
                    dateTimeIn = p['DateTime']
                    #dayIn = dateTimeIn[0].split(" ")[-1]
                    dateIn = getDate(dateTimeIn)
                    if dateExit < dateIn:
                        out = dateIn - dateExit
                        tabel = []
                        #tabel.append (i)
                        tabel.append (doorExit)
                        tabel.append (dateExit)
                        tabel.append (doorIn)
                        tabel.append (dateIn)
                        tabel.append (out)
                        inout.append(tabel)
                        #print (dateExit,doorExit )
                        #print (dateIn, doorIn)
                        
                        #print ( out)
                        #print ("\n")
                if out :
                    break            
    print ('---------------------------------------------------')
    #print (inout)
    print(tabulate(inout,headers=['Exit Door','Exit Date','Door In','Date in','Out Time'],tablefmt='grid'))
    return tabulate(inout,headers=['Exit Door','Exit Date','Door In','Date in','Out Time'], tablefmt='html')
            
        #break
#print (len(df.index))
#print(df.loc[[111],"Addr"])