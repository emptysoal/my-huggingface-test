import timm
import torch
from PIL import Image

img = Image.open("../banana.jpeg")


model = timm.create_model('resnet50.a1_in1k', pretrained=True, pretrained_cfg_overlay=dict(file="./model.safetensors"))
model = model.eval()

data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))
top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1) * 100, k=5)

print(top5_probabilities)
print(top5_class_indices)

