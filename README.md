# Huggingface 相关测试

## 简介

- `huggingface` 网址：https://huggingface.co/

- 测试了该网址上的 2 个模型，分别为：[resnet50](https://huggingface.co/timm/resnet50.a1_in1k)   和 [vit](https://huggingface.co/google/vit-base-patch16-224)

## 环境

在安装有 `torch` 的环境的基础上，安装以下库：

```bash
pip install timm
pip install transformers
```

## 运行

- resnet50

根据上方链接下载 `model.safetensors` 模型文件，放入 `resnet` 目录下，然后运行：

```bash
cd resnet
python infer.py
```

- vit

根据上方链接下载 `model.safetensors` 模型文件，`config.json` 和 `preprocessor_config.json`，放入 `vit/vit` 目录下，然后运行：

```bash
cd vit
python infer.py
```

