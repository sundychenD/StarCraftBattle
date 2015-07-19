import sys
sys.path.append("buildings")

from buildings.human_b import *

def initialize_buildings():
	comcen = CommandCenter()
	comcen.print_status()

	comcen.receive_attack(10)
	comcen.print_status()

	comcen2 = CommandCenter()
	comcen2.print_status()

	comcen2.receive_attack(10)
	comcen2.print_status()

	CommandCenter.print_total_count()


def start_battle():
	print("Battle Start!")


if __name__ == "__main__":
	start_battle()
	initialize_buildings()