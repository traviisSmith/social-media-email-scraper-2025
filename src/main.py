thonfrom fastapi import FastAPI
from pydantic import BaseModel
from email_finder.youtube import find_email_youtube
from email_finder.tiktok import find_email_tiktok
from email_finder.linkedin import find_email_linkedin

app = FastAPI()

class UserRequest(BaseModel):
    platform: str
    userId: str

@app.post("/find_email/")
async def find_email(request: UserRequest):
    if request.platform.lower() == "youtube":
        return find_email_youtube(request.userId)
    elif request.platform.lower() == "tiktok":
        return find_email_tiktok(request.userId)
    elif request.platform.lower() == "linkedin":
        return find_email_linkedin(request.userId)
    else:
        return {"error": "Platform not supported"}