//go:build !libznn || metrics
// +build !libznn metrics

package main

import (
	"net/http"

	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/zenon-network/go-zenon/app"
)

// znnd is the official command-line client
func main() {
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(":2112", nil)
	app.Run()
}
