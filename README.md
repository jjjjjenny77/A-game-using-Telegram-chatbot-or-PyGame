# A-game-using-Telegram-chatbot-or-PyGame
> This note record and share the final project of python course in 【112上】 about using Telegram chatbot or PyGame to play Hidden Chess
## How to run the code
* First, you have to apply for a bot from [@BotFather]:https://web.telegram.org/k/#@BotFather
  - Enter /newbot in the dialog box
  - Enter the name of your bot
  - Enter the account number of your bot(must end with"bot")
  - Then you will get your Bot ID and the TOKEN of API
* Download the files code and TOKEN
* Type your token in the TOKEN file
* Run the code and open your telegram bot to plat the game!
## (暗棋)Game rules:
* 棋盤為 4*8 方格
* 在最一開始，棋子反面朝上隨機布置於棋格。反面朝上的棋子稱為暗棋，正面朝上稱為明棋
* 為兩人遊戲
* 兩方棋子分別為
  - 將、士、象、車、馬、砲、卒
  - 帥、仕、相、俥、傌、炮、兵
* 棋子數量共 32 個，分別為
  - 將/帥：各一個
  - 士/仕：各二個
  - 象/相：各二個
  - 車/俥：各二個
  - 馬/傌：各二個
  - 砲/炮：各二個
  - 卒/兵：各五個
* 棋子等級分別為（ > => 左邊等級比右邊大，自己跟自己同等）
  - 將帥 > 士仕、象相、車俥、馬傌
  - 士仕 > 象相、車俥、馬傌、砲炮、卒兵
  - 象相 > 車俥、馬傌、砲炮、卒兵
  - 車俥 > 馬傌、砲炮、卒兵
  - 馬傌 > 砲炮、卒兵
  - 砲炮 > 將帥、士仕、象相、車俥、馬傌、卒兵
  - 卒兵 > 將帥
* 每方回合需選擇以下行動之一（請參考圖一）
  - 將一枚暗棋翻成明棋，先行方第一次翻出棋子的顏色，該色成為他的棋子；反之為敵方
  - 移動一枚本方棋至空格：移動應朝縱或橫向移動且只能移動棋至鄰邊格（一格差）
  - 剋除(吃)一枚低等或同等的敵方明棋
    - 除了砲/炮以外的其他棋，只能剋除(吃)鄰邊格（一格差）
    - 砲/炮只能在縱或橫向有一個且唯一個棋子時才能剋除(吃)
      
![image](https://github.com/jjjjjenny77/images/blob/main/%E6%9A%97%E6%A3%8B.png)

（圖一）綠色代表可吃子/移動，紅色代表不可吃子/移動
## Watch my demo video below!
https://youtu.be/rItKAJCIUYs?si=kAbyi7Daa74A37QF
