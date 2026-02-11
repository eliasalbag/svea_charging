import time
from btree import NodeStatus, Node, ActionNode, Sequence, Fallback #imported behaviour tree implementation from Elisa Bin's repo: https://github.com/elisabin/btree



class Btree:
    def __init__(self, defaultBatteryLevel=20.0, communicationStatus = True):
        self.batteryLevel = float(defaultBatteryLevel) #percentage, we could change this
        self.communicationStatus = communicationStatus
        self.chargerVisible = False
        self.vehicleAligned = False
        self.chargingActive = False
        self.chargingError = False
        self.tickingFreqency = 10.0 #Hz
        self.period = 1.0 / self.tickingFrequency
        self.batteryLevelUpperThreshold = 80.0 #percentage
        self.batteryLevelLowerThreshold = 20.0 #percentage
        self.max_ticks = 100 #is this necessary?? ASK KAJ. max number of ticks before we stop the process, can be changed depending on how long we want to run the process for

        # the tree should be built according to our logic, and should use the functions defined below as leaf nodes
        self.tree = Sequence(
            Fallback(
                ActionNode(self.communicationOk),
                ActionNode(self.alertCommunicationError),
                name="communicationGuard",
            ),
            Sequence(
                Fallback(
                    ActionNode(self.batteryLevelNotOk),
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
            name="root",
        )


    def tick(self):
        self.tree.tick()
        time.sleep(self.period) #should this sleep here? idk if this is the approach. ASK KAJ and Elisa


    #condition
    def communicationOk(self):
        #check if communication with the car is ok
        if self.communicationStatus:
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE
        
    #action
    def alertCommunicationError(self):
        #alert the user that communication with the car is not ok, check with Kaj what is the best way to do handle this
        print("ALERT: Communication issues.")
        return NodeStatus.FAILURE #How should we handle this? Should we return FAILURE here, or SUCCESS since we have alerted the user? ASK KAJ and Elisa

    #condition
    def batteryLevelNotOk(self):
        #check if the battery level is above a charging threshold
        if self.batteryLevel < self.batteryLevelLowerThreshold:
            return NodeStatus.SUCCESS
        else:
            return NodeStatus.FAILURE

    #action
    def GoToChargingStation(self):
        #navigate to the charging station using High Level Planner & Controller
        try:
            if self.chargerVisible:
                print("Charger is now visible.")
                return NodeStatus.SUCCESS
            else:
                print("Navigating to the charging station...")
                #should add navigation code here, and set self.chargerVisible to True when we are close enough to the charger
                return NodeStatus.RUNNING
        except Exception as e:
            print(f"Error while navigating to the charging station: {e}")
            return NodeStatus.FAILURE


    #condition
    def vehicleCloseEnoughToCharger(self):
        #check if the vehicle is within some decided proximity of the charger
        if self.vehicleAligned:
            return NodeStatus.SUCCESS
        else:
            print("Vehicle is not close enough to the charger.")
            return NodeStatus.FAILURE

    #action
    def FineAlign(self):
        #navigate to be within a finer proximity using a Low Level Controller
        try:
            if self.vehicleAligned:
                print("Vehicle is now aligned with the charger.")
                return NodeStatus.SUCCESS
            print("Fine aligning with the charger...")
            #should add fine alignment code here, and set self.vehicleAligned to True when we are close enough to the charger
            return NodeStatus.RUNNING
        except Exception as e:
            print(f"Error while fine aligning with the charger: {e}")
            return NodeStatus.FAILURE
        

    #condition
    def vehicleDocked(self):
        #check if the vehicle is docked and have contact with the charger
        if self.vehicleDockedStatus:
            return NodeStatus.SUCCESS
        else:
            print("Vehicle is not docked with the charger yet.")
            return NodeStatus.FAILURE

    #action
    def dockVehicle(self):
        #some action that would dock the vehicle
        try:
            if self.vehicleDockedStatus:
                print("Vehicle is now docked with the charger.")
                return NodeStatus.SUCCESS
            print("Docking with the charger...")
            #should add docking code here, and set self.vehicleDockedStatus to True when we are docked with the charger
            return NodeStatus.RUNNING
        except Exception as e:
            print(f"Error while docking with the charger: {e}")
            return NodeStatus.FAILURE

    #condition
    def chargingProcessOk(self):
        #check if the charging process is going ok
        if self.chargingError: # check with Kaj and Nils. add another method which enables chargingError when anomalies are detected.
            return NodeStatus.FAILURE
        else:
            return NodeStatus.SUCCESS

    #action
    def alertChargingError(self):
        #alert the user that the charging process is not going ok
        print("ALERT: Charging process issues detected.")
        return NodeStatus.FAILURE #How should we handle this? Should we return FAILURE here, or SUCCESS since we have alerted the user? ASK KAJ
    
    #condition
    def doneCharging(self):
        #check if the battery is sufficiently charged
        if self.batteryLevel >= self.batteryLevelUpperThreshold:
            return NodeStatus.SUCCESS
        else:
            print("Battery is not sufficiently charged yet.")
            return NodeStatus.FAILURE

    def undockVehicle(self):
        #some action that would undock the vehicle
        try:
            if not self.vehicleDockedStatus:
                print("Vehicle is now undocked from the charger.")
                return NodeStatus.SUCCESS
            print("Undocking from the charger...")
            #should add undocking code here, and set self.vehicleDockedStatus to False when we are undocked from the charger
            return NodeStatus.RUNNING
        except Exception as e:
            print(f"Error while undocking from the charger: {e}")
            return NodeStatus.FAILURE
        

    def run(self):
        for tick in range(self.max_ticks):
            print(f"--- TICK {tick} ---")
            status = self.tree.run()               # one full evaluation
            print(f"* Tree returned: {status}\n")
            time.sleep(self.period)
            if status == NodeStatus.SUCCESS:
                print("Charging process completed successfully.")
                break
            elif status == NodeStatus.FAILURE:
                print("Charging process failed.")
                break
