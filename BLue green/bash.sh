#!/bin/bash

# Replace with your region
AWS_REGION="us-west-2"
CLUSTER_NAME=$(terraform output -raw cluster_name)

aws eks --region $AWS_REGION update-kubeconfig --name $CLUSTER_NAME