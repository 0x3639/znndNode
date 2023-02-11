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

Update the docker-compose.yml file with the correct Domain Name and Public IP address
```
cd znndNode
nano docker-compose.yml
```

Change the Domain and Public IP Variables
```
DOMAIN=${DOMAIN:-example.com} #Change the domain name
PUBLIC_IP=${PUBLIC_IP:-1.1.1.1} #Change the public IP Address of the node
```
Make sure to leave `DOMAIN=${DOMAIN:-` and only change the domain name
Make sure to leave `PUBLIC_IP=${PUBLIC_IP:-` and only change the IP address

For Example:
DOMAIN=${DOMAIN:-public.zenon-node.com} #Change the domain name
PUBLIC_IP=${PUBLIC_IP:-69.69.69.69} #Change the public IP Address of the node

Save and exit `ctrl-x`

Ensure the following ports are open and forwarded to the private node IP address

TCP: 3000, 35995, 35997, 35998, 80, 443
UDP: 35995

Start the Docker stack
```
cd ~/znndNode
sudo docker compose up -d
```

Docker images will be built or downloaded and configured.  After all image are started you can check to make sure the images are running with the following command. Make sure you are in the `/znndNode` directory.

```
sudo docker-compose ps
```