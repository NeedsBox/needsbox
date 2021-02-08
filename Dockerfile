FROM python:3.8.5
# Create app directory
WORKDIR /app
# Install app dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Install GDAL dependencies
RUN apt-get install -y libgdal-dev g++ --no-install-recommends && \
    apt-get clean -y

# Update C env vars so compiler can find gdal
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Bundle app source
COPY src /app
EXPOSE 8080
CMD [ "python", "server.py" ]