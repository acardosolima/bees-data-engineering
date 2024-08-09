# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Install Java 13
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    openjdk-17-jdk=17.0.12+7-2~deb12u1 \
    tar=1.34+dfsg-1.2+deb12u1 \
    curl=7.88.1-10+deb12u6 \
    gzip=1.12-1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download and install Apache Spark
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
RUN curl -O https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar xvf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /opt/spark && \
    rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

# Set Spark environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Copy project requirements file into Docker image
COPY requirements.txt /app/requirements.txt

# Copy logging conf file into Docker image
COPY logging.conf /app/logging.conf

# Install required Python packages
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Keep container running to accept Spark jobs
ENTRYPOINT ["tail", "-f", "/dev/null"]
