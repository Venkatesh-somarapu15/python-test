import boto3

IAM_RESOURCE = boto3.resource('iam')

users = IAM_RESOURCE.users.all()

print('All account users')

for user in users:
    print(f'  - {user.name}')