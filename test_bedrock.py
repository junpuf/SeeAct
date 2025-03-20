
import os
import boto3

MODEL_ID = "arn:aws:bedrock:us-west-2:your bedrock model arn"
IMAGE_NAME = "dog.jpeg"
IMAGE_FORMAT = IMAGE_NAME.split(".")[-1]

bedrock_runtime = boto3.client("bedrock-runtime", 
                               aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"], 
                               aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"], 
                               aws_session_token=os.environ["AWS_SESSION_TOKEN"])

with open(IMAGE_NAME, "rb") as f:
    image = f.read()

user_message = "What's in the image?"

messages = [
    {
        "role": "user",
        "content": [
            {"image": {"format": IMAGE_FORMAT, "source": {"bytes": image}}},
            {"text": user_message},
        ],
    }
]

response = bedrock_runtime.converse(
    modelId=MODEL_ID,
    messages=messages,
)
response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)