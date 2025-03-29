# AIOPS
 
aws-vpc-create.sh, that performs the requested tasks. It includes proper variable naming, checks for AWS CLI installation, ensures AWS is configured, and supports create and teardown actions.


This script:
	•	Checks if AWS CLI is installed and configured.
	•	Supports create and teardown options to create or delete the VPC and subnet.
	•	Uses meaningful variable names for better readability.
	•	Provides error handling for invalid inputs.


chmod +x aws-vpc-create.sh

./aws-vpc-create.sh create     # To create resources

./aws-vpc-create.sh teardown   # To delete resources