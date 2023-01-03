# Script to identify active node locations for Grafana geomap

import IP2Location
import os
import requests
from fastapi import FastAPI

app = FastAPI()

node = "znnd"              # node's address
nodes = []                 # array of nodes
locations = []             # location of each node
data = None                # raw jsonrpc data

# Get IP location for a live node
def getHostInfo(ip):
    database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB3.BIN"))
    rec = database.get_all(ip)

    _json = {
        "ip": ip,
        "city": rec.city,
        "region": rec.region,
        "country": rec.country_long
    }
    locations.append(_json)


def getPeers(ip):
    try:
        params = {"jsonrpc": "2.0", "id": 40, "method": "stats.networkInfo", "params": []}
        header = {"content-type": "application/json"}
        global data

        results = requests.get("http://" + ip + ":35997", headers=header, json=params, timeout=10)
        data = results.json()
        peers = data['result']['peers']
        for peer in peers:
            if peer == "127.0.0.1":
                pass
            nodes.append(peer['ip'])
    except:
        print("Error: could not get peers")


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api")
async def root():
    getPeers(node)
    if nodes:
        for n in nodes:
            getHostInfo(n)
        return locations
    else:
        return {"message": "error"}
