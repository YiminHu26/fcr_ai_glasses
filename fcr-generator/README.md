# 自动生成FCR脚本
将结构化存储的检测结果转化为终检报告(FCR)

## 设置
1. 阅读[教程](https://docs.astral.sh/uv/getting-started/installation/),下载uv,这里我用winget方法
```bash
winget install --id=astral-sh.uv  -e
```

## 使用
1. 将检测结果的数据库/结构化表格下载到根目录下，以下假设该数据库名称为```inspection_report_xxx.xlsx```
1. 确保[FCR报告模板](fcr-generator\fcr_template.xlsx)或其他模板也在根目录下
1. 运行以下代码
```bash
# 如果用的是默认FCR模板
uv run fcr-generator inspection_report_xxxxx.xlsx
# 如果有确定的FCR命名，假设最终名字是```FCR_70xxxx_D01.xlsx```
uv run –o FCR_70xxxx_D01.xlsx inspection_report_xxxxx.xlsx
# 如果用的是自己的FCR模板，假设该模板名称为```fcr_xxx_template.xlsx```
uv run fcr-generator –o FCR_70xxxx_D01.xlsx --template fcr_xxx_template.xlsx inspection_report_xxxxx.xlsx
```

## 快速开始
目前该目录下已经存有检测数据和报告模板，可以直接运行以下命令来验证
```bash
uv run fcr-generator inspection_report_706271_D01_mock.xlsx
```

## 问题
- 好像现在左上角的logo没有复制进新报告中