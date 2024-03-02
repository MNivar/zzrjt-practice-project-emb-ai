''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, request, render_template
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app : TODO
app = Flask(__name__)
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """
    Analyzes the sentiment of the given text.

    Parameters:
    text_to_analyse (str): Text to analyze.

    Returns:
    dict: A dictionary containing the sentiment label and score.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)
    label = response['label']
    score = response['score']
    if label is None:
        return "Invalid input ! Try again."
    return f"The given text has been identified as {label.split('_')[1]} with a score of {score}."
@app.route("/")
def render_index_page():
    """

    renders page

    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
