from StarCraftBattle.buildings.building import Building
from StarCraftBattle.buildings.names import BuildingName

class CommandCenter(Building):
	
	__info = {
		"name" : BuildingName.command_center,
		"hp" : 400,
		"mineral_cost" : 400,
		"time_cost" : 40
	}

	def __init__(self):
		Building.__init__(self, CommandCenter.__info['name'], CommandCenter.__info['mineral_cost'], 
								CommandCenter.__info['hp'], CommandCenter.__info['time_cost'])


class Bunker(Building):
	
	__info = {
		"name" : BuildingName.bunker,
		"hp" : 150,
		"mineral_cost" : 150,
		"time_cost" : 15
	}

	def __init__(self):
		Building.__init__(self, Bunker.__info['name'], Bunker.__info['mineral_cost'], 
								Bunker.__info['hp'], Bunker.__info['time_cost'])


class MissleTurret(Building):
	
	__info = {
		"name" : BuildingName.missle_turret,
		"hp" : 200,
		"mineral_cost" : 200,
		"time_cost" : 20
	}

	def __init__(self):
		Building.__init__(self, MissleTurret.__info['name'], MissleTurret.__info['mineral_cost'], 
								MissleTurret.__info['hp'], MissleTurret.__info['time_cost'])


class Barracks(Building):
	
	__info = {
		"name" : BuildingName.barracks,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Barracks.__info['name'], Barracks.__info['mineral_cost'], 
								Barracks.__info['hp'], Barracks.__info['time_cost'])


class Starport(Building):
	
	__info = {
		"name" : BuildingName.starport,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Starport.__info['name'], Starport.__info['mineral_cost'], 
								Starport.__info['hp'], Starport.__info['time_cost'])


class Factory(Building):
	
	__info = {
		"name" : BuildingName.factory,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Factory.__info['name'], Factory.__info['mineral_cost'], 
								Factory.__info['hp'], Factory.__info['time_cost'])


class SupplyDepot(Building):
	
	__info = {
		"name" : BuildingName.supply_depot,
		"hp" : 100,
		"mineral_cost" : 100,
		"time_cost" : 10
	}

	def __init__(self):
		Building.__init__(self, SupplyDepot.__info['name'], SupplyDepot.__info['mineral_cost'], 
								SupplyDepot.__info['hp'], SupplyDepot.__info['time_cost'])

class Armory(Building):
	
	__info = {
		"name" : BuildingName.armory,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Armory.__info['name'], Armory.__info['mineral_cost'], 
								Armory.__info['hp'], Armory.__info['time_cost'])