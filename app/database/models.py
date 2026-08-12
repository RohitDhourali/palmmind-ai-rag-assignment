from pydantic import BaseModel

class InterviewBooking(BaseModel):
    name: str
    email: str
    date: str
    time: str