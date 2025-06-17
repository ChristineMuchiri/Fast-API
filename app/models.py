from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Leak(BaseModel):
    description: str
    type: Optional[str] = "text"
    media_url: Optional[str] = None
    timestamp: Optional[str] = datetime.utcnow().isoformat()
    
