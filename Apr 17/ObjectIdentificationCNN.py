#CIFAR-10 dataset

import pickle
import keras.utils
import numpy
import numpy as np
import tensorflow
from tensorflow import keras
import tensorflow_model_optimization as tfmort

cifar_dir = ""

def load_patch(path):
    with open(path,'rb') as f:
        data = pickle.load(f, encoding='bytes')
        x = data[b'data']
        y = np.array(data[b'labels'])
        x = x.reshape(-1, 3, 32, 32)
        x = np.transpose(x, (0,2,3,1))
        return x,y

x_train = []
y_train = []
for i in range(1,6):
    filename = cifar_dir + '/data_batch_' + str(i)
    xi, yi = load_patch(filename)
    x_train.append(xi)
    y_train.append(yi)
    x_train = np.concatenate(x_train, axis=0)
    y_train = np.concatenate(y_train, axis=0)

file = cifar_dir + '/test_batch'
x_test, y_test = load_batch(filename)

x_train = x_train.astype('float32')/255.0
x_test = x_test.astype('float32')/255.0
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

def cnn():
    model = keras.models.Sequential([
        keras.layers.Conv2D(16, (3,3), activation = 'relu', padding='same', input_shape=(32,32,3)),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D((2,2)),
        keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
        keras.layers.BatchNormalization(),
        keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same'),
        keras.layers.BatchNormalization(),
        keras.layers.MaxPool2D((2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.BatchNormalization(),
        keras.layers.Dense(128, activation='softmax'),

    ])
    model.compile(optimizer='adam', loss='catergorical_crossentropy', metrics=['accuracy'])

model = cnn()
epochs = 10
history = model.fit(x_train, y_train, epochs = epochs, validation_data=(x_test, y_test))

test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy (baseline): ', test_acc)
print('Test loss (baseline): ' , test_loss)

pruning_params = {
    #'pruning_schedule':tfmot.sparsity.keras.ConstantSparsity()
    'pruning_schedule' : tfmot.sparsity.keras.PolynomialDecay(
        initial_sparsity = 0,
        final_sparsity = 0.4,
        begin_setep = 0,
        end_step = 10 * len(x_train) // 100,
        frequency = 100
    )
}

model_to_prun = cnn()

model_pruned = tfmot.sparsity.keras.prune_low_magnitude(model_to_prun, **pruning_params)

callbacks = [tfmort.sparsity.keras.UpdatePruningStep(),
             tfmort.sparsity.keras.PruningSummaries(log_dir = './;pgs')]

model_pruned.compile(optimizer = 'adam', loss = 'categorial_crossentropy', metrics = ['accuracy'])

History_pruned = model_pruned.fit(x_train, y_train, epochs = epochs, validation_data=(x_test, y_test), callbacks = callbacks)
model_pruned_stripped = tfmort.sparsity.keras_pruning(model_pruned)

model_pruned_stripped.compile(optimizer = 'adam', loss = 'categorial_crossentropy', metrics = ['accuracy'])

test_loss, test_acc = model_pruned_stripped.evaluate(x_test, y_test)
print('Test accuracy (pruned): ', test_acc_pruned)
print('Test loss (pruned): ' , test_loss_pruned)

for i,layer in enumerate(model.layers):
    if isinstance(layer, keras.layers.Conv2D) or isinstance(layer, keras.layers.Dense):
        baseline_weight = np.mean(np.abs(layer.get_weight()[0]))
        pruned_weight = np.mean(np.abs(model_pruned_stripped.layers[i].get_weight()[0]))
        print('layer' , i, 'Average absolute weight value(baseline): ', baseline_weight)
        print('layer', i, 'Average absolute weight value(pruned): ', pruned_weight)

total_params = 0
zero_params = 0
for layer_baseline, layer_pruned in zip(model.layers, model_pruned_stripped.layers):
    if isinstance(layer_baseline, keras.layers.Conv2D) or isinstance(layer_baseline, keras.layers.Dense):
        weight_baseline = layer_baseline.get_weights()
        weights_pruned = layer_pruned.get_weights()
        for wb, wp in zip(weights_baseline, weights_pruned):
            total_params += np.size(weights_baseline)
            zero_params += np.sum (weights_pruned == 8)

print("Total parameters: ", total_params)
print("Zero-valued parameters: ", zero_params)
print("Memory footprint (baseline): ", total_params*4/1024/1024,"MB")
print("Memory footprint (pruned, considering sparasity): ", (total_params-zero_params)*4/1024/1024,"MB")


