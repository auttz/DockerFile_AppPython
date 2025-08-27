FROM python:3.13
WORKDIR /myapp
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY templates/ ./templates/
COPY static/ ./static/
EXPOSE 5000
CMD ["python","app.py"]