from StarCraftBattle.buildings.names import TBuildingName
from StarCraftBattle.buildings.names import PBuildingName
from StarCraftBattle.buildings.names import ZBuildingName

class Building:

	__terran_building_list = {
		TBuildingName.command_center: 0,
		TBuildingName.bunker: 0,
		TBuildingName.missle_turret: 0,
		TBuildingName.barracks: 0,
		TBuildingName.starport: 0,
		TBuildingName.factory: 0,
		TBuildingName.supply_depot: 0,
		TBuildingName.armory: 0
	}

	__protoss_building_list = {
		PBuildingName.pylon: 0,
		PBuildingName.gateway: 0,
		PBuildingName.nexus: 0,
		PBuildingName.templar_archives: 0,
		PBuildingName.photon_cannon: 0,
		PBuildingName.twilight_council: 0,
		PBuildingName.assimilator: 0,
		PBuildingName.stargate: 0
	}

	__zerg_building_list = {
		ZBuildingName.creep_colony: 0,
		ZBuildingName.spawning_pool: 0,
		ZBuildingName.hatchery: 0,
		ZBuildingName.defiler_mound: 0,
		ZBuildingName.sunken_colony: 0,
		ZBuildingName.evolution_chamber: 0,
		ZBuildingName.extractor: 0,
		ZBuildingName.spire: 0
	}

	__t_count = 0
	__p_count = 0
	__z_count = 0

	def __init__(self, name, mineral_cost, hp, time_cost):
		self.__name = name
		self.__display_name = self.__name.name
		self.__mineral_cost = mineral_cost
		self.__hp = hp
		self.__time_cost = time_cost
		
		# Increment building instance number
		if name in TBuildingName:
			Building.__t_count += 1
			Building.add_to_t_building_list(self, name)

		elif name in PBuildingName:
			Building.__p_count += 1
			Building.add_to_p_building_list(self, name)

		elif name in ZBuildingName:
			Building.__z_count += 1
			Building.add_to_z_building_list(self, name)


	def get_name(self):
		return self.__name


	def get_mineral_cost(self):
		return self.__mineral_cost


	def get_hp(self):
		return self.__hp


	def get_build_time_cost(self):
		return Building.__time_cost


	def receive_attack(self, attack_point):
		self.__hp -= attack_point


	def repair(self, repair_point):
		self.__hp += repair_point


	def add_to_t_building_list(self, name):
		Building.__terran_building_list[name] += 1


	def add_to_p_building_list(self, name):
		Building.__protoss_building_list[name] += 1


	def add_to_z_building_list(self, name):
		Building.__zerg_building_list[name] += 1


	def print_total_count():
		print("Terran building counts: " + str(Building.__t_count))
		print("Protoss building counts: " + str(Building.__p_count))
		print("Zerg building counts: " + str(Building.__z_count))


	def print_status(self):
		self.print_name()
		print(Building.get_hp(self))


	def print_name(self):
		print(self.__display_name)


	def print_t_building_list(self):
		print(Building.__terran_building_list)


	def print_p_building_list(self):
		print(Building.__protoss_building_list)


	def print_z_building_list(self):
		print(Building.__zerg_building_list)


