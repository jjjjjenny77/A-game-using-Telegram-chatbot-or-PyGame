# A-game-using-Telegram-chatbot-or-PyGame
> This note record and share the midterm project of python course about using pyautohui and opencv to create a game agent
## How to run the code
* First, you have to apply for a bot from [@BotFather]:https://web.telegram.org/k/#@BotFather
  - Enter /newbot in the dialog box
  - Enter the name of your bot
  - Enter the account number of your bot(must end with"bot")
  - Then you will get your Bot ID and the TOKEN of API
## Game rules:
* 有梅花七的玩家先出，但不一定要先出梅花七
* 有牌可以出就一定要出，若沒有牌可以出則需蓋一張牌，蓋牌規則如下：
  - 挑最小的牌去蓋
    - 例如你沒牌可出，有梅花A，那就蓋他
  - 挑蓋了之後對其他玩家影響(總和)大於自己的蓋
    - 例如你沒牌可出，但有黑桃8，沒有黑桃9~K，那麼你蓋掉黑桃8，對其他玩家影響最大
    - 或者是你有愛心8和Q，你也可以蓋掉愛心8，因為另外三家總會蓋掉9、10、J、K
    - 承上，當然你要蓋掉Q也無所謂，總是會有人蓋一張K
* 直到沒有牌時，遊戲結束
## Watch my demo video below!
https://www.youtube.com/watch?v=MepVbut_TIY
