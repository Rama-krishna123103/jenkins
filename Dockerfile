FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the model and application files
COPY iris_model.pkl /app/
COPY app.py /app/

# Install necessary packages
RUN pip install --no-cache-dir flask joblib

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
