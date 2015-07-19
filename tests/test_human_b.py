import sys
sys.path.append("/Users/sundychen/Documents/Programming/Python/StarCraftBattleProj")

from StarCraftBattle.buildings.human_b import *

def test_initialize_buildings():
	# Test Command Center
	comcen = CommandCenter()
	comcen.print_status()
	assert comcen.get_hp() == 400

	comcen.receive_attack(10)
	assert comcen.get_hp() == 390

	comcen2 = CommandCenter()
	comcen2.print_status()
	assert comcen2.get_hp() == 400

	comcen2.receive_attack(10)
	assert comcen2.get_hp() == 390

	CommandCenter.print_total_count()

	# Test Bunker
	bunk = Bunker()
	bunk.print_status()
	assert bunk.get_hp() == 150

	bunk.receive_attack(10)
	assert bunk.get_hp() == 140

	bunk2 = Bunker()
	bunk2.print_status()
	assert bunk2.get_hp() == 150

	bunk2.receive_attack(10)
	assert bunk2.get_hp() == 140

	Bunker.print_total_count()

	# Test Missle turret
	mistu = MissleTurret()
	mistu.print_status()
	assert mistu.get_hp() == 200

	mistu.receive_attack(10)
	assert mistu.get_hp() == 190

	mistu2 = MissleTurret()
	mistu2.print_status()
	assert mistu2.get_hp() == 200

	mistu2.receive_attack(10)
	assert mistu2.get_hp() == 190

	MissleTurret.print_total_count()

	# Test Barracks
	barra = Barracks()
	barra.print_status()
	assert barra.get_hp() == 250

	barra.receive_attack(10)
	assert barra.get_hp() == 240

	barra2 = Barracks()
	barra2.print_status()
	assert barra2.get_hp() == 250

	barra2.receive_attack(10)
	assert barra2.get_hp() == 240

	Barracks.print_total_count()

	# Test Starport
	starp = Starport()
	starp.print_status()
	assert starp.get_hp() == 250

	starp.receive_attack(10)
	assert starp.get_hp() == 240

	starp2 = Starport()
	starp2.print_status()
	assert starp2.get_hp() == 250

	starp2.receive_attack(10)
	assert starp2.get_hp() == 240

	Starport.print_total_count()

	# Test Factory
	fact = Factory()
	fact.print_status()
	assert fact.get_hp() == 250

	fact.receive_attack(10)
	assert fact.get_hp() == 240

	fact2 = Factory()
	fact2.print_status()
	assert fact2.get_hp() == 250

	fact2.receive_attack(10)
	assert fact2.get_hp() == 240

	Factory.print_total_count()

	# Test Supply Depot
	supd = SupplyDepot()
	supd.print_status()
	assert supd.get_hp() == 100

	supd.receive_attack(10)
	assert supd.get_hp() == 90

	supd2 = SupplyDepot()
	supd2.print_status()
	assert supd2.get_hp() == 100

	supd2.receive_attack(10)
	assert supd2.get_hp() == 90

	SupplyDepot.print_total_count()

	# Test Factory
	arm = Armory()
	arm.print_status()
	assert arm.get_hp() == 250

	arm.receive_attack(10)
	assert arm.get_hp() == 240

	arm2 = Armory()
	arm2.print_status()
	assert arm2.get_hp() == 250

	arm2.receive_attack(10)
	assert arm2.get_hp() == 240

	Armory.print_total_count()


def start_tests():
	print("Test Start")
	test_initialize_buildings()


if __name__ == "__main__":
	start_tests()
	