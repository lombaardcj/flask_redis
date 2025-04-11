# flask_redis

## Running the Application

This guide provides instructions to run the Fast API application in both development and production modes using Docker Compose.

### Prerequisites

- Ensure Docker and Docker Compose are installed on your system.
- Clone this repository to your local machine.

### Running in Development Mode

1. Navigate to the project directory:
   ```bash
   cd <>...>/flask_redis
   ```

2. Start the application in development mode:
   ```bash
   docker compose up --build --force-recreate --remove-orphans -d

   COMPOSE_BAKE=true docker compose up --build --force-recreate --remove-orphans
   ```

   - The `--build` flag ensures that any changes to the code are reflected in the container.
   - The application will be accessible at `http://localhost:8083` (or the port specified in the `docker-compose.yml` file).

3. To stop the application:
   ```bash
   docker-compose down
   ```

### Running in Production Mode

1. Update the `docker-compose.yml` file to use the production configuration (if applicable).

2. Start the application in production mode:
   ```bash
   docker-compose -f docker-compose.yml up --build -d
   ```

   - The `-d` flag runs the containers in detached mode.
   - The application will be accessible at `http://localhost` (or the port specified in the `nginx.conf` file).

3. To stop the application:
   ```bash
   docker-compose down
   ```

### Notes

- Ensure that the `nginx.conf` file is properly configured for production.
- Logs can be viewed using:
  ```bash
  docker-compose logs
  ```
- For troubleshooting, use:
  ```bash
  docker ps
  docker logs <container_id>
  ```
