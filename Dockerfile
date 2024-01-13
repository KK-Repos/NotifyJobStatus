FROM python:3

WORKDIR /work
COPY . .
RUN pip install -r requirements.txt
CMD ["python","main.py"]