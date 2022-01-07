price = int(input("price? :"))
def vatCalculate(totalPrice):
    result = int(totalPrice+(totalPrice*7/100))
    return result
print("Vat calculate:",vatCalculate(price))