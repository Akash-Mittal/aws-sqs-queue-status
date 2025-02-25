import boto3
import argparse
import json
import sys

def get_queues_message_totals(queue_names):
    try:
        sqs = boto3.client('sqs')
        results = {}
        for queue_name in queue_names:
            try:
                response = sqs.get_queue_url(QueueName=queue_name)
                print(f"Raw Response {response}")
                queue_url = response['QueueUrl']
                results[queue_name] = {"messages": get_queue_message_count(sqs, queue_url), "url": queue_url}
                get_deadletterqueue(sqs, results, queue_url)
            except Exception as exception:
                print(f"Error processing queue  {queue_name}: {exception}", file=sys.stderr)
                return None  
        return results

    except Exception as exception:
        print(f"General error: {exception}", file=sys.stderr)
        return None

def get_deadletterqueue(sqs, results, queue_url):
    attributes = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['RedrivePolicy'])
    if 'RedrivePolicy' in attributes['Attributes']:
        redrive_policy = json.loads(attributes['Attributes']['RedrivePolicy'])
        dlq_arn = redrive_policy['deadLetterTargetArn']
        dlq_name = dlq_arn.split(':')[-1] 
        dlq_url = sqs.get_queue_url(QueueName=dlq_name)['QueueUrl']
        results[dlq_name] = {"messages": get_queue_message_count(sqs, dlq_url), "url": dlq_url}


def get_queue_message_count(sqs, queue_url):
    """Gets the approximate number of messages in a queue."""
    try:
      attributes = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['ApproximateNumberOfMessages'])
      return int(attributes['Attributes']['ApproximateNumberOfMessages'])
    except Exception as e:
      print(f"Error getting message count for {queue_url}: {e}", file=sys.stderr)
      return 0  



def print_results(results):
    """Prints the queue message totals to stdout."""

    if results:
      for queue_name, data in results.items():
          print(f"Queue: {queue_name}")
          print(f"  - Messages: {data['messages']}")
    else:
        print("No queues processed.", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get SQS queue message totals.")
    parser.add_argument('queues', nargs='+', help='List of SQS queue names')
    args = parser.parse_args()

    queue_names = args.queues
    results = get_queues_message_totals(queue_names)

    if results:
      print_results(results)