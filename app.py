import flask
from flask import request
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing.text import Tokenizer

app = flask.Flask(__name__)

def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    keras.backend.get_session().run(tf.local_variables_initializer())
    return auc

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('natgeo.h5', custom_objects={'auc': auc})


# define a predict function as an endpoint 
@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}
    # get the request parameters
    
    req_data = request.get_json()
    text = req_data['text']
    #print(text)
    tokenizer = Tokenizer(num_words=45000)
    tokenizer.fit_on_texts([text])
    x = tokenizer.texts_to_matrix([text], mode='tfidf')
    #print(x.shape)
    #print(x)
    with graph.as_default():
        y = model.predict(x)
        #print(y.shape)
        if (y[0][0] < 0.70):
            data["prediction"] = "release"
            
        else:
            data["prediction"] = "contract"
        data["success"] = True
        data["confidence"] = str(y[0][0])

    # return a response in json format 
    return flask.jsonify(data)   
# start the flask app, allow remote connections
app.run(host='0.0.0.0')
