import logging

from tasktiger import Task

from src.apps.read_model.key_value.common import get_read_model_name
from src.libs.job_utils.shared_tiger_connection import get_shared_tiger_connection
from src.libs.key_value_utils.key_value_provider import get_key_value_client

logger = logging.getLogger(__name__)


def process_items_for_job(job_key, item_id):
  kdb = get_key_value_client()

  ret_val = kdb.sadd(get_read_model_name('job_processed_items:{0}', job_key), item_id)

  return ret_val


def get_processed_items_for_job(job_key):
  kdb = get_key_value_client()

  ret_val = kdb.smembers(get_read_model_name('job_processed_items:{0}', job_key))

  return ret_val


def provide_journal_items_for_job(job_key, item_ids):
  kdb = get_key_value_client()

  ret_val = kdb.sadd(get_read_model_name('job_journal_items:{0}', job_key), *item_ids)

  return ret_val


def get_journaled_items_for_job(job_key):
  kdb = get_key_value_client()

  ret_val = kdb.smembers(get_read_model_name('job_journal_items:{0}', job_key))

  return ret_val


def retry_tasks(queue='default', state='error'):
  tiger = get_shared_tiger_connection()
  n, tasks = Task.tasks_from_queue(tiger, queue, state)
  for task in tasks:
    try:
      task.retry()
    except:
      logger.warning('Error retrying job: %s', task, exc_info=True)

  return n
