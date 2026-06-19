def info(x,y):
    import requests

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": x,
        "longitude": y,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,precipitation_probability_mean",
        "timezone": "Asia/Kolkata",
        "forecast_days": 7
    }

    response = requests.get(url, params=params)
    data = response.json()

    d=data["daily"]
    return d

def main_menu(location):
    print("|---------------------------- FARMER WEATHER ASSISTANCE----------------------------------|")
    print("                               Location: ",location,"                                       ")
    print("|========================================================================================|")
    print("| 1. Rainfall Alert                                                                      |")
    print("| 2. Irrigation Scheduler                                                                |")
    print("| 3. Best Day to Spray                                                                   |")
    print("| 4. Heat / Cold wave Warning                                                            |")
    print("| 5. Crop Suitability Checker                                                            |")
    print("| 6. Change Location                                                                     |")
    print("| 7. Exit                                                                                |")
    print("|========================================================================================|")

def save_(dta):
    from datetime import datetime
    lst1=dta["time"]
    lst2=dta["precipitation_sum"]
    formated_date=[]
    formatted_rain=[]
    for i in lst1:
        dt = datetime.strptime(i.replace("-",""), "%Y%m%d")
        formatted = dt.strftime("%A %d %B %Y")
        formated_date.append(formatted+" "+"->"+" ")
    for i in range(len(lst2)):
        if(lst2[i]>12):
            formatted_rain.append(f"Heavy Rain ({lst2[i]}mm)")
        elif(lst2[i]>=6 and lst2[i]<12):
            formatted_rain.append(f"Moderate Rain ({lst2[i]}mm)")
        elif(lst2[i]<=0):
            formatted_rain.append(f"NO Rain ({lst2[i]}mm)")
        else:
            formatted_rain.append(f"Light Rain ({lst2[i]}mm)")
    final_list=[]
    for i in range(len(lst1)):
        str_=formated_date[i]+formatted_rain[i]+"\n"
        final_list.append(str_)
    f=open("data.txt","w")
    f.writelines(final_list)
    f.close()
def coordinates(s):
    import requests
    url=f"https://geocoding-api.open-meteo.com/v1/search?name={s}&count=1&language=en"
    response=requests.get(url)
    j=response.json()
    l=[j["results"][0]["latitude"],j["results"][0]["longitude"]]
    return l

def start():
    import fun_ctions
    mainflag=True
    while(mainflag==True):
        loc=input("Enter your location:")
        cod_lst=coordinates(loc)
        dta=info(cod_lst[0],cod_lst[1])
        save_(dta)
        flag=True
        ch_oice=-1
        while(flag==True):
            main_menu(loc)
            choice=int(input("Enter your choice:"))
            ch_oice=choice
            match choice:
                case 1:
                    f1=True
                    while(f1==True):
                        fun_ctions.rain_alert()
                        c=input("press no to return to main menu->>>")
                        if(c=="no"):
                            f1=False
                        else:
                            print("Invalid input...")
                case 2:
                    f2=True
                    while(f2==True):
                        fun_ctions.irrigation_scheduler()
                        c=input("press no to return to main menu->>>")
                        if(c=="no"):
                            f2=False
                        else:
                            print("Invalid input...")
                case 3:
                    f3=True
                    while(f3==True):
                        fun_ctions.best_day_to_spray(dta)
                        c=input("press no to return to main menu->>>")
                        if(c=="no"):
                            f3=False
                        else:
                            print("Invalid input...")
                case 4:
                    f4=True
                    while(f4==True):
                        fun_ctions.temperature(dta)
                        c=input("press no to return to main menu->>>")
                        if(c=="no"):
                            f4=False
                        else:
                            print("Invalid input...")
                case 5:
                    f5=True
                    while(f5==True):
                        fun_ctions.crop_check(dta)
                        c=input("press yes to cotinue or no to return to main menu->>>")
                        if(c=="no"):
                            f5=False
                case 6:
                    flag=False
                case 7:
                    flag=False
                case _:
                    print("Invalid entry....")
        if(ch_oice==7):
            mainflag=False
start()