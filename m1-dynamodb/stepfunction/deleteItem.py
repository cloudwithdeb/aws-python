"""
This code sniperts help us to
delete data from dynamodb using
stepfunction dynamodb connector.
"""

{
  "TableName": "students",
  "Key": {
    "id": {
      "S.$": "$.id"
    }
  }
}