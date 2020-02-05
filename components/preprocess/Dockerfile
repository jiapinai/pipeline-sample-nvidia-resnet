# Copyright (c) 2019, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#FROM nvcr.io/nvidia/tensorflow:19.03-py3
FROM registry.cn-hangzhou.aliyuncs.com/kubeflow-ai/nvcr.io-nvidia-tensorrtserver:20.01-py3

RUN pip3 install keras -i https://pypi.tuna.tsinghua.edu.cn/simple
ADD src /workspace
WORKDIR /workspace

#RUN python /workspace/download.py

#https://github.com/tensorflow/tensorflow/issues/32278
# https://github.com/keras-team/keras/blob/d954aef2a2e33532f8725f58183cf605f5c54656/keras/datasets/cifar10.py
# https://github.com/tensorflow/tensorflow/blob/r2.1/tensorflow/python/keras/utils/data_utils.py#L164-L283
#download it from https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
#rename it as cifar-10-batches-py.tar.gz
#copy it to /root/.keras/datasets/
RUN mkdir -p /root/.keras/datasets/ && \
    wget 'http://public.jiapinai.com/files_manager/1580182143647_kubeflow-nvidia-reset-cifar-10-python.tar.gz' -q -O /root/.keras/datasets/cifar-10-batches-py.tar.gz && \
    ls -alh /root/.keras/datasets/

ENTRYPOINT ["python3", "preprocess.py"]
