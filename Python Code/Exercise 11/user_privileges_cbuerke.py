"""
Author: Cameron Buerke, cbuerke@purdue.edu
Assignment: 11.4 - Bank Accounts
Date: 11/18/2022

Description:
    Doesn't matter

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


"""Write new functions below this line (starting with unit 4)."""
class Privileges:
    def __init__(self, privs):
        if privs == None:
            self.privs = ['interact', 'post']
        else:
            self.privs = privs

    def grant(self, priv):
        self.privs += [priv]
        print(f"Granted {priv}")
        return

    def revoke(self, priv):
        for i in range(len(self.privs) - 1):
            if self.privs[i] == priv:
                del self.privs[i]

        print(f"Revoked {priv}")

    def get_privs(self):
        strang = ''
        for i in range(len(self.privs)):
            if i != len(self.privs) - 1:
                strang += self.privs[i] + ", "
            else:
                strang += self.privs[i]
        printable = f"{strang}"
        return printable


class User(Privileges):
    def __init__(self, name, email, privs):
        super().__init__(privs)
        self.name = name
        self.email = email

    def describe_user(self):
        print("User Profile")
        print(f"  Name: {self.name}")
        print(f"  Email: {self.email}")
        print(f"  Privs: " + self.get_privs())
        return


def main():
    alice = User("Alice", "alice@example.com",None)
    alice.describe_user()
    alice.grant('teleport')
    alice.describe_user()
    alice.revoke('post')
    alice.describe_user()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
