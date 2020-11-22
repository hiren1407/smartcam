import face_recognition
import cv2
import operations as op
import numpy as np



def run():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(1)

    # Load a sample picture and learn how to recognize it.
    #obama_image = face_recognition.load_image_file("obama.jpg")
    #obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

    # Load a second sample picture and learn how to recognize it.
    #hiren_image = face_recognition.load_image_file("hiren_known.jpg")
    #hiren_face_encoding = face_recognition.face_encodings(hiren_image)[0]
    #op.insert(obama_face_encoding)
    

    # Create arrays of known face encodings, their names and their rollno
    known_face_encodings = [
        #obama_face_encoding,
        #hiren_face_encoding
        #data[2]["face_encodings"]
    ]
    
    known_face_details=[

    ]
    data=op.read()
    
    #data containing face,name and rollno are added in respective arrays
    for i in data:
        
        known_face_encodings.append(np.asarray(i["face_encodings"]))
        known_face_details.append([i["name"],i["rollno"],i["attendance"]])
        
    #print(known_face_encodings)
    
    # Initialize some variables
    face_locations = []
    face_encodings = []
    rollno_check = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        #print(ret)

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            face_rollno = []
            face_attendance = []
            
            
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                
                name = "Unknown"
                rollno = 0
                attendance = 0
                # If a match was found in known_face_encodings, just use the first one.
                
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_details[first_match_index][0]
                    rollno = known_face_details[first_match_index][1]
                    attendance = known_face_details[first_match_index][2]
                    
                    if rollno not in rollno_check:
                        op.update(rollno)
                        rollno_check.append(rollno)
                        
                        
                   

    
                face_names.append(name)
                face_rollno.append(rollno)
                face_attendance.append(attendance)
               
                
                


        process_this_frame = not process_this_frame
        #print(process_this_frame)


        # Display the results
        cv2.putText(frame, "Press Q to exit" , (255,30),cv2.FONT_HERSHEY_SIMPLEX , 0.5, (255, 255, 255), 1)
        for (top, right, bottom, left), name, rollno, attendance in zip(face_locations, face_names, face_rollno, face_attendance):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            font = cv2.FONT_HERSHEY_SIMPLEX
            if name=="Unknown":
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)
            else:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom+2), (right, bottom+63), (0, 0, 0), cv2.FILLED)
            
            
            cv2.putText(frame,  "name : "+name, (left + 25, bottom + 15), font, 0.5, (255, 255, 255), 1)

            cv2.putText(frame,  "fid : "+str(rollno), (left + 25, bottom + 37), font, 0.5, (255, 255, 255), 1)
            cv2.putText(frame,  "days attended : "+str(int(attendance)), (left , bottom + 59), font, 0.5, (255, 255, 255), 1)

        # Display the resulting image
        
        
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    # Release handle to the webcam

    video_capture.release()
    cv2.destroyAllWindows()

#run()