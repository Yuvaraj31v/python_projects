import random

class Leader:

    def get_leader(self):
        members = ("Bharani","kannapan","Vijay")
        leader = random.choice(members)
        assis_leader=random.choice(members)
        print(f"({leader},{assis_leader})")