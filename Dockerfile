FROM golang:1.19.4 as build-env

WORKDIR /go/src/znnd

# copy Go modules and dependencies to image
COPY go-zenon/go.mod .
COPY go-zenon/go.sum .

# download Go modules and dependencies
RUN go mod download

# copy go-zenon to image
COPY go-zenon .

# compile code
RUN go build -o /go/bin/znnd main.go

# move binary to thin image
FROM gcr.io/distroless/base

COPY --from=build-env /go/bin/znnd /
CMD ["/znnd"]

EXPOSE 35995/tcp
EXPOSE 35995/udp
EXPOSE 35997/tcp
EXPOSE 35998/tcp
