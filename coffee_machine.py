def ask_choice():
    coffee_options = ['espresso','expresso','latte','cappuccino','capuchino']
    while True:
        
        choice = input("What would you like? (espresso/latte/cappuccino/): ")
        if choice in coffee_options:
            return choice
        elif choice == 'off' :
            print('\n')
            break
        
class Coffee_type():
    water = 0
    milk = 0
    coffee = 0
    price = 0
    
class Coffee_machine():
    
    water = 500
    milk = 500
    money = 0
    coffee = 1000
    
    resources = {'Water':[water,'mL'],'Milk':[milk,'mL'],'Coffee':[coffee,'g'], 'Money':[money,'€']}
    
    def report():
        print('These are the available resources:')
        for item,quantity in resources.items():
            print(f'{item}: {quantity[0]} {quantity[1]}')
    
    def check_enough(coffee_type, coins):
        requirements = [coffee_type.water, coffee_type.milk, coffee_type.coffee, coffee_type.price]
        
        enough = False
        
        if requirements[0] > resources['Water'][0] :
            print("There isn't enough water left. I can't serve your order. Sorry for the inconvenience.")
        elif requirements[1] > resources['Milk'][0] :
            print("There isn't enough milk left. I can't serve your order. Sorry for the inconvenience.")
        elif requirements[2] > resources['Coffee'][0] :
            print("There isn't enough coffee left. I can't serve your order. Sorry for the inconvenience.")
        else:
            enough = True
        
        return enough
    
    def process_coins():
        entered_money = 0
        
        types_coins = {'5 cents':0.05,'10 cents':0.1,'50 cents':0.5, '1 euro': 1, '2 euros': 2}
        for name,value in types_coins.items():
                  
            while True:
                num_coins = input(f'{name} coins? ')
                if num_coins = '':
                    break
                else:
                    try:
                        num_coins = int(num_coins)
                    except ValueError:
                    print(f'Please, enter a valid number of {name} coins. Try again...')
                    continue
                    entered_money += num_coins * value
                    break
       
            
        print("""
              Type 'how many coins' and 'its type', following this notation:\n")
              A: 5 cents, B: 10 cents, C: 20 cents, D: 50 cents, E: 1 euro, F: 2 euros.
              For example: "E 1 D 1" means 1.50 €.""")
        entered_coins
        
        
            
        