### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources


    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] >= ingredients["bread"] and self.machine_resources["ham"] >= ingredients["ham"] and self.machine_resources["cheese"] >= ingredients["cheese"]:
            return True
        else:
            return False

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        self.coins = int(input("How many quarters do you have?: "))
        self.coins =  self.coins * 0.25
        return self.coins
        

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print("Transaction successful!")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False
        

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(order_ingredients):
            coins = self.process_coins()
            if self.transaction_result(coins, recipes[sandwich_size]["cost"]):
                self.machine_resources["bread"] = self.machine_resources["bread"] - order_ingredients["bread"]
                self.machine_resources["ham"] = self.machine_resources["ham"] - order_ingredients["ham"]
                self.machine_resources["cheese"] = self.machine_resources["cheese"] - order_ingredients["cheese"]
                print("Sandwich is ready!")
            else:
                print("Transaction failed.")
        else:
            print("Insufficient resources, sorry!")


### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)
user_choice = input("What type of sandwich would you like?\n small, medium, large: ")
machine.make_sandwich(user_choice, recipes[user_choice]["ingredients"])

while True:
    user_choice = input("Would you like to make another sandwich? (yes/no): ")
    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        user_choice = input("What type of sandwich would you like?\n small, medium, large: ")
        machine.make_sandwich(user_choice, recipes[user_choice]["ingredients"])
    else:
        print("Have a good day!")
        break