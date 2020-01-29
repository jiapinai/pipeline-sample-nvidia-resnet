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

FROM registry.cn-hangzhou.aliyuncs.com/kubeflow-ai/tensorrt-inference-server-client-base

RUN pip3 install flask
ADD src /workspace/web_server
WORKDIR /workspace/web_server

RUN curl -L -o images.tar.gz http://public.jiapinai.com/files_manager/1580132373388_kubeflow-nvidia-reset-test_images.tar.gz \
 && tar -zxvf images.tar.gz -C /workspace/web_server/static \
 && rm images.tar.gz

EXPOSE 8080

ENTRYPOINT ["python3", "flask_server.py"]
