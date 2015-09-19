import sys
sys.path.append("/Users/sundychen/Documents/Programming/Python/StarCraftBattleProj")

from StarCraftBattle.buildings.zerg_b import *

def test_initialize_buildings():
	# Test Hatchery
	comcen = Hatchery()
	comcen.print_status()
	assert comcen.get_hp() == 400

	comcen.receive_attack(10)
	assert comcen.get_hp() == 390

	comcen2 = Hatchery()
	comcen2.print_status()
	assert comcen2.get_hp() == 400

	comcen2.receive_attack(10)
	assert comcen2.get_hp() == 390

	Hatchery.print_total_count()

	# Test Extractor
	bunk = Extractor()
	bunk.print_status()
	assert bunk.get_hp() == 150

	bunk.receive_attack(10)
	assert bunk.get_hp() == 140

	bunk2 = Extractor()
	bunk2.print_status()
	assert bunk2.get_hp() == 150

	bunk2.receive_attack(10)
	assert bunk2.get_hp() == 140

	Extractor.print_total_count()

	# Test Photon Cannon
	mistu = SunkenColony()
	mistu.print_status()
	assert mistu.get_hp() == 200

	mistu.receive_attack(10)
	assert mistu.get_hp() == 190

	mistu2 = SunkenColony()
	mistu2.print_status()
	assert mistu2.get_hp() == 200

	mistu2.receive_attack(10)
	assert mistu2.get_hp() == 190

	SunkenColony.print_total_count()

	# Test SpawningPool
	barra = SpawningPool()
	barra.print_status()
	assert barra.get_hp() == 250

	barra.receive_attack(10)
	assert barra.get_hp() == 240

	barra2 = SpawningPool()
	barra2.print_status()
	assert barra2.get_hp() == 250

	barra2.receive_attack(10)
	assert barra2.get_hp() == 240

	SpawningPool.print_total_count()

	# Test Spire
	starp = Spire()
	starp.print_status()
	assert starp.get_hp() == 250

	starp.receive_attack(10)
	assert starp.get_hp() == 240

	starp2 = Spire()
	starp2.print_status()
	assert starp2.get_hp() == 250

	starp2.receive_attack(10)
	assert starp2.get_hp() == 240

	Spire.print_total_count()

	# Test DefilerMound
	fact = DefilerMound()
	fact.print_status()
	assert fact.get_hp() == 250

	fact.receive_attack(10)
	assert fact.get_hp() == 240

	fact2 = DefilerMound()
	fact2.print_status()
	assert fact2.get_hp() == 250

	fact2.receive_attack(10)
	assert fact2.get_hp() == 240

	DefilerMound.print_total_count()

	# Test CreepColony
	supd = CreepColony()
	supd.print_status()
	assert supd.get_hp() == 100

	supd.receive_attack(10)
	assert supd.get_hp() == 90

	supd2 = CreepColony()
	supd2.print_status()
	assert supd2.get_hp() == 100

	supd2.receive_attack(10)
	assert supd2.get_hp() == 90

	CreepColony.print_total_count()

	# Test EvolutionChamber
	arm = EvolutionChamber()
	arm.print_status()
	assert arm.get_hp() == 250

	arm.receive_attack(10)
	assert arm.get_hp() == 240

	arm2 = EvolutionChamber()
	arm2.print_status()
	assert arm2.get_hp() == 250

	arm2.receive_attack(10)
	assert arm2.get_hp() == 240

	EvolutionChamber.print_total_count()


def start_tests():
	print("====== Start Testing Zerg Buidling ======")
	test_initialize_buildings()


if __name__ == "__main__":
	start_tests()