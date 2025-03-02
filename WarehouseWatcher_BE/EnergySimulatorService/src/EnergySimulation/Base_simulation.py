# FILE :BaseSimulation.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically  base simulation for the energy Consumption
from loguru import logger
class BaseSimulation:
   

    def __init__(self):
        # By Python convention, a single underscore indicates
        # an internal-use (protected-like) attribute.
        self._occupant_count = 0
    # function name: set_occupant_count
    # Description: Setter method to update the occupant count, ensuring the value is not negative.
    #  Parameters:
    #     self: the instance of the class
    #     count: int, new occupant count
    #  return: None
    def set_occupant_count(self, count):
        """
        Encapsulates occupant count in a 'setter' method.
        """
        self._occupant_count = max(0, count)  # enforce non-negative

    

    # function name: get_occupant_count
    # Description: Getter method to return the current occupant count.
    # Parameters:
    # self: the instance of the class
    # return: int, the occupant count
        
    def get_occupant_count(self):
        """
        Encapsulates occupant count in a 'getter' method.
        """
        return self._occupant_count
    
    # function name: update_simulation
    # Description: Base method intended to be overridden by child classes 
    #              to provide custom simulation logic.
    # Parameters:
    #   - self: the instance of the class
    # return: None (or a relevant dictionary/structure in child classes)
    # Raises:
    #   NotImplementedError: if not overridden by a child class
    
    def update_simulation(self):
    #    raise NotImplementedError("Must be implemented in a child class.")
          logger.warning("Exiting multi-building Energysimulation",file="./Logs/EnergySimulator_Publisher_Logs.log")
