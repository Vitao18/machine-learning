#!/usr/bin/python

## @serialize_model.py
#  This file serializes, and deserializes an SVM object in memory.
from six.moves import cPickle as pickle

    ## constructor
    def __init__(self, obj):
        self.obj = obj
        self.acceptable = [svm.classes.SVC]

    ## serialize: serializes the provided object.
    def serialize(self, obj):
        if type(obj) in self.acceptable:
            return pickle.dumps(obj)

    ## deserialize: deserializes the provided object.
    def deserialize(self, obj):
        return pickle.loads(obj)
