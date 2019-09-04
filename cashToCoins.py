dollarAmount = 8.99

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def calc_coins():
    piggyBank["quarters"] = int(round((dollarAmount // .25), 2))
    piggyBank["dimes"] = int(round(dollarAmount % .25, 2) / .10)
    piggyBank["nickels"] = int(round(dollarAmount % .10, 2) // .05)
    piggyBank["pennies"] = int(round(dollarAmount % .05, 2) / .01)
    print(piggyBank)
    # print(round((dollarAmount % .05) / .01, 2))
    print(int(round((dollarAmount // .25), 2)))
    print(round(dollarAmount % .10, 2) // .05)
    # print(round(dollarAmount % .25, 2) / .10)
    # print(round(dollarAmount % .05, 2) / .01)


calc_coins()

# piggyBank = {
#     "pennies": 0,
#     "nickels": 0,
#     "dimes": 0,
#     "quarters": 0
# }

# def cash_to_coins(amt):
#     quarters = amt // .25
#     piggyBank["quarters"] = quarters
#     diff = amt - (quarters * .25)

#     dimes = diff // .1
#     piggyBank["dimes"] = dimes
#     diff = diff - (dimes * .1)

#     nickels = diff // .05
#     piggyBank["nickels"] = nickels
#     diff = diff - (nickels * .05)

#     pennies = diff // .01
#     piggyBank["pennies"] = pennies
#     diff = diff - (pennies * .01)

#     print(piggyBank)

# cash_to_coins(dollarAmount)