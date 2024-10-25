from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.admin_controller import admin_route
from app.controller.attendence_controller import attendence_route
from app.controller.mentors_controller import mentors_route
from app.controller.school_controller import school_route
from app.controller.event_controller import event_route
from app.controller.feedback_controller import feedback_route
from app.controller.students_controller import student_route

app= FastAPI()

#CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_headers=["*"], # Allows all origins
    allow_methods=["*"], # Allows all origins

)

#Controllers
app.include_router(admin_route, tags=["Admin"])
app.include_router(attendence_route, tags=["Attendence"])
app.include_router(school_route, tags=["School"])
app.include_router(event_route, tags=["Event"])
app.include_router(mentors_route, tags=["Mentor"])
app.include_router(feedback_route, tags=["Feedback"])
app.include_router(student_route, tags=["Student"])

@app.get("/")
async def root():
    return("hello world I am stark")





