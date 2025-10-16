import argparse
import json

"""TODO: 数据集模板的下载可以写成方法"""
def do_transform(name_zh: str, name_en:str, author_zh:str, author_en:str):
    with open("self_cognition.jsonl", "r") as f, open("self_cognition_futureai.jsonl", "w") as f_out:
        for line in f:
            data = json.loads(line)
            if data["tag"] == "zh":
                data["response"] = data["response"].replace(r"{{NAME}}", name_zh).replace(r"{{AUTHOR}}", author_zh)
            else:
                data["response"] = data["response"].replace(r"{{NAME}}", name_en).replace(r"{{AUTHOR}}", author_en)
            f_out.write(json.dumps(data, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="自我认知数据集转换")

    parser.add_argument("--name_zh", type=str, required=True, help="模型名称(中文)")
    parser.add_argument("--name_en", type=str, required=True, help="模型名称(英文)")
    parser.add_argument("--author_zh", type=str, required=True, help="作者(中文)")
    parser.add_argument("--author_en", type=str, required=True, help="作者(英文)")

    args = parser.parse_args()
    do_transform(args.name_zh, args.name_en, args.author_zh, args.author_en)
