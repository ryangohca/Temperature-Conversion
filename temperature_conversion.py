from math import ceil
#temperature conversion program
#Celsius - Fahrenheit / Fahrenheit - Celsius

def displayWelcome():
    print("This program will convert a range of temperatures.")
    print("Enter (F) to convert Fahrenheit to Celsius.")
    print("Enter (C) to convert Celcius to Fahrenheit.")

def getConvertTo():
    convertType = input("Enter selection: ")
    start = input("Enter starting temperature to convert: ")
    end = input("Enter ending temperature to convert: ")
    return convertType, int(start), int(end)

def convertToFahren(celcius):
    return round(celcius * (9 / 5) + 32, 1)

def convertToCelcius(fahren):
    return round((fahren - 32) * (5 / 9), 1)

def print_formatting(title1, title2, list1, list2, maxlen1, maxlen2):
    title1 = title1.split('\n')
    title2 = title2.split('\n')
    title1[0] = title1[0].center(max(len(title1[1]), maxlen1))
    title1[1] = title1[1].center(max(len(title1[1]), maxlen1))
    title2[0] = title2[0].center(max(len(title2[1]), maxlen2))
    title2[1] = title2[1].center(max(len(title2[1]), maxlen2))
    print(title1[0], title2[0])
    print(title1[1], title2[1])
    for str1, str2 in zip(list1, list2):
        print(str1.center(max(len(title1[1]), maxlen1)), str2.center(max(len(title2[1]), maxlen2)))
    
    
def displayFahrenToCelsius(start,end):
    maxlen1 = 0
    maxlen2 = 0
    list1 = []
    list2 = []
    for i in range(start, end + 1):
        list1.append("%.1f" % float(i))
        maxlen1 = max(maxlen1, len("%.1f" % i))
        list2.append("%.1f" % convertToCelcius(i))
        maxlen2 = max(maxlen2, len("%.1f" % convertToCelcius(i)))
    print_formatting("  Degrees \nFarhenheit", "Degrees\nCelcius", list1, list2, maxlen1, maxlen2)
    

def displayCelsiusToFahren(start,end):
    maxlen1 = 0
    maxlen2 = 0
    list1 = []
    list2 = []
    for i in range(start, end + 1):
        list1.append("%.1f" % float(i))
        maxlen1 = max(maxlen1, len("%.1f" % i))
        list2.append("%.1f" % convertToFahren(i))
        maxlen2 = max(maxlen2, len("%.1f" % convertToFahren(i)))
    print_formatting("Degrees\nCelcius", "  Degrees \nFarhenheit", list1, list2, maxlen1, maxlen2)



def main():
    displayWelcome()
    convertType, start, end = getConvertTo()
    if convertType.lower() == 'f':
        displayFahrenToCelsius(start, end)
    else:
        displayCelsiusToFahren(start, end)

if __name__ == '__main__':
    main()
