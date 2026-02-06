FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml pyproject.toml
COPY . /app

# Install build essentials and project with optional extras (yt/transcribe) and test deps
RUN apt-get update && apt-get install -y --no-install-recommends gcc git curl ca-certificates && \
    python -m pip install --upgrade pip setuptools wheel && \
    pip install -e .[yt,transcribe] pytest && \
    apt-get remove -y gcc && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home appuser || true
USER appuser

ENV PATH="/home/appuser/.local/bin:$(PATH)"

CMD ["bash"]
