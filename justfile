default:
    just --list

build-http-api:
    cd http-api && docker build -t rexhaif/http-api .
