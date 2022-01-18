class Card():

    def __init__(self,holder,number):

        self.holder = holder
        self.number = number
        self.amount = 100000

    def spend(self,a):
        pass

    def show(self):
       return f"""

name = {self.holder} 
card number =  {self.number}
summa =  {self.amount}

"""

class UzCard(Card):

    def spend(self, a):
        self.amount -= a


class Visa(Card):

    def spend(self, a):
        self.amount -= (a*10700)


class Atto(Card):

    def spend(self,a):
        self.amount -= 1400

name = input("Enter First Name and List Name: ")

uz = UzCard(name,"8600 1203 1445 1887")
vis = Visa(name,"1204 4563 2442 1323")
at = Atto(name, "8600 1243 1665 8334")

h = int(input("""

Kartani tanlang

1. UzCard
2. Visa
3. Atto
"""))

if h == 1:
    a = int(input("sarflangan summani kiriting: "))
    uz.spend(a)
    print(uz.show())

elif h == 2:
    a = int(input("sarflangan summani kiriting: "))
    vis.spend(a)
    print(vis.show())
elif h == 3:
    at.spend()
    print(at.show())
else:
    print("Afsuski bizda mavjud bo'lmagan menyuni kiritdingiz!")