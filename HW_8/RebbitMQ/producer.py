import pika
import json
from seed import seed_contacts


credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
)
channel = connection.channel()

channel.exchange_declare(exchange="task_mock", exchange_type="direct")
channel.queue_declare(queue="task_queue", durable=True)
channel.queue_bind(exchange="task_mock", queue="task_queue")


def main():
    contacts = seed_contacts()
    for i in range(len(contacts)):
        obj_id = contacts[i].id
        channel.basic_publish(
            exchange="task_mock",
            routing_key="task_queue",
            body=json.dumps(str(obj_id)).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        print(" [x] Sent %r" % obj_id)
    connection.close()


if __name__ == "__main__":
    main()
