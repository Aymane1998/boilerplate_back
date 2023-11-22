# Docker Compose Configuration

## Overview

Our Docker Compose setup manages container orchestration for different environments - development, testing, staging, and production. Each environment has its own Docker Compose file and associated `.env` file.

## File Structure

- `docker-compose.yml` for development.
- `docker-compose.test.yml` for testing.
- `docker-compose.staging.yml` for staging.
- `docker-compose.prod.yml` for production.

Environment-specific `.env` files:
- `.env.dev`
- `.env.testing`
- `.env.staging`
- `.env.production`

## Usage Instructions

### Development

- **File**: `docker-compose.yml`
- **Environment**: `.env.dev`
- **Command**: `docker-compose up -d --build`
- **Description**: Includes services like the application and a database, tailored for development.

### Testing

- **File**: `docker-compose.test.yml`
- **Environment**: `.env.testing`
- **Command**: `docker-compose -f docker-compose.test.yml up -d --build`
- **Description**: Configured for deploying the application in a testing environment. This environment is used for manual or exploratory testing.

### Staging

- **File**: `docker-compose.staging.yml`
- **Environment**: `.env.staging`
- **Command**: `docker-compose -f docker-compose.staging.yml up -d --build`
- **Description**: Mirrors production as closely as possible for final testing and validation before deployment to production.

### Production

- **File**: `docker-compose.prod.yml`
- **Environment**: `.env.production`
- **Command**: `docker-compose -f docker-compose.prod.yml up -d --build` or `./scripts/run-compose-prod.sh`
- **Description**: Optimized for live production deployment, focusing on performance, security, and reliability.

## Managing Environment Variables

- Environment configurations are managed through respective `.env` files.
- These files contain sensitive information and should not be stored in version control.

## Security Considerations

- Avoid storing sensitive data in version control.
- Staging and Production `.env` files should be securely stored and managed.

## Additional Information

- Ensure Docker and Docker Compose are installed and updated.
