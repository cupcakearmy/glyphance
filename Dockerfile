FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app
COPY . .
RUN uv sync --frozen

ENTRYPOINT [ "uv", "run", "python", "src/main.py" ]

ENV GLYPHANCE_CONFIG=/data/glyphance.yaml
ENV GLYPHANCE_OUTPUT_DIRECTORY=/data/generated
