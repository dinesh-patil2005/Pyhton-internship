def calculateElectronicsGST(a, b):
    total = a + b
    return total + total * 18 / 100

def calculateFashionGST(c, d):
    total = c + d
    return total + total * 13 / 100

def calculateFoodGST(e):
    return e + (e * 7 / 100)

def totalBILL(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food

def calculateDiscount(a, b, c, d, e):
    total = totalBILL(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount

a = 100
b = 100
c = 100
d = 100
e = 100

total_bill = totalBILL(a, b, c, d, e)
discount = total_bill * 20 / 100
final_amount = calculateDiscount(a, b, c, d, e)

print(f"total after GST = {total_bill:.2f}")
print(f"discount = {discount:.2f}")
print(f"final payment amount = {final_amount:.2f}")
