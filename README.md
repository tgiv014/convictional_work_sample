# Convictional Work Sample

This project serves as my work sample for the [Convictional Engineering Challenge](https://github.com/convictional/engineering-interview).
It implements a simple REST server built on Flask in Python. I chose Python for this task because it is a very readable and expressive language.

## Running for Development
This assumes you have python3 and pip3 available.

```shell
$ pip3 install -r requirements.txt
...
$ python3 app.py
...
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Testing
There is a test suite for this API made using pytest. The tests can be run with:

```shell
$ pytest
```
or
```shell
$ python3 -m pytest
```

## Docker Build
This project is also ready to be built as a docker container:

```shell
$ docker build -t tgiv014/convictional_work_sample .
Sending build context to Docker daemon  113.2kB
Step 1/6 : FROM python:3.7.3-slim
...
```

## Docker Run
For convenience, the image for this project is pushed to docker hub.
This command will work whether or not the container has been built locally.

```
$ docker run -p 5000:5000 -d tgiv014/convictional_work_sample
```
