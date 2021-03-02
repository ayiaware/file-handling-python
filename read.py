
# Opening file 
count = 0  
stockPrice = "stock price"
# Using for loop 
with open ('acme-info.txt', 'rt') as myfile:
    for line in myfile: 
        count += 1
        if line.lower().find(stockPrice) != -1:
            stockPrice = line.strip()
        print("Line {}: {}".format(count, stockPrice))

for price in stockPrice:
    print(price.split(" ", len(stockPrice)))

