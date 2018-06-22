#!/usr/bin/env python

from mickey import *

EPOCH_COUNT = 40

model = InceptionResNet("Inception-ResNet-v2")
model.model.summary()
model.train(EPOCH_COUNT)
model.save('model_weights.h5')
