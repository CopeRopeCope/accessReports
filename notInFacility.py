from ast import And
from pickle import FALSE
import pandas as pd
from datetime import date, datetime, timedelta
from tabulate import tabulate

def getDate(x):
    date = datetime.fromisoformat(" ".join(x.split(" ")[:-1]))
    return date




def calculate (file):
    #print ('**********************************************')
    tabel = calculate_by_day(file)
    sumOut = timedelta(minutes = 0, seconds=0)
    inout = []
    seenDate = FALSE
    for i in tabel:
        exitDate = i[1].date()
        inDate = i[3].date()
        outTime = i[4]
        #print (type(outTime))
        if seenDate:
            if exitDate == inDate :
                print ("datum ulaza i izlaza su isti")
                #sumOut =  outTime - outTime
                sumOut = outTime + sumOut
                print (exitDate)
            else:
                print ("datum ulaza i izlaza nisu isti")
                if sumOut:
                    tmp = []
                    tmp.append(exitDate)
                    tmp.append(sumOut)
                    inout.append(tmp)
            sumOut = timedelta(minutes = 0, seconds=0)

        seenDate = exitDate
        #for i+1 in tabel:

    #return inout
    return tabulate(inout,headers=['Date','Out Time'], tablefmt='html')




    # a = pd.read_excel (file)
    # df = a.sort_values(by=['DateTime'])
    # inout =[]
    # name = ''
    # sumOut = NULL
    # dateExit = NULL
    # print (df[df["DateTime"] == "2022-03-25 19:17:46 Friday"])
    # for i,r in df.iterrows():
    #     table = []
    #     sumOut = 0
    #     if (r['Addr'] in  "Prod. Exit-Exit") or (r['Addr'] in  "Main Entry-Exit"):
    #         dateTimeExit = r['DateTime']
    #         doorExit = r['Addr']
    #         dateExit = getDate(dateTimeExit)
    #         name = r['User Name']
    #         for x,p in df.iterrows():
    #             doorIn = p['Addr']
    #             if "-In" in doorIn:
    #                 dateTimeIn = p['DateTime']
    #                 dateIn = getDate(dateTimeIn)
    #                 if dateExit.date() == dateIn.date():
    #                     if dateExit < dateIn:
    #                         out = dateIn - dateExit
    #                         sumOut = out
    #                         sumOut = out + sumOut
    #                 else:
    #                     if dateExit < dateIn:
    #                         print (dateExit.date(),dateIn.date())
    #                         table.append(dateExit)
    #                         table.append(dateExit)
    #                         table.append(sumOut)
    #                         inout.append(table) 
    #                         break
        
        
        
               
    print ('---------------------------------------------------')
    #print (inout)


    #print(tabulate(inout,tablefmt='grid'))
    return tabulate(inout,headers=['Exit Door','Exit Date','Door In','Date in','Out Time'], tablefmt='html')
            
        #break
#print (len(df.index))
#print(df.loc[[111],"Addr"])

def calculate_by_day (file):
    #print ('**********************************************')

    a = pd.read_excel ('C:\\attendence_report\\swipe\\' + file)
    df = a.sort_values(by=['DateTime'])
    inout =[]
    name = ''
    #print (df[df["DateTime"] == "2022-03-25 19:17:46 Friday"])
    for i,r in df.iterrows():
        if (r['Addr'] in  "Prod. Exit-Exit") or (r['Addr'] in  "Main Entry-Exit"):
            dateTimeExit = r['DateTime']
            doorExit = r['Addr']
            #dayExit = dateTimeExit.split(" ")[-1]
            dateExit = getDate(dateTimeExit)
            name = r['User Name']
            for x,p in df.iterrows():
                doorIn = p['Addr']
                out = False
                if "-In" in doorIn:
                    
                    dateTimeIn = p['DateTime']
                    #dayIn = dateTimeIn[0].split(" ")[-1]
                    dateIn = getDate(dateTimeIn)
                    if dateExit < dateIn:
                        out = dateIn - dateExit
                        tabel = []
                        tabel.append (doorExit)
                        tabel.append (dateExit)
                        tabel.append (doorIn)
                        tabel.append (dateIn)
                        tabel.append (out)
                        inout.append(tabel)

                if out :
                    break            
    #print ('---------------------------------------------------')
    #print (inout)
    #print(tabulate(inout,headers=['Exit Door','Exit Date','Door In','Date in','Out Time'],tablefmt='grid'))
    return tabulate(inout,headers=['Exit Door','Exit Date','Door In','Date in','Out Time'],tablefmt='html')
    print (inout)
    return inout