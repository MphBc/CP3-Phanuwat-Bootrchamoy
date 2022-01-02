print("Hello")
username = input("username :")
password = input("password :")
if username == "moo" and password == "mink" :
    print("Login")
elif username and password:
    print("Wrong username or password")
if username == "moo" and password == "mink" :
    print("---------------------------------")
    print("Welcome moo & mink store")
    print("Do you pay cash or credit card ?")
    print("1. cash")
    print("2. credit card")
    pay = input(">>")
    if pay == "1":
        print("---------------------------------")
        print("cash calculate")
        print("List")
        list1 = input("1.")
        quantity1 = int(input("quantity:"))
        price1 = int(input("price (THB):"))
        calculate1 = quantity1 * price1
        list2 = input("2.")
        quantity2 = int(input("quantity:"))
        price2 = int(input("price (THB):"))
        calculate2 = quantity2 * price2
        list3 = input("3.")
        quantity3 = int(input("quantity:"))
        price3 = int(input("price (THB):"))
        calculate3 = quantity3 * price3
        Total = int(calculate1 + calculate2 + calculate3)
        Vat = 7
        Vat1 = (Total * Vat) / 100
        Totalvat = (Total + (Total * Vat) / 100)
        print("---------------------------------")
        print("Cash reciept")
        print("Desception", "        ", "Price")
        print(quantity1, "x", list1, "       ", calculate1, "THB")
        print(quantity2, "x", list2, "       ", calculate2, "THB")
        print(quantity3, "x", list3, "       ", calculate3, "THB")
        print("Total : ", calculate1 + calculate2 + calculate3)
        print("Vat 7% :", Vat1)
        print("Total vat :", Totalvat)
        print("---------------------------------")
    elif pay == "2":
        print("---------------------------------")
        print("credit card calculate")
        print("List")
        list1 = input("1.")
        quantity1 = int(input("quantity:"))
        price1 = int(input("price (THB):"))
        calculate1 = quantity1 * price1
        list2 = input("2.")
        quantity2 = int(input("quantity:"))
        price2 = int(input("price (THB):"))
        calculate2 = quantity2 * price2
        list3 = input("3.")
        quantity3 = int(input("quantity:"))
        price3 = int(input("price (THB):"))
        calculate3 = quantity3 * price3
        Total = int(calculate1 + calculate2 + calculate3)
        Vat = 10
        Vat1 = (Total * Vat) / 100
        Totalvat = (Total + (Total * Vat) / 100)
        print("---------------------------------")
        print("Credit card reciept")
        print("Desception", "        ", "Price")
        print(quantity1, "x", list1, "       ", calculate1, "THB")
        print(quantity2, "x", list2, "       ", calculate2, "THB")
        print(quantity3, "x", list3, "       ", calculate3, "THB")
        print("Total : ", calculate1 + calculate2 + calculate3)
        print("Vat 10% :", Vat1)
        print("Total vat :", Totalvat)
        print("---------------------------------")