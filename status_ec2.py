import boto3
ec2 = boto3.client('ec2', region_name = 'us-east-1')
def check_status_insatnce(instance_id):
    try
        ec2.status_instances(InstanceIds = [instance_id])
        print(f"status of {instance_id}: ")
    except Exception as e :
        print(f"Error: {e}")
if __name__ == "__main__":
    status_instance = 'i-0e13829aa840a8c17'   
    check_status_insatnce(status_instance)    