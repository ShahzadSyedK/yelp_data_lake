FROM python:3.9-bullseye


# Switch to root to install OpenJDK
USER root

# Update the package list and install necessary packages
RUN apt-get update
RUN apt-get install -y bash
RUN apt-get install -y openjdk-11-jdk
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Verify Java installation
RUN java -version

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

# Set the working directory
WORKDIR /app

# Copy the application code
COPY main.py /app/main.py
COPY scripts /app/scripts
COPY src /app/src

# Install required Python packages
RUN pip install pyspark==3.2.1 pandas

# Define the entry point
CMD ["python3", "main.py"]
