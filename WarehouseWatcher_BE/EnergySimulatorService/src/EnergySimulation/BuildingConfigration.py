# FILE :BuildingConfigration.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically conisist of BuildingConfigration 
class BuildingConfiguration:
    def __init__(self, building_id, occupant_capacity=100, hvac_power_multiplier=1.0):
        self.building_id = building_id
        self.occupant_capacity = occupant_capacity
        self.hvac_power_multiplier = hvac_power_multiplier
