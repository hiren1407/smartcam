from connection import db
import createExcel as ce


def insert(data,name,fid):
        #print(data)
        try:
            db.sdetails.insert_one(
                {
                    "face_encodings":list(data),
                    "name":name,
                    "rollno":int(fid),
                    "attendance":0
                    
            })
            #ce.addName(int(fid),name)
            return 'Inserted data successfully'
        except :
            return 'Duplicate Data'

    
def read():
    data=db.sdetails.find()
    return data
    #for i in data:
        #print(i)
def update(fid):
    rno=db.sdetails.find_one({'rollno':fid})

    attendance=rno['attendance']+1
    #print(attendance)
    db.sdetails.update_one({

            'rollno':fid
            },
            {"$set":{'attendance':attendance}
        })
    #ce.updateAttendance(fid,'P')