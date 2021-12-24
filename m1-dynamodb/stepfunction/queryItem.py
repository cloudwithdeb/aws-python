"""
This code snipert contains code
of stepfunction dynamodb connector
to query and retrieve data from dynamodb.
"""

{
  "TableName": "students",
  "Limit": 1,
  "ConsistentRead": "true",
  "ProjectionExpression": "id, scores, fullname",
  "KeyConditionExpression": "id = :v1",
  "FilterExpression": "age = :v2 AND fullname = :v3",
  "ExpressionAttributeValues": {
    ":v1": {
      "S.$": "$.id"
    },
    ":v2": {
      "S.$": "$.age"
    },
    ":v3": {
      "S.$": "$.fullname"
    }
  },
  "ReturnConsumedCapacity": "TOTAL"
}