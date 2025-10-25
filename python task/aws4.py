import json
import boto3
def create__iam__policy():
    iam=boto3.client('iam')
    my__managed__policy={
        "version":"2021-10-17",
        "Statement":[
            {
                "Effect":"Allow",
                "Action":[
                    "dynamodb:GetItem",
                    "dynamodb:Scan",

                ],
                "Resource":"*"
            }
        ]
    }
    Response=iam.create__policy(
        PolicyName='testDynamoDBPolicy',
        PolicyDocument=json.dumps(my__managed__policy)
    )
    print(response)
create__iam__policy()