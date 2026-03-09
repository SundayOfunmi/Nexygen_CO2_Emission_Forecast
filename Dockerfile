# 1. Use a specific base image
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy ONLY the requirements file first
COPY requirements.txt .

# 4. Install dependencies (this layer will be cached)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

