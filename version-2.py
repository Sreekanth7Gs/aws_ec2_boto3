import boto3

def manage_instance(instance_id, action=None):
    ec2 = boto3.client('ec2')

    try:
        if not action:
            action = input("Enter 'start' to start the instance or 'stop' to stop the instance: ")

        if action.lower() == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            print("Waiting for a few seconds...")
            import time
            time.sleep(5)
        elif action.lower() == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            print("Waiting for a few seconds...")
            import time
            time.sleep(5)
        else:
            print("Invalid Input...Please enter 'start' or 'stop'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    instance_id = input("Enter instance_id (press enter for all instances): ")
    if not instance_id:
        ec2_action = input("Enter 'start' to start all instances or 'stop' to stop all instances: ")
        instances = boto3.client('ec2').describe_instances()['Reservations']
        instance_ids = [instance['InstanceId'] for reservation in instances for instance in reservation['Instances']]

        for id in instance_ids:
            manage_instance(id, ec2_action)
    else:
        manage_instance(instance_id)
