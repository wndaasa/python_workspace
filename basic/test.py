import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    direction = "No hand detected"
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
        # Calculate the average x coordinate of the hand landmarks
        x_coords = [landmark.x for landmark in hand_landmarks.landmark]
        avg_x = np.mean(x_coords)
        
        # Determine direction based on average x coordinate
        if avg_x < 0.4:
          direction = "Right"
        elif avg_x > 0.6:
          direction = "Left"
        else:
          direction = "Center"
    
    # Flip the image horizontally for a selfie-view display.
    flipped_image = cv2.flip(image, 1)
    
    # Display the direction on the flipped image
    cv2.putText(flipped_image, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('MediaPipe Hands', flipped_image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
