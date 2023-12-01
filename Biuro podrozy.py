import random

class DestinationSelector:
    def __init__(self):
        self.base1 = {
            "Paris": {"duration": 7, "capacity": 5, "price": None},
            "Berlin": {"duration": 5, "capacity": 4, "price": None},
            "Warsaw": {"duration": 6, "capacity": 3, "price": None}
        }
        self.base2 = {
            "New York": {"duration": 8, "capacity": 4, "price": None},
            "Papeete": {"duration": 10, "capacity": 3, "price": None},
            "Sydney": {"duration": 7, "capacity": 7, "price": None}
        }
        self.base3 = {
            "Tokyo": {"duration": 9, "capacity": 10, "price": None},
            "Beijing": {"duration": 6, "capacity": 6, "price": None},
            "Seoul": {"duration": 8, "capacity": 4, "price": None}
        }
        self.base4 = {
            "Riyad": {"duration": 5, "capacity": 2, "price": None},
            "Cairo": {"duration": 7, "capacity": 5, "price": None},
            "Lagos": {"duration": 4, "capacity": 3, "price": None}
        }

        self.bases = [self.base1, self.base2, self.base3, self.base4]

        self.destinations_tuple = (("Paris", 7, 5), ("Berlin", 5, 4), ("Warsaw", 6, 3))
        self.unique_destinations_set = {"Paris", "Berlin", "Warsaw", "New York", "Papeete", "Sydney", "Tokyo", "Beijing", "Seoul", "Riyad", "Cairo", "Lagos"}

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
    print("2. Display all destinations")
    print("3. Exit")

def display_all_destinations(selector):
    print("\nAll Destinations:")
    for base in selector.bases:
        for place, details in base.items():
            price = details['price'] if details['price'] is not None else "N/A"
            print(f"{place}: ${price}, Duration: {details['duration']} days, Capacity: {details['capacity']} people")

    print("\nDestinations Tuple:")
    for destination in selector.destinations_tuple:
        print(f"{destination[0]}: Duration: {destination[1]} days, Capacity: {destination[2]} people")

    print("\nUnique Destinations Set:")
    for destination in selector.unique_destinations_set:
        print(destination)

    print()

def main():
    print("Welcome to the Extended Destination Selector!")
    
    selector = DestinationSelector()

    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")

        match choice:
            case "1":
                selected_place, details = selector.select_destination()
                print(f"You are going to: {selected_place}")
                print(f"Details: ${details['price']}, Duration: {details['duration']} days, Capacity: {details['capacity']} people\n")

            case "2":
                display_all_destinations(selector)

            case "3":
                print("Exiting the program. Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter a number between 1 and 3.\n")

if __name__ == "__main__":
    main()

