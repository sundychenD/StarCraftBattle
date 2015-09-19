from StarCraftBattle.buildings.building import Building
from StarCraftBattle.buildings.names import ZBuildingName

class Hatchery(Building):
	
	__info = {
		"name" : ZBuildingName.hatchery,
		"hp" : 400,
		"mineral_cost" : 400,
		"time_cost" : 40
	}

	def __init__(self):
		Building.__init__(self, Hatchery.__info['name'], Hatchery.__info['mineral_cost'], 
								Hatchery.__info['hp'], Hatchery.__info['time_cost'])


class Extractor(Building):
	
	__info = {
		"name" : ZBuildingName.extractor,
		"hp" : 150,
		"mineral_cost" : 150,
		"time_cost" : 15
	}

	def __init__(self):
		Building.__init__(self, Extractor.__info['name'], Extractor.__info['mineral_cost'], 
								Extractor.__info['hp'], Extractor.__info['time_cost'])


class SunkenColony(Building):
	
	__info = {
		"name" : ZBuildingName.sunken_colony,
		"hp" : 200,
		"mineral_cost" : 200,
		"time_cost" : 20
	}

	def __init__(self):
		Building.__init__(self, SunkenColony.__info['name'], SunkenColony.__info['mineral_cost'], 
								SunkenColony.__info['hp'], SunkenColony.__info['time_cost'])


class SpawningPool(Building):
	
	__info = {
		"name" : ZBuildingName.spawning_pool,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, SpawningPool.__info['name'], SpawningPool.__info['mineral_cost'], 
								SpawningPool.__info['hp'], SpawningPool.__info['time_cost'])


class Spire(Building):
	
	__info = {
		"name" : ZBuildingName.spire,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Spire.__info['name'], Spire.__info['mineral_cost'], 
								Spire.__info['hp'], Spire.__info['time_cost'])


class DefilerMound(Building):
	
	__info = {
		"name" : ZBuildingName.defiler_mound,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, DefilerMound.__info['name'], DefilerMound.__info['mineral_cost'], 
								DefilerMound.__info['hp'], DefilerMound.__info['time_cost'])


class CreepColony(Building):
	
	__info = {
		"name" : ZBuildingName.creep_colony,
		"hp" : 100,
		"mineral_cost" : 100,
		"time_cost" : 10
	}

	def __init__(self):
		Building.__init__(self, CreepColony.__info['name'], CreepColony.__info['mineral_cost'], 
								CreepColony.__info['hp'], CreepColony.__info['time_cost'])

class EvolutionChamber(Building):
	
	__info = {
		"name" : ZBuildingName.evolution_chamber,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, EvolutionChamber.__info['name'], EvolutionChamber.__info['mineral_cost'], 
								EvolutionChamber.__info['hp'], EvolutionChamber.__info['time_cost'])