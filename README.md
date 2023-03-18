# ChatGPT Tinder Bot

中文 | [English](README.en.md)

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/ChatGPT-Tinder-Bot)](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/releases/)


## 更新
- 2023/03/03 模型換成 chat completion: `gpt-3.5-turbo`


## 介紹
ChatGPT 的強大，是否也想要把他串到各個聊天平台呢？這個 Repository 教你如何串到 Tinder 上，讓你忙碌時也能夠自動回覆訊息去交朋友，而這邊提供最基本的架構，只有從過去的聊天記錄去推測，會寫程式的工程師們，當然也可以把用戶的背景資訊，甚至去串圖像相關的模型，去偵測圖片，讓 ChatGPT 能夠回應的更適切。

![Demo](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/blob/main/demo/chatgpt-tinder-bot.gif)

## 安裝步驟
### Token 取得
1. 取得 OpenAI 給的 API Token：
    1. [OpenAI](https://beta.openai.com/) 平台中註冊/登入帳號
    2. 右上方有一個頭像，點入後選擇 `View API keys`
    3. 點選中間的 `Create new secret key` -> 生成後即為 `OPENAI_API` （稍晚會用到）
    - 注意：每隻 API 有免費額度，也有其限制，詳情請看 [OpenAI Pricing](https://openai.com/api/pricing/)
2. 取得 Tinder Token：
    1. 登入 [Tinder](https://tinder.com/)
    2. 按下`右鍵` -> `檢查` -> `網路` -> 挑選任一隻 Request -> 尋找 Request 裡的 `x-auth-token`
    * ![Tinder Token](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot/blob/main/demo/tinder-token.png)

### 專案設置
1. Fork Github 專案：
    1. 註冊/登入 [GitHub](https://github.com/)
    2. 進入 [ChatGPT-Tinder-Bot](https://github.com/TheExplainthis/ChatGPT-Tinder-Bot)
    3. 點選 `Star` 支持開發者
    4. 點選 `Fork` 複製全部的程式碼到自己的倉庫
2. 部署（免費空間）：
    1. 進入 [replit](https://replit.com/)
    2. 點選 `Sign Up` 直接用 `Github` 帳號登入並授權 -> 按下 `Skip` 跳過初始化設定
    3. 進入後中間主頁的部分點選 `Create` -> 跳出框，點選右上角 `Import from Github`
    4. 若尚未加入 Github 倉庫，則點選連結 `Connect GitHub to import your private repos.` -> 勾選 `Only select repositories` -> 選擇 `ChatGPT-Tinder-Bot`
    5. 回到第四步，此時 `Github URL` 可以選擇 `ChatGPT-Tinder-Bot` 專案 -> 點擊 `Import from Github`。

### 專案執行
1. 環境變數設定
    1. 接續上一步 `Import` 完成後在 `Replit` 的專案管理頁面左下方 `Tools` 點擊 `Secrets`。
    2. 右方按下 `Got it` 後，即可新增環境變數，需新增：
        1. OpenAI API Token：
            - key: `OPENAI_API`
            - value: `[由上方步驟一取得]`
        2. 欲選擇的模型：
            - key: `OPENAI_MODEL_ENGINE`
            - value: `gpt-3.5-turbo`  
        3. ChatGPT 要讓助理扮演的角色詞（目前官方無釋出更多的使用方法，由玩家自行測試）
            - key: `SYSTEM_MESSAGE`
            - value: `You are a helpful assistant.`
        4. Tinder Token:
            - key: `TINDER_TOKEN`
            - value: `[由步驟一取得]`
2. 開始執行
    1. 點擊上方的 `Run`
    2. 成功後右邊畫面會顯示 `{"message": "Hello World"}`，並將畫面中上方的**網址複製**下來
    - 注意：若一小時內沒有任何請求，則程式會中斷，因此需要下步驟
3. CronJob 定時發送請求
    1. 註冊/登入 [cron-job.org](https://cron-job.org/en/)
    2. 進入後面板右上方選擇 `CREATE CRONJOB`
    3. `Title` 輸入 `ChatGPT-Tinder-Bot`，網址輸入上一步驟的網址，例如：`https://ChatGPT-Tinder-Bot.explainthis.repl.co/`
    4. 下方則每 `5 分鐘` 打一次
    5. 按下 `CREATE`

## 說明
- 回覆的時間點為？
    - 每五分鐘掃一次，若發現對方尚未回覆則會略過，若超過一天對方無回覆，則才會再次留言

- 如何客製化調整？
    - 在 `main.py` 中，27 行的 `scheduled_job` 可以調整多久回覆一次
    - 在 `main.py` 中，34 行的 `for` 可以調整要回覆多少聊天室內容
    - 在 `main.py` 中，47 行的 `if` 可以調整什麼樣的狀況才會回應訊息

- 如何加入更多資訊？
    - `/src/dialog.py` 中，有一個 `prefix`，可以將資訊加入其中，像是你可以訓練機器人，說明你的回應風格是什麼類型，因此希望他照著你的回應風格去做回應。


## 支持我們
如果你喜歡這個專案，願意[支持我們](https://www.buymeacoffee.com/explainthis)，可以請我們喝一杯咖啡，這會成為我們繼續前進的動力！

[<a href="https://www.buymeacoffee.com/explainthis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="45px" width="162px" alt="Buy Me A Coffee"></a>](https://www.buymeacoffee.com/explainthis)


## 相關專案
- [auto-tinder](https://github.com/joelbarmettlerUZH/auto-tinder/tree/master)
- [ChatGPT-Discord-Bot](https://github.com/TheExplainthis/ChatGPT-Discord-Bot)
- [ChatGPT-Line-Bot](https://github.com/TheExplainthis/ChatGPT-Line-Bot)

## 授權
[MIT](LICENSE)
