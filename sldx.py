import boto3
import json


bedrock=boto3.client(service_name="bedrock-runtime")
prompt = "Sri lanka tea plantation."
payload={
    "text_prompts": [{"text":prompt,
                      "weight":1}],
                    "cfg_scale":10,
                    "seed":0,
                    "steps":50,
                    "width":1024,
                    "height":1024
}
body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"
response=bedrock.invoke_model(
    'batchRequestId': "e37d82c8-e2c9-4145-97ab-31f901f35cf1",
    'status': "SUCCESS")

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)