FROM python:3.11-slim

# Set environment variables for non-interactive install
ENV DEBIAN_FRONTEND=noninteractive \
    NODE_VERSION=20

# Install dependencies for uv and Node.js
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gnupg \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# ✅ Install Node.js and npm (via NodeSource)
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - && \
    apt-get update && apt-get install -y --no-install-recommends nodejs && \
    rm -rf /var/lib/apt/lists/*

# Test installs
RUN npm --version && node --version

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

RUN npm install prisma --save-dev

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]