import logging
from fastapi import Request, HTTPException
import time

# In-memory storage for request counters
request_counters = {}


# Custom RateLimiter class with dynamic rate limiting values per route
class RateLimiter:
    def __init__(self, requests_limit: int, time_window: int, limit_globally: bool = True):
        self.requests_limit = requests_limit
        self.time_window = time_window
        self.limit_globally = limit_globally
        logging.info(
            f"Rate limiting initialized with {requests_limit} requests per {time_window} seconds"
        )

    async def __call__(self, request: Request):
        if not request.client:
            raise HTTPException(status_code=400, detail="Invalid client")
        client_ip = request.client.host
        route_path = request.url.path

        # Get the current timestamp
        current_time = int(time.time())

        # Create a unique key based on client IP and route path
        key = client_ip if self.limit_globally else f"{client_ip}:{route_path}"

        # Check if client's request counter exists
        if key not in request_counters:
            request_counters[key] = {"timestamp": current_time, "count": 1}
        else:
            # Check if the time window has elapsed, reset the counter if needed
            if current_time - request_counters[key]["timestamp"] > self.time_window:
                # Reset the counter and update the timestamp
                request_counters[key]["timestamp"] = current_time
                request_counters[key]["count"] = 1
            else:
                # Check if the client has exceeded the request limit
                if request_counters[key]["count"] >= self.requests_limit:
                    logging.warning(
                        f"Rate limit exceeded for {client_ip}. Made {request_counters[key]['count']} requests in {current_time - request_counters[key]['timestamp']} seconds"
                    )
                    raise HTTPException(status_code=429, detail="Too Many Requests")
                else:
                    request_counters[key]["count"] += 1

        # Clean up expired client data (optional)
        for k in list(request_counters.keys()):
            if current_time - request_counters[k]["timestamp"] > self.time_window:
                request_counters.pop(k)

        return True
