def gramOunce(percent, grams):
    oz = float((grams * percent)/31.1035)
    return oz

pureGold = 0.99
scrapGold = 0.985
scrapSilverCoin = 0.95
scrapDirtySilver = 0.90

sterlingSilver = 0.925
eightQuarters = 0.50
sevenQuarters = 0.65
sixQuarters = 0.80

ounceConversion = 31.1035

totalGrams = float(input("Input the total grams"))

metalType = input("A: Gold  B: Silver")

if metalType == "A":
    goldType = input("A: Pure Gold  B: Scrap Gold")
    goldPercent = float(input("Input the percentage of Gold (decimal)"))
    spotPrice = float(input("Input the spot price of Gold"))
    fineOunces = gramOunce(goldPercent,totalGrams)

    if goldType == "A":
        comPrice = spotPrice * pureGold
        ouncePrice = comPrice * fineOunces
        print(spotPrice , "   " , "Gold" , "   " , fineOunces , "   " . comPrice , "   " , ouncePrice)
    elif goldType == "B":
        comPrice = spotPrice * scrapGold
        ouncePrice = comPrice * fineOunces
        print(spotPrice , "   " , "Gold" , "   " , fineOunces , "   " , comPrice , "   " , ouncePrice)
    else:
        print("Not a valid input")

elif metalType == "B":
    typeSilverObject = input("A: Silver Melt    B: Silver Quarters ")
    if typeSilverObject == 1:
        silverType = input("A: Scrap Silver Coin    B: Scrap Dirty Silver")
        silverPercent = float(input("Input the percentage of Silver (decimal)"))
        spotPrice = float(input("Input the spot price of Silver"))
        fineOunces = gramOunce(silverPercent,totalGrams)

        if silverType == "A":
            comPrice = spotPrice * scrapSilverCoin
            ouncePrice = comPrice * fineOunces 
            print(spotPrice , "   " , "Silver" , "   " , fineOunces , "   " , comPrice , "   " , ouncePrice)
        elif silverType == "B": 
            comPrice = spotPrice * scrapDirtySilver
            ouncePrice = comPrice * fineOunces 
            print(spotPrice , "   " , "Silver" , "   " , fineOunces , "   " , comPrice , "   " , ouncePrice)
        else: 
            print("Input invalid")

    elif typeSilverObject == "B":
        quarterType = input("A: 1968    B: 1967    C: 1966 and Prior")
        if quarterType == "A" or "B" or "C":
            print("See Price Chart")
        else:
            print("Error invalid input")



elif metalType == "B":
    silverType = input("1: Scrap Silver Coin    2: Scrap Dirty Silver")
    silverPercent = input("Input the percent of Silver")
else:
    print("Not a valid input") 
    






