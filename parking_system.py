import time
import json
import os
print("\n\n\n                               _______   WELCOME TO THE GO PARKING LOT   _______\n\n\n")

def Parking_checkOut_Data():
    while True:
        list_of_all_vehicle_number=[]
        Vnumber=input("\n\nPlease enter your Vehicle Number for CheckOut:   ")
        with open ("task1.json") as file:
            data_for_amount1=json.load(file)
            for element1 in data_for_amount1["caruser"]:       
                list_of_all_vehicle_number.append(element1["vehicle_number"])
            if Vnumber in list_of_all_vehicle_number:
                for dict in data_for_amount1["caruser"]:
                    if Vnumber ==dict["vehicle_number"]:
                        temp_variable_for_slot_addintion=dict["vehicle_type"]
                        intime=dict["inTime"][11:17]
                        Index=data_for_amount1["caruser"].index(dict)                        
                        for_amount1=intime.replace(":","")
                        outtime= time.asctime(time.localtime(time.time()))
                        temp_outtime=outtime[11:17]
                        for_amount2=temp_outtime.replace(":","")
                        amount=abs(int(for_amount1)-int(for_amount2))
                        if amount<30:
                            amount=30
                            print(amount)
                        else:
                            amount=amount//30*30
                            print(amount)
                        print("__This is your check in data__ \nout_vehicle_number  :  ",dict["vehicle_number"],"\nvehicle_type  :  ",dict["vehicle_type"],"\nlarge_spots_number  :  ",dict["Parking_spots_number"],"\ninTime  :  ",dict["inTime"],"\nCheck out time :   ",outtime,"\nYour amount is :   ",amount,"\n\n++   NOW YOU CAN CHECK OUT WITH YOUR VEHICLE  ++")
                        data_for_amount1["caruser"].pop(Index)
                        with open ("task1.json","w") as data_delete:
                                file=json.dump(data_for_amount1,data_delete,indent=4)
                        return temp_variable_for_slot_addintion
            else:
                print("\n\n              XXX   Your data does not exist  XXX    ")
        
def Parking_checkIn_Data():
    inTime= time.asctime(time.localtime(time.time()))
    list1=[]
    main_dict={"caruser":list1}
    Total_bike_parking_spots=10
    Total_car_parking_spots=10
    Total_bus_parking_spots=10
    bikeSpot_number=0
    carSpot_number=0
    busSpot_number=0
    while True:
        specific_data={}

        print ("\n***We have Theseslots available : ***","\nMotorcycle spots = ",Total_bike_parking_spots ,"\nCompact spots = ",Total_car_parking_spots,"\nLarge spots = ",Total_bus_parking_spots,"\nToday = ",inTime)
    
        Vnumber=input("\n\nPlease enter your Vehicle Number for CheckIn :   ")
        Vtype=(input("Please enter your Vehicle Type :  "))
        if Vtype =="bike" or Vtype =="Bike" :
            if Total_bike_parking_spots==0:
                print("\nNO SPACE AVAILAVBLE FOR BIKE\n")
            else:
                Total_bike_parking_spots-=1
                bikeSpot_number+=  1
                print("\n\n___THIS IS YOUR RECEIPT___\n**FOR STARTING TO FIRST 30 MINUTES COST WILL BE 30 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES **\n\nSpot available  :  ",Total_bike_parking_spots,"\nVehicle type  :  ",Vtype,"\nVehicle number  :  ",Vnumber,"\nSpot Number  :  ",bikeSpot_number,"\nParking_spots_type  :  ","Motorcycle spots")
                specific_data["vehicle_number"]=Vnumber
                specific_data["vehicle_type"]=Vtype
                specific_data["Parking_spots_type"]="Motorcycle spots"
                specific_data["Parking_spots_number"]=bikeSpot_number
                specific_data["inTime"]=inTime
                if os.path.exists("task1.json")==True:
                    with open("task1.json") as f1:
                        file1=json.load(f1)
                        k=file1["caruser"]
                        k.append(specific_data)
                        main_dict["caruser"]=k
                        with open("task1.json","w") as f_2:
                            json.dump(main_dict, f_2, indent=4)
                else:
                    list1.append(specific_data)
                    with open ("task1.json","w") as f:
                        file=json.dump(main_dict,f,indent=4)
        elif Vtype =="car" or Vtype =="Car" :
            if Total_bus_parking_spots==0:
                print("\nNO SPACE AVAILAVBLE FOR CAR\n")
            else:
                Total_car_parking_spots-=1
                carSpot_number+=1
                print("\n\n___THIS IS YOUR RECEIPT___\n**FOR STARTING TO FIRST  30 MINUTES COST WILL BE 30 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES **\n\nspot available  :  ",Total_car_parking_spots,"\nVehicle Type  :  ",Vtype,"\nVehicle number  :  ",Vnumber,"\nSpot Number  :  ",carSpot_number,"\nParking_spots_type  :  ","Motorcycle spots")
                specific_data["vehicle_number"]=Vnumber
                specific_data["vehicle_type"]=Vtype
                specific_data["Parking_spots_type"]="Car spots"
                specific_data["Parking_spots_number"]=carSpot_number
                specific_data["inTime"]=inTime
                if os.path.exists("task1.json")==True:
                    with open("task1.json") as f1:
                        file1=json.load(f1)
                        k=file1["caruser"]
                        k.append(specific_data)
                        main_dict["caruser"]=k
                        with open("task1.json","w") as f_2:
                            json.dump(main_dict, f_2, indent=4)
                else:
                    list1.append(specific_data)
                    with open ("task1.json","w") as f:
                        file=json.dump(main_dict,f,indent=4)
        elif Vtype =="bus" or Vtype =="Bus" :
                if Total_bus_parking_spots==0:
                    print("\nNO SPACE AVAILAVBLE OFR BUS\n")
                else:
                    Total_bus_parking_spots-=1
                    busSpot_number+=1
                    print("\n\n___THIS IS YOUR RECEIPT____\n** FOR STARTING TO FIRST 30 MINUTES COST WILL BE 30 RUPEES FOR EVERY NEXT 30 MINUTES WILL INCREASE BY 30 RUPEES **\n\nspot available  :  ",Total_bus_parking_spots,"\nVehicle type  :  ",Vtype,"\nVehicle number  :  ",Vnumber,"\nSpot Number  :  ",busSpot_number,"\nParking_spots_type  :  ","Motorcycle spots")
                    specific_data["vehicle_number"]=Vnumber
                    specific_data["vehicle_type"]=Vtype
                    specific_data["Parking_spots_type"]="Bus spots"
                    specific_data["Parking_spots_number"]=busSpot_number
                    specific_data["inTime"]=inTime
                    if os.path.exists("task1.json")==True:
                        with open("task1.json") as f1:
                            file1=json.load(f1)
                            k=file1["caruser"]
                            k.append(specific_data)
                            main_dict["caruser"]=k
                            with open("task1.json","w") as f_2:
                                json.dump(main_dict, f_2, indent=4)
                    else:
                        list1.append(specific_data)
                        with open ("task1.json","w") as f:
                            file=json.dump(main_dict,f,indent=4)
        else:
            print("\n\n -- SORRY WE DON'T HAVE SLOT FOR THIS TYPE OF VEHICLE --")
        if Total_bike_parking_spots==0 and Total_car_parking_spots==0 and Total_bus_parking_spots==0 :
            print("jjj")
            break
        again=input("\n\nIf you want to check out your then press 2 / for check in press any key ")
        if again=="2":
            temp_var_for_spot_addition=Parking_checkOut_Data()
            if temp_var_for_spot_addition=="bus":
                Total_bus_parking_spots+=1
            if temp_var_for_spot_addition=="car":
                Total_car_parking_spots+=1
            if temp_var_for_spot_addition=="bike":
                Total_bike_parking_spots+=1
            
Enquiry=int(input("If you want to checkIn for it press 1\nIf you want to check out for it press 2\nIf you are here for visit only press 3\n\nPRESS  :   "))
if Enquiry==1:
    Parking_checkIn_Data()
elif Enquiry==2:
    Parking_checkOut_Data()
elif Enquiry==3:
    print("Thank you for visiting ")
else:
    print("\nERROR\nPlease press right key!")
        

