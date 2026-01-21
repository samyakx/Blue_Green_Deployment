# Blue-Green Deployment with Terraform, EKS, Kubernetes, Docker, and MySQL


This repository provides a complete setup for implementing a blue-green deployment strategy on AWS using Terraform for infrastructure provisioning, Kubernetes (EKS) for orchestration, Docker for containerization, and MySQL as the database. The example application is a simple Python Flask web app that connects to MySQL to fetch and display a version-specific message.
The blue-green approach allows zero-downtime deployments by maintaining two identical environments:

Blue: The current production environment.
Green: The staging environment for new releases.
Traffic is switched by updating the Kubernetes Service selector.
