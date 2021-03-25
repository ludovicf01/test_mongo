FROM mongo:latest
# Define mountable directories.
VOLUME ["/data/db"]

# Define working directory.
WORKDIR /data

EXPOSE 27017