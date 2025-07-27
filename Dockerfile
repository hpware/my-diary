# VITE BUILDER
FROM oven/bun:latest AS form-frontend-builder
WORKDIR /frontend
COPY submit-front/package*.json ./
COPY submit-front/bun.lock* ./
RUN bun install
COPY frontend .
RUN bun run build

# FLASK APP BUILDER
FROM python:3.11-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=form-frontend-builder /frontend/dist /app/static/submit_form
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
