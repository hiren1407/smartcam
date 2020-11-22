import face_recognition
import cv2
import operations as op


def run(name,rollNo):
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    #sleep(2)
    while True:
    
        check, frame = webcam.read()
        key = cv2.waitKey(1)
    
   
        cv2.putText(frame,  "Press S to take picture", ( 220, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame,  "Press E to exit", ( 250, 45),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.rectangle(frame, (120, 70), (499, 410), (0, 255, 0), 1)
        cv2.imshow('Capturing' , frame)
        if key == ord('s'):

            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            
            message=insertS(name,rollNo)
            
            #print(message)
            if message=='Inserted data successfully':
                webcam.release()
                cv2.destroyAllWindows()
                return 'Record added succesfully'
            else:
                webcam.release()
                cv2.destroyAllWindows()
                return "Record already exist"
            break
        elif key == ord('e'):
            webcam.release()
            cv2.destroyAllWindows()
            break

def insertS(name,rollNo):
    new_image = face_recognition.load_image_file("saved_img.jpg")
    new_face_encoding = face_recognition.face_encodings(new_image)[0]
    message=op.insert(new_face_encoding,name, rollNo)
    return message