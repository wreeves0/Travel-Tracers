FROM python:3.10-bullseye

# Upgrades pip to the latest version
RUN python -m pip install --upgrade pip

# Sets the working directory inside the container where our app will run
WORKDIR /app

# Copy all files and directories from your service's directory
COPY . .

# Installs all the python packages listed in our requirements.txt file
RUN python -m pip install -r requirements.txt

# This is the command that runs when the docker container starts
CMD uvicorn main:app --host 0.0.0.0 --port 80 --forwarded-allow-ips "*"


# If you're using a relational database and want migrations
# to be run automatically, delete the previous CMD line and
# uncomment the following COPY and CMD lines
# COPY migrations migrations
# CMD python -m migrations up && uvicorn main:app --host 0.0.0.0 --port 80 --forwarded-allow-ips "*"
