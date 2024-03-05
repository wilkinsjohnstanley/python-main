import random
#create the class
class Coin:
    #iniit method
    def __init__(self):
        self.sideup='Heads'
#toss the coin
    def toss(self):
        #if it's a 0, this is head, otherwise its tails
        if random.randint(0,1)==0:
            self.sideup='Heads'
        else:
            self.sideup='Tails'
    def get_sideup(self):
        return self.sideup

#main function


def main():
    #create an object(an instance) from the class (Coin)
    my_coin=Coin()
    print('This is side is up: ', my_coin.get_sideup())
    #toss the coin
    print('I will now toss the coin')
    my_coin.toss()

    #display the side of the coin that is facing up
    print('This side is up: ', my_coin.get_sideup())

main()