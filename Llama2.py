import boto3
import json

client = boto3.client('bedrock-runtime')

messages= [
      {
        "role": "user",
        "content": [
          {
            "text": "[INST]You are a very intelligent bot with exceptional language skills[/INST]\nA \"lemurwhat\" is a small, furry animal native to Tanzania. An example of a sentence that uses\nthe word lemurwhat is:\nWe were traveling in Africa and we saw these very cute lemurwhats\nTo do a \"cuteduddle\" means to jump up and down really fast. An example of a sentence that uses\nthe word cuteduddle is:"
          }
        ]
      }
    ]
inferenceConfig= {"maxTokens": 512, "temperature": 0.5, "topP": 0.9}
response=client.converse_stream(
    messages=messages,
    modelId='meta.llama2-70b-chat-v1',
    inferenceConfig=inferenceConfig,
    additionalModelRequestFields={}
)

response_body=json.loads(response.get("body").read())
repsonse_text=response_body['generation']
print(repsonse_text)
