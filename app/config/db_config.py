from motor import motor_asyncio
import os

password=os.environ.get("PSD")
client=motor_asyncio.AsyncIOMotorClient(f"## please here write mongodb database connection url ##")

database=client.mohit

mentors_collection=database.mentors
school_collection=database.school
admin_collection=database.admins
attendence_collection=database.attendence
event_collection=database.event
feedback_collection=database.feedback
student_collection=database.student
feedback_collection= database.feedback
