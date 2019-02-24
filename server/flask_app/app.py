import numpy as np
import requests
from time import sleep
from keras.layers import Input, Embedding, Flatten, Dot
from keras.models import Model
from flask import Flask, request, jsonify

app = Flask(__name__)
model = None

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/train', methods=['POST'])
def train():
    global model
    d = request.json
    nb_users = d['nb_users']
    nb_items = d['nb_items']
    user_history = d['user_history']
    item_history = d['item_history']
    rating_history = d['rating_history']

    # Model
    user_id_input = Input(shape=[1], name='user')
    item_id_input = Input(shape=[1], name='item')

    embedding_size = 30
    user_embedding = Embedding(output_dim=embedding_size, input_dim=int(nb_users) + 1,
                               input_length=1, name='user_embedding')(user_id_input)

    item_embedding = Embedding(output_dim=embedding_size, input_dim=int(nb_items) + 1,
                               input_length=1, name='item_embedding')(item_id_input)

    user_vecs = Flatten()(user_embedding)
    item_vecs = Flatten()(item_embedding)

    y = Dot(axes=1)([user_vecs, item_vecs])

    model = Model(inputs=[user_id_input, item_id_input], outputs=y)

    model.compile(optimizer='adamax', loss='mean_squared_error')

    # Training the model
    history = model.fit([user_history, item_history], rating_history,
                        batch_size=64, epochs=20, validation_split=0.1,
                        shuffle=True)
    
    return('Model training complete.')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    global model
    user = request.args.get('user')
    item = request.args.get('item')
    prediction = model.predict([[user], [item]])[0][0]
    d = {'rating': float(prediction)}
    return jsonify(d)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

