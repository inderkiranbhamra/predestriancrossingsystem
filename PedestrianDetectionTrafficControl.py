import cv2
import time

class PedestrianDetectionTrafficControl:
    def _init_(self):
        self.traffic_light = 'Green'
        self.pedestrian_detected = False
        self.capture = cv2.VideoCapture(0)  # 0 for webcam; or provide a video file path
        
        # Initialize HOG descriptor for pedestrian detection
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect_pedestrian(self, frame):
        # Detect people in the image
        (rects, weights) = self.hog.detectMultiScale(frame, winStride=(4, 4),
                                                     padding=(8, 8), scale=1.05)
        return len(rects) > 0, rects

    def control_traffic(self, pedestrian_present):
        if pedestrian_present:
            if self.traffic_light != 'Red':
                print("Pedestrian detected! Switching traffic light to RED...")
                self.traffic_light = 'Red'
                self.alert_vehicles()
        else:
            if self.traffic_light != 'Green':
                print("No pedestrian detected. Switching traffic light to GREEN...")
                self.traffic_light = 'Green'

    def alert_vehicles(self):
        print("ALERT: Vehicles must STOP! Pedestrian crossing.")

    def run_system(self):
        try:
            while True:
                ret, frame = self.capture.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                pedestrian_present, rects = self.detect_pedestrian(frame)
                self.control_traffic(pedestrian_present)

                # Draw rectangles around detected pedestrians
                for (x, y, w, h) in rects:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Display Traffic Light Status on Frame
                cv2.putText(frame, f"Traffic Light: {self.traffic_light}",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if self.traffic_light == 'Green' else (0, 0, 255), 2)

                # Show the frame
                cv2.imshow("Pedestrian Detection", frame)

                key = cv2.waitKey(30) & 0xFF
                if key == 27:  # ESC key to break
                    break

        except KeyboardInterrupt:
            print("System stopped manually.")
        finally:
            self.capture.release()
            cv2.destroyAllWindows()

if _name_ == "_main_":
    system = PedestrianDetectionTrafficControl()
    system.run_system()
