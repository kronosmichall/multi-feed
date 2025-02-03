# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set environment variables (optional for custom username, password, and database)
ENV POSTGRES_USER=michal
ENV POSTGRES_PASSWORD=pass
ENV POSTGRES_DB=multifeed

# Add any custom initialization scripts (optional)
# COPY ./init-scripts/ /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432
