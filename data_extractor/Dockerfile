FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY historic_extractor/ historic_extractor/
COPY general_information_extractor/ general_information_extractor/
COPY real_time_extractor/ real_time_extractor/
COPY db/ db/

ENV PYTHONPATH=/app

ENTRYPOINT ["python"]