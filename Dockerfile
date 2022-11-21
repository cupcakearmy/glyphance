FROM python:3.10-alpine

# Install Poetry
RUN apk add --no-cache curl
ENV POETRY_HOME=/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH ${POETRY_HOME}/bin:$PATH

# Install Deps
WORKDIR /app
COPY poetry.lock poetry.toml pyproject.toml ./
RUN poetry install

# Copy code
COPY . .
ENTRYPOINT [ "/poetry/bin/poetry" ]
CMD [ "run", "python", "src/main.py" ]

ENV GLYPHANCE_CONFIG=/data/glyphance.yaml
ENV GLYPHANCE_OUTPUT_DIRECTORY=/data/generated
