from prettytable import PrettyTable

countries = PrettyTable()

columns = ['Country', 'Official Language'] 
country_names = [
    'Spain', 'France', 'Portugal', 'Italy',
    'Belgium', 'Germany', 'Poland', 'Denmark']
country_lang = ['Spanish', 'French',
                     'Portuguese', 'Italian',
                     'French', 'German', 'Polish',
                     'Danish']

countries.add_column('Country', country_names)
countries.add_column('Official Language',country_lang)
print(countries)