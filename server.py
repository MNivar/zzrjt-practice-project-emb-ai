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
    text_to_analyze = request.form["textToAnalyze"]
    result = sent_analyzer(text_to_analyze)

    # return render index with the result this would be for a POST?


@app.route("/")
def render_index_page():
    return render_template("index.html")
    

if __name__ == "__main__":
   app.run(debug=True)
