from ..config import app, db
from ..forms.user_form import registerForm
from ..models.user import Demo_User
from werkzeug.security import generate_password_hash, check_password_hash

# @app.route('/register', methods=['POST'])
def register():
    form = registerForm()

    print(form.data)
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Demo_User(username=form.username.data,
                             first_name=form.first_name.data,
                             last_name=form.last_name.data,
                             email=form.email.data,
                             password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return "new user added"

    return "ERROR: User Not Added"


def home():
    return "home"
