from pydantic import BaseModel
from typing import List

class UpworkProfile(BaseModel):
    title: str
    overview: str
    skills: List[str]
    hourly_rate: str
    profile_tips: List[str]