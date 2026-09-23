import pandas as pd
import qrcode
import json
import os
import re


def _safe_filename(value: object) -> str:
    return re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", str(value))

def main() -> None:
    # 读取指定Sheet
    df = pd.read_excel(
        "assets/data.xlsx",
        sheet_name="sheet0"
    )

    # 输出目录
    output_dir = os.path.join("assets", "qrcodes")
    os.makedirs(output_dir, exist_ok=True)

    for _, row in df.iterrows():

        # 整行转JSON
        qr_text = json.dumps(
            row.to_dict(),
            ensure_ascii=False,
            default=str
        )
    # for _, row in df.iterrows():

    #     # 生成JSON内容
    #     qr_content = {
    #         "Plant": str(row["Plant"]),
    #         "Material": str(row["Material"]),
    #         "Batch": str(row["Batch"]),
    #         "Qty": row["Qty"]
    #     }

    #     # 转成JSON字符串
    #     qr_text = json.dumps(
    #         qr_content,
    #         ensure_ascii=False
    #     )

        # 文件名由多个单元格组合
        filename = (
            f"{_safe_filename(row['proj_id'])}_"
            f"{_safe_filename(row['bay_id'])}_"
            f"{_safe_filename(row['transportation_cell_symbol'])}.png"
        )

        # 生成二维码
        img = qrcode.make(qr_text)

        # 保存
        img.save(os.path.join(output_dir, filename))

    print("完成")