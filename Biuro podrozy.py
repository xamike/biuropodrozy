import random

class DestinationSelector:
    def __init__(self):
        self.base1 = {
            "Paris": {"duration": 7, "capacity": 5},
            "Berlin": {"duration": 5, "capacity": 4},
            "Warsaw": {"duration": 6, "capacity": 3}
        }
        self.base2 = {
            "New York": {"duration": 8, "capacity": 2},
            "Papeete": {"duration": 10, "capacity": 3},
            "Sydney": {"duration": 7, "capacity": 4}
        }
        self.base3 = {
            "Tokyo": {"duration": 9, "capacity": 2},
            "Beijing": {"duration": 6, "capacity": 3},
            "Seoul": {"duration": 8, "capacity": 4}
        }
        self.base4 = {
            "Riyad": {"duration": 5, "capacity": 2},
            "Cairo": {"duration": 7, "capacity": 3},
            "Lagos": {"duration": 4, "capacity": 4}
        }

        self.bases = [self.base1, self.base2, self.base3, self.base4]

    def generate_random_price(self):
        return random.randint(800, 3000)

    def select_destination(self):
        selected_base = random.choice(self.bases)
        selected_place = random.choice(list(selected_base.keys()))
        price = self.generate_random_price()
        selected_base[selected_place]["price"] = price
        return selected_place, selected_base[selected_place]

def display_menu():
    print("Destination Selector Menu:")
    print("1. Roll a random place")
    print("2. Explore a specific base")
    print("3. Exit")

def explore_base(base):
    print("\nExploring Base:")
    for place, details in base.items():
        print(f"- {place}: ${details['price']}, Duration: {details['duration']} days, Capacity: {details['capacity']} people")
    print("")

def main():
    print("Welcome to the Extended Destination Selector!")
    
    selector = DestinationSelector()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            selected_place, details = selector.select_destination()
            print(f"You are going to: {selected_place}")
            print(f"Details: ${details['price']}, Duration: {details['duration']} days, Capacity: {details['capacity']} people\n")
        elif choice == "2":
            base_choice = int(input("Enter the base number to explore (1-4): "))
            if 1 <= base_choice <= 4:
                explore_base(selector.bases[base_choice - 1])
            else:
                print("Invalid base number. Please enter a number between 1 and 4.\n")
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.\n")

if __name__ == "__main__":
    main()
