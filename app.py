from flask import Flask, request, jsonify
from complete import complete_sentence
from csvparser import get_words

app = Flask(__name__)

@app.route('/storyline', methods=["POST"])
def autocomplete():
    train_data = get_words("data_storyline.csv")
    search_phrase = request.json['search_phrase']
    final_output = complete_sentence(search_phrase, train_data)
    return final_output.to_json()

@app.route('/cause', methods=["POST"])
def cause():
    train_data = get_words("data_cause.csv")
    search_phrase = request.json['search_phrase']
    final_output = complete_sentence(search_phrase, train_data)
    return final_output.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9009)