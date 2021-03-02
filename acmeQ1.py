                        
strPrice = "Stock Price"        # Substring to search for.

strProducts = "Notable Products"        # Substring to search for.


USD = '$'
GBP = '£'
exRate =  0.77


def extractStockPrice():
    with open ('files/acme-info.txt', 'rt') as acmefile:
        for line in acmefile:                                           #use for loop to iterate through file
            if line.lower().find(strPrice.lower()) != -1:               # if case-insensitive match, add the line to stockPrices list
                stockPriceLine = line.rstrip('\n') .split()             #split stock price line by spaces and asign to variale
                priceIndex = len(stockPriceLine)-1                      #get price index which is usually the last on the line
    
                priceUSD = float(stockPriceLine[priceIndex].strip(USD)) #exclude currency symbol from price and convert and asign to float type
    
                return priceUSD                                         #return  line containing stockprice on first match and exit loop


def covertUSDToGBP(priceUSD):                                   #function to convert USD to GBP using defined exhange rate
    priceGBP  =  priceUSD*exRate                                #convert to GBP
    return priceGBP


def extractNotableProducts():                                   #function to extract products under notable products heading 
    notableProducts = []                                        #list to hold all notable products 
    
    with open ('files/acme-info.txt', 'rt') as acmefile:
        
        for line in acmefile:                                   #use for loop to iterate through file
            if line.lower().find(strProducts.lower()) != -1:    #start extraction at NOTABLE PRODUCTS heading
               for line in acmefile:                            #read through remaining file
                   if line == "\n":                             #stop extraction at the end of NOTABLE PRODUCTS paragraph
                       break
                   elif line.find("-") == -1:                   #omit ----
                      notableProducts.append(line.strip())      #add notable products to list
        return notableProducts                                  #return list of notable products



def findBestSeller(notableProducts):                            #function to find best seller from list of extracted notable products
    productName = []                                            
    productSold = []
    
    for product in notableProducts:
       productName.append(product.split("(")[0])                #use (brackets) isolate products sold and names
       productSold.append(float(product.split("(")[1].split()[0]))

    soldMax = productSold.index(max(productSold))               #get highest selling product from productSold list
    return productName[soldMax]                                 #return the name of best selling product
        
                            
priceGBP = covertUSDToGBP(extractStockPrice())
    
print("Stock price: "+GBP+str(round(priceGBP, 2)))     #print price rounded to two decimal places
                
print("Best-selling product : "+findBestSeller(extractNotableProducts()))     #print price rounded to two decimal places



