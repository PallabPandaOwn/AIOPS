#!/bin/bash

# Variables
VPC_NAME="MyVPC"
SUBNET_NAME="MyPublicSubnet"
CIDR_BLOCK="10.0.0.0/16"
SUBNET_CIDR="10.0.1.0/24"
REGION="us-east-1"

# Check if AWS CLI is installed
if ! command -v aws &> /dev/null; then
    echo "Error: AWS CLI is not installed. Please install AWS CLI and try again."
    exit 1
fi

# Check if AWS CLI is configured
if ! aws configure list | grep -q "access_key"; then
    echo "Error: AWS CLI is not configured. Please run 'aws configure'."
    exit 1
fi

# Function to create VPC and subnet
create_resources() {
    echo "Creating VPC..."
    VPC_ID=$(aws ec2 create-vpc --cidr-block $CIDR_BLOCK --query 'Vpc.VpcId' --output text --region $REGION)
    echo "VPC created with ID: $VPC_ID"

    echo "Creating Public Subnet..."
    SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block $SUBNET_CIDR --query 'Subnet.SubnetId' --output text --region $REGION)
    echo "Subnet created with ID: $SUBNET_ID"
}

# Function to teardown resources
teardown_resources() {
    echo "Fetching VPC ID..."
    VPC_ID=$(aws ec2 describe-vpcs --filters "Name=cidr-block,Values=$CIDR_BLOCK" --query 'Vpcs[0].VpcId' --output text --region $REGION)
    
    if [[ $VPC_ID == "None" ]]; then
        echo "No VPC found with CIDR $CIDR_BLOCK. Exiting."
        exit 1
    fi
    
    echo "Fetching Subnet ID..."
    SUBNET_ID=$(aws ec2 describe-subnets --filters "Name=vpc-id,Values=$VPC_ID" --query 'Subnets[0].SubnetId' --output text --region $REGION)
    
    if [[ $SUBNET_ID != "None" ]]; then
        echo "Deleting Subnet: $SUBNET_ID"
        aws ec2 delete-subnet --subnet-id $SUBNET_ID --region $REGION
    fi
    
    echo "Deleting VPC: $VPC_ID"
    aws ec2 delete-vpc --vpc-id $VPC_ID --region $REGION
    echo "Resources deleted successfully."
}

# Main logic
case "$1" in
    create)
        create_resources
        ;;
    teardown)
        teardown_resources
        ;;
    *)
        echo "Invalid option. Usage: $0 {create|teardown}"
        exit 1
        ;;
esac
