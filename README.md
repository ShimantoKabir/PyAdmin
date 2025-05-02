# PyAdmin

A user, role, menu, and api access management system built with FastAPI1

# to install all library

```bash
pip install -r requirements.txt
```

# Other commands

```bash
python -m venv env
env/Scripts/activate
pip install "fastapi[standard]"
pip install alembic
alembic init migrations
pip install sqlmodel
alembic revision --autogenerate -m "initial commit"
alembic upgrade head
fastapi dev main.py
```
