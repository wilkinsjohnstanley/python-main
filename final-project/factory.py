#superclass
class Logistics:
    def __init__(self, product, transport, destination, price):
        self.product=product
        self.transport=transport
        self.destination=destination
        self.price=price
    def set_product(self, product):
        self.product=product
    def set_transport(self, transport):
        self.transport=transport
    def set_destination(self, destination):
        self.destination=destination
    def set_price(self, price):
        self.price=price
    def get_product(self):
        return self.product
    def get_transport(self):
        return self.transport
    def get_destination(self):
        return self.destination
    def get_price(self):
        return self.price 

class Land(Logistics):
    def __init__(self, product, transport,destination,price):
        Logistics.__init__(self, product, transport, destination, price)
class Sea(Logistics):
     def __init__(self, product, transport,destination,price):
        Logistics.__init__(self, product, transport, destination, price)

def main():
    print("Thank you for using our Logistics service!")
    product=input("What are you shipping?")
    transport=input("Will you ship the product by land or by sea? (land/sea):")
    destination=input("Where are you shipping it to?")
    price=int(input("What is the value of the item your shipping?"))

    item=Land(product, transport, destination, price)
    if(transport=="land"){
       
        print('\nSummary of Shipment Logistics\n')
        print('Product: ', landTransport.get_product())
        print('Transportation method: ', landTransport.get_transport())
        print('Destination: ', landTransport.get_destination())
        print('Price: ', landTransport.get_price())
        }
    else if (transport=="sea"){

        print('Product: ', seaTransport.get_product())
        print('Transportation method: ', seaTransport.get_transport())
        print('Destination: ', seaTransport.get_destination())
        print('Price: ', seaTransport.get_price())
    }
 #   else {
  #      print("Error: Start over. Check that you entered transportation method correctly.")
  #  }
    
    


main()