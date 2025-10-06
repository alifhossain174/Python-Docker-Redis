import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    # password="MyS3curePassw0rd!",
    decode_responses=True,  # return str instead of bytes
    socket_timeout=5,
)

# Simple health check
print("PING ->", r.ping())

# Round-trip
# r.set("framework", "docker+redis")
print("Get framework ->", r.get("framework"))

# r.delete("framework")
# print("OK")