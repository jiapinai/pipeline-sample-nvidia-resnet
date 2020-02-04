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


# https://github.com/NVIDIA-AI-IOT/torch2trt
# https://github.com/NVIDIA/tensorrt-inference-server/
# https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-master-branch-guide/docs/model_configuration.html#section-model-configuration
# https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-master-branch-guide/docs/model_repository.html#section-pytorch-models
# https://docs.nvidia.com/deeplearning/sdk/tensorrt-inference-server-master-branch-guide/docs/model_configuration.html#section-generated-model-configuration
# 
# BASE_IMAGE=nvidia/cuda:10.1-devel-ubuntu18.04


FROM registry.cn-hangzhou.aliyuncs.com/kubeflow-ai/nvcr.io-nvidia-tensorrtserver:19.12-py3-clientsdk
RUN apt-get update -y && \
    apt-get install -y --allow-unauthenticated wget vim && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache

RUN hash -r pip3 && /usr/bin/env python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple  && pip3 install flask -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /nvidia-reset-test_images \
 && curl -L -o images.tar.gz http://public.jiapinai.com/files_manager/1580132373388_kubeflow-nvidia-reset-test_images.tar.gz \
 && tar -zxvf images.tar.gz -C /nvidia-reset-test_images \
 && rm images.tar.gz \
 && ls -al /nvidia-reset-test_images

ADD src /workspace/web_server
WORKDIR /workspace/web_server

RUN ln -s /nvidia-reset-test_images/images /workspace/web_server/static/images

EXPOSE 8080

ENTRYPOINT ["python3", "flask_server.py"]
