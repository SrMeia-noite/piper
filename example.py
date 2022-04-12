from pipe import ( where
                 , select
                 , get
                 , sum
                 , name
                 , greater_or_equal
                 , less_than 
                 )

inventory = [
    { 'id': 1, 'name': 'Armor' , 'price': 1000 },
    { 'id': 2, 'name': 'Helmet', 'price': 500  },
    { 'id': 3, 'name': 'Sword' , 'price': 2000 },
    { 'id': 4, 'name': 'Shield', 'price': 1500 },
    { 'id': 5, 'name': 'Ring'  , 'price': 500  },
    { 'id': 6, 'name': 'Potion'                },
]

# Get the total price of inventory:
total_price = inventory | get ('price') | sum

# Get the items that costs or costs more than 1000:
expensive_items = inventory                                      \
                | where ( name& 'price' ^ greater_or_equal& 1000 )

# Get the id of items that costs less than 1000:
id_of_cheap_items = inventory                                 \
                  | where ( name& 'price' ^ less_than& 1000 ) \
                  | select ('id')

print(f'Total price: {total_price}')
print(f'Expensive items: {expensive_items}')
print(f'Id and names: {id_of_cheap_items}')
