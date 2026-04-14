FROM mcr.microsoft.com/playwright/python:v1.58.0-noble

WORKDIR /app

COPY main.py .

COPY state.json .

RUN pip install playwright

CMD ["python","./main.py"]