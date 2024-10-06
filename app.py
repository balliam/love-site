from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store form submissions
submissions = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        submissions.append({'name': name, 'message': message})
        return redirect(url_for('home'))
    return render_template('home.html', submissions=submissions)

@app.route('/clear', methods=['POST'])
def clear_submissions():
    global submissions
    submissions = []
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)