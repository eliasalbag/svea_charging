import time
from btree import NodeStatus, Node, ActionNode, Sequence, Fallback #imported behaviour tree implementation from Elisa Bin's repo: https://github.com/elisabin/btree


class btree:
    def __init__(self):
        # the tree should be built according to our logic, and should use the functions defined below as leaf nodes
        self.tree = Sequence(
            Fallback(
                ActionNode(self.communicationOk),
                ActionNode(self.alertCommunicationError),
                name="communicationGuard",
            ),
            Sequence(
                Fallback(
                    ActionNode(self.batteryLevelOk),
                    ActionNode(self.GoToChargingStation),
                    name="batteryLevelCheck",
                ),
                Fallback(
                    ActionNode(self.vehicleCloseEnoughToCharger),
                    ActionNode(self.FineAlign),
                    name="approachCharger",
                ),
                Fallback(
                    ActionNode(self.vehicleDocked),
                    ActionNode(self.dockVehicle),
                    name="docking",
                ),
                Fallback(
                    ActionNode(self.chargingProcessOk),
                    ActionNode(self.alertChargingError),
                    name="chargingProcessCheck",
                ),
                Sequence(
                    ActionNode(self.doneCharging),
                    ActionNode(self.undockVehicle),
                    name="undocking",
                ),
            ),
        )


    #condition
    def communicationOk(self):
        #check if communication with the car is ok
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE
        

    #action
    def alertCommunicationError(self):
        #alert the user that communication with the car is not ok, check with Kaj what is the best way to do handle this
        pass

    #condition
    def batteryLevelOk(self):
        #check if the battery level is above a charging threshold
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    #action
    def GoToChargingStation(self):
        #navigate to the charging station using High Level Planner & Controller
        pass

    #condition
    def vehicleCloseEnoughToCharger(self):
        #check if the vehicle is within some decided proximity of the charger
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    #action
    def FineAlign(self):
        #navigate to be within a finer proximity using a Low Level Controller
        pass

    #condition
    def vehicleDocked(self):
        #check if the vehicle is docked and have contact with the charger
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    #action
    def dockVehicle(self):
        #some action that would dock the vehicle
        pass

    #condition
    def chargingProcessOk(self):
        #check if the charging process is going ok
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    #action
    def alertChargingError(self):
        #alert the user that the charging process is not going ok
        pass

    #condition
    def doneCharging(self):
        #check if the battery is sufficiently charged
        if True: #PLACEHOLDER: replace with actual check
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    def undockVehicle(self):
        #some action that would undock the vehicle
        pass