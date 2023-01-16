import configparser
import argparse
import pandas as pd
import logging

from google.cloud import pubsub_v1
from google.oauth2.service_account import Credentials


def publish_data(publisher: pubsub_v1.PublisherClient, topic_name: str, data_path: str, chunksize: int = 1000, max_chunks: int = 5) -> None:
    for chunk_count, data_chunk in enumerate(pd.read_csv(data_path, chunksize=chunksize)):
        if chunk_count >= max_chunks:
            break

        data = data_chunk.to_csv(index=False).encode()
        future = publisher.publish(topic=topic_name, data=data)

        try:
            message_id = future.result()
        except Exception as e:
            print(f"Failed to publish chunk {chunk_count}. {e}")
        else:
            print(f"Succesfuly published chunk {chunk_count}. Message id {message_id}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Google cloud config file.")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)

    credentials_path = config.get("gcp", "credentials")
    credentials = Credentials.from_service_account_file(credentials_path)

    publisher = pubsub_v1.PublisherClient(credentials=credentials)
    publish_data(publisher=publisher, topic_name=config.get("pubsub", "topic_name"), data_path=config.get("data", "covid_data_path"), chunksize=1, max_chunks=5)

