from datetime import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ui_agent"]

db.screenshots.insert_one({
    "screenshot_id": "screen_001",
    "file_path": "/screenshots/screen_001.png",
    "device_info": {
        "device_name": "Pixel 6",
        "os": "Android",
        "os_version": "13"
    },
    "timestamp": datetime.utcnow()
})

db.ui_dumps.insert_one({
    "screenshot_id": "screen_001",
    "ui_dump_format": "json",
    "parsed_elements": [
        {
            "element_id": "com.app:id/icon_settings",
            "text": None,
            "content_desc": "Settings",
            "bounds": [100, 50, 150, 100]
        }
    ]
}
)

db.query_logs.insert_one({
    "query_text": "Where is the settings icon?",
    "screenshot_id": "screen_001",
    "matched_element_id": "com.app:id/icon_settings",
    "bounding_box": [100, 50, 150, 100],
    "confidence_score": 0.92,
    "resolved_by": "vision_model",
    "timestamp": datetime.utcnow()
})

db.icon_artifacts.insert_one({
    "icon_name": "settings",
    "aliases": ["gear", "preferences", "config"],
    "image_path": "/icons/settings.png"
})


db.screenshots.create_index("screenshot_id", unique=True)
db.ui_dumps.create_index("screenshot_id")
db.query_logs.create_index("screenshot_id")

db.ui_dumps.create_index("parsed_elements.element_id")
db.query_logs.create_index("matched_element_id")

db.icon_artifacts.create_index("icon_name", unique=True)




