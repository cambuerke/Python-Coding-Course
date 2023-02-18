"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 11.1 - Dice
Date: 11/16/2022

Description:
    Doesnt matter

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random as r

"""Write new functions below this line (starting with unit 4)."""
class Garage:
    def __init__(self,name,spaces,cars):
        self.name = name
        self.spaces = spaces
        self.cars = cars

    def car_in(self):
        if self.cars == self.spaces:
            print(f"  {self.name} is full. Can not add another car.")
        else:
            self.cars += 1
            print(f"  Added a car to {self.name}")

    def car_out(self):
        if self.cars == 0:
            print(f"  {self.name} is empty. There are no cars to remove.")
        else:
            self.cars -= 1
            print(f"  Removed a car from {self.name}")

    def status(self):
        print(f"  {self.name}: {(self.spaces - self.cars)} out of {self.spaces} spaces are available.")

def main():
    lot_a = Garage("Lot A", 10, 8)
    lot_b = Garage("Lot B", 15, 1)

    print("Welcome to the Garage Manager!")
    print("------------ Menu ------------")
    print("  0. Exit")
    print("  1. Print current status.")
    print("  2. Add a car to A lot.")
    print("  3. Add a car to B lot.")
    print("  4. Remove a car from A lot.")
    print("  5. Remove a car from B lot.")

    option = int(input("Please choose an option (0-5): "))
    while option != 0:
        if option == 1:
            print("Current Garage Status:")
            lot_a.status()
            lot_b.status()
        elif option == 2:
            lot_a.car_in()
        elif option == 3:
            lot_b.car_in()
        elif option == 4:
            lot_a.car_out()
        elif option == 5:
            lot_b.car_out()
        else:
            print("Please input a valid number")
        option = int(input("Please choose an option (0-5): "))
    
    print("End of the Day Garage Status:")
    lot_a.status()
    lot_b.status()




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
