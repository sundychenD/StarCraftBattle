from StarCraftBattle.buildings.building import Building
from StarCraftBattle.buildings.names import PBuildingName

class Nexus(Building):
	
	__info = {
		"name" : PBuildingName.nexus,
		"hp" : 400,
		"mineral_cost" : 400,
		"time_cost" : 40
	}

	def __init__(self):
		Building.__init__(self, Nexus.__info['name'], Nexus.__info['mineral_cost'], 
								Nexus.__info['hp'], Nexus.__info['time_cost'])


class Assimilator(Building):
	
	__info = {
		"name" : PBuildingName.assimilator,
		"hp" : 150,
		"mineral_cost" : 150,
		"time_cost" : 15
	}

	def __init__(self):
		Building.__init__(self, Assimilator.__info['name'], Assimilator.__info['mineral_cost'], 
								Assimilator.__info['hp'], Assimilator.__info['time_cost'])


class PhotonCannon(Building):
	
	__info = {
		"name" : PBuildingName.photon_cannon,
		"hp" : 200,
		"mineral_cost" : 200,
		"time_cost" : 20
	}

	def __init__(self):
		Building.__init__(self, PhotonCannon.__info['name'], PhotonCannon.__info['mineral_cost'], 
								PhotonCannon.__info['hp'], PhotonCannon.__info['time_cost'])


class Gateway(Building):
	
	__info = {
		"name" : PBuildingName.gateway,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Gateway.__info['name'], Gateway.__info['mineral_cost'], 
								Gateway.__info['hp'], Gateway.__info['time_cost'])


class Stargate(Building):
	
	__info = {
		"name" : PBuildingName.stargate,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, Stargate.__info['name'], Stargate.__info['mineral_cost'], 
								Stargate.__info['hp'], Stargate.__info['time_cost'])


class TemplarArchives(Building):
	
	__info = {
		"name" : PBuildingName.templar_archives,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, TemplarArchives.__info['name'], TemplarArchives.__info['mineral_cost'], 
								TemplarArchives.__info['hp'], TemplarArchives.__info['time_cost'])


class Pylon(Building):
	
	__info = {
		"name" : PBuildingName.pylon,
		"hp" : 100,
		"mineral_cost" : 100,
		"time_cost" : 10
	}

	def __init__(self):
		Building.__init__(self, Pylon.__info['name'], Pylon.__info['mineral_cost'], 
								Pylon.__info['hp'], Pylon.__info['time_cost'])

class TwilightCouncil(Building):
	
	__info = {
		"name" : PBuildingName.twilight_council,
		"hp" : 250,
		"mineral_cost" : 250,
		"time_cost" : 25
	}

	def __init__(self):
		Building.__init__(self, TwilightCouncil.__info['name'], TwilightCouncil.__info['mineral_cost'], 
								TwilightCouncil.__info['hp'], TwilightCouncil.__info['time_cost'])