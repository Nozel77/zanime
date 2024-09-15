from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.security.jwt import get_current_user

def admin_required(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have the necessary permissions"
        )
    return current_user