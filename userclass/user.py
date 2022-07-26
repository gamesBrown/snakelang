class User:
    def __init__(self,first_name,last_name,age,email):
        self.first_name =first_name
        self.last_name=last_name
        self.age=age
        self.email=email
        self.is_rewards_member =False
        self.gold_card_points=200

    def display_info(self):
        print(f"Name = {self.first_name} {self.last_name}\nAge: {self.age}\nEmail: {self.email}\nRewards Status:{self.is_rewards_member}\nRewards Points: {self.gold_card_points}")
        return self
    def enroll(self):
        if self.is_rewards_member == True:
                print("User is already a rewards member")
        else:
            self.is_rewards_member=True
            print(f"{self.first_name} is now a rewards member.")
        return self
    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            print(f"{self.first_name} {self.last_name} spent {amount} Points!")
            self.gold_card_points -= amount
        else:
            print("You don't have enough points to spend...")
        return self


print("Jello!")

user_ada=User("Adaline","Robertson",42,"ada.robertson@fakemail.com")



print(user_ada.first_name)

class Shoe:
    def __init__(self):
        self.brand="Adidas"
        self.type="tennis shoe"
        self.price=45.99
        self.in_stock=True



shoe_adidas =Shoe()
print(shoe_adidas.brand)
shoe_adidas.in_stock=False
print(shoe_adidas.in_stock)

user_ada.display_info()
user_ada.enroll()
user_ada.enroll().spend_points(100).spend_points(50).spend_points(50).spend_points(1)

