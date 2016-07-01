import subprocess
import uuid

from django.conf import settings

import boto3
from botocore.exceptions import ClientError

from jobs.models import Job


class PersistentStorage(object):
    """ Utility class that will handle persisting job files into a persistent storage
        that should handle different cloud vendors
    """
    vendor = None
    client = None

    def __init__(self, *args, **kwargs):
        if settings.CLOUD_VENDOR == 'AWS':
            self.vendor = 'AWS'
        else:
            raise NotImplemented
        self.__init_client()

    def __init_client(self):
        if self.vendor == 'AWS':
            self.client = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
            )

    def prepare_storage(self):
        if self.vendor == 'AWS':
            try:
                self.client.create_bucket(
                    ACL='public-read',
                    Bucket=settings.PERSISTENT_STORAGE_BUCKET_NAME,
                    CreateBucketConfiguration={
                        'LocationConstraint': 'eu-west-1'
                    }
                )
            except ClientError:
                pass

    # TODO: This needs to be able to handle pagination
    def list_jobs(self):
        job_ids = []
        if self.vendor == 'AWS':
            response = self.client.list_objects(
                Bucket=settings.PERSISTENT_STORAGE_BUCKET_NAME
            )
            if response.get('Contents'):
                job_ids = [content['Key'].strip('.tar.gz') for content in response['Contents']]
        return job_ids

    def save_job(self, job_instance):
        """ Compress job files, and upload it to the bucket
        """
        # Compress the job folder
        job_file = "{}.tar.gz".format(str(job_instance.id))
        cmd = 'tar -czf {} {}'.format(
            job_file,
            job_instance.get_job_directory_path()
        )
        subprocess.call(cmd, shell=True)

        # Upload the job file
        self.client.upload_file(job_file,
                                settings.PERSISTENT_STORAGE_BUCKET_NAME,
                                job_file)

        # Delete compressed file
        cmd = 'rm {}'.format(job_file)
        subprocess.call(cmd, shell=True)

    def get_job(self, job_id):
        # Prepare job filename and instance
        job_id = uuid.UUID(job_id)
        job_file = "{}.tar.gz".format(str(job_id))
        job, created = Job.objects.get_or_create(id=job_id)

        # Download
        self.client.download_file(settings.PERSISTENT_STORAGE_BUCKET_NAME,
                                  job_file,
                                  job_file)

        # Uncompress
        cmd = 'tar -xzf {} '.format(job_file)
        subprocess.call(cmd, shell=True)

        # Delete compressed file
        cmd = 'rm {}'.format(job_file)
        subprocess.call(cmd, shell=True)

        # Link the appropriate instance attribute to the file
        job.sync_files()