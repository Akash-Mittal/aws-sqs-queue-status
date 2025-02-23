# aws-sqs-queue-status
Python project with boto3 library to fetch and display the current number of items in one or more SQS queues and their dead letter queues.

```markdown
# SQS Queue Message Counter

This Python script uses the `boto3` library to fetch and display the current number of items (messages) in one or more SQS queues and their associated dead-letter queues (DLQs).

## Script Specifications

The script is named `sqs_queues.py` and contains the core function `get_queues_message_totals(queues: List)`.  It's designed to be used both directly from the command line and imported as a module.

## Installation

```bash
pip install boto3  # Ensure you have boto3 installed (version 1.16+ recommended)
```

## Usage

### Command Line

```bash
python sqs_queues.py queue-1 queue-2 queue-3 ...
```

Where `queue-1`, `queue-2`, `queue-3`, etc., are the names of your SQS queues.

**Example:**

```bash
python sqs_queues.py my-queue-1 my-queue-2
```

### Import

```python
from sqs_queues import get_queues_message_totals

queue_names = ["my-queue-1", "my-queue-2"]
message_counts = get_queues_message_totals(queue_names)
print(message_counts) # Or process the returned data as needed
```

## Output

### Command Line

The script outputs a list of SQS queues and their dead-letter queues with the number of messages in each queue to `stdout`. Any errors are printed to `stderr`.

**Example:**

```
Queue: my-queue-1
  - Messages: 10
DLQ: my-queue-1-dlq
  - Messages: 5
Queue: my-queue-2
  - Messages: 20
DLQ: my-queue-2-dlq
  - Messages: 0
```

### Import

The `get_queues_message_totals()` function returns a data structure (a dictionary) containing the queue names and their message counts.

**Example:**

```python
{
    "my-queue-1": {"messages": 10},
    "my-queue-1-dlq": {"messages": 5},
    "my-queue-2": {"messages": 20},
    "my-queue-2-dlq": {"messages": 0},
}
```

## Extra Credit Features

### JSON Output

To get the output in JSON format, use the `--json` flag:

```bash
python sqs_queues.py --json queue-1 queue-2 queue-3 ...
```

### Packaging and `-m` invocation

The project is packaged to allow invocation using `python -m`:

```bash
python -m sqs_queues queue-1 queue-2 queue-3 ...
python -m sqs_queues --json queue-1 queue-2 ... #With JSON output
```

To install the package locally for development:

```bash
pip install -e .
```

## Testing

The `moto` library can be used for testing. Install it using:

```bash
pip install moto
```

You can then run the tests (if included in the project) using a testing framework like `pytest`:

```bash
pip install pytest
pytest
```

## Python Version

The module is compatible with Python 3.8 and later.

## Dependencies

* `boto3` (version 1.16+ recommended)

## File Structure

```
sqs_queues/
├── sqs_queues.py  # The main script
├── __init__.py  # Makes sqs_queues a package
└── README.md      # This file
```

## Git History

The project includes a `.git` folder with the commit history.

## Author

[Your Name]

## License

[Your License (e.g., MIT)]
```

This is the content for a *single* `README.md` file.  Just copy and paste this into a file named `README.md` in the root directory of your project.  Remember to replace `[Your Name]` and `[Your License]` with your actual information.
