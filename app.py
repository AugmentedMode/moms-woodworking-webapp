from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # if profile_image:
        #     filename = secure_filename(profile_image.filename)
        #     filename = str(session['id']) + '-' + filename
        #     profile_image.save(os.path.join(app.config['PROFILE_UPLOAD_FOLDER'], filename))
        #
        #
        # functions.update_profile(username, user_email, user_bio, session['id'], filename)
        print(title)
        print(description)
        #return redirect('/')
        #return render_template('home.html')
    return render_template('home.html')
