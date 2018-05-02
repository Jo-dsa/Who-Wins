#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 23:41:07 2018

@author: mira
"""

from pyspark.ml.classification import MultilayerPerceptronClassifier
from functions_ml import spark_context, training_set, test_set, write_result, brexit_labeled_data, model_predict


def MLP_train(training):
    print("ici")
    
    num_cols = rescaledData.select('features').collect()[0].features.size  #vocabulary size
    layers = [num_cols , 100 , 2]
    MLP_trainer = MultilayerPerceptronClassifier(maxIter=100, layers=layers, blockSize=128, seed=1234)
    model = MLP_trainer.fit(training)
    
    print("ici")
    
    return model

if __name__ == "__main__":

    numFeatures = 10000
    
    sc = spark_context()
    
    print("Training...\n")
    
    (rescaledData, idfModel) = training_set(sc = sc, numFeatures = numFeatures)
    print(3)
    model = MLP_train(training = rescaledData)

    print("Test... \n")

#    rescaled_test_df = test_set(sc, numFeatures = numFeatures, idfModel = idfModel)
#    (num_pos, num_neg) = model_predict(model, rescaled_test_df)
    
    print("Test on Brexit labeled data...\n")
    
    (accuracy, f1) = brexit_labeled_data(sc = sc, numFeatures = numFeatures, idfModel = idfModel , model = model)
   
    print("Saving results...\n")
    
    write_result(1, 1, accuracy = accuracy, f1 = f1, name = "Neural Network")
    
    