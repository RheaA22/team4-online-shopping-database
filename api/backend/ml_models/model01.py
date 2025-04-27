"""
model_products.py — ML model for predicting product price/popularity.
Retrieves model parameters from online shopping database for prediction.
"""

from backend.db_connection import db
import numpy as np
import logging

def train():
    """
    Placeholder for training a model based on historical product data.
    """
    return 'Training product model...'

def test():
    """
    Placeholder for testing model accuracy on test product dataset.
    """
    return 'Testing product model...'

def predict(price, feature_count):
    """
    Makes a real-time prediction with params.
    Predicts "popularity score" or "sales potential".
    """
    # get a database cursor
    cursor = db.get_db().cursor()

    # get model parameters
    query = 'SELECT beta_vals FROM product_model_params ORDER BY sequence_number DESC LIMIT 1'
    cursor.execute(query)
    return_val = cursor.fetchone()

    params = return_val['beta_vals']
    logging.info(f'Model parameters = {params}')
    logging.info(f'Params datatype = {type(params)}')

    # turn DB string into numpy array
    params_array = np.array(list(map(float, params[1:-1].split(','))))
    logging.info(f'params array = {params_array}')
    logging.info(f'params_array datatype = {type(params_array)}')

    input_array = np.array([1.0, float(price), float(feature_count)])

    prediction = np.dot(params_array, input_array)

    return prediction

