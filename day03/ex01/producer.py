import common as com


def get_args() -> int:
    parser = com.ArgumentParser(description="producer.py: generate JSON\
      messages and put them as a payload into a Redis pubsub queue")
    parser.add_argument("--rand", type=int, default=0, help="type=int. Provide\
      account numbers number for random generating (default=0)")
    return parser.parse_args().rand


def gen_account() -> int:
    return com.random.randint(com.min_account, com.max_account)
    
    
def gen_amount() -> int:
    return com.random.randint(com.min_amount, com.max_amount)


def gen_messages(messages_number: int) -> list:
    messages_list = []
    if messages_number > 0:
        for i in range(messages_number):
            message = {
                "metadata": {
                    "from": gen_account(),
                    "to": gen_account()
                  },
                "amount": gen_amount()
              }
            messages_list.append(com.json.dumps(message))
    else:
        messages_list.append(com.json.dumps(com.mess_1))
        messages_list.append(com.json.dumps(com.mess_2))
        messages_list.append(com.json.dumps(com.mess_3))
    return messages_list


def publicate_messages(messages_list: list) -> None:
    redis_client = com.Redis(host="localhost", port=com.port, db=com.db, decode_responses=True)
    redis_client.flushall()
    for message in messages_list:
        redis_client.publish(com.channel_name, str(message))
    redis_client.close()


def main():
    messages_number = get_args()
    messages_list = gen_messages(messages_number)
    for message in messages_list:
        print(str(message))
    publicate_messages(messages_list)


if __name__ == "__main__":
    main()
