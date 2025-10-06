# Python + Redis Quickstart

This project demonstrates how to run a password-protected, persistent Redis instance in Docker and connect to it from Python.

## Prerequisites

- WSL 2 and Docker Desktop installed/enabled
- Verify Docker works:

  ```sh
  docker --version
  docker run --rm hello-world
  ```

## 1. Create a persistent Redis data volume

```sh
docker volume create redis-data
```

## 2. Start Redis (persistent, password-protected)

```sh
# Set your password
docker run -d --name redis -p 127.0.0.1:6379:6379  -v redis-data:/data  --restart unless-stopped redis:latest redis-server --appendonly yes
```

- `-p 127.0.0.1:6379:6379` exposes Redis to your PC only (not LAN)
- `-v redis-data:/data` persists data
- `--restart unless-stopped` auto-starts Redis on reboot
- `--appendonly yes` enables AOF persistence
- `--requirepass` sets your password

## 3. Confirm Redis is running

```sh
docker ps
docker logs --tail=50 redis
```

## 4. Test Redis with redis-cli

```sh
docker exec -it redis redis-cli -a "MyS3curePassw0rd!" ping
# Expect: PONG

docker exec -it redis redis-cli -a "MyS3curePassw0rd!" set hello world
docker exec -it redis redis-cli -a "MyS3curePassw0rd!" get hello
# Expect: "world"
```

## 5. Python Client Usage

Install dependencies:

```sh
pip install -r requirements.txt
```

Run the demo script:

```sh
python main.py
```

## Maintenance

- Stop Redis: `docker stop redis`
- Start Redis: `docker start redis`
- Remove container: `docker rm -f redis`
- Remove data volume (deletes all data): `docker volume rm redis-data`