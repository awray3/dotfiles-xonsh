from dataclasses import dataclass, field

import boto3
from mypy_boto3_s3 import S3ServiceResource

s3 = boto3.resource("s3")


@dataclass
class S3Bucket:
    name: str
    bucket: S3ServiceResource = field(init=False)

    def __post_init__(self):
        self.bucket = s3.Bucket(self.name)
