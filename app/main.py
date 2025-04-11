from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from . import models, schemas, utils
from .database import engine, Base, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["home"])
async def index():
    return RedirectResponse(url="/docs")



@app.post("/shorten", response_model=schemas.URLInfo)
async def shorten_url(url: schemas.URLCreate, db: AsyncSession = Depends(get_db)):
    try:
        short_code = utils.generate_short_code()
        new_url = models.URL(short_code=short_code, long_url=url.long_url)
        db.add(new_url)
        await db.commit()

        short_url = f"http://localhost:8000/{short_code}"
        return {"short_url": short_url}
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Short code already exists")
    except Exception as e:
        print(" Error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/{short_code}")
async def redirect_url(short_code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.URL).where(models.URL.short_code == short_code))
    url = result.scalar_one_or_none()
    if url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url.long_url)
