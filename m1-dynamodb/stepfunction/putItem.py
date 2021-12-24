"""
This code sniperts help us to
add/save data into dynamodb using
stepfunction dynamodb connector.
"""

#A FUNCTION TO ADD DATA INTO DYNAMODB
#TABLE USING AWS STEPFUNCTION DYNAMODB
#CONNECTOR

{
  "TableName": "students",
  "Item": {
    "id": {
      "S.$": "$.id"
    },
    "fullname": {
      "S.$": "$.fullname"
    },
    "scores": {
      "M.$": "$.scores" #For map items
    },
    "classes": {
      "L.$": "$.classes" #For list items
    }
  }
}