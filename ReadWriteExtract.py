stockPrices = []                       # store all stock prices line in a list
                        
subString = "Stock Price"        # Substring to search for.

USD = '$'
GBP = '£'
exRate =  0.77

linenum = 0

with open ('files/acme-info.txt', 'rt') as acmefile:
    for line in acmefile:                       #use for loop to iterate through file
        linenum += 1
        if line.lower().find(subString.lower()) != -1:    # if case-insensitive match, add the line to stockPrices list
            print("Line " + str(linenum) + ": " + line.rstrip('\n'))
            stockPrices.append(line.rstrip('\n'))  
            
for stockPrice in stockPrices:

    print(stockPrice)
    
    mySplit = stockPrice.split()  #split stock price line by spaces
    
    #print(str(res))
    
    priceIndex = len(mySplit)-1 #get price index which is usually the last on the line
    
    #print(mySplit[priceIndex].split(USD)[1])
    
    priceUSD = float(mySplit[priceIndex].split(USD)[1] )#remove currency symbol from price 
    
    #print(priceUSD)
    
    priceGBP  =  priceUSD*exRate
    
   # print(priceGBP)
    
   # print(mySplit[priceIndex].split(USD))
    
    print(subString+": "+GBP+str(round(priceGBP, 2)))     #print price rounded to two decimal places