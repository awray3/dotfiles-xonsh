from dataclasses import dataclass, field

import boto3

s3 = boto3.resource("s3")


@dataclass
class S3Bucket:
    name: str
    bucket: "Bucket" = field(init=False)

    def __post_init__(self):
        self.bucket = s3.Bucket(self.name)
