from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turn_on', methods=['POST'])
def turn_on_led():
    with open("command.txt", "w") as file:
        file.write("ON")
    return redirect(url_for('index'))

@app.route('/turn_off', methods=['POST'])
def turn_off_led():
    with open("command.txt", "w") as file:
        file.write("OFF")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=7800)
