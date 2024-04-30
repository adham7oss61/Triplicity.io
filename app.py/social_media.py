from flask import Flask
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_dance.contrib.instagram import make_instagram_blueprint

app = Flask(_Socialmedia_)
os.environ.get('FLASK_SECRET_KEY')

google_blueprint = make_google_blueprint(
    client_id="your-google-client-id",
    client_secret="your-google-client-secret",
    scope=["profile", "email"]
)
facebook_blueprint = make_facebook_blueprint(
    client_id="your-facebook-client-id",
    client_secret="your-facebook-client-secret",
    scope=["email"]
)
instagram_blueprint = make_instagram_blueprint(
    client_id="your-instagram-client-id",
    client_secret="your-instagram-client-secret",
    scope=["user_profile", "user_media"]
)

app.register_blueprint(google_blueprint, url_prefix="/login")
app.register_blueprint(facebook_blueprint, url_prefix="/login")
app.register_blueprint(instagram_blueprint, url_prefix="/login")             Create a login route that redirects the user to the appropriate social media login page:                                                                                               @app.route("/login")
def login():
    return redirect(url_for("google.login"))                                                           Create a callback route that handles the OAuth response and logs the user in:                                                                                                        @app.route("/login/callback")
@google.authorized_handler
@facebook.authorized_handler
@instagram.authorized_handler
def authorized(blueprint):
    resp = blueprint.authorized_response()
    if resp is None:
        return "Access denied: reason=%s error=%s" % (
            request.args["error_reason"],
            request.args["error_description"]
        )
    session["access_token"] = (resp["access_token"], "")
    me = blueprint.get("/me").data
    return "Logged in as %s" % me["name"]                                                        Create a logout route that logs the user out and revokes their access token:                                                                                                                @app.route("/logout")
def logout():
    for blueprint in [google_blueprint, facebook_blueprint, instagram_blueprint]:
        if "access_token" in session:
            blueprint.revoke(session["access_token"])
    session.pop("access_token", None)
    return "Logged out"                                                                                        Create a share route that allows the user to share their bookings and reviews with their friends and followers:                                                            @app.route("/share")
@login_required
def share():
    # Get the user's bookings and reviews from the database
    bookings = Booking.query.filter_by(user_id=current_user.id).all()
    reviews = Review.query.filter_by(user_id=current_user.id).all()

    # Render a template that displays the bookings and reviews and allows the user to share them on social media
    return render_template("share.html", bookings=bookings, reviews=reviews)                                                                                                  In the share.html template, use the appropriate social media sharing buttons to allow the user to share their bookings and reviews. For example, to share on Facebook, you can use the following code:                <a href="https://www.facebook.com/sharer/sharer.php?u={{ url_for('booking', booking_id=booking.id) }}" target="_blank></a>
