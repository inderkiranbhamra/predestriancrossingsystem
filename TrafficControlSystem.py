import time
import random

class TrafficControlSystem:
    def _init_(self):
        self.traffic_light = 'Green'  # Traffic starts with green light
        self.pedestrian_detected = False

    def detect_pedestrian(self):
        # Simulate pedestrian detection (randomly for now)
        self.pedestrian_detected = random.choice([True, False])
        print(f"Pedestrian detected: {self.pedestrian_detected}")

    def control_traffic(self):
        if self.pedestrian_detected:
            print("Pedestrian detected! Switching traffic light to RED...")
            self.traffic_light = 'Red'
            self.alert_vehicles()
            time.sleep(5)  # Keep red for 5 seconds
            print("Pedestrian crossed. Switching traffic light to GREEN...")
            self.traffic_light = 'Green'
        else:
            print("No pedestrian. Traffic light remains GREEN.")
            self.traffic_light = 'Green'

    def alert_vehicles(self):
        print("ALERT: Vehicles must STOP. Pedestrian crossing in progress.")

    def run_system(self):
        try:
            while True:
                self.detect_pedestrian()
                self.control_traffic()
                print(f"Current Traffic Light: {self.traffic_light}")
                print("-" * 40)
                time.sleep(3)  # Check every 3 seconds
        except KeyboardInterrupt:
            print("System stopped manually.")

if _name_ == "_main_":
    system = TrafficControlSystem()
    system.run_system()
