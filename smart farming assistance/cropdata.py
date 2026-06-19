def rice(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F33E',"Rice needs: Temp 25-35°C | High Humidity | Good Rainfall")
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_max"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=25 and avg<=35):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def wheat(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F33E',"Wheat needs: Temp 10-25°C | Moderate Rainfall | Cool Climate")
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=10 and avg<=25):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def maize(dta):
        print("-----------------------------------------------------------------")
        print('\U0001F33D',"Maize needs: Temp 21-27°C | Moderate Rainfall | Well-drained Soil")
        l1=dta["temperature_2m_min"]
        l2=dta["temperature_2m_min"]
        avg=(sum(l1)+sum(l2))/7
        print("\n")
        print("This Week's Forecast:")
        if(avg>=21 and avg<=27):
            print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
        else:
            print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
        prob=sum(dta["precipitation_probability_mean"])/7
        print(f"\u2705 Rainfall Probability  -> {prob} %")
        print("-----------------------------------------------------------------")

def sugarcane(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F38B',"Sugarcane needs: Temp 20-35°C | High Rainfall | Humid Climate")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=20 and avg<=35):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def cotton(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F9F6',"Cotton needs: Temp 21-30°C | Moderate Rainfall | Black Soil")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=21 and avg<=30):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def jute(dta):
    print("-----------------------------------------------------------------")
    print('\U0001FAA2',"Jute needs: Temp 24-35°C | Heavy Rainfall | Humid Climate")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=24 and avg<=35):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def tea(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F375',"Tea needs: Temp 20-30°C | Heavy Rainfall | Hilly Areas")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=20 and avg<=30):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def coffee(dta):
    print("-----------------------------------------------------------------")
    print('\u2615',"Coffee needs: Temp 15-28°C | Moderate Rainfall | Shade and Humidity")   
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=15 and avg<=28):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def tobacco(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F6AC',"Tobacco needs: Temp 20-30°C | Low to Moderate Rainfall | Fertile Soil")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=20 and avg<=30):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def mustard(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F331',"Mustard needs: Temp 10-25°C | Low Rainfall | Cool Climate")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=10 and avg<=25):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def potato(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F954',"Potato needs: Temp 15-20°C | Moderate Rainfall | Cool Weather")
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=15 and avg<=20):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def nut(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F95C',"Groundnut needs: Temp 20-30°C | Moderate Rainfall | Sandy Loam Soil")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=20 and avg<=30):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def brinjal(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F346',"Brinjal needs: Temp 22-30°C | Moderate Water | Warm Climate")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=22 and avg<=30):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")

def tomato(dta):
    print("-----------------------------------------------------------------")
    print('\U0001F345',"Tomato needs: Temp 20-27°C | Moderate Water | Well-drained Soil")    
    l1=dta["temperature_2m_min"]
    l2=dta["temperature_2m_min"]
    avg=(sum(l1)+sum(l2))/7
    print("\n")
    print("This Week's Forecast:")
    if(avg>=20 and avg<=27):
        print(f"\u2705 Temperature  -> SUitable (avg {avg} \u00B0 C)")
    else:
        print(f"\u2705 Temperature  -> NOT suitable (avg {avg} \u00B0 C)")
    prob=sum(dta["precipitation_probability_mean"])/7
    print(f"\u2705 Rainfall Probability  -> {prob} %")
    print("-----------------------------------------------------------------")
