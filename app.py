from flask import Flask, request, jsonify
from complete import complete_sentence
from csvparser import get_words

app = Flask(__name__)

@app.route('/autocomplete', methods=["POST"])
def autocomplete():
    train_data = get_words("data.csv")
    search_phrase = request.json['search_phrase']
    final_output = complete_sentence(search_phrase, train_data)
    return jsonify(final_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9009)