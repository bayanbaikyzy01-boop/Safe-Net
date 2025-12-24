from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Цифрлық саяхат")

# Шаблондарды орналастыру
templates = Jinja2Templates(directory="templates")

# Статикалық файлдар
app.mount("/static", StaticFiles(directory="static"), name="static")


# =================== БАСТЫ БЕТТЕР ===================

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Басты бет - index.html"""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Цифрлық саяхат"
        }
    )


@app.get("/user_profile", response_class=HTMLResponse)
async def user_profile(request: Request):
    """Пайдаланушы профилі"""
    return templates.TemplateResponse(
        "user_profile.html",
        {
            "request": request,
            "title": "Қолданушы профилі"
        }
    )


@app.get("/my_course", response_class=HTMLResponse)
async def my_course(request: Request):
    """Курс беті"""
    return templates.TemplateResponse(
        "my_course.html",
        {
            "request": request,
            "title": "Менің курсым"
        }
    )

@app.get("/my_course1", response_class=HTMLResponse)
async def my_course(request: Request):
    """Курс беті"""
    return templates.TemplateResponse(
        "my_course1.html",
        {
            "request": request,
            "title": "Менің курсым"
        }
    )


@app.get("/test_tasks", response_class=HTMLResponse)
async def test_tasks(request: Request):
    """Тест тапсырмалары"""
    return templates.TemplateResponse(
        "test_tasks.html",
        {
            "request": request,
            "title": "Тест тапсырмалары"
        }
    )


@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    """Баптаулар"""
    return templates.TemplateResponse(
        "settings.html",
        {
            "request": request,
            "title": "Баптаулар"
        }
    )


@app.get("/achievements", response_class=HTMLResponse)
async def achievements(request: Request):
    """Жетістіктер беті"""
    return templates.TemplateResponse(
        "achievements.html",
        {
            "request": request,
            "title": "Курс аяқталды"
        }
    )





