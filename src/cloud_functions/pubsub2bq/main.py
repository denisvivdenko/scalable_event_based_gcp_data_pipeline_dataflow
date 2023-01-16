from google.cloud import bigquery

import pandas as pd
import base64
import io


def pubsub2bq(event, context):
     """
     Triggered from a message on a Cloud Pub/Sub topic.
     Args:
          event (dict): Event payload.
          context (google.cloud.functions.Context): Metadata for the event.
     """
     bq_client = bigquery.Client()
     dataset_id = "health"
     table_id = "covid_stream"
     table_ref = bq_client.dataset(dataset_id).table(table_id)
     table = bq_client.get_table(table_ref)
     
     pubsub_message = base64.b64decode(event["data"]).decode("utf-8")

     dataframe = pd.read_csv(io.StringIO(pubsub_message))
     print(dataframe)
     errors = bq_client.insert_rows(table, [tuple(row) for row in dataframe.values])
     if errors:
          raise Exception(f"Failed to insert rows to bq. {errors}")