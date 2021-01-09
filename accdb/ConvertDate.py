def convertdate(date,swapmd):
    count = 0
    year = ''
    month = ''
    day = ''
    #newdate = ''
    raw = ['','','']

    
    for n in date:
        #check if the characters in the date are digits (0-9)
        if n.isdigit():
            if count == 0:     
                raw[0]=raw[0]+n
            elif count == 1:
                raw[1]=raw[1]+n
            elif count == 2:
                raw[2]=raw[2]+n
        else:
            count +=1
    
    #Loop through every item in the list and check for the year
    for i in range(len(raw)):
        if len(raw[i]) == 2:
            #swap the month and the day if required
            if swapmd:
                month = raw[i]
                day = raw[i-1]
            else:
                day = raw[i]
                month = raw[i-1]
        #length of a raw piece is > 2, so this must be a year
        elif len(raw[i]) > 2:
            year = raw[i]
        
    return day+'-'+month+'-'+year