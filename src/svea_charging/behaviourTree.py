import time
from btree import NodeStatus, Node, ActionNode, Sequence, Fallback #imported behaviour tree implementation from Elisa Bin's repo: https://github.com/elisabin/btree


class btree:
    def __init__(self):
        #build the behaviour tree here using the imported implementation
        #the tree should be built according to the our logic, and should use the functions defined below as leaf nodes
        pass

    #condition
    def communicationOk(self):
        #check if communication with the car is ok
        pass

    #action
    def alertCommunicationError(self):
        #alert the user that communication with the car is not ok
        pass

    #condition
    def batteryLevelOk(self):
        #check if the battery level is above a charging threshold
        pass

    #action
    def GoToChargingStation(self):
        #navigate to the charging station using High Level Planner & Controller
        pass

    #condition
    def vehicleCloseEnoughToCharger(self):
        #check if the vehicle is within some decided proximity of the charger
        pass

    #action
    def FineAlign(self):
        #navigate to be within a finer proximity using a Low Level Controller
        pass

    #condition
    def vehicleDocked(self):
        #check if the vehicle is docked and have contact with the charger
        pass

    #action
    def dockVehicle(self):
        #some action that would dock the vehicle
        pass

    #condition
    def chargingProcessOk(self):
        #check if the charging process is going ok
        pass

    #action
    def alertChargingError(self):
        #alert the user that the charging process is not going ok
        pass

    #condition
    def doneCharging(self):
        #check if the battery is sufficiently charged
        pass

    def undockVehicle(self):
        #some action that would undock the vehicle
        pass