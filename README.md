# Description
Fetch current mortgage rates, store as a time series in Influxdb, to be used for display on a dashboard such as grafana.

# Running
1. From the root of the project: `python3 -m pip venv venv`
2. Enable virtual env: `source ./venv/bin/activate`
3. `cd ./app`
4. Install required packages: `pip install -r requirements.txt`
5. Setup configuration: `cp env.example .env`
6. Edit configuration: `vim .env`
7. Run the script: `python3 app.py`

# Running Docker Container
1. Setup config: `cd ./app`
2. `cp env.example .env`
3. Enter your config settings: `vim .env`
4. From the root of project `cd ..` build container image `docker build -t <image name>:<image version> .`
5. Run container: `docker run -d <image name>:<image version> `
