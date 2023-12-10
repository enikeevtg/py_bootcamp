import common as com
import argparse
import redis
import json
import logging as log


log.basicConfig(level=log.INFO, format="\
%(asctime)s - %(levelname)s: %(message)s")


def get_args() -> list:
    parser = argparse.ArgumentParser(description="consumer: receiving an\
argument with a list of account numbers")
    parser.add_argument("-e",
                        "--accounts",
                        required=False,
                        type=str,
                        default=com.default_bad_guys,
                        help="provide a list of bad guys\' account numbers\
                          default=" + str(com.default_bad_guys))
    return parser.parse_args().accounts.split(',')


def messages_processing(bad_guys_list: list) -> None:
    redis_client = redis.Redis(host="localhost", port=com.port, db=com.db)
    sub = redis_client.pubsub()
    sub.subscribe(com.channel_name)

    for message in sub.listen():
        if message['type'] == "message":
            data = message['data']
            parsed_message = json.loads(data)
            log.info(f"received data: {parsed_message}")
            sender = parsed_message['metadata']['from']
            receiver = parsed_message['metadata']['to']
            amount = parsed_message['amount']
            if str(receiver) in bad_guys_list and amount >= 0:
                parsed_message['metadata']['from'] = receiver
                parsed_message['metadata']['to'] = sender
                log.info(f"modifyed data: {parsed_message}")

    redis_client.close()


def main():
    bad_guys = get_args()
    args_check = True
    for el in bad_guys:
        if el.isdigit() is False or len(el) != 10:
            args_check = False

    if args_check is True:
        messages_processing(bad_guys)
    else:
        print("incorrect element(s) of bad guys' account numbers list")


if __name__ == "__main__":
    main()
