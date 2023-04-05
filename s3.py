import logging
import boto3
from botocore.exceptions import ClientError
client = boto3.client('s3')

response = client.create_bucket(
    ACL='public-read',
    Bucket='nirajnfrompython',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-northeast-1' },
    # GrantFullControl='string', yesle chai read w
    # GrantRead='string', created permission herna sakdainan only the content is shown to the user
    # GrantReadACP='string', created permissions users le pani herna sakxan 
    # GrantWrite='string', naya object bucket ma banuna permssion dinxa 
    # GrantWriteACP='string', the iam user can modify the access control policy of an object or bucket to grant write access to other users or groups
    # ObjectLockEnabledForBucket=False,
    ObjectOwnership='BucketOwnerPreferred'
)
print(response)

# note: grantfullcontrol - allows grantee the read write acp and write acp permission on the bucket
# grantread : allows grantee to list the objects in the bucket
# grantreadAcp : allows grantee to read the bucket acl
# grantwrite allows grantee to create new objects in the ibject


# in the context of the aws acls are the basic level control access
# acp are the fine grained access control for s3 buckets and objects
# they allow you to define access policies that use IAM users and roles to grant or deny access to specific resources
# in case of operation side, between the normal operation rule defined and the other one which is defined on acp side , read oprtaion refers to accessing the actual content of an object
# while a read acp operation refers to accessing the access control policy of an object or bucket
# 
# read operation allows a user to retrieve the data stored in the object
# while a read acp operation allows a user to view the permissions that are set for  the object
#  


# now object ownership 
# its an optional parameter than can be set when uploading an object to  an S3 bucket using the aws sdk
# or aps
# it specifies who owns the object and who has permission specific actions on the object
# there are three values that can be specified for "objectownership " paramerter
# bucketownerPerferred: this is the default value for the objectownership parameter it indicates that the object should be owned by the bucket owner but the
# object uploader has the ability to overwrite the bucket owners permmssion
# if the object uploader doesnot specifiy an ACL or permission settings the object will inherit the bucket's default acl.