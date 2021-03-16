price_before_tax = float (input('Enter a price without taxes: '))
tax_percent = 0.21
price_after_tax = price_before_tax * (1+tax_percent)

output = f'''
Subtotal: {price_before_tax:>10,.2f} €
Taxes:    {price_before_tax * tax_percent:>10,.2f} €
Total:    {price_after_tax:>10,.2f} €
'''
print(output)