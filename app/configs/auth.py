from flask import current_app
from flask_httpauth import HTTPTokenAuth
from sqlalchemy.orm import Session
from app.models.user_model import UserModel


auth = HTTPTokenAuth()


@auth.verify_token
def verify_token(api_key: str):
    session: Session = current_app.db.session

    user = session.query(UserModel).filter_by(api_key=api_key).first()

    return user