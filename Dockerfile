FROM golang:latest as build-env

WORKDIR /app

# copy Go modules and dependencies to image
COPY go-zenon/go.mod .
COPY go-zenon/go.sum .

# download Go modules and dependencies
RUN go mod download

# copy go-zenon to image
COPY go-zenon .

# compile code
RUN make znnd

# move binary to thin image
FROM gcr.io/distroless/base

COPY --from=build-env /app/build/znnd /

CMD ["/znnd"]

EXPOSE 35995/tcp
EXPOSE 35995/udp
EXPOSE 35997/tcp
EXPOSE 35998/tcp
