# https://ngc.nvidia.com/catalog/containers/nvidia:tensorrtserver/tags
# https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html

# Before 19.07, pytorch models are not supported
# ref: https://github.com/NVIDIA/tensorrt-inference-server/releases

# <Release 1.4.0, corresponding to NGC container 19.07>
# Added libtorch as a new backend. PyTorch models manually decorated or automatically 
# traced to produce TorchScript can now be run directly by the inference server.

#FROM nvcr.io/nvidia/tensorflow:19.03-py3

# https://docs.nvidia.com/deeplearning/sdk/inference-release-notes/rel_20-01.html#rel_20-01
# The inference server container image version 20.01 is based on NVIDIA TensorRT Inference Server 1.10.0, 
# TensorFlow 1.15.0, ONNX Runtime 1.0.0, and PyTorch 1.3.0.
FROM registry.cn-hangzhou.aliyuncs.com/kubeflow-ai/nvcr.io-nvidia-tensorrtserver:20.01-py3

# Install tensorflow-gpu
RUN mkdir /root/.pip/ \
    && echo "[global]" > /root/.pip/pip.conf \
    && echo "index-url = http://mirrors.aliyun.com/pypi/simple/" >> /root/.pip/pip.conf \
    && echo "[install]" >> /root/.pip/pip.conf \
    && echo "trusted-host=mirrors.aliyun.com" >> /root/.pip/pip.conf \
    && cat /root/.pip/pip.conf \
    && pip3 install apache-beam \
	tensorflow-gpu==1.14.0 \
	tensorflow-transform==0.13.0 \
	tensorflow_model_analysis==0.13.0 \
	tensorflow_data_validation==0.13.0 \
    keras \
	--ignore-installed 

ADD src /workspace
WORKDIR /workspace

ENTRYPOINT ["python3", "train.py"]
