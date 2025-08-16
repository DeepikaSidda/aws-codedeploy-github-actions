# Multi-Region CI/CD Pipeline with AWS CodePipeline and GitHub Actions

## Overview

This project implements a robust multi-region Continuous Integration and Continuous Delivery (CI/CD) pipeline using AWS CodePipeline and GitHub Actions. The pipeline automates the deployment of a containerized application across multiple AWS regions, ensuring high availability and resilience.

## Key Features

- **Multi-Region Deployment**: Deploy applications across primary (us-east-1) and secondary (ap-south-1) AWS regions.
- **Containerized Applications**: Utilize Docker containers for application deployment.
- **Automated Workflows**: Leverage GitHub Actions for CI and AWS CodePipeline for CD.
- **ECR and EKS Integration**: Store container images in Amazon ECR and deploy to Amazon EKS clusters.

## Benefits

- **High Availability**: Distributes application load across regions to maintain uptime.
- **Disaster Recovery**: Facilitates quick recovery in case of regional failures.
- **Reduced Latency**: Serves users from the nearest geographical region.
- **Improved Resilience**: Minimizes single points of failure.


## Prerequisites

- An AWS account with necessary permissions.
- AWS CLI installed and configured.
- A GitHub account and repository.
- Basic knowledge of AWS services and GitHub Actions.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DeepikaSidda/aws-codedeploy-github-actions.git
   cd aws-codedeploy-github-actions

 2. **Configure AWS Credentials**

Ensure your AWS credentials are set up by running the following command in your terminal:

```bash
aws configure

After, please follow the detailed steps provided in the Whizlabs lab:

[Build a Multi-Region CI/CD Pipeline with AWS CodePipeline and GitHub Actions](https://www.whizlabs.com/labs/build-a-multi-region-cicd-pipeline-with-aws-codepipeline-and-github-actions)

### Steps to Follow:

1. Create Amazon EKS clusters in multiple regions using AWS CLI.
2. Set environment variables.
3. Create an Amazon ECR repository.
4. Create an AWS CodeStar connection in us-east-1.
5. Add the OIDC provider to your AWS account.
6. Create CodeBuild projects.
7. Create the pipeline using the AWS Console in us-east-1.
8. Create a GitHub OIDC role.
9. Map the CodeBuild IAM role to EKS clusters in us-east-1.
10. Install the AWS Load Balancer Controller with Helm.
11. Map the CodeBuild IAM role to EKS clusters in ap-south-1 and install the AWS Load Balancer Controller with Helm.
12. Add GitHub secrets for CodeBuild trigger.
13. Final deployment and verification.
