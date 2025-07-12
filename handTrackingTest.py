import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
x=0
y=0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    height,width,_  =frame.shape
    frame = cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame,handLms,mp_hands.HAND_CONNECTIONS)
            lm = handLms.landmark[8]
            x=int(lm.x*width)
            y=int(lm.y*height)
            cv2.rectangle(frame, (x,y), (x+5,y+5), (0,255,0), -1)
        
    cv2.imshow("Hand Tracking", frame)
    if cv2.waitKey(1) & 0xFF ==  27:
        break
cap.release()
cv2.destroyAllWindows()



