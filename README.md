# fast-api-tutorial

## setup

```bash
pip install pandas
pip install numpy
pip install sklearn
# pip install pickle # standard lib python
pip install FastAPI
pip install "uvicorn[standard]"
pip install requests
pip install pydantic
```

## Create VENV

```bash
python3 -m venv fast-api-venv
source fast-api-venv/bin/activate
```

## Test

```bash
# TEST SCRIPTS
uvicorn app.main:app 
```

## Build Images

```bash
docker build -t <image name> .
docker run -d --name <container name> -p 80:80 <image name>

docker build -t fast-api-tutorial .
docker run -d --name fast-api-tutorial -p 80:80 fast-api-tutorial:latest
```
