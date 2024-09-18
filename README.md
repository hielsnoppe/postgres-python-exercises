# postgres-python-exercises

Setup:

```
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) ...$ pip install -r requirements.txt
```

Create database `exampledb` in `psql`:

```{sql}
CREATE DATABASE exampledb;
```

Update PostgreSQL credentials in `fabricatedata.py`:

```{python}
engine = create_engine('postgresql://postgres:mypass@localhost:5432/exampledb')
```

Run `fabricatedata.py`:

```
(.venv) ...$ python fabricatedata.py
```