FROM python:3-alpine
COPY * /meteors/
WORKDIR /meteors/
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "find_meteors.py"]
