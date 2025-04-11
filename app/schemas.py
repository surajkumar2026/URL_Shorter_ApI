from pydantic import BaseModel

class URLCreate(BaseModel):
    long_url: str

class URLInfo(BaseModel):
    short_url: str
