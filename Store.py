# Name: Jamar Hill
# Date: 4/10/2021
# Description: CS 162 Project 2

import re
"""Define Class Product"""
class Product:
    """Initialize five values that define the product. Def must be indented to initialize when self turns purple"""
    def __init__(self, id_code, title, description, price, quantity):
        self._id = id_code
        self._title = title
        self._description = description
        self._price = price
        self._quantity = quantity
    def get_id_code(self): #initalize get_id_code
        return self._id

    def get_title(self): #initalize _get_title
        return self._title

    def get_description(self): #initalize _get_description
        return self._description

    def get_price(self): #initalize get_id
        return self._price

    def get_quantity(self): #initalize get_quantity
        return self._quantity

    def decrease_quantity(self): #initalize get_decrease
        self.quantity = self._quantity - 1
        return self.quantity

"""Define Class Customer"""
class Customer:
    """Initialize three values that define the product"""
    def __init__(self, name, account_id, premium_member):
        self.name = name
        self.account_id = account_id
        self.premium_member = premium_member
        self.cart = []

    def get_cart(self): #define get_cart
        return self.cart
    def get_name(self): #define get_name
        return self.name
    def get_account_id(self): #define get_account_id
        return self.account_id
    def is_premium_member(self): #define_premium_member
        return self.premium_member
    def add_product_to_cart(self,id_code): #define add_product_to_cart
        self.cart.append(id_code)
    def empty_cart(self): #define empty_cart
        self.cart = []
"""Define Class Store"""
class Store:

    def __init__(self): #Initalize inventory and members
        self.inventory = []
        self.members = []

    def add_product(self, product): #Define add porduct as appending list
        self.inventory.append(product)
    def add_member(self,customer): #Define add customer as appending list
        self.members.append(customer)
    def get_product_from_id(self,id_code): #Define get_product_from_id. p is the variable. if p = id code the return p
        for p in self.inventory:
            if id_code == p.get_id_code():
                return p
        return None #If p doesn't match than return none

    def get_member_from_id(self, account_id): #Define get_member_from_if
        for c in self.members: #c represents the variable for customer. If c matches the account ID the it will return account id
            if c.get_account_id() == account_id:
                return c
        return None #If c doesnt match than the code will return none

    def add_product_to_member_cart(self, prd_id, mem_id):#Defines product to retrieve from ID
        p = self.get_product_from_id(prd_id)
        m = self.get_member_from_id(mem_id)

        if p is None:
                return "product ID not found" #Returns message if product ID cannot be matched up with a product
        elif m is None:
            return "member ID not found" #Returns message if member ID cannot be matched up with a product
        else:
            quan = p.get_quantity()
            if quan > 0: #Tests to see if the is enough quanitiy to fulfil the order
                m.add_product_to_cart(p.get_id_code())
                return "product added to cart"
            else:
                return "product out of stock" #Returns an our of stock message if their isn't suffient inventory

    def check_out_member(self, m_id):
        sum_total = 0.00 #Sets the total to zero

        grand_total = 0.00 #Sets the grand total to zero

        ship = 0.0 #Set shipping to zero
        if p is None:
            return "product ID not found" #If Product = None return None
        elif m is None:
            return "member ID not found" #Else if Member is None return None.
        else:
            quantity = prd.get_quantity() #Retrived quantity and test inventory levels for being greater than zero.
        if quantity > 0:
            m.add_product_to_cart(prd.get_id_code())
            return "product added to cart" #If greater than zero, add prduct to cart.
        else:
            return "product out of stock" #if inventory id not greater than zero, return our of stock.
    def check_out_member(self,mem_id):
        sum_total = 0.00 #Set sum total ot zero.
        grand_total = 0.00 #Set grand total to zero.
        ship = 0.00 #Set shipping to zero

        c = self.get_member_from_id(mem_id) #Match customer with ID.

        if c is None:
            raise InvalidCheckoutError() #Raise error if customer is not matched with ID.
        else:
            if len(c.get_cart()) == 0:
                print("No items in cart"); #Test if there are items in cart.
        for i in c.get_cart():
            p = self.get_product_from_id(i)
        if p.get_quantity() <= 0:
            print("Sorry, product " + p.get_id_code() + "," + p.getTitle()) #Test for quantity levels in cart
        else:
            sum_total = sum_total + p.get_price()
            p.decrease_quantity()
        if c.is_premium_member() is True: #apply premium_member benfits
            grand_total = sum_total
        else:
            ship = 0.07*sum_total #Calculate shipping
            grand_total = sum_total + ship #calculate grand total by adding shipping go sum.
            print("Subtotal: $" + str(sum_total))
            print("Shipping Cost: $" + str(ship))
            print("Total: $" + str(grand_total)) #Print grand total.
            c.empty_cart() #Empty cart.
            return grand_total

    def searchStore(self,txt):
        inStock = False #Start with the assumption that product is not available to initate the append feature

        search_str = []
        f = txt[:1] #Checks First Letter
        r = txt[1:] #Checks Remaining Letters
        t = re.compile("(?i)" + txt) #Total string# defines object Disregards letters after first letter
        for p in self.inventory:

            if re.search(t,p.get_title()) or re.search(t,p.get_description()):
                search_str.append(p.get_id_code())
        search_str.sort()
        return search_str
class InvalidCheckoutError(BaseException):
    pass
    if __name__ == '__main__':
        store = Store()

        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        c1 = Customer("Yinsheng", "QWF", False)
        myStore = Store()
        myStore.add_product(p1)
        myStore.add_member(c1)
        myStore.add_product_to_member_cart("889", "QWF")
        result = myStore.check_out_member("QWF")
        print(result)