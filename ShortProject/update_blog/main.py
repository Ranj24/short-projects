import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/dc68e844617681ac3322")
    all_posts= response.json()
    return render_template('index.html', blogs=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog/<blog_id>')
def get_blog(blog_id):
    response = requests.get(url="https://api.npoint.io/dc68e844617681ac3322")
    relevant_post = response.json()[int(blog_id)-1]
    return render_template('post.html', post=relevant_post)


if __name__ == '__main__':
    app.run(debug=True)