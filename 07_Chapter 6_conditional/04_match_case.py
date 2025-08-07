num = int(input("Enter the number from 1 - 7 : "))

match num:
    case 1 : 
          print("1 is for Sunday")  
    case 2 : 
          print("2 is for Monday")  
    case 3 : 
          print("3 is for Tuesday")  
    case 4 : 
          print("4 is for Wednedday")  
    case 5 : 
          print("5 is for Thrusday")  
    case 6 : 
          print("6 is for Friday")  
    case 7 : 
          print("7 is for Saturday")  
    case _:
        print("Please enter the valid number.")