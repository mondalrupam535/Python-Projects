def rain_alert():
    print("\U0001F4A7","Rainfall Alert FOR THIS WEEK")
    print("-------------------------------------------------")
    f=open("data.txt","r")
    lst=[]
    for i in range(7):
        a=f.readline()
        print("\u27A4",a.rstrip("\n"))
        lst.append(a)
    print("-------------------------------------------------")
    dry_days=[]
    for i in lst:
        if("NO Rain" in i):
            dry_days.append(i.replace("->",","))
    print("Dry days:",end="")
    for i in dry_days:
        print(i,end=" ")
    print("-> Good for Field Work...")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def irrigation_scheduler():
    f=open("data.txt","r")
    c=0
    print("IRRIGATION SCHEDULE FOR THIS WEEK")
    print("_______________________________________________")
    for i in range(7):
        a=f.readline()
        if("NO Rain" in a):
            print("\u27A4",a.rstrip("\n")," ->>> Irrigate Today...")
            c+=1
        else:
            print("\u27A4",a.rstrip("\n")," ->>> Skip Irrigation...")
    print("_______________________________________________")
    print(f"You Need to irrigate {c} days this week")
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def best_day_to_spray(dta):
    print("\U0001F9EA","BEST DAYS TO SPRAY PESTICIDE")
    print("-------------------------------------------------------------------")
    wind_lst=dta["windspeed_10m_max"]
    temp=dta["temperature_2m_max"]
    f=open("data.txt","r")
    for i in range(7):
        ls=(f.readline()).split()
        if(wind_lst[i]<14):
            if(ls[5]=="Heavy Rain" or ls[5]=="Light Rain"):
                print("\u27A4",ls[0],"->",temp[i],"|",ls[5],ls[6],"|","Low Wind","->>> Avoid")
            else:
                print("\u27A4",ls[0],"->",temp[i],"|",ls[5],ls[6],"|","Low Wind","->>> Good Day")
        else:
            print("\u27A4",ls[0],"->",temp[i],"|",ls[5],ls[6],"|","Low Wind","->>> Avoid")
    f.close()
    print("-------------------------------------------------------------------")
    print("\U0001F4A1","Tip: Spray early morning or evening for best results...")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def temperature(dta):
    print("\U0001F321","TEMPERATURE ALERTS THIS WEEK")
    print("-------------------------------------------------------------------")
    ls=dta["temperature_2m_max"]
    f=open("data.txt","r")
    safedays=[]
    for i in range(7):
        a=(f.readline()).split()
        if(ls[i]>=32.0 and ls[i]<=37.0):
            print(a[0],a[1],a[2],"-->",ls[i],"\u00B0 C","\U0001F7E1","VERY HOT - Avoid afternoon work")
        elif(ls[i]>=38.0):
            print(a[0],a[1],a[2],"-->",ls[i],"\u00B0 C","\U0001F534","HEAT WAVE - WATER CROPS IN MORNING")
        else:
            print(a[0],a[1],a[2],"-->",ls[i],"\u00B0 C","\U0001F7E2","COOL DAY - GOOD FOR FARMING WORKS")
            safedays.append(a[0])
    print("-------------------------------------------------------------------")
    print("\u2705","Safe Days",end="")
    for i in safedays:
        print(i,", ",end="")
    print("\U0001F4A1","Tip: ON heat Wave days, cover young plants...")

def crop_check(dta):
    import cropdata
    a=input("Enter your crop name:")
    b=a.lower()
    match b:
        case "rice":
            cropdata.rice(dta)
        case "wheat":
            cropdata.wheat(dta)
        case "maize":
            cropdata.maize(dta)
        case "sugarcane":
            cropdata.sugarcane(dta)
        case "cotton":
            cropdata.cotton(dta)
        case "jute":
            cropdata.jute(dta)
        case "tea":
            cropdata.tea(dta)
        case "coffee":
            cropdata.coffee(dta)
        case "tobacco":
            cropdata.tobacco(dta)
        case "mustard":
            cropdata.mustard(dta)
        case "potato":
            cropdata.potato(dta)
        case "groundnut":
            cropdata.nut(dta)
        case "brinjal":
            cropdata.brinjal(dta)
        case "tomato":
            cropdata.tomato(dta)
        case _:
            print("Invalid Input... Try names like Rice, Jute")

        
