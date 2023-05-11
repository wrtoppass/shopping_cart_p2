class Cart():
    grocery_dict={}
    '''
        {
            grocery_item : {
                quantity: int,
                price: float
            }
        }
    '''
    def driver(self):
        shopping = True
        while shopping:
#         user option for add, removing showing or quit
            res = input("Would you like to add/remove/show/quit?: ").lower()
#         handle add
            if res == 'add':
                self.add()
#         handle remove
            if res == 'remove':
                self.remove()
#         handle show
            if res == 'show':
                self.show()
#         handle quit
            if res == 'quit':
                shopping = False
#         continue until quit
            
    
    def add(self):
        item = input('What item are you adding?').lower()
        while True:
            quantity = input(f"How many {item} would you like to add?: ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print('Please enter quantity in digits')
        while True:
            try:
                price = float(input(f'How much does {item} cost?: '))
                break
            except:
                print('Please enter price in digits')
            
        if item in self.grocery_dict:
            pass
        else:
            self.grocery_dict[item] = {
                'quantity' : quantity,
                'price' : price
            }
        self.show()
    
    def remove(self):
        item_to_remove = input('What item would you like to remove?: ').lower()
        while True:
            try:
                quantity = int(input('How many would you like to remove?: '))
                break
            except:
                print('Please enter quantity in digits!')
        if item_to_remove in self.grocery_dict:
            self.grocery_dict[item_to_remove]['quantity'] -= quantity
            if self.grocery_dict[item_to_remove]['quantity'] < 1:
                self.grocery_dict.pop(item_to_remove)
        else:
            print("Item not in list")
        self.show()
    
    def show(self):
        print(self.grocery_dict)

    def test_case_add_items(self):
        cart = Cart()
        cart.add()
        cart.add()
        cart.add()
        cart.show()

    def test_case_remove_items(self):
        cart = Cart()
        cart.add()
        cart.add()
        cart.remove()
        cart.show()

    def test_case_add_remove_items(self):
        cart = Cart()
        cart.add()
        cart.add()
        cart.remove()
        cart.add()
        cart.show()