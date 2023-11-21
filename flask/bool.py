from flask import Flask, render_template, request
import os.path


app = Flask(__name__)

@app.route('/')
def home():
    thing = request.args.get("thing")
    height = request.args.get("height")
    color = request.args.get("color")
    print(thing, color, height)
    return render_template('''<html>
<head>
    <title>It's alive</title>
</head>
<body>
I'm of course reffering to {{thing}}, whick is {{height}} feet tail and {{color}}.
</body>
</html>''', color=color, height=height, thing=thing)

app.run(debug=True)