from flask import g, jsonify
from flask import request
from app.models import User
from app.mobile_register import mobile_register
from app import db
import json


@mobile_register.route('/register/', methods=['POST'])
def register():
    if request.method == 'POST':

        if request.json:
            form = request.json
        else:
            form = request.data.decode('utf8')
            form = json.loads(form)

        try:
            if not (form.get("email") and form.get("username") and form.get("password")):
                return jsonify({"email": form.get("email"), "username": form.get("username"),
                                "password": form.get("password"), "state": "User register failed.",
                                "form": form})
        except AttributeError as e:
            return jsonify({"state": "Wrong data as {}".format(form)})

        user = User(email=form.get("email"),
                    username=form.get("username"),
                    password=form.get("password"),
                    confirmed=True)
        db.session.add(user)
        db.session.commit()
        return jsonify({"email": form.get("email"), "username": form.get("username"),
                        "state": "success"})

    return jsonify({"state": "User register failed."})
