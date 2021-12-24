"""
This code snipert contains code
of stepfunction dynamodb connector
to update items in dynamodb table
"""

{
  "TableName": "students",
  "Key": {
    "id": {
      "S.$": "$.id"
    }
  },
  "UpdateExpression": "SET fullname = :fullname, age = :age",
  "ExpressionAttributeValues": {
    ":fullname": {
      "S.$": "$.fullname"
    },
    ":age": {
      "S.$": "$.age"
    }
  }
}