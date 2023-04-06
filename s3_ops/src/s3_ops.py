import boto3
import json


BUCKET_NAME = 'sidi-s3-2023-bucket'


def s3_client():
    s3 = boto3.client('s3')
    """ :type : pyboto3.s3"""   # The code does NOT work without this comment!
    return s3


def create_bucket(bucket_name):
    return s3_client().create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'
        }
    )


def create_bucket_policy():
    bucket_policy = {
        "Version": "2012-10-17",    # Specific version
        "Statement": [
            {
                "Sid": "AddPerm",  # 'Sid' defines the type of permission
                "Effect": "Allow",
                "Principal": "*",    # Opens the bucket to public and accessed by everyone
                "Action": ["s3:*"],  # Allows all operations
                "Resource": "arn:aws:s3:::" + BUCKET_NAME + "/*"  # '/*' allows operation on all objects in the bucket
            }
        ]
    }
    policy_string = json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=policy_string
    )


def list_buckets():
    return s3_client().list_buckets()


def get_bucket_policy():
    return s3_client().get_bucket_policy(Bucket=BUCKET_NAME)


def get_bucket_encryption():
    return s3_client().get_bucket_encryption(Bucket=BUCKET_NAME)


def update_bucket_policy(bucket_name):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:DeleteObject", "s3:GetObject", "s3:PutObject"],
                "Resource": "arn:aws:s3:::" + bucket_name + "/*"
            }
        ]

    }
    policy_string = json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


def server_side_encrypt_bucket():               # Might NOT work!
    return s3_client().put_bucket_encryption(
        Bucket=BUCKET_NAME,
        ServerSideEncryptionConfiguration={
            "Rules": [
                {
                    "ApplyServerSideEncryptionByDefault": {
                        "SSEAlgorithm": "AES256"
                    }
                }
            ]
        }
    )


def delete_bucket():
    return s3_client().delete_bucket(Bucket=BUCKET_NAME)


if __name__ == '__main__':
    # print(create_bucket(BUCKET_NAME))
    # print(create_bucket_policy())
    # print(list_buckets())
    # print(get_bucket_policy())
    # print(get_bucket_encryption)
    # print(update_bucket_policy(BUCKET_NAME))
    # print(server_side_encrypt_bucket())
    # print(delete_bucket())
    print("Program ran successfully.")
