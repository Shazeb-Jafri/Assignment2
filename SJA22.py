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

class StatementStock:
    def __init__(self, product):
        self.monthly_stock = []
        self.product = product
        self.final_revenue = 0
        self.final_manufacture_cost = 0

    def generate_monthly_sale(self):
        sold_units = random.randint(0, min(self.product.stock_level, 20))
        self.product.stock_level -= sold_units
        return sold_units

    def generate_stock_statement(self, months=12):
        header = f"{'Month':<7}{'Manufacture':<15}{'Sold':<10}{'Stock':<10}"

        for i in range(1, months + 1):
            self.generate_and_display_monthly_statement(i, header)
        

    def generate_and_display_monthly_statement(self, month, header):
        sold_units = self.generate_monthly_sale()
        manufactured_units = self.product.generate_monthly_production()
        self.monthly_stock.append(self.product.stock_level)

        if self.product.stock_level < 0:
            print("Out of Stock")
            self.product.stock_level = 0
        else:
            line = f"{month:<7}{manufactured_units:<15}{sold_units:<10}{self.product.stock_level:<10}"
            print(f"\n{header}\n{line}")
            revenue = sold_units * self.product.product_price
            self.final_revenue += revenue
            print()
        return self.monthly_stock

class SalesApplication:
    def __init__(self):
        self.product = None
        self.stock_statement = None

    def perform_sales_simulation(self):
        self.create_product()
        self.display_product_info()
        self.create_stock_statement()
        self.simulate_sales()
        self.display_total_revenue()

    def display_total_revenue(self):
        if self.stock_statement:
            print("\nFinal Revenue Statement: ")
            print("Total Revenue: $", self.stock_statement.final_revenue)
        else:
            print("Invalid input, try again")

    def get_user_input(self, data_type, prompt):
        while True:
            user_input = input(prompt)
            try:
                return data_type(user_input)
            except ValueError:
                print("Invalid input, please enter a valid value.")

    def create_product(self):
        product_name = self.get_user_input(str, "Enter the Name of the Product: ")
        product_code = input("Enter the code of the product: ")
        manufacture_cost = self.get_user_input(float, "Enter the Manufacturing Cost of the Product: ")
        product_price = self.get_user_input(float, "Enter the Product Sale Price: ")
        est_monthly_units = self.get_user_input(int, "Enter Estimated Monthly Units: ")
        stock_level = self.get_user_input(int, "Enter the Product Stock Level: ")
        self.product = Product(product_price, manufacture_cost, stock_level, est_monthly_units, product_code, product_name)

    def create_stock_statement(self):
        self.stock_statement = StatementStock(self.product)

    def display_product_info(self):
        if self.product:
            print("\nProduct created successfully:")
            print("Product Name:", self.product.product_name)
            print("Product Code:", self.product.product_code)
            print("Product Manufacture Cost:", self.product.manufacture_cost)
            print("Product Price:", self.product.product_price)
            print("Estimated Monthly Units:", self.product.est_monthly)
            print("Stock Level:", self.product.stock_level)
        else:
            print("Invalid input. Please enter a valid input.")

    def simulate_sales(self):
        if self.stock_statement:
            print("\n12 Months Stock Statement:")
            monthly_stock = self.stock_statement.generate_stock_statement()
        else:
            print("Error, try again.")
        

app = SalesApplication()
app.perform_sales_simulation()
