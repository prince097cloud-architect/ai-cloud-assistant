import boto3
from dotenv import load_dotenv
load_dotenv()

# Define the tools for AWS EC2 and Auto Scaling Groups
def list_ec2_instance(_=None):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    result = []

    for i in instances['Reservations']:
        for j in i['Instances']:
            instance_id = j['InstanceId']
            instance_type = j['InstanceType']
            state = j['State']['Name']
            result.append(f"{instance_id} | {instance_type} | {state}")

    return "\n".join(result) if result else "No EC2 instances found."


def list_asg(_=None):
    asg = boto3.client('autoscaling')
    response = asg.describe_auto_scaling_groups()
    result = []

    for group in response['AutoScalingGroups']:
        group_name = group['AutoScalingGroupName']
        desired_capacity = group['DesiredCapacity']
        min_size = group['MinSize']
        max_size = group['MaxSize']
        result.append(f"{group_name} | Desired: {desired_capacity}, Min: {min_size}, Max: {max_size}")

    return "\n".join(result) if result else "No Auto Scaling Groups found."
