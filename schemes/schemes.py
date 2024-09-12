"""Схемы API для валидации"""

valid_announcement_single_non_exist = {
    "type": "object",
    "properties": {
        "result": {
            "type": "object",
            "properties": {
                "message": {"type": "string"},
                "messages": {"type": "null"},
            },
            "required": ["message", "messages"]
        },
        "status": {"type": "string"},
    },
    "required": ["status"]
}

valid_announcement_single_exist = {
    "type": "object",
    "properties": {
        "createdAt": {"type": "string"},
        "id": {"type": "string"},
        "name": {"type": "string"},
        "price": {"type": "number"},
        "sellerId": {"type": "number"},
        "statistics": {
            "type": "object",
            "properties": {
                "contacts": {"type": "number"},
                "likes": {"type": "number"},
                "viewCount": {"type": "number"}
            },
            "required": ["contacts", "likes", "viewCount"]
        },
    },
    "required": ["createdAt", "id", "name", "price", "sellerId", "statistics"]
}

valid_post_announcement = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "price": {"type": "number"},
        "sellerId": {"type": "number"},
        "statistics": {
            "contacts": {"type": "number"},
            "like": {"type": "number"},
            "viewCount": {"type": "number"}
        },
    },
    "required": ["name", "price", "sellerId"]
}