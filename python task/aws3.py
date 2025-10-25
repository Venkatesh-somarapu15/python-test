#retrive the info of single iam user.
import boto3
iam = boto3.client('iam')
a=iam.get_user(UserName='programmer')
print(a)