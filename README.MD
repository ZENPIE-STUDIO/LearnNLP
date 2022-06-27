# LearnNLP

### 01. 英文-文本預處理

- 英文的 word 是最小單位

- 轉成小寫

- 移除標點符號 (Removing punctuations)

- 分句 sent_tokenize：分段為句

- 分詞 word_tokenize：分句為詞
  - NLTK 有下列分詞的方法
    - TreebankWordTokenizer
    - PunktWordTokenizer
    - RegexpTokenizer
      - 可以斷出 `Let's`、`it's`
      - 無法斷出 `Cheng's` 
    - WhitespaceTokenizer：用空白斷詞
  
- 刪除停用詞 (Removing stopwords)
  - 日常生活中會遇到的出現頻率很高的詞，如do, I, am, is, are等等
  
- 詞性標註 (Part-of-speech Tagging)

- 實體辨識（Named Entity Recognition, NER)

  - 使用 spacy 處理，有下列

    ```
    PERSON	People, including fictional.	人物
    NORP	Nationalities or religious or political groups.	國家、宗教、政治團體
    FAC	Buildings, airports, highways, bridges, etc.	建築、機場、高速公路、橋樑等
    ORG	Companies, agencies, institutions, etc.	組織公司、機構等
    GPE	Countries, cities, states.	國家、城市、州
    LOC	Non-GPE locations, mountain ranges, bodies of water.	山脈、水體等
    PRODUCT	Objects, vehicles, foods, etc. (Not services.)	車輛、食物等非服務性的產品
    EVENT	Named hurricanes, battles, wars, sports events, etc.	颶風、戰爭、體育賽事等
    WORK_OF_ART	Titles of books, songs, etc.	書名、歌名等
    LAW	Named documents made into laws.	法律文書
    LANGUAGE	Any named language.	語言
    DATE	Absolute or relative dates or periods.	日期
    TIME	Times smaller than a day.	小於1天的時間
    PERCENT	Percentage, including “%”.	百分比
    MONEY	Monetary values, including unit.	貨幣價值
    QUANTITY	Measurements, as of weight or distance.	度量單位
    CARDINAL	數量詞
    ORDINAL	“first”, “second”, etc.	序數詞
    ```



#### 文字正規化 (Text Normalisation)

- 語幹提取 / 去除字尾 (Stemming)
  - 例：change, changing, changes, changed, chager => `chang`
  - [Stemming algorithms](https://www.geeksforgeeks.org/introduction-to-stemming/?ref=lbp)

- 詞形還原 (Lemmatization)

  - 例：change, changing, changes, changed, chager => `change`

  

#### 條件次數分配（Conditional Frequency Distribution）

- 使用 nltk.probability
- 字數統計
- 每個詞出現的頻率

#### N-Gram

- https://devopedia.org/n-gram-model
- n-gram 就是n個連續單詞構成的序列，例如 "store" 就是 1-gram、 "the store" 就是 2-gram、"to the store" 就是 3-gram ，以此類推。
- 分析文本中 連續單詞 出現的次數
- 用來預測關鍵字



----

### 詞性標註 Part-of-speech tagging 說明

- CC（Coordinating Conjunction）：並列連詞
- CD（Cardinal Digit）：基數
- DT（Determiner）：限定詞
- EX（Existential There）：存在句
  - Example: “there is” … think of it like “there exists”
- FW（Foreign Word）：外來語
- IN（Preposition/Subordinating Conjunction）：介詞/從屬連詞
- JJ（Adjective）：形容詞
- JJR（Adjective, Comparative）：形容詞，比較級
- JJS（Adjective, Superlative）：形容詞，最高級
- LS（List Marker 1）：
- MD（Modal）：模態
- NN（Noun, Sigular）：名詞，單數
- NNS（Noun Plural）：名詞，複數
- NNP（Proper Noun, Singular）：專有名詞，單數
- NNPS（Proper Noun, Plural）：專有名詞，複數
- PDT（Predeterminer）：預定義器。
- POS（Possessive Ending）：所有格結尾，例：parent’s
- PRP（Personal Pronoun）：人稱代詞，例：I, he, she
- PRP$（Possessive Pronoun）：所有格代詞。 例：my, his, hers
- RB（Adverb）：副詞。例：very, silently
- RBR（Adverb, Comparative）：副詞、比較。例：better
- RBS（Adverb, Superlative）：副詞、最高級。例：best
- PR（Particle）：粒子，Ex. give up
- TO（to）：就是 go 'to' ...
- UH（Interjection）：呃感嘆詞。 Ex：errrrrrrrm
- VB（Verb, Base Form）：動詞，基本形式。Ex. take
- VBD（Verb, Past Tense）：動詞，過去式。Ex. took
- VBG（Verb, Gerund/Present Participle）：動詞，動名詞/現在分詞。Ex. taking
- VBN（Verb, Past Participle）：動詞，過去分詞。Ex. taken
- VBP（Verb,non-3rd person singular present）：動詞，非第三人稱單數
- VBZ（Verb, 3rd person singular present）：動詞，第三人稱單數
- WDT（Wh-determiner）： 限定詞
  - 關係限定詞：whose, which
  - 疑問限定詞：what, which, whose
- WP（Wh-pronoun）：代詞, who whose which
- WP$（Possessive wh-pronoun）：所有格代詞
- WRB（Wh-adverb）：疑問代詞   how where when
