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


# TODO FINISH

## Before You Start
How do you know this node will not harm [Zenon Network](https://zenon.network) or the Node Operator?

Let's start by making sure the node software is based on the Official Zenon Network `go-zenon` node implementation. Open the `Dockerfile` and let's review the build instructions.  

```
# Establishes the image used to compile the node software.  It's from golang.
FROM golang:1.18 as build-env 

# Establishes the working directory
WORKDIR /go/src/znnd 

# Copies modules and dependencies to image necessary to compile go-zenon
COPY go-zenon/go.mod .
COPY go-zenon/go.sum .
RUN go mod download

# Copies go-zenon from the Official Repo to the image to be compiled.  go-zenon is a [Submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules) of the Official Repo.  You can confirm this by clicking on the `go-zenon` folder in [znndNode](https://github.com/0x3639/znndNode).  It will redirect you to the Official Repo.
COPY go-zenon .

# Compiles go-zenon and stores it in the folder /go/bin/znnd
RUN go build -o /go/bin/znnd main.go

# Estabishes a minimal image to run `znnd`.  The Image is created and hosted by google.  Visit this website to see the image.  gcr.io/distroless
FROM gcr.io/distroless/base

# Copies `znnd` from the output above into the new runtime image at location `/`.  After copying `znnd` the binary is started.
COPY --from=build-env /go/bin/znnd /
CMD ["/znnd"]

# Exposes ports 35995, 35997, and 35998 on the image
EXPOSE 35995/tcp
EXPOSE 35995/udp
EXPOSE 35997/tcp
EXPOSE 35998/tcp
```

All other Docker Images are open source and can be independently audited are reviewed by the user.

## Quick Start

Install requirements, clone this repository on your host and run docker-compose.

```bash
git clone --recurse-submodules https://github.com/0x3639/znndNode.git

cd znndNode

# Update all references to domain names

sudo docker-compose up -d
```
