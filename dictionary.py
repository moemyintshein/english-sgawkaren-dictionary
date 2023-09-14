from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Create a dictionary with word definitions (replace with your data)
dictionary = json.load(open("data.json"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the word entered by the user from the form
        word = request.form["word"].lower()

        # Look up the word in the dictionary
        definition = dictionary.get(word, "Word not found in the dictionary.")

        return render_template("index.html", word=word, definition=definition)
    
    return render_template("index.html", word=None, definition=None)

if __name__ == "__main__":
    app.run(debug=True)

