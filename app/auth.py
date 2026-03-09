## JWT (JSON Web Token)
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

FAKE_TOKEN = "mysecrettoken"


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    
    if credentials.credentials != FAKE_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid token")

    return credentials.credentials

