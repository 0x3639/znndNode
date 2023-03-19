# znndNode

Easily run a node for Zenon Network on Docker with a full suite of open source monitoring, alerting, and servicing tools. The Docker Containers includes:
* [Zenon Network Node](https://github.com/zenon-network/go-zenon)
* [Grafana](http://grafana.org/)
* [NodeExporter](https://github.com/prometheus/node_exporter)
* [Prometheus](https://prometheus.io/)
* [cAdvisor](https://github.com/google/cadvisor)
* [Monit-Docker](https://github.com/decryptus/monit-docker)
* [AlertManager](https://github.com/prometheus/alertmanager)
* [Caddy](https://hub.docker.com/_/caddy)
* [Push Gateway](https://prometheus.io/docs/practices/pushing/)

## Quick Start

Install Ubuntu Desktop or Server and Update
```
sudo apt update && sudo apt upgrade
```

Install Dependencies
```
sudo apt install git && sudo apt install curl
```

Install Docker
```
cd ~
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

Confirm Docker is installed correctly
```
docker -v
```

Clone the znndNode Repository and Submodules
```
git clone --recurse-submodules https://github.com/0x3639/znndNode.git
```

Update the .env file with the correct Domain Name and Public IP address
```
cd znndNode
nano .env
```

Change the Domain and Public IP Variables
```
DOMAIN=example.com #UPDATE THE DOMAIN NAME
PUBLIC_IP=1.1.1.1 #UPDATE THE IP ADDRESS
ADMIN_USER=admin
ADMIN_PASSWORD=admin
ADMIN_PASSWORD_HASH=$2a$14$1l.IozJx7xQRVmlkEQ32OeEEfP5mRxTpbDTCTcXRqn19gXD8YK1pO
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=admin
GF_USERS_ALLOW_SIGN_UP=false
GF_INSTALL_PLUGINS=marcusolsson-json-datasource
```
Save and exit `ctrl-x`

Ensure the following ports are open and forwarded to the private node IP address

TCP: 3000, 35995, 35997, 35998, 80, 443
UDP: 35995

IMPORTANT:
Make sure to insert an A Record at your DNS provider pointing the domain name (setup above) to the IP address (setup above) of your server.

Start the Docker stack
```
cd ~/znndNode
sudo docker compose up -d
```

Docker images will be built or downloaded and configured.  After all image are started you can check to make sure the images are running with the following command. Make sure you are in the `/znndNode` directory.

```
sudo docker compose ps
```

Log into grafana and setup a new password
```
https://example.com:3000 #Replace example.com with the domain you setup above.
```
Default User ID = `admin` Password = `admin`

## Node Access

Replace `example.com` with your domain name

- Grafana Access `https://example.com:3000
- Syrius Access `wss://example.com:35998`
- API Access `https://example.com:35997`
- Check Sync Status `curl -X GET https://example.com:35997 -H "content-type: application/json" -d '{"jsonrpc": "2.0", "id": 40, "method": "stats.syncInfo", "params": []}'`

