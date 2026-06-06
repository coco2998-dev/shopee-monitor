import requests
import pandas as pd

print("🤖 機器人出動！開始巡邏莊頭北商品...")

# --- 【第一步：測試用的商品資料】 ---
爬到的資料 = [
    {"平台": "momo", "品名": "莊頭北 13L 數位恆溫熱水器", "價格": 12500, "網址": "https://www.momoshop.com.tw/正常網址"},
    {"平台": "蝦皮", "品名": "莊頭北 TH-7139FE", "價格": 12000, "網址": "https://shopee.tw/正常網址"},
    # 下面這個是故意設定的異常低價，一定會觸發警報！
    {"平台": "蝦皮", "品名": "【超殺低價】莊頭北 隨便賣", "價格": 6500, "網址": "https://shopee.tw/我要檢舉這個賣家"} 
]

# --- 【第二步：大腦開始計算】 ---
表格 = pd.DataFrame(爬到的資料)
一般價錢 = 表格['價格'].median() 
太便宜的底線 = 一般價錢 * 0.8   

# --- 【第三步：設定 Telegram 密碼】 ---
# 🚨 老大！請務必把下面這兩個換成你真正的密碼！(引號要留著喔)
機器人暗號 = "8762067732:AAGfkpfYqozSbHzcwb8aSi-gQAgtnUo9cKg" 
老大的號碼 = "8913656476"

郵差網址 = f"https://api.telegram.org/bot{機器人暗號}/sendMessage"

# --- 【第四步：開始檢查並傳送通知】 ---
for index, row in 表格.iterrows():
    if row['價格'] < 太便宜的底線:
        
        警告訊息 = f"🚨 老大注意！發現異常低價！\n📍 平台：{row['平台']}\n📦 品名：{row['品名']}\n💰 價格：{row['價格']} 元\n🔗 直達現場：{row['網址']}"
        
        # 寄出 Telegram 通知並聽聽總機怎麼說
        回應 = requests.post(郵差網址, data={"chat_id": 老大的號碼, "text": 警告訊息})
        
        # 🔍 把 Telegram 總局的回報印出來看！
        print(f"✅ 已嘗試發送！Telegram 總局的回報紀錄：{回應.text}")

print("🤖 報告老大，今日巡邏完畢！")
