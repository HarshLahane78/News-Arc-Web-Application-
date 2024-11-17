# app/notifications.py
import requests
from flask import current_app
from models import User


def get_user_fcm_token(user_id):
    # Assuming you have some way to get the Firebase Cloud Messaging token for the user
    # Replace this with actual logic to fetch the token from your database or user model
    user = User.query.get(user_id)
    return user.fcm_token if user else None

def send_notification(user_id, message):
    fcm_token = get_user_fcm_token(user_id)  # Assume a function to retrieve FCM token
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        "Authorization": "key=YOUR_FCM_SERVER_KEY",
        "Content-Type": "application/json"
    }
    payload = {
        "to": fcm_token,
        "notification": {
            "title": "News Arc",
            "body": message
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        current_app.logger.info(f"Notification sent to user {user_id}")
    else:
        current_app.logger.error("Failed to send notification")
