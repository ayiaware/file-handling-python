                        
subString = "Stock Price"        # Substring to search for.

USD = '$'
GBP = '£'
exRate =  0.77

def extractStockLine():
    with open ('acme-info.txt', 'rt') as acmefile:
        for line in acmefile:                       #use for loop to iterate through file
            if line.lower().find(subString.lower()) != -1:    # if case-insensitive match, add the line to stockPrices list
                stockPriceLine = line.rstrip('\n') .split() #split stock price line by spaces and asign to variale
                return stockPriceLine

def covertUSDToGBP(priceUSD):
    priceGBP  =  priceUSD*exRate  #convert to GBP
    return priceGBP


stockPriceLine = extractStockLine()
                            
priceIndex = len(stockPriceLine)-1  #get price index which is usually the last on the line
    
priceUSD = float(stockPriceLine[priceIndex].strip(USD)) #exclude currency symbol from price and convert and asign to float type
    
priceGBP = covertUSDToGBP(priceUSD)
    
print(subString+": "+GBP+str(round(priceGBP, 2)))     #print price rounded to two decimal places

