from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def home_page():
    """Returns the homepage"""

    return render_template('questions.html',
                           prompts=silly_story.prompts)


@app.get("/results")
def results_page():
    """Returns the result page"""

    story = silly_story.get_result_text(request.args)
    return render_template("results.html",
                           interpolated_story=story)