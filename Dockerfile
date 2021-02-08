FROM python:3.8.5
# Create app directory
WORKDIR /app
# Install app dependencies
COPY src/requirements.txt ./
RUN pip install -r requirements.txt
RUN apt-get install binutils libproj-dev gdal-bin -y
# Bundle app source
COPY src /app
EXPOSE 8080
CMD [ "python", "server.py" ]