
subString = "Notable Products"        # Substring to search for.

def extractNotableProducts():                                   #function to extract all information under notable products heading #asuming all lines are notable products with amounts in brackets
                                                                #another method would be to extract all lines with sold at the end without checking if they under heading
                                                                # a more practical method will be to do both
    notableProducts = []                                        #list to hold all notable products 
    
    with open ('acme-info.txt', 'rt') as acmefile:
        
        for line in acmefile:                                   #use for loop to iterate through file
            if line.lower().find(subString.lower()) != -1:      #start extraction at NOTABLE PRODUCTS heading
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
        
                
print("Best-selling product : "+findBestSeller(extractNotableProducts()))     #print price rounded to two decimal places

