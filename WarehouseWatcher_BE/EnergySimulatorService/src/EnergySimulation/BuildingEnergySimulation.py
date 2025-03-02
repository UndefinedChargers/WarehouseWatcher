# FILE :BuildingEnergySimulation.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically the code for BuildingEnergySimulation

from EnergySimulation.Base_simulation import BaseSimulation
from EnergySimulation.BuildingConfigration import BuildingConfiguration

class BuildingEnergySimulation(BaseSimulation):
  

    def __init__(self, config: BuildingConfiguration):
        super().__init__()  
        self.config = config
        self.building_id = config.building_id
        self._it_consumption = 0.0
        self._lighting_consumption = 0.0
        self._ventilation_consumption = 0.0
        self._hvac_consumption = 0.0 #(heating and ventilation system)
        self._transport_consumption = 0.0

        # TrackS the current hour (0–23).
        self._current_hour = 0

    #  function name: update_simulation
    #  Description: 
    #     1) Determines occupant count using _calc_occupant_count() for the current hour
    #     2) Calculates energy consumption for IT, lighting, ventilation, HVAC, and transport
    #     3) Returns the data as a dictionary
    #     4) Advances the hour, wrapping at 24
    # Parameters:
    #   - self: the instance of the class
    # return: dict containing occupant_count, building_id, and consumption values
    # 
    def update_simulation(self):
        occupant_count = self._calc_occupant_count(self._current_hour)
        self.set_occupant_count(occupant_count)

        #calculates the consumption of energy on each sector
        self._it_consumption = self._calc_it_consumption()
        self._lighting_consumption = self._calc_lighting_consumption()
        self._ventilation_consumption = self._calc_ventilation_consumption()
        self._hvac_consumption = self._calc_hvac_consumption()
        self._transport_consumption = self._calc_transport_consumption()

        # Advance hour of day (wrap at 24)
        self._current_hour = (self._current_hour + 1) % 24

        return {
            "building_id": self.building_id,
            "occupant_count": self.get_occupant_count(),
            "IT_energy": round(self._it_consumption, 2),
            "Lighting_energy": round(self._lighting_consumption, 2),
            "Ventilation_energy": round(self._ventilation_consumption, 2),
            "HVAC_energy": round(self._hvac_consumption, 2),
            "Transport_energy": round(self._transport_consumption, 2),
        }
    
    #  
    #  function name: _calc_occupant_count
    #  Description: Determines the occupant count for a given hour of day
    #               using a simple schedule:
    #                 - 0–7 : 0 occupants
    #                 - 7–9 : ramp 0..occupant_capacity
    #                 - 9–17: occupant_capacity
    #                 - 17–20: ramp occupant_capacity..0
    #                 - 20–24: 10 occupants
    #  Parameters:
    #    - self: the instance of the class
    #    - hour: int representing the current hour [0..23]
    #  return: int occupant count
    #  
    def _calc_occupant_count(self, hour):
        cap = self.config.occupant_capacity
        if 0 <= hour < 7:
            return 0
        elif 7 <= hour < 9:
            fraction = (hour - 7) / 2.0
            return int(cap * fraction)
        elif 9 <= hour < 17:
            return cap
        elif 17 <= hour < 20:
            fraction = 1.0 - ((hour - 17) / 3.0)
            return int(cap * fraction)
        else:
            return 10

     
       
    def _calc_it_consumption(self):
      
        base_load = 10.0 # 10 set as a base value
        occupant_factor = self.get_occupant_count() * 0.1
        return base_load + occupant_factor
    #  
    # function name: _calc_lighting_consumption
    # Description: If occupant_count is 0, minimal safety lighting (1.0 kW).
    #              Otherwise occupant_count * 0.05 + 10.0 kW for general lighting.
    # Parameters:
    #   - self: the instance of the class
    # return: float representing the lighting consumption in kW
    # 
    def _calc_lighting_consumption(self):
        if self.get_occupant_count() == 0:
            return 1.0  # minimal safety lighting
        else:
            return self.get_occupant_count() * 0.05 + 10.0#(base value)
     
    # function name: _calc_ventilation_consumption
    # Description: Sets a base ventilation load of 8.0 kW plus 
    #              an occupant factor of 0.02 kW per occupant.
    # Parameters:
    #   - self: the instance of the class
    # return: float representing the ventilation consumption in kW
    #
    def _calc_ventilation_consumption(self):
        return 8.0 + (self.get_occupant_count() * 0.02)

    # function comment
    # 
    # function name: _calc_hvac_consumption
    # Description: Uses base_hvac (9 kW) plus occupant load (0.02 kW each),
    #              multiplied by hvac_power_multiplier from the config.
    # Parameters:
    #   - self: the instance of the class
    # return: float representing the HVAC consumption in kW
    def _calc_hvac_consumption(self):
        base_hvac = 9 
        occupant_load = self.get_occupant_count() * 0.02
        return (base_hvac + occupant_load) * self.config.hvac_power_multiplier


    #  function name: _calc_transport_consumption
    #  Description: Base transport consumption of 9.0 kW, plus occupant factor
    #               of 0.01 kW each for internal transport/elevators.
    #  Parameters:
    #    - self: the instance of the class
    #  return: float representing the transport consumption in kW
    def _calc_transport_consumption(self):
        return 9.0 + (self.get_occupant_count() * 0.01)
