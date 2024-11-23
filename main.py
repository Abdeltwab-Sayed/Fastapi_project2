from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow requests from any origin   
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

class Student(BaseModel):
    id: int
    name: str
    grade: int

students = [
    Student(id=1, name="John", grade=10),
    Student(id=3, name="Bob", grade=12)
]

# Read all students
@app.get("/students/")
async def read_all_students():
    return students

# Create a new student
@app.post("/students/")
async def create_student(New_student:Student):
    students.append(New_student)
    return New_student

# Update a student by ID
@app.put("/students/{student_id}/")
async def update_student(student_id:int, updated_student:Student):
    for idex,student in enumerate(students):
        if student.id == student_id:
            students[idex] = updated_student
            return 
        
    return {"error":"student not found"}

# Delete a student by ID
@app.delete("/students/{student_id}/")
async def delete_student(student_id:int):
    for idex,student in enumerate(students):
        if student.id == student_id:
            del students[idex]
            return {"message":"student deleted"}
        
    return {"error":"student not found"}

    

