#!/bin/bash


AWS_REGION="ap-south-1"
CLUSTER_NAME=$(terraform output -raw cluster_name)

aws eks --region $AWS_REGION update-kubeconfig --name $CLUSTER_NAME
