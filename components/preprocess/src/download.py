
import os
from keras.utils import get_file
# processed_data = cifar10.load_data()
dirname = 'cifar-10-batches-py'
#origin = 'https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
origin = 'http://public.jiapinai.com/files_manager/1580182143647_kubeflow-nvidia-reset-cifar-10-python.tar.gz'
path = get_file(dirname, origin=origin, untar=True)
