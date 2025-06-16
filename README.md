# prisma-python-example
Trying out prisma in python

## Steps to run the project
### docker-compose 
```bash
docker-compose up
```
and you are good to do, checkout http://localhost:8000/docs

### local deployment
1. initialize python environment (using uv)
```bash
uv sync
```

2. run container
```bash
docker-compose up
```
simple

3. setup database
```bash
prisma db push
```

4. run python server
```bash
uvicorn main:app
```

5. checkout swagger api
url: http://localhost:8000/docs
