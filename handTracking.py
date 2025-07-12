import cv2
import mediapipe as mp
import threading

class HandTracker:
    def __init__(self):
        self.x = 0
        self.frame = None
        self.running = True
        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7, 
            min_tracking_confidence=0.7
        )
        self.hand_thread = threading.Thread(target=self.update,daemon=True)
        self.hand_thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue
            frame = cv2.flip(frame,1)
            rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb)
            if results.multi_hand_landmarks:
                for handLms in  results.multi_hand_landmarks:
                    lm = handLms.landmark[8]
                    self.x = lm.x
            self.frame=frame
         
    def getXcoordinate(self):
        return self.x 
    def getFrame(self):
        return self.frame
    def exit(self):
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    ht = HandTracker()
    while True:
        if frame is not None:
            frame = ht.getFrame()
            print(ht.getXcoordinate())
            cv2.imshow("cam",frame)
        if cv2.waitKey(1) & 0xFF ==  27:
            break   
    ht.exit()
