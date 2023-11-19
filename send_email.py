from google.cloud import pubsub_v1
import json
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./primeval-alloy-383019-66a5b359fa11.json"
project_id = "primeval-alloy-383019"
topic_name = "application-status-email"


def publish_to_pubsub(project_id, topic_name, message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    message_data = json.dumps(message).encode('utf-8')

    future = publisher.publish(topic_path, data=message_data)
    print(f"Published message '{message}' to {topic_path}")

    future.result()


def publish(to, subject, body):
    message = {"to": to,
               "subject": subject,
               "body": body}
    publish_to_pubsub(project_id, topic_name, message)


def publish_json(message):
    publish_to_pubsub(project_id, topic_name, message)


if __name__ == "__main__":
    message = {
        "to": "dz2506@columbia.edu",
        "subject": "On python",
        "body": "This is the email body content."
    }

    publish_to_pubsub(project_id, topic_name, message)
