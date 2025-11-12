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


## 🔧 Prerequisites

- An **active AWS account** with sufficient permissions to create and manage IAM roles, CodeBuild, CodePipeline, EKS, and ECR resources.  
- **AWS CLI** installed and configured with administrative credentials.  
- A **GitHub account** and repository for source code integration.  
- Basic knowledge of **AWS Developer Tools** and **GitHub Actions** workflows.  
- A **CodeBuild IAM Role** with the required permissions to interact with **EKS**, **ECR**, **CodePipeline**, **CodeStar Connections**, and **CloudWatch Logs**.  

---

### 🛠️ Create the IAM Role

#### Role Details
- **Role Name:** `CodeBuildServiceRole`  
- **Attached Inline Policy:** `CodeBuildServiceRole-Policy`

### 🛠️ Creating the CodeBuild IAM Role

#### Steps to Create the Role

1. Navigate to the **IAM Console** → **Roles** → **Create role**.  
2. Choose **AWS Service** → **CodeBuild** → click **Next**.  
3. Skip attaching any default policies and click **Next**.  
4. Provide the role name: **`CodeBuildServiceRole`** and click **Create role**.  
5. After creation, open the role and click **Add permissions** → **Create inline policy**.  
6. Paste the following JSON policy and name it **`CodeBuildServiceRole-Policy`**.  

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "*",
               "Resource": "*"
           }
       ]
   }
7. Click Next, review the details, and then click Create policy.

8. Go to the Trust relationships tab and click Edit trust policy.
Replace the existing trust relationship with the following JSON:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "codebuild.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}





