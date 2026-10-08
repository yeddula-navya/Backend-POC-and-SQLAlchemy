from typing import Any
def create_response(
    status: int,
    message: str,
    data: Any = None
):
    return {
        "status": status,
        "message": message,
        "data": data
    }