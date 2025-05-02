# PyAdmin

A user, role, menu, and api access management system built with FastAPI1

# To install all library

```bash
pip install -r requirements.txt
```

# To generate product evn

```bash
python -m venv env
```

# To active project evn

```bash
env/Scripts/activate
```

# DB migration commands

```bash
alembic init migrations
```

```bash
alembic revision --autogenerate -m "initial commit"
```

```bash
alembic upgrade head
```

# To start the development server

```bash
fastapi dev main.py
```
