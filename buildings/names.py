from enum import Enum

class TBuildingName(Enum):

	# Terran Building Names
	command_center = "Command Center"
	bunker = "Bunker"
	missle_turret = "Missle turret"
	barracks = "Barracks"
	starport = "Starport"
	factory = "Factory"
	supply_depot = "Supply Depot"
	armory = "Armory"


class PBuildingName(Enum):

	# Protoss Buidling Names
	pylon = "Pylon"
	gateway = "Gateway"
	nexus = "Nexus"
	templar_archives = "Templar Archives"
	photon_cannon = "Photon Cannon"
	twilight_council = "Twilight Council"
	assimilator = "Assimilator"
	stargate = "Stargate"


class ZBuildingName(Enum):

	# Zerg Buidling Names
	creep_colony = "Creep Colony"
	spawning_pool = "Spawning Pool"
	hatchery = "Hatchery"
	defiler_mound = "Defiler Mound"
	sunken_colony = "Sunken Colony"
	evolution_chamber = "Evolution Chamber"
	extractor = "Extractor"
	spire = "Spire"