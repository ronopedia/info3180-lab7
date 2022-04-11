"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from sqlalchemy import false
from app import app
from flask import render_template, request, jsonify, send_file, flash
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
import os

from .forms import UploadForm
from .config import Config

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

""" @app.route('/api/upload', methods=['POST'])
def upload():
     # Instantiate your form class
    form = UploadForm()

    # Validate file upload on submit
    if request.method == 'POST':
        if form.validate_on_submit():
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            tasks = {
                tasks: [
                    {'message': 'File Upload Successful'},
                    {'filename': filename},
                    {'description': form.description.data}
                ]
            }
            return jsonify(tasks=tasks), 202
        else:
            errors= {
                "errors": [
                    {'success': False},
                    {'errors': form_errors()}
                ]
            }
            return jsonify (errors=errors), 403 """

@app.route('/api/upload', methods=['POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit() == True:
            description = request.form['description']
            file = request.files['photo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File Uploaded Succesfully','sucessful')
            return jsonify({"message": "File Upload Successful", "filename": filename, "description": description})
    else:
        return jsonify({"errors":[{"filename": form_errors(form)}]})


@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")