from StarCraftBattle.buildings.names import BuildingName

class Building:

	__terran_building_list = {
		BuildingName.command_center: 0,
		BuildingName.bunker: 0,
		BuildingName.missle_turret: 0,
		BuildingName.barracks: 0,
		BuildingName.starport: 0,
		BuildingName.factory: 0,
		BuildingName.supply_depot: 0,
		BuildingName.armory: 0
	}

	__count = 0

	def __init__(self, name, mineral_cost, hp, time_cost):
		self.__name = name
		self.__display_name = self.__name.name
		self.__mineral_cost = mineral_cost
		self.__hp = hp
		self.__time_cost = time_cost
		
		# Increment building instance number
		Building.__count += 1

		# Increment 1 for in terran building list
		Building.add_to_building_list(self, name)

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


	def add_to_building_list(self, name):
		Building.__terran_building_list[name] += 1


	def print_total_count():
		print(Building.__count)

	
	def print_status(self):
		self.print_name()
		print(Building.get_hp(self))


	def print_name(self):
		print(self.__display_name)


	def print_building_list(self):
		print(Building.__terran_building_list)


