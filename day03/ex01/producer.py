import common as com
import time


def get_args() -> int:
    parser = com.ArgumentParser(description="producer.py: generate JSON\
      messages and put them as a payload into a Redis pubsub queue")
    parser.add_argument("--mode", type=int, default=0, help="type=int.\
      Positive mode provides account numbers number for random generating;\
      nill mode provides default accounts genereting; negative mode provides\
      infinite cycle of messages pushing (default=0)")
    return parser.parse_args().mode


def gen_account() -> int:
    return com.random.randint(com.min_account, com.max_account)


def gen_amount() -> int:
    return com.random.randint(com.min_amount, com.max_amount)


def gen_message():
    return {
        "metadata": {
            "from": gen_account(),
            "to": gen_account()
          },
        "amount": gen_amount()
      }


def continuous_messaging() -> None:
    redis_client = com.Redis(host=com.hostname, port=com.port, db=com.db,
                             decode_responses=True)
    redis_client.flushall()

    while True:
        message = com.json.dumps(gen_message())
        redis_client.publish(com.channel_name, str(message))
        time.sleep(1)


def gen_messages_list(messages_number: int) -> list:
    messages_list = []
    if messages_number > 0:
        for i in range(messages_number):
            messages_list.append(com.json.dumps(gen_message()))
    else:
        messages_list.append(com.json.dumps(com.mess_1))
        messages_list.append(com.json.dumps(com.mess_2))
        messages_list.append(com.json.dumps(com.mess_3))
    return messages_list


def publicate_messages_list(messages_list: list) -> None:
    redis_client = com.Redis(host=com.hostname, port=com.port, db=com.db,
                             decode_responses=True)
    redis_client.flushall()
    for message in messages_list:
        redis_client.publish(com.channel_name, str(message))
    redis_client.close()


def main():
    messages_number = get_args()
    if messages_number < 0:
        continuous_messaging()
    else:
        messages_list = gen_messages_list(messages_number)
        # for message in messages_list:
        #     print(str(message))
        publicate_messages_list(messages_list)


if __name__ == "__main__":
    main()
