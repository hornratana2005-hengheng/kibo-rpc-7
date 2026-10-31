import random 

#declare battery = 100
battery = 100




for waypoint in range(1, 11):
    
    #simulate battery consumption
    consumption = random.uniform(1.5, 3.5)
    battery -= consumption
     
    print (f"Waypoint {waypoint}: Battery level is {battery:.2f}%")
    
    #emergency check
    if battery < 75:
        print("EMERGENCY RETURN TRIGGERED.")
    elif battery < 80:
        print("[CAUTION] Battery level below 80%!")
    
