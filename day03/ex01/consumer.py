import common as com


def get_args() -> list:
    parser = com.ArgumentParser(description="consumer: receiving an\
                                argument with a list of account numbers")
    parser.add_argument("-e",
                        "--accounts",
                        type=str,
                        default=com.default_bad_guys,
                        help="provide a list of bad guys\' account numbers\
                          default=" + str(com.default_bad_guys))
    return parser.parse_args().accounts.split(',')


def messages_processing(bad_guys_list: list) -> None:
    redis_client = com.Redis(host="localhost", port=com.port, db=com.db)
    sub = redis_client.pubsub()
    sub.subscribe(com.channel_name)

    for message in sub.listen():
        if message['type'] == "message":
            data = message['data']
            parsed_message = com.json.loads(data)
            sender = parsed_message['metadata']['from']
            receiver = parsed_message['metadata']['to']
            amount = parsed_message['amount']
            if str(receiver) in bad_guys_list and amount >= 0:
                parsed_message['metadata']['from'] = receiver
                parsed_message['metadata']['to'] = sender
            print(parsed_message)

    redis_client.close()


def main():
    bad_guys = get_args()
    args_check = True
    for el in bad_guys:
        if el.isdigit() is False:
            args_check = False

    if args_check == True:
        messages_processing(bad_guys)
    else:
        print("incorrect element(s) list of bad guys' account numbers")


if __name__ == "__main__":
    main()
