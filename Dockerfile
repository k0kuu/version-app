FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
RUN useradd -m -u 10001 app
USER 10001
EXPOSE 8000
CMD ["python", "app.py"]
