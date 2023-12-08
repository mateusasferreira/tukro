#!/bin/bash

# Check if the version argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>"
  exit 1
fi

# Assign the new version
NEW_VERSION=$1

# Define the path to your Dockerrun.aws.json file
DOCKER_RUN_FILE="infra/Dockerrun.aws.json"

# Check if the Dockerrun.aws.json file exists
if [ ! -f "$DOCKER_RUN_FILE" ]; then
  echo "Error: $DOCKER_RUN_FILE not found."
  exit 1
fi

# Update the version in the Dockerrun.aws.json file
sed -i.bak "s/\(\"Name\": \"466706364244.dkr.ecr.us-east-2.amazonaws.com\/tukro_repo:\)\(.*\)\(\"\)/\1$NEW_VERSION\3/" $DOCKER_RUN_FILE

echo "Dockerrun.aws.json updated with version $NEW_VERSION"
