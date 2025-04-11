from functools import wraps
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from redis import Redis
import json
from time import sleep

# Initialize Redis client
redis_client = Redis(host="redis", port=6379, decode_responses=True)

# Create a FastAPI instance
app = FastAPI(
    debug=True,
    title="My FastAPI Application",
    summary="FastAPI Example",
    description="A simple FastAPI application",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    contact={
        "name": "X-Force",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    }
)

# Add a global variable to toggle caching
use_cache = True

# Modify the cache_response decorator to respect the global toggle
def cache_response(key_prefix, ttl=300):  # Default TTL is 5 minutes
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not use_cache:
                # If caching is disabled, directly call the endpoint function
                return func(*args, **kwargs)

            # Generate a cache key using the key_prefix and endpoint arguments
            cache_key = f"{key_prefix}:{json.dumps(kwargs, sort_keys=True)}"

            # Check if the response is in the cache
            cached_response = redis_client.get(cache_key)
            if cached_response:
                # Return the cached response
                return JSONResponse(content=json.loads(cached_response))

            # Call the original endpoint function
            response = func(*args, **kwargs)

            # Store the response in the cache with the specified TTL
            redis_client.set(cache_key, json.dumps(response), ex=ttl)

            return response

        return wrapper
    return decorator

# Modify the read_root endpoint to return a larger JSON message body
@app.get("/", summary="Root Endpoint")
@cache_response("root", ttl=300)
def read_root():
    sleep(1)
    return {
        "message": "Hello, FastAPI!",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "details": {
            "info": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "extra": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        },
        "metadata": {
            "author": "John Doe",
            "version": "1.0.0",
            "timestamp": "2025-04-11T12:00:00Z"
        },
        "additional_data": [
            {"section": "A", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
            {"section": "B", "content": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."},
            {"section": "C", "content": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."},
            {"section": "D", "content": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."},
            {"section": "E", "content": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."},
            {"section": "F", "content": "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio."},
            {"section": "G", "content": "Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris."},
        ]
    }

# Modify the health_check endpoint to return a larger JSON message body
@app.get("/health", summary="Health Check")
@cache_response("health_check", ttl=300)
def health_check():
    sleep(1)
    return {
        "status": "healthy",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "details": {
            "uptime": "123456 seconds",
            "services": {
                "database": "operational",
                "cache": "operational",
                "api": "operational"
            }
        },
        "metadata": {
            "author": "Jane Doe",
            "version": "1.0.0",
            "timestamp": "2025-04-11T12:00:00Z"
        },
        "additional_data": [
            {"section": "A", "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
        ]
    }

# Add an endpoint to toggle caching
@app.post("/toggle-cache", summary="Toggle Caching")
def toggle_cache(status: bool):
    global use_cache
    use_cache = status
    return {"use_cache": use_cache}

if __name__ == "__main__":
    # Gunicorn will be used to run the app, so no need for uvicorn here
    pass

# Return current cache status
@app.get("/cache-status", summary="Cache Status")
def cache_status():
    return {"use_cache": use_cache}
