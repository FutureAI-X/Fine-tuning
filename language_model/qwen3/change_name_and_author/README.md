# Qwen3 微调改名
1 下载数据集模板

ModelScope Swift 团队发布的 self-cognition 自我认知数据集，共108条数据，包括中文和英文。

下载地址：https://modelscope.cn/datasets/swift/self-cognition/resolve/master/self_cognition.jsonl

下载后的文件命名为 self_cognition.jsonl 并放在当前目录下。

2 执行转换戒本
```
python transform_data.py --name_zh 小新 --author_zh FutureAI实验室 --name_en Xiao-xin --author_en FutureAILab
```