from fastapi import FastAPI

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

# Add a FastAPI route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Add a health check route
@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    # Gunicorn will be used to run the app, so no need for uvicorn here
    pass
