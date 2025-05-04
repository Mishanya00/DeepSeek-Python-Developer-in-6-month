from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel, EmailStr

from send_real_email import send_email


app = FastAPI()


class EmailRequest(BaseModel):
    email: EmailStr
    subject: str | None = "Notification from FastAPI"
    body: str | None = "Hello from FastAPI!"


@app.post("/send-email/")
async def post_send_email(
    request: EmailRequest,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        send_email,
        recepient=request.email,
        subject=request.subject,
        body=request.body
    )
    
    return {
        "message": "Email is being sent in background",
        "email": request.email,
        "status": "queued"
    }