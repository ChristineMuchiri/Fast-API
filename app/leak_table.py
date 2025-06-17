import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table("Leaks") # type: ignore

def save_leak(description, media_url=None, type="text"):
    leak_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()
    
    item = {
        "leak_id": leak_id,
        "description": description,
        "type": type,
        "media_url": media_url or "",
        "timestamp": timestamp,
    }
    
    table.put_item(Item=item)
    return item

def get_all_leaks():
    response = table.scan()
    return response.get("Items", [])