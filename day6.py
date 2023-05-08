# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by me. The output
# should print the total of the 3 inputs rounded to 2 decimal places

coffee = float(input('1 coffee @: $ '))
sandwich = float(input('1 sandwich @: $ '))
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

print('Your total bill is $', bill_total)
