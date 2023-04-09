import boto3
from os import environ
from git import Repo
from exitstatus import ExitStatus
import logging

from netkan.repos import CkanMetaRepo
from netkan.common import netkans, sqs_batch_entries


GAME_QUEUE_NAMES = {
    'ksp':  'Inbound.fifo',
    'ksp2': 'InboundKsp2.fifo',
}

def inflate_netkan() -> None:
    game_id = environ['INPUT_GAME_ID']
    messages = (nk.sqs_message(CkanMetaRepo(Repo('CKAN-meta')).highest_version(nk.identifier))
                for nk in netkans('NetKAN', [environ['INPUT_IDENTIFIER']], game_id))
    for batch in sqs_batch_entries(messages):
        logging.info(f'Queueing inflation request batch: {batch}')
        boto3.client('sqs').send_message_batch(
            QueueUrl=boto3.resource('sqs').get_queue_by_name(
                QueueName=GAME_QUEUE_NAMES[game_id]).url,
            Entries=batch)
    exit(ExitStatus.success)
