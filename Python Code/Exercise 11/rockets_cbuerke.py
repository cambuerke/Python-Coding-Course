"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 11.3 - Rockets
Date: 11/18/2022

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
class Rocket:
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost


    def cost_per_launch(self):
        cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:0.2f} million per launch.")
        return

class ReusableRocket(Rocket):
    def cost_per_launch(self, uses):
        cost = self.booster_cost / uses + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${cost:0.2f} million per launch.")
        return


def main():
    atlas_v = Rocket("Atlas V", 65.4, 42.6, 0.23)
    atlas_5 = Rocket("Atlas 5", 83.5, 55.6, 0.69)
    long_march_3b = Rocket("Long March 3B", 28.5, 19.0, 2.38)
    soyuz_2 = Rocket("Soyuz 2", 20.9, 13.9, 0.24)
    falcon_9 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45)

    atlas_v.cost_per_launch()
    atlas_5.cost_per_launch()
    long_march_3b.cost_per_launch()
    soyuz_2.cost_per_launch()
    falcon_9.cost_per_launch(10)




"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
