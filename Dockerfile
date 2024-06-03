FROM python:3.11

ENV PYTHONPATH=/app
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 5000

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r /requirements/base.txt


CMD ["uvicorn", "run:main_app", "--host", "0.0.0.0", "--port", "5000"]
