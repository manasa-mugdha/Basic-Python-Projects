''' 
Install the required dependencies by running pip install flask and pip install sqlite3 in your terminal.
Copy the code into a Python file, e.g., url_shortener.py.
Run the Python file using python url_shortener.py.
Access the URL provided in the terminal (usually http://127.0.0.1:5000) to open the web interface.
Enter a long URL and click the "Shorten" button.
The web interface will display the generated short URL.
Access the short URL in your browser, and you should be redirected to the original long URL.

'''


#code

from flask import Flask, redirect, render_template, request
import string
import random
import sqlite3

app = Flask(__name__)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def create_short_link(long_url):
    short_url = generate_short_url()

    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("INSERT INTO urls (short_url, long_url) VALUES (?, ?)", (short_url, long_url))
    conn.commit()
    conn.close()

    return short_url

def get_long_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_url=?", (short_url,))
    result = c.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = create_short_link(long_url)
        return render_template('index.html', short_url=short_url)
    else:
        return render_template('index.html')

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found."

if __name__ == '__main__':
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS urls (short_url TEXT, long_url TEXT)")
    conn.close()
    app.run()
