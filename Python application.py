class supermarket:
    _product_code=[]
    _product_name=[]
    _product_price=[]
    _product_Quantity=[]

    def updatestore(self):
        self.p = int(input("Enter no of products to store"))
        for x in range(self.p):
            self._product_code.append(int(input("Enter product code: ")))
            self._product_name.append(int(input("Enter product name: ")))
            self._product_price.append(int(input("Enter product price: ")))
            self._product_Quantity.append(int(input("Enter product Quantity: ")))
    def display(self):
        print("product in our store")
        print("---------------------------------------------")
        print("product code \t product name \t product price ")
        print("---------------------------------------------")
        for x in range(self.p):
            print(self._product_code[x], "\t",self._product_name[x], "\t\t",self._product__price[x], "\t\t\t",self._product_Quantity[x],"\t\t\t\t")
            print("------------------------------------------------")
    def print_bill(self):
        total_price=0
        for x in range(self.p):
            Quantity = int(input("Enter Quantity for product code %d "%self._product_code[x]))
            self._product_Quantity.append(Quantity)
            total_price = total_price + self._product_price[x] * self._product_Quantity[x]
            print("\t\t\t invoice Receipt \t\t\t")
            print("---------------------------------------------------------------")
            print("product code\t product name\t product price\t Quantity \t Total Amount")
            print("---------------------------------------------------------------")
        for x in range (self.p):
            print(self._product_code[x],"\t\t",self._product_name[x],"\t\t\t",self._product_price[x] * self._product_Quantity[x])

Storekeeper=supermarket()
Storekeeper.updatestore()
Storekeeper.display()
Storekeeper.print_bill()
