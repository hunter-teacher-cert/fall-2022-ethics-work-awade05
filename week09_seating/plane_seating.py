import random
def createPlane(rows,cols):
   
    plane = []
    for r in range(rows):
        s = ["window"]+["available"]*(cols-2)+["window"]
        plane.append(s)
    return plane

def numEconSold(econSold):
    
    sold = 0
    for b in econSold.values():
        sold = sold + b
    return sold
  
def availableableSeats(plane,econSold):
    
    available = 0;
    for r in plane:
        for c in r:
            if c == "available" or c == "window":
                available = available + 1
    available = available - numEconSold(econSold)
    return available

def totalSeats(plane):
    
    return len(plane)*len(plane[0])

def planeString(plane):
    
    s = ""
    for r in plane:
        r = ["%14s"%x for x in r] 
        s = s + " ".join(r)
        s = s + "\n"
    return s
  
def buyEconPlus(plane,econSold,name):
    
    rows = len(plane)
    cols = len(plane[0])  
    seats = availableableSeats(plane,econSold)

    if seats < 1:
        return plane
      
    if random.randrange(100) > 30:
        order = [x for x in range(rows)]

        random.shuffle(order)
   
        for row in order:
            if plane[row][0] == "window":
                plane[row][0] = name
                return plane
            elif plane[row][len(plane[0])-1] == "window":
                plane[row][len(plane[0])-1] = name
                return  plane

    found_seat = False
    while not(found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "window" or plane[r_row][r_col] == "available":
            plane[r_row][r_col] = name
            found_seat = True
    return plane

def seatEcon(plane,econSold,name):
    
    rows =len(plane)
    cols=len(plane[0])


  

    found_seat = False
    while not (found_seat):
        r_row = random.randrange(0,rows)
        r_col = random.randrange(0,cols)
        if plane[r_row][r_col] == "window" or plane[r_row][r_col] == "available":
              plane[r_row][r_col] = name
              found_seat = True
   
    return plane

def buyEconBlock(plane,econSold,number,name):
    
    seats_available = totalSeats(plane)
    seats_available = seats_available - numEconSold(econSold)

    if seats_available >= number:
        econSold[name]=number
    return econSold

def fullPlane(plane):
    
    econSold={}
    total_seats = totalSeats(plane)
    
    ecNum=1
    unNumber=1

    max_family_size = 3
    while total_seats > 1:
        r = random.randrange(100)
        if r > 30:
            plane = buyEconPlus(plane,econSold,"ec-%d"%ecNum)
            ecNum = ecNum + 1
            total_seats = availableableSeats(plane,econSold)
        else:
            econSold = buyEconBlock(plane,econSold,1+random.randrange(max_family_size),"un-%d"%unNumber)
            unNumber = unNumber + 1

        
    for name in econSold.keys():
        for i in range(econSold[name]):
          plane = seatEcon(plane,econSold,name)
    
     
    return plane
        
def main():
    plane = createPlane(28,5)
    plane = fullPlane(plane)
    print(planeString(plane))
if __name__=="__main__":
    main()
