FROM python:3.11.13-slim

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN python -c "import easyocr; easyocr.Reader(['en'], model_storage_directory='./easyocr_model')"

COPY app/ .

EXPOSE 8000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]