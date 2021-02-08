FROM python:3.8.5
# Create app directory
WORKDIR /app
# Install app dependencies
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
COPY src/requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY src /app
EXPOSE 8080
CMD [ "python", "server.py" ]