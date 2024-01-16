# python docker hello world

Starts a flask server in debug mode so you can edit code and see results immediately.

## Requirements

- [Docker](https://docs.docker.com/engine/install/)

## Start

```
docker compose up --build
```

Takes care of install, build, start (via `Dockerfile` & `compose.yaml`).

Server will be running on http://localhost:5001

(because macOS has rudely taken over port 5000 for airplay)

## License

[CC0](https://creativecommons.org/public-domain/cc0/)
