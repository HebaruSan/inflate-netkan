import boto3
from os import environ
from git import Repo
from exitstatus import ExitStatus
import logging

from netkan.repos import CkanMetaRepo
from netkan.common import netkans, sqs_batch_entries


def inflate_netkan() -> None:
    messages = (nk.sqs_message(CkanMetaRepo(Repo('CKAN-meta')).highest_version(nk.identifier))
                for nk in netkans('NetKAN', [environ['INPUT_IDENTIFIER']]))
    for batch in sqs_batch_entries(messages):
        logging.info(f'Queueing inflation request batch: {batch}')
        boto3.client('sqs').send_message_batch(
            QueueUrl=boto3.resource('sqs').get_queue_by_name(QueueName='Inbound.fifo').url,
            Entries=batch
        )
    exit(ExitStatus.success)
