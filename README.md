# EmberFlow Queue

EmberFlow Queue is a lightweight in-memory message queue library for Python.

## Features

- **Redis backend**: persistent message backend via Redis.
- **SQS backend**: integration with Amazon Simple Queue Service.
- **Batch consumption**: consume many messages in a single call.
- **Dead-letter queue**: automatic retries and DLQ for failed messages.
- **At-least-once delivery**: messages are never silently lost.

## Requirements

- Python 3.9+
