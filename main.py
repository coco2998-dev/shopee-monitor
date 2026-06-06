import os
import requests
import pandas as pd

print("🤖 雲端大金剛啟動！開始巡邏...")

# 🔑 關鍵魔法：讓大金剛去 GitHub 保險箱裡面拿你的密碼！
機器人暗號 = os.environ.get("TG_TOKEN")
老大的號碼 = os.environ.get("TG_CHAT_ID")

# 這裡放我們之前的巡邏資料 (未來可以改成去抓 Yahoo 或蝦皮)
爬到的資料 = [
    {"平台": "momo", "品名": "莊頭北 13L 熱水器", "價格": 12500, "網址": "https://www.momoshop.com.tw/"},
    {"平台": "蝦皮", "品名": "【超殺低價】莊頭北 隨便賣", "價格": 6500, "網址": "https://shopee.tw/"}
]

表格 = pd.DataFrame(爬到的資料)
一般價錢 = 表格['價格'].median()
太便宜的底線 = 一般價錢 * 0.8   

郵差網址 = f"https://api.telegram.org/bot{機器人暗號}/sendMessage"

for index, row in 表格.iterrows():
    if row['價格'] < 太便宜的底線:
        警告訊息 = f"🚨 雲端回報！發現異常低價！\n📍 平台：{row['平台']}\n📦 品名：{row['品名']}\n💰 價格：{row['價格']} 元\n🔗 直達現場：{row['網址']}"
        requests.post(郵差網址, data={"chat_id": 老大的號碼, "text": 警告訊息})
        print(f"✅ 成功將低價警告傳送到老大的 Telegram！")
