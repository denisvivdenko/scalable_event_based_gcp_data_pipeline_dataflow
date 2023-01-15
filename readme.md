# Building scalable Event Based GCP data pipeline using dataflow


![architecure](img/architecture.png)


## Dataset

Covid data


## Reasons to use Event Based design pattern:

1. Interoperability
2. Scalability
3. Serverless

## Process

1. Set up service account API on GCP

    A service account is a special kind of Google account that belongs to your application or service, rather than to an individual user. This allows you to limit the scope of the account's permissions and reduce the risk of accidental data breaches or misuse.

    - Enable IAM Service Account Credentials API
    - Add service account and give it "owner" role
    - Create key in JSON format

2. Install GCP SDK
    - run gcloud init
    - set current project

3. Pub/Sub

    Messaging service. Similar to Kafka. That can be used as middleware for event based ingestion and streaming data loads.
    - It can automaticaly scale.
    - Have low latency.

    Main concepts:
    1. Publisher >>> sends message >>> Topic 
    2. Subsriber >>> subscribe to >> Topic
    3. Subscription represents the stream of messages from a specific topic 
    4. Message (the combination of data and attributes)
    5. Message attribute (key-value pair that publisher sends can add to a message)

![pub/sub](img/pub_sub_flow.svg)

4. BigQuery

    DataWarehouse that offers batch streaming insertion capabilities and is integrated with Tensorflow.
    - Higly scalable
    - Cost-effective

    Data Studio quick visualization on top of Bigquery data
     