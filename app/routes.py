# app/routes.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import News, Category, User
from sqlalchemy import or_

main = Blueprint('main', __name__)


@main.route('/feed')
@login_required
def feed():
    # Example logic for personal feed based on categories user has interacted with
    preferences = current_user.preferences.split(',') if current_user.preferences else []
    news_feed = News.query.filter(
        or_(News.category.has(name=category) for category in preferences)
    ).order_by(News.date_posted.desc()).all()

    return render_template("feed.html", news_feed=news_feed)
