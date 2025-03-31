def calculate_discount(price, discount_percent):
    discount_percent /= 100
    if discount_percent >= 0.2:
        final_price = price * (1 - discount_percent)
        return final_price
    else:
        return price
    
while True:
    print("---Amount after discount calculator---")
    print("Please input the given information when asked")

    try:
        price = int(input("Please input the original price of the product: "))
        discount_percent = int(input("Please input the percentage discount without the % sign: "))
        
        discount_price = calculate_discount(price, discount_percent)
        print(discount_price)

    except ValueError:
        print("Please enter numbers only, no percent sign or letters")

    again = input("Would you like to make another calculation?(yes/no) ").strip().lower()
    if again == "yes":
        pass
    elif again == "no":
        print("Thank you for using our program. Good bye")
        break
    else:
        print("Please enter either yes or no")