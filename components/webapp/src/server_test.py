#!/usr/bin/env python3
import os
# from threading import Timer

from trtis_client import get_prediction, random_image


name_arg = os.getenv('MODEL_SERVE_NAME', 'pytorch')
addr_arg = os.getenv('TRTSERVER_HOST', '10.110.20.210')
port_arg = os.getenv('TRTSERVER_PORT', '8001')
model_version = os.getenv('MODEL_VERSION', '-1')
name_arg = 'resnet'
name_arg = 'pytorch'
name_arg = 'resnet_graphdef'
args = {"name": str(name_arg), "addr": str(addr_arg), "port": str(port_arg), "version": str(model_version)}
print('args:', args)
output = None
connection = {"text": "", "success": False}

# get a random test MNIST image
file_name, truth, serving_path = random_image('/workspace/web_server/static/images')
# get prediction from TensorFlow server
pred, scores = get_prediction(file_name,
                              server_host=addr_arg,
                              server_port=int(port_arg),
                              model_name=name_arg,
                              model_version=int(model_version))
# if no exceptions thrown, server connection was a success
connection["text"] = "Connected (model version: {0}".format(str(model_version))+ ")"
connection["success"] = True
# parse class confidence scores from server prediction
output = {"truth": truth, "prediction": pred,
          "img_path": serving_path, "scores": scores}

print('output', output)
print('connection', connection)