from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return redirect(url_for('thank_you', name=name))  
    return render_template('contact.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form.get('feedback')
        # Process the feedback (e.g., save to a database)
        return redirect(url_for('thank_you', name='User')) 
    return render_template('feedback.html')


@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Guest')
    return f"Thank you, {name}! Your message has been received."

if __name__ == '__main__':
    app.run(debug=True)
