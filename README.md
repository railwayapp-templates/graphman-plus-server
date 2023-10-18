# Railway GraphQL API Collection

This repo contains two components which allow Railway to distribute the GraphQL API collection for Railway's public API.

We have captured this in a template for Railway users to deploy, should they find it useful.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/graphman)

## Components

### 1. file-server/

A [Flask](https://flask.palletsprojects.com/en/3.0.x/) application with the following routes:

- **/upload** (POST): Accepts a JSON body which is compared against the current collection file to be stored in `/data` if any changes are detected.
- **/** (GET): Renders a simple File Explorer of the `/data` directory and allows for downloading the existing collection file.  An archive directory also exists to store old versions of the file.

### 2. graphman/

A modified version of the [Graphman](https://github.com/Escape-Technologies/graphman) CLI. It runs on a cron schedule defined in `graphman/railway.toml`.  It is responsible for:

- Generating the GraphQL API collection.
- Sending a POST request to the `file-server` `/upload` endpoint with the GraphQL API collection object.

## Environment Variables
The Graphman component expects two environment variables.  Both are preconfigured in the Railway template, as follows -
- API_URL=`${{file-server.RAILWAY_PUBLIC_DOMAIN}}` *(URL of the file server)*
- GRAPHQL_ENDPOINT=`https://backboard.railway.app/graphql/v2` *(GraphQL API endpoint from which to generate a colection)*

*Note: If using this service to generate a collection from another GraphQL API, keep in mind that some API's may have authentication requirements that will require a modification of the Graphman cron.  Refer to the [Graphman Documentation](https://github.com/Escape-Technologies/graphman) for more information.*