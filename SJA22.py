import random

class Product:
   def __init__ (self, product_price, manufacture_cost, stock_level, est_monthly, product_code, product_name):
       self.product_price = product_price
       self.manufacture_cost = manufacture_cost
       self.stock_level = stock_level
       self.est_monthly = est_monthly
       self.product_code = product_code
       self.product_name = product_name

   def generate_monthly_production(self):
       units_produced = random.randint(self.est_monthly - 5, self.est_monthly + 5)
       self.stock_level += units_produced
       return units_produced

class Stock:
   def __init__(self, product):
       self.monthly_stock = []
       self.product = product

   def generate_monthly_sales(self):
       units_sold = random.randint (0, min(self.product.stock_level, 20))
       self.product.stock_level -= units_sold
       return units_sold

   def generate_stock_statement(self, months = 12):
       for i in range(months):
           sold_units = self.generate_monthly_sales()
           self.monthly_stock.append(self.product.stock_level)
           if self.product.stock_level < 0:
               print ("Out of Products")
               self.product.stock_level = 0
       return self.monthly_stock

def create_product():
   product_name = input("Enter the Name of the Product: ")
   product_code = input("Enter the code of the product: ")
   manufacture_cost = float(input("Enter the Manufacturing Cost of the Product: "))
   product_price = float(input("Enter the Product Sale Price: "))
   est_monthly_units = int(input("Enter Estimated Monthly Units: "))
   stock_level = int(input("Enter the Product Stock Level: "))
   return Product(product_name, product_code, manufacture_cost, product_price, est_monthly_units, stock_level)

class SalesApplication:
   def __init__ (self):
       self.product = None

   def perform_sales_simulation(self):
       self.create_product()
       self.display_product_info()
       self.simulate_sales()

   def get_user_input(self, data_type, prompt):
       while True:
           user_input = input(prompt)
           try:
               return data_type(user_input)
           except ValueError:
               print ("Invalid input, please enter a valid value.")

   def create_product(self):
       product_name = self.get_user_input(str, "Enter the Name of the Product: ")
       product_code = input("Enter the code of the product: ")
       manufacture_cost = self.get_user_input(float, "Enter the Manufacturing Cost of the Product: ")
       product_price = self.get_user_input(float, "Enter the Product Sale Price: ")
       est_monthly_units = self.get_user_input(int, "Enter Estimated Monthly Units: ")
       stock_level = self.get_user_input(int, "Enter the Product Stock Level: ")
       self.product = Product(product_price, manufacture_cost, stock_level, est_monthly_units, product_code, product_name)

   def display_product_info(self):
       if self.product:
           print("Product created successfully: ")
           print("Product Name: ", self.product.product_name)
           print("Product Code: ", self.product.product_code)
           print("Product Manufacture Cost: ", self.product.manufacture_cost)
           print("Product Price: ", self.product.product_price)
           print("Estimated Monthly Units: ", self.product.est_monthly)
           print("Stock Level", self.product.stock_level)
       else:
           print("Invalid input. Please enter a valid input.")

   def simulate_sales(self):
       stock_statement = Stock(self.product)
       stock_statement.generate_stock_statement()
       
app = SalesApplication()
app.perform_sales_simulation()
