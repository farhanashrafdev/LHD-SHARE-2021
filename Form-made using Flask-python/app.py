from flask import Flask, render_template

app = Flask(__name__)

@app.route('/subscribe')
def subscribe():
    title = "Subscribe to the newsletter"
    return render_template("sub.html", title=title)
