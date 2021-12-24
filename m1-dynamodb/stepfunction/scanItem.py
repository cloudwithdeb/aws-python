"""
This code snipert contains code
of stepfunction dynamodb connector
to scan and retrieve data from dynamodb.
"""

#A FUNCTION TO SCAN TO RETRIEVE DATA FROM DYNAMODB
#TABLE USING STEPFUNCTION DYNAMODB CONNECTOR

#Note:
    #(0). This function cant be used but you should copy
    #And paste the code into a stepfunction state machine
    #and change the parameters to what you wont.
    #(1). Remove the quotes form true in ConsistentRead


#Inside filter expression, you can add the following
#FilterExpression: "age = :val AND age = :val2 OR 
# age = :val3 AND :age BETWEEN :val4 AND :val5"

{
    "TableName": "users",
    "FilterExpression": "age = :val",
    "ExpressionAttributeValues": {
      ":val": {
        "S.$": "$.age"
      }
    },
    "ConsistentRead": "true",
    "ProjectionExpression": "age, fullname, contact"
}