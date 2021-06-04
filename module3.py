import requests
def data_Past_Hour():    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary
    # This will all be data from the past hour.

    # We only want the features key values to access our values.
    data = data.get('features')
    
    
    # start a count to access each line of data.
    count = 0
    
    # start a dictionary to see location

    location_Counter = dict()

    # Start counter magnitude 5 or greater.

    mag_5 = 0

    for location in data:
        # split the data into a list with two values.
        location_List = data[count]['properties']['place'].split(", ")

        # If cannot be split and length of list is only 1 work with 1st value of list.

        if len(location_List) == 1:
            if location_List[0] not in location_Counter:
                location_Counter[location_List[0]] = 1
            else:
                location_Counter[location_List[0]] += 1

        # Else if statements if length of list is greater than 1 we will use the second element.

        elif location_List[1] not in location_Counter:
            location_Counter[location_List[1]] = 1
        else:
            location_Counter[location_List[1]] += 1        

        location_List.clear()

        # Print the magnitutde and location.

        print(data[count]['properties']['place'],"- Mag", data[count]['properties']['mag'])
        

        print(" ")

        # Make sure the data value is not null if it is dont enter the if statement.

        if data[count]['properties']['mag'] != None:

            # if greater than mag 5 increment. 

            if 5 <= float(data[count]['properties']['mag']):
                mag_5 += 1


        # Print the coordinates.

        print("These are the coordinates:" , data[count]['geometry']['coordinates'])

        print("       ")
        
        # Increment the count.

        count = count + 1
    
    # Get the total number of earthquakes 
       
    if count == 1:    
        print("    ")
        print("Number of total Earthquakes: 0")
    else:
        print("    ")
        print("Number of total Earthquakes: ", count)
    
    # print values by location.
    print("    ")
    print("Earthquakes by location: ",location_Counter)  

    # print number of earthquakes mag 5 or greater.
    print("    ")
    print("Magnitude 5 or greater Earthquakes: ", mag_5)

def data_Past_Day():    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary
    # This will all be data from the past day.

    # We only want the features key values to access our values.
    data = data.get('features')
    
    # start a count to access each line of data.
    count = 0

    # start a dictionary to see location
    location_Counter = dict()

    # start a magnitutde counter for magnitudes over 5
    mag_5 = 0

    for location in data:
        # split the data into a list with two values.
        location_List = data[count]['properties']['place'].split(", ")

        # If cannot be split and length of list is only 1 work with 1st value of list.

        if len(location_List) == 1:
            if location_List[0] not in location_Counter:
                location_Counter[location_List[0]] = 1
            else:
                location_Counter[location_List[0]] += 1

        # Else if statements if length of list is greater than 1 we will use the second element.

        elif location_List[1] not in location_Counter:
            location_Counter[location_List[1]] = 1
        else:
            location_Counter[location_List[1]] += 1        

        location_List.clear()

        # Print the magnitutde and location.

        print(data[count]['properties']['place'],"- Mag", data[count]['properties']['mag'])
        

        print(" ")

        # Make sure the data value is not null if it is dont enter the if statement.

        if data[count]['properties']['mag'] != None:

            # if greater than mag 5 increment. 

            if 5 <= float(data[count]['properties']['mag']):
                mag_5 += 1


        # Print the coordinates.

        print("These are the coordinates:" , data[count]['geometry']['coordinates'])

        print("       ")
        
        # Increment the count.

        count = count + 1

    # Get the total number of Earthquakes:

    print("    ")
    print("Number of total Earthquakes: ", count + 1)

    # Print out location counter  
    print("    ")
    print("Earthquakes by location: ",location_Counter) 
    
    # Number of Earthquakes greater than magnitude 5
    print("   ") 
    print("Magnitude 5 or greater EarthQuakes: ", mag_5)   
        
def data_Past_Month():    
    req = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson")
    data = req.json() # The .json() function will convert the json data from the server to a dictionary
    # This will all be data from the past 30 days or month.

    # We only want the features key values to access our values.
    data = data.get('features')
    
    # start a count to access different values.
    count = 0
    # start a dictionary to see location
    mag_5 = 0

    location_Counter = dict()
    for location in data:
        # split the data into a list with two values.
        location_List = data[count]['properties']['place'].split(", ")

        # If cannot be split and length of list is only 1 work with 1st value of list.

        if len(location_List) == 1:
            if location_List[0] not in location_Counter:
                location_Counter[location_List[0]] = 1
            else:
                location_Counter[location_List[0]] += 1

        # Else if statements if length of list is greater than 1 we will use the second element.

        elif location_List[1] not in location_Counter:
            location_Counter[location_List[1]] = 1
        else:
            location_Counter[location_List[1]] += 1        

        location_List.clear()

        # Print the magnitutde and location.

        print(data[count]['properties']['place'],"- Mag", data[count]['properties']['mag'])
        

        print(" ")

        # Make sure the data value is not null if it is dont enter the if statement.

        if data[count]['properties']['mag'] != None:

            # if greater than mag 5 increment. 

            if 5 <= float(data[count]['properties']['mag']):
                mag_5 += 1


        # Print the coordinates.

        print("These are the coordinates:" , data[count]['geometry']['coordinates'])

        print("       ")
        
        # Increment the count.

        count = count + 1

    # Get the total number of Earthquakes:

    print("    ")
    print("Number of total Earthquakes: ", count + 1)

    # Print out location counter  
    print("    ")
    print("Earthquakes by location: ",location_Counter) 
    
    # Number of Earthquakes greater than magnitude 5
    print("   ") 
    print("Magnitude 5 or greater EarthQuakes: ", mag_5)         
        
def main():
    print("   ")
    print("--------------------------------------------")
    print("What EarthQuake data would you like to see? ")
    print("Menu Options")
    print("--------------------------------------------")
    user_Choice = 1
    while user_Choice != 0:
        print("       ")
        print("1 - Last Hour")
        print("2 - Yesterday")
        print("3 - Past Month")
        print("0 - To quit program")
        user_Choice = int(input("Enter number here for your choice: "))
        print("      ")
        if user_Choice == 0:
            break
        elif user_Choice == 1:
            data_Past_Hour()
        elif user_Choice == 2:
            data_Past_Day()
        elif user_Choice == 3:
            data_Past_Month()
        else: 
            print("Error: Invalid selection please enter a valid number")
main()