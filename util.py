
character_set = lambda s: {c for l in s.split('\n') for c in l.split(' ') if l}

hiragana = character_set("""
ぁ あ ぃ い ぅ う ぇ え ぉ お
か が き ぎ く ぐ け げ こ ご
さ ざ し じ す ず せ ぜ そ ぞ
た だ ち ぢ っ つ づ て で と ど
な に ぬ ね の
は ば ぱ ひ び ぴ ふ ぶ ぷ へ べ ぺ ほ ぼ ぽ
ま み む め も
ゃ や ゅ ゆ ょ よ
ら り る れ ろ
ゎ わ ゐ ゑ を
ん
ゔ
""")

katakana = character_set("""
ァ ア ィ イ ゥ ウ ェ エ ォ オ
カ ガ キ ギ ク グ ケ ゲ コ ゴ
サ ザ シ ジ ス ズ セ ゼ ソ ゾ
タ ダ チ ヂ ッ ツ ヅ テ デ ト ド
ナ ニ ヌ ネ ノ
ハ バ パ ヒ ビ ピ フ ブ プ ヘ ベ ペ ホ ボ ポ
マ ミ ム メ モ
ャ ヤ ュ ユ ョ ヨ
ラ リ ル レ ロ
ヮ ワ ヰ ヱ ヲ
ン
ヴ ヵ ヶ
""")

kanji = character_set("""
一 丁 七 万 丈 三 上 下 不 与 丐 丑 且 世 丘 丙 业 丞 両 並 中 串 丶 丸 丹 主 丼 丿 乃 久
乇 之 乍 乎 乏 乖 乗 乙 九 乞 也 习 乱 乳 乾 亀 了 予 争 事 二 于 云 互 五 井 亘 些 亜 亞
亡 亢 交 亥 亦 亨 享 京 亭 亮 亶 人 什 仁 仄 仅 仇 今 介 仏 仔 仕 他 仗 付 仙 代 令 以 仮
仰 仲 件 任 企 伊 伍 伎 伏 伐 休 会 伜 伝 伯 伴 伶 伸 伺 似 伽 佃 但 佇 位 低 住 佐 佑 体
何 余 佛 作 佞 你 佩 佯 佰 佳 併 佻 使 侃 來 侈 例 侍 侏 侑 侘 供 依 侠 価 侭 侮 侯 侵 侶
便 係 促 俄 俊 俎 俑 俗 俘 俚 保 信 俣 修 俯 俱 俳 俵 俸 俺 倅 倆 倉 個 倍 倒 倖 候 借 倣
値 倦 倨 倩 倫 倭 倶 倹 偃 假 偈 偉 偏 偕 做 停 健 偲 側 偵 偶 偸 偽 傀 傅 傍 傑 傘 備 催
傭 傲 傳 債 傷 傾 僅 働 像 僑 僕 僚 僥 僧 僭 僻 儀 儂 億 儒 儕 儘 儚 償 儡 優 儲 儺 儿 允
元 兄 充 兆 兇 先 光 克 免 兎 児 兒 兔 兕 党 兜 入 內 全 兪 八 公 六 共 兵 其 具 典 兼 冀
内 円 冊 再 冑 冒 冗 写 冠 冢 冤 冥 冨 冬 冱 冴 冶 冷 冽 凄 准 凉 凋 凌 凍 凛 凜 凝 几 凡
処 凧 凩 凪 凭 凰 凱 凶 凸 凹 出 函 刀 刃 分 切 刈 刊 刎 刑 列 创 初 判 別 利 刪 刮 到 刳
制 刷 券 刹 刺 刻 剃 則 削 剋 剌 前 剖 剛 剝 剣 剤 剥 剪 副 剰 剱 割 剴 創 剽 劇 劈 劉 劍
力 功 加 劣 助 努 劫 劭 励 労 効 劾 勁 勃 勅 勇 勉 勒 動 勘 務 勝 募 勢 勤 勧 勲 勾 勿 匁
匂 包 匆 匈 匍 匐 匕 化 北 匙 匠 匡 匣 匪 匹 区 医 匿 區 十 千 升 午 半 卍 卑 卒 卓 協 南
単 博 卜 卞 占 卦 卯 印 危 即 却 卵 卷 卸 卿 厄 压 厖 厘 厚 原 厠 厦 厨 厩 厭 厮 厳 去 参
參 又 叉 及 友 双 反 収 叔 取 受 叙 叛 叟 叡 叢 口 古 句 叩 只 叫 召 叭 可 台 叱 史 右 叶
号 司 吃 各 合 吉 吊 同 名 后 吏 吐 向 君 吝 吟 吠 否 含 听 吭 吶 吸 吹 吻 吼 吽 吾 呀 呂
呆 呈 呉 告 呑 呟 周 呪 味 呵 呻 呼 命 咀 咄 咆 和 咎 咒 咤 咥 咫 咬 咲 咳 咸 咽 哀 品 哄
哉 員 哥 哨 哭 哮 哲 哺 唄 唆 唇 唐 唖 售 唯 唱 唸 唼 唾 啀 啄 商 問 啓 啖 啜 啼 啾 喀 善
喇 喉 喊 喋 喘 喙 喚 喜 喝 喧 喩 喪 喫 喬 喰 喵 営 喼 嗄 嗅 嗚 嗜 嗟 嗣 嗤 嗽 嗾 嘆 嘉 嘔
嘗 嘘 嘛 嘩 嘯 嘱 嘲 嘴 嘶 嘸 噂 噌 噎 噛 噤 噦 器 噪 噬 噯 噴 噺 嚇 嚔 嚢 嚥 嚮 嚼 囀 囁
囂 囃 囗 囚 四 回 因 団 囮 困 囲 図 固 国 圀 圃 國 圏 園 圓 團 土 圧 在 圭 地 坂 均 坊 坏
坐 坑 坡 坤 坦 坩 坪 垂 型 垓 垢 垣 埃 埋 城 埒 埓 埜 域 埠 埴 執 培 基 埼 堀 堂 堅 堆 堕
堝 堡 堤 堪 堯 堰 報 場 堵 堺 塀 塁 塊 塌 塑 塒 塔 塗 塙 塚 塞 塢 塩 填 塵 塹 塾 境 墓 増
墜 墟 墨 墳 墻 墾 壁 壇 壊 壌 壕 壟 壤 士 壬 壮 声 壱 売 壷 壺 変 夏 夕 外 多 夜 夢 夥 大
天 太 夫 央 失 夷 夾 奄 奇 奈 奉 奏 奐 契 奔 奕 套 奚 奢 奥 奧 奨 奪 奬 奮 女 奴 奸 好 如
妃 妄 妆 妊 妓 妖 妙 妥 妨 妬 妲 妹 妻 妾 姆 姉 始 姐 姑 姒 姓 委 姜 姥 姦 姪 姫 姶 姻 姿
威 娑 娘 娜 娠 娩 娯 娶 娼 婆 婚 婢 婦 婬 婿 媒 媚 媛 媼 嫁 嫉 嫋 嫌 嫡 嬉 嬌 嬢 嬪 嬬 嬰
嬲 嬴 嬶 子 孑 孔 孕 字 存 孝 孟 季 孤 学 孩 孫 孵 學 宅 宇 守 安 宋 完 宍 宏 宕 宗 官 宙
定 宛 宜 宝 実 客 宣 室 宥 宦 宮 宰 害 宴 宵 家 宸 容 宿 寂 寄 寅 密 寇 富 寒 寓 寛 寝 寞
察 寡 寥 實 寧 審 寮 寵 寶 寸 对 寺 対 寿 封 専 射 将 將 尉 尊 尋 導 小 少 尖 尚 尤 尨 尭
就 尸 尹 尺 尻 尼 尽 尾 尿 局 屁 居 屈 届 屋 屍 屏 屑 屓 展 属 屠 屡 層 履 屬 屯 山 屹 岐
岡 岨 岩 岫 岬 岱 岳 岸 峙 峠 峡 峨 峩 峯 峰 島 峻 崇 崋 崎 崑 崔 崖 崗 崙 崚 崩 嵌 嵐 嵜
嵩 嵬 嵯 嶄 嶋 嶌 嶺 嶼 嶽 巌 巖 巛 川 州 巡 巣 工 左 巧 巨 巫 差 己 已 巳 巴 巷 巻 巽 巾
市 布 帆 希 帖 帛 帝 帥 師 席 帯 帰 帳 帷 常 帽 幅 幇 幌 幔 幕 幟 幡 幣 干 平 年 并 幸 幹
幻 幼 幽 幾 庁 広 庄 庇 床 序 底 庖 店 庚 府 度 座 庫 庭 庵 庶 康 庸 廃 廉 廊 廓 廟 廠 廣
廬 延 廷 建 廻 弁 弄 弊 弌 弍 式 弐 弑 弓 弔 引 弖 弗 弘 弛 弟 弥 弦 弧 弩 弱 張 強 弼 弾
彊 当 彗 彙 彝 彡 形 彦 彩 彫 彬 彰 影 彷 役 彼 彿 往 征 径 待 徊 律 後 徐 徒 従 得 徘 御
徨 復 循 微 徳 徴 徹 徽 心 必 忌 忍 忖 志 忘 忙 応 忝 忠 快 念 忸 忽 怒 怖 怙 怜 思 怠 急
性 怨 怩 怪 怯 恁 恃 恋 恍 恐 恒 恕 恙 恢 恣 恤 恥 恨 恩 恪 恫 恬 恭 息 恰 恵 悄 悉 悌 悍
悔 悖 悛 悟 悠 患 悦 悧 悩 悪 悲 悴 悶 悸 悼 情 惇 惑 惚 惜 惟 惠 惣 惧 惨 惰 想 惹 愁 愈
愉 意 愕 愚 愛 感 愧 愴 愾 慄 慇 慈 慊 態 慌 慎 慕 慙 慚 慟 慢 慣 慧 慨 慮 慰 慳 慶 慷 慾
憂 憊 憎 憐 憑 憔 憚 憤 憧 憩 憫 憬 憮 憲 憶 憺 憾 懃 懇 應 懊 懍 懐 懣 懦 懲 懶 懸 懺 懼
戈 戉 戊 戌 戎 成 我 戒 或 戚 戟 戦 截 戮 戯 戴 戸 戻 房 所 扁 扇 扈 扉 手 才 打 払 托 扠
扮 扱 扶 批 扼 承 技 抄 抉 把 抑 抒 抓 投 抗 折 抛 抜 択 披 抱 抵 抹 押 抽 担 拇 拉 拌 拍
拐 拒 拓 拗 拘 拙 招 拝 拠 拡 括 拭 拮 拱 拳 拵 拶 拷 拾 拿 持 挂 指 按 挑 挙 挟 挧 挨 挫
振 挺 挽 挿 捉 捌 捏 捐 捕 捗 捜 捥 捧 捨 捩 据 捲 捷 捺 捻 掃 授 掉 掌 掎 掏 排 掘 掛 掟
掠 採 探 掣 接 控 推 掩 措 掬 掲 掴 掻 揃 揄 揆 揉 描 提 揖 揚 換 握 揮 援 揶 揺 損 搏 搗
搦 搬 搭 携 搾 摂 摎 摑 摘 摩 摯 摶 摸 摺 撃 撒 撓 撚 撞 撤 撥 撫 播 撮 撰 撲 撹 撻 撼 擁
擂 操 擡 擢 擦 擬 擲 擽 擾 攀 攘 攣 攪 攫 支 攵 攸 改 攻 放 政 故 敏 救 敗 教 敢 散 敦 敬
数 敲 整 敵 敷 斂 斃 文 斉 斎 斐 斑 斗 料 斜 斟 斡 斤 斥 斧 斬 断 斯 新 斷 方 於 施 旁 旅
旆 旋 旌 族 旒 旗 无 既 日 旦 旧 旨 早 旬 旭 旱 时 旺 昂 昆 昇 昊 昌 明 昏 易 昔 星 映 春
昧 昨 昭 是 昴 昵 昼 時 晃 晋 晏 晒 晦 晨 晩 普 景 晰 晴 晶 智 暁 暄 暇 暈 暉 暎 暑 暖 暗
暢 暦 暫 暮 暴 暹 曄 曇 曖 曙 曜 曝 曠 曰 曲 曳 更 曷 書 曹 曺 曼 曽 曾 替 最 會 月 有 朋
服 朔 朕 朗 望 朝 期 朦 朧 木 未 末 本 札 朱 朴 朶 机 朽 杉 杌 李 杏 材 村 杓 杖 杙 杜 杞
束 杠 条 来 杭 杯 東 杳 杵 杷 松 板 枇 枉 析 枕 林 枚 果 枝 枠 枡 枢 枯 枳 架 枷 枸 柄 柊
柏 某 柑 染 柔 柘 柚 柝 柩 柱 柳 柴 柵 査 柾 柿 栂 栃 栄 栓 栖 栗 栞 校 株 核 根 格 栽 桁
桂 桃 案 桎 桐 桑 桒 桓 桔 桜 桟 桧 桴 桶 桿 梁 梃 梅 梏 梓 梔 梗 條 梟 梢 梧 梨 梯 械 梱
梲 梳 梵 梶 梻 棄 棋 棍 棒 棕 棗 棘 棚 棟 棠 森 棲 棹 棺 椀 椅 椋 植 椎 椏 椒 椚 椛 検 椥
椰 椴 椿 楊 楓 楔 楕 楚 楝 楠 楡 楢 業 楯 楳 極 楸 楼 楽 榀 概 榊 榎 榑 榛 榜 榮 榴 槃 槇
構 槌 槍 槐 槓 様 槙 槻 槽 槿 樂 樅 樊 樋 樓 標 樟 模 樣 権 横 樫 樵 樹 樺 樽 橄 橅 橇 橈
橋 橘 橙 機 檀 檄 檎 檔 檜 檣 檬 檮 檸 檻 櫂 櫃 櫓 櫚 櫛 櫞 櫟 櫺 櫻 欄 欅 欒 欖 欠 次 欣
欧 欲 欹 欺 欽 款 歌 歎 歓 歡 止 正 此 武 歩 歪 歯 歳 歴 死 殃 殆 殉 殊 残 殖 殛 殤 殪 殯
殱 殲 殴 段 殷 殺 殻 殿 毀 毅 母 毎 毒 比 毘 毛 毟 毬 毯 毳 氈 氏 民 気 氣 水 氷 永 氾 汀
汁 求 汎 汐 汗 汚 汝 汞 江 池 汰 汲 決 汽 沁 沂 沃 沈 沌 沐 沓 沖 沙 沛 没 沢 沫 沮 河 沸
油 治 沼 沽 沿 況 泄 泉 泊 泌 法 泗 泡 波 泣 泥 注 泪 泰 泳 洋 洌 洒 洗 洛 洞 洟 津 洩 洪
洱 洲 洸 活 派 流 浄 浅 浙 浚 浜 浣 浦 浩 浪 浮 浴 海 浸 涅 消 涌 涎 涙 涛 涜 涯 液 涸 涼
淀 淋 淑 淘 淙 淡 淨 淫 淮 深 淳 淵 混 淹 添 清 渇 済 渉 渋 渓 渕 渚 減 渟 渠 渡 渣 渤 渦
温 測 港 游 渾 湃 湊 湍 湑 湖 湘 湛 湣 湧 湫 湮 湯 湾 湿 満 溌 源 準 溜 溝 溢 溶 溺 滄 滅
滉 滋 滎 滑 滓 滝 滞 滬 滲 滴 滸 滾 漁 漂 漆 漉 漏 漑 漓 演 漕 漠 漢 漣 漫 漬 漱 漲 漸 漿
潁 潅 潑 潔 潘 潜 潟 潤 潮 潰 澁 澄 澎 澤 澪 澱 澳 澹 激 濁 濃 濘 濛 濠 濡 濤 濫 濮 濯 濱
濾 瀆 瀉 瀑 瀕 瀚 瀝 瀞 瀟 瀧 瀬 瀰 瀾 灌 灘 火 灯 灰 灸 灼 災 炉 炊 炎 炒 炙 炬 炭 炮 炸
点 為 烈 烏 烙 烹 烽 焉 焔 焙 焚 焜 無 焦 焱 然 焼 煉 煌 煎 煕 煖 煙 煤 煥 照 煩 煮 煽 熈
熊 熔 熙 熟 熨 熱 熾 燁 燃 燈 燎 燐 燕 燗 燠 燥 燦 燬 燭 燵 燻 燼 燿 爆 爛 爨 爪 爬 爱 爵
父 爺 爻 爽 爾 牆 片 版 牌 牒 牙 牛 牝 牟 牡 牢 牧 物 牲 特 牽 犀 犇 犍 犠 犬 犯 犲 状 狂
狄 狆 狐 狒 狗 狙 狛 狡 狢 狩 独 狭 狷 狸 狼 狽 猊 猖 猛 猜 猟 猥 猩 猪 猫 献 猴 猶 猾 猿
獄 獅 獏 獠 獣 獨 獪 獰 獲 獺 玄 率 玉 王 玖 玩 玲 玳 玻 珀 珈 珊 珍 珎 珠 珪 班 現 球 理
琉 琢 琥 琲 琳 琴 琵 琶 琼 瑁 瑕 瑙 瑚 瑛 瑜 瑞 瑠 瑣 瑤 瑪 瑾 璃 璧 環 璽 瓊 瓏 瓜 瓠 瓢
瓦 瓶 甕 甘 甚 甜 生 産 甥 甦 用 甫 田 由 甲 申 男 町 画 界 畏 畑 畔 留 畜 畝 畠 畢 略 畦
番 異 畳 當 畷 畿 疆 疇 疋 疎 疑 疚 疣 疫 疱 疲 疵 疸 疹 疼 疽 疾 痂 病 症 痍 痒 痔 痕 痘
痙 痛 痢 痣 痩 痰 痴 痺 痼 痾 瘋 瘍 瘡 瘣 瘤 瘴 瘻 療 癇 癌 癒 癖 癩 癪 癰 癲 癸 発 登 發
白 百 的 皆 皇 皋 皎 皐 皓 皙 皮 皰 皹 皺 皿 盃 盆 益 盒 盗 盛 盞 盟 監 盤 盥 盧 盪 目 盲
直 相 盾 省 眈 眉 看 県 眞 真 眠 眦 眩 眷 眸 眺 眼 着 睛 睡 督 睦 睨 睫 睾 瞋 瞑 瞞 瞠 瞥
瞬 瞭 瞰 瞳 瞼 矍 矛 矜 矢 知 矩 短 矮 矯 石 砂 砒 研 砕 砥 砦 砧 砰 砲 破 硝 硫 硬 硯 硼
碁 碇 碌 碍 碑 碓 碗 碧 碩 確 磁 磊 磋 磐 磔 磧 磨 磯 礁 礎 礫 礬 示 礼 社 祀 祇 祈 祉 祐
祓 祖 祝 神 祟 祠 祢 祥 票 祭 祷 禁 禄 禅 禊 禍 禎 福 禦 禮 禰 禺 禽 禾 禿 秀 私 秋 科 秒
秘 租 秤 秦 秩 称 移 稀 程 税 稔 稗 稚 稜 稟 稠 種 稲 稷 稼 稽 稿 穀 穂 穆 積 穎 穏 穗 穢
穣 穫 穴 究 穹 空 穽 穿 突 窃 窄 窒 窓 窖 窗 窘 窟 窩 窪 窮 窯 窶 窺 竃 竄 竅 竈 立 站 竜
竟 章 竣 童 竦 竪 竭 端 競 竹 竺 竿 笄 笈 笊 笏 笑 笙 笛 笞 笠 笥 符 第 笹 筆 筈 等 筋 筌
筍 筏 筐 筑 筒 答 策 筧 筵 箆 箇 箋 箍 箏 箒 箔 箕 算 箝 管 箪 箭 箱 箴 箸 節 範 篇 築 篝
篠 篤 篦 篩 篭 簀 簒 簗 簡 簪 簳 簾 簿 籃 籍 籐 籔 籠 籤 米 籾 粉 粋 粒 粕 粗 粘 粛 粟 粥
粧 粱 粳 粹 粽 精 糊 糖 糜 糞 糟 糠 糧 糯 糸 系 糾 紀 紂 約 紅 紆 紊 紋 納 紐 純 紗 紘 紙
級 紛 素 紡 索 紫 紬 紮 累 細 紳 紹 紺 終 絃 組 絆 経 絎 結 絞 絡 絢 給 絨 統 絲 絵 絶 絹
絽 継 続 綜 綬 維 綯 綱 網 綴 綸 綺 綻 綽 綾 綿 緊 緋 総 緑 緒 緘 線 緞 締 編 緩 緬 緯 練
緻 縁 縄 縅 縊 縋 縒 縛 縞 縢 縣 縦 縫 縮 縷 縹 縺 績 繁 繃 繊 繋 繍 織 繕 繚 繞 繡 繭 繰
纂 纈 纏 组 给 缶 罅 罌 罔 罠 罧 罪 罫 置 罰 署 罵 罷 罹 羅 羆 羈 羊 羌 美 羚 羞 群 羨 義
羯 羹 羽 翁 翅 翌 習 翔 翟 翠 翡 翦 翰 翳 翻 翼 耀 老 考 耄 者 耆 而 耐 耕 耗 耘 耳 耶 耽
耿 聊 聖 聘 聚 聞 聡 聰 聳 聴 職 聾 肅 肆 肇 肉 肋 肌 肖 肘 肚 肛 肝 股 肢 肥 肩 肪 肯 肱
育 肴 肺 胃 胄 胆 背 胎 胚 胝 胞 胡 胤 胥 胱 胴 胸 胼 能 脂 脅 脆 脇 脈 脊 脚 脛 脱 脳 脹
腋 腎 腐 腑 腓 腔 腕 腥 腫 腰 腱 腸 腹 腺 腿 膀 膂 膊 膏 膚 膜 膝 膠 膣 膨 膳 膵 膻 膾 膿
臀 臂 臆 臍 臑 臓 臙 臣 臥 臧 臨 自 臭 至 致 臼 舁 舅 與 興 舌 舎 舐 舒 舗 舘 舜 舞 舟 舩
航 舫 般 舳 舵 舶 舷 舸 船 艇 艘 艤 艦 艨 艪 艫 艮 良 艱 色 艶 艾 芋 芍 芒 芙 芝 芥 芦 芭
芯 花 芳 芸 芹 芻 芽 苅 苑 苔 苗 苛 苞 苣 若 苦 苧 苫 英 苺 茂 范 茄 茅 茉 茎 茗 茘 茜 茣
茨 茫 茱 茴 茶 茸 茹 荀 草 荊 荏 荒 荘 荷 荻 荼 莉 莢 莫 莱 莽 菅 菇 菊 菌 菓 菖 菘 菜 菟
菠 菩 菫 華 菰 菱 萃 萄 萌 萎 萠 萩 萬 萱 萵 萸 落 葈 葉 葎 著 葛 葡 董 葦 葫 葬 葭 葱 葵
葺 蒋 蒐 蒔 蒙 蒜 蒟 蒡 蒲 蒸 蒻 蒼 蓄 蓉 蓋 蓑 蓖 蓙 蓬 蓮 蓴 蓼 蔑 蔓 蔔 蔕 蔗 蔡 蔦 蔬
蔭 蔵 蔽 蕁 蕃 蕈 蕉 蕊 蕎 蕗 蕨 蕩 蕪 蕭 蕷 蕾 薄 薇 薊 薐 薔 薗 薙 薦 薨 薩 薪 薫 薬 薮
薯 薹 薺 藁 藉 藍 藏 藜 藝 藤 藩 藪 藷 藹 藺 藻 蘆 蘇 蘊 蘭 蘿 虎 虐 虔 處 虚 虜 虞 號 虫
虱 虹 虻 蚊 蚋 蚓 蚕 蚤 蚩 蚯 蚰 蛄 蛆 蛇 蛉 蛋 蛍 蛎 蛙 蛛 蛞 蛟 蛤 蛭 蛮 蛯 蛸 蛹 蛾 蜀
蜂 蜃 蜆 蜉 蜊 蜋 蜒 蜘 蜜 蜥 蜩 蜴 蜷 蜻 蜾 蝉 蝋 蝎 蝓 蝕 蝗 蝙 蝠 蝣 蝦 蝨 蝮 蝶 蝸 蝿
螂 融 螢 螫 螳 螺 螻 螽 蟀 蟄 蟇 蟋 蟒 蟜 蟠 蟯 蟲 蟷 蟹 蟻 蠃 蠅 蠍 蠕 蠢 蠣 蠱 蠹 血 衆
行 衒 術 街 衙 衛 衝 衞 衡 衣 表 衰 衷 衾 衿 袁 袂 袈 袋 袍 袖 袢 被 袱 袴 袷 裁 裂 装 裏
裔 裕 補 裟 裡 裳 裸 製 裾 褄 複 褌 褐 褒 褓 褞 褥 褪 褸 褻 襁 襄 襖 襞 襟 襤 襦 襲 襷 西
要 覆 覇 見 規 視 覗 覚 覧 親 覯 観 覿 见 角 觝 解 触 言 訂 訃 計 訊 討 訓 託 記 訛 訝 訞
訟 訣 訥 訪 設 許 訳 訴 訶 診 証 詈 詐 詔 評 詛 詞 詠 詢 詣 試 詩 詫 詭 詮 詰 話 該 詳 誂
誅 誇 誉 誌 認 誑 誓 誕 誘 語 誠 誣 誤 誦 説 読 誰 課 誹 誼 誾 調 諂 諄 談 請 諌 諍 諏 諒
論 諚 諛 諜 諡 諤 諦 諧 諫 諭 諮 諱 諸 諺 諾 謀 謁 謂 謄 謎 謐 謖 謗 謙 講 謝 謡 謨 謬 謳
謹 識 譚 譜 警 譫 議 譲 譴 護 讃 讐 讒 讓 讚 译 诸 谷 谿 豆 豈 豊 豌 豚 象 豪 豫 豹 豺 貂
貌 貘 貝 貞 負 財 貢 貧 貨 販 貪 貫 責 貮 貯 貰 貴 貶 買 貸 費 貼 貽 貿 賀 賁 賂 賃 賄 資
賈 賊 賎 賑 賓 賛 賜 賞 賠 賢 賣 賤 賦 質 賭 賺 購 賽 贄 贅 贈 贋 贔 贖 赤 赦 赫 赭 走 赴
起 超 越 趙 趣 趨 足 趾 跋 距 跟 跡 跨 跪 路 跳 践 踉 踊 踏 踝 踠 踪 踵 蹂 蹄 蹇 蹉 蹊 蹌
蹙 蹟 蹲 蹴 躁 躄 躅 躇 躊 躍 躑 躓 躙 身 躬 躯 躰 躱 躾 軈 車 軋 軌 軍 軒 軛 軟 転 軫 軸
軻 軼 軽 較 載 輌 輔 輝 輩 輪 輯 輳 輸 輻 輿 轂 轄 轆 轍 轟 轡 轢 轤 轴 辛 辜 辞 辟 辣 辰
辱 農 辺 辻 込 辿 迂 迄 迅 迎 近 返 迚 迦 迫 迭 述 迷 迸 追 退 送 逃 逅 逆 逍 透 逐 途 逗
這 通 逝 逞 速 造 逡 逢 連 逮 週 進 逸 逼 遁 遂 遅 遇 遊 運 遍 過 道 達 違 遙 遜 遠 遡 遣
遥 適 遭 遮 遵 遶 遷 選 遺 遼 遽 避 邀 邁 邂 邃 還 邇 邉 邏 邑 那 邦 邪 邯 邸 郁 郊 郎 郛
郡 部 郭 郵 郷 都 鄒 鄙 鄭 鄲 鄽 酉 酊 酌 配 酎 酒 酔 酢 酣 酩 酪 酬 酵 酷 酸 醂 醇 醋 醍
醐 醒 醗 醜 醤 醪 醸 采 釈 釉 里 重 野 量 金 釘 釜 針 釣 釦 釧 釵 鈍 鈎 鈞 鈩 鈴 鈷 鈿 鉄
鉈 鉋 鉏 鉗 鉛 鉞 鉢 鉤 鉦 鉱 鉾 銀 銃 銅 銓 銘 銚 銛 銜 銭 鋏 鋒 鋤 鋭 鋲 鋳 鋸 鋼 錆 錏
錐 錘 錚 錠 錦 錨 錫 錬 錮 錯 録 鍋 鍍 鍔 鍛 鍬 鍮 鍵 鍼 鍾 鎌 鎖 鎗 鎚 鎧 鎬 鎮 鎰 鎹 鏃
鏑 鏖 鏝 鏡 鏢 鏤 鏨 鐔 鐘 鐙 鐚 鐵 鐸 鑑 鑚 鑞 鑠 鑢 鑼 鑽 鑿 镖 長 門 閂 閃 閇 閉 開 閏
閑 閒 間 閘 関 閣 閤 閥 閧 閨 閭 閲 閻 閾 闇 闊 闌 闍 闐 闖 闘 關 闢 闥 间 阜 阪 防 阻 阿
陀 附 陋 降 限 陛 陜 院 陣 除 陥 陪 陰 陳 陵 陶 陸 険 陽 隅 隆 隈 隊 隋 階 随 隔 隕 隘 隙
際 障 隠 隣 隧 隰 隴 隷 隻 隼 雀 雁 雄 雅 集 雇 雉 雋 雌 雍 雑 雕 雙 雛 離 難 雨 雪 雫 雰
雲 零 雷 雹 電 需 霄 霆 震 霊 霐 霙 霜 霞 霧 霰 露 霹 靂 靄 青 靖 静 非 靡 面 靨 革 靫 靭
靱 靴 鞁 鞄 鞆 鞋 鞍 鞘 鞠 鞣 鞭 鞴 韃 韋 韓 韮 音 韻 響 頁 頂 頃 項 順 須 預 頑 頒 頓 頗
領 頚 頤 頬 頭 頷 頸 頻 頼 頽 顆 題 額 顎 顏 顔 顕 願 顚 顛 類 顧 顰 顳 風 颪 颯 颱 颶 飄
飛 飜 食 飢 飩 飯 飲 飴 飼 飽 飾 餃 餅 餉 養 餌 餐 餓 餞 餡 館 餮 饂 饅 饉 饌 饒 饕 饗 首
馗 馘 香 馥 馨 馬 馭 馮 馳 馴 駁 駄 駅 駆 駈 駐 駒 駕 駝 駱 駿 騎 騒 験 騙 騨 騰 騾 驀 驁
驃 驍 驕 驚 驟 驢 驤 驪 骨 骸 髄 髎 髏 髑 體 高 髙 髢 髪 髭 髮 髯 髱 髷 髻 鬆 鬘 鬚 鬢 鬣
鬨 鬩 鬱 鬻 鬼 魁 魂 魃 魄 魅 魍 魎 魏 魑 魔 魘 魚 魯 鮃 鮎 鮑 鮒 鮓 鮗 鮟 鮠 鮨 鮪 鮫 鮭
鮮 鮴 鯉 鯊 鯒 鯔 鯖 鯛 鯣 鯨 鯰 鯱 鯵 鰆 鰈 鰊 鰌 鰍 鰐 鰓 鰤 鰥 鰭 鰯 鰰 鰹 鰻 鱇 鱈 鱒
鱗 鱚 鱧 鱶 鱸 鳥 鳩 鳰 鳳 鳴 鳶 鴇 鴉 鴎 鴒 鴛 鴦 鴨 鴫 鴬 鴻 鵄 鵜 鵞 鵠 鵡 鵬 鵯 鵲 鵺
鶇 鶉 鶏 鶙 鶚 鶫 鶯 鶲 鶴 鶸 鶺 鶿 鷂 鷇 鷲 鷸 鷹 鷺 鷽 鸚 鸛 鹵 鹸 鹹 鹿 麃 麋 麒 麓 麗
麝 麟 麦 麩 麴 麵 麸 麹 麺 麻 麼 麾 麿 黄 黍 黎 黐 黑 黒 黙 黛 黴 黽 鼈 鼎 鼓 鼠 鼬 鼯 鼻
鼾 齎 齕 齟 齢 齣 齧 齪 齬 齷 龍 龐 隆 﨑
""")

alpha = character_set("""
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
a b c d e f g h i j k l m n o p q r s t u v w x y z
Ａ Ｂ Ｃ Ｄ Ｅ Ｆ Ｇ Ｈ Ｉ Ｊ Ｋ Ｌ Ｍ Ｎ Ｏ Ｐ Ｑ Ｒ Ｓ Ｔ Ｕ Ｖ Ｗ Ｘ Ｙ Ｚ
ａ ｂ ｃ ｄ ｅ ｆ ｇ ｈ ｉ ｊ ｋ ｌ ｍ ｎ ｏ ｐ ｑ ｒ ｓ ｔ ｕ ｖ ｗ ｘ ｙ ｚ
""")

numeric = character_set("""
0 1 2 3 4 5 6 7 8 9
０ １ ２ ３ ４ ５ ６ ７ ８ ９
""")

alphanumeric = alpha.union(numeric)

halfwidth_kana = {
    'ｧ': 'ァ',
    'ｱ': 'ア',
    'ｨ': 'ィ',
    'ｲ': 'イ',
    'ｩ': 'ゥ',
    'ｳ': 'ウ',
    'ｪ': 'ェ',
    'ｴ': 'エ',
    'ｫ': 'ォ',
    'ｵ': 'オ',
    'ｶ': 'カ',
    'ｶﾞ': 'ガ',
    'ｷ': 'キ',
    'ｷﾞ': 'ギ',
    'ｸ': 'ク',
    'ｸﾞ': 'グ',
    'ｹ': 'ケ',
    'ｹﾞ': 'ゲ',
    'ｺ': 'コ',
    'ｺﾞ': 'ゴ',
    'ｻ': 'サ',
    'ｻﾞ': 'ザ',
    'ｼ': 'シ',
    'ｼﾞ': 'ジ',
    'ｽ': 'ス',
    'ｽﾞ': 'ズ',
    'ｾ': 'セ',
    'ｾﾞ': 'ゼ',
    'ｿ': 'ソ',
    'ｿﾞ': 'ゾ',
    'ﾀ': 'タ',
    'ﾀﾞ': 'ダ',
    'ﾁ': 'チ',
    'ﾁﾞ': 'ヂ',
    'ｯ': 'ッ',
    'ﾂ': 'ツ',
    'ﾂﾞ': 'ヅ',
    'ﾃ': 'テ',
    'ﾃﾞ': 'デ',
    'ﾄ': 'ト',
    'ﾄﾞ': 'ド',
    'ﾅ': 'ナ',
    'ﾆ': 'ニ',
    'ﾇ': 'ヌ',
    'ﾈ': 'ネ',
    'ﾉ': 'ノ',
    'ﾊ': 'ハ',
    'ﾊﾞ': 'バ',
    'ﾊﾟ': 'パ',
    'ﾋ': 'ヒ',
    'ﾋﾞ': 'ビ',
    'ﾋﾟ': 'ピ',
    'ﾌ': 'フ',
    'ﾌﾞ': 'ブ',
    'ﾌﾟ': 'プ',
    'ﾍ': 'ヘ',
    'ﾍﾞ': 'ベ',
    'ﾍﾟ': 'ペ',
    'ﾎ': 'ホ',
    'ﾎﾞ': 'ボ',
    'ﾎﾟ': 'ポ',
    'ﾏ': 'マ',
    'ﾐ': 'ミ',
    'ﾑ': 'ム',
    'ﾒ': 'メ',
    'ﾓ': 'モ',
    'ｬ': 'ャ',
    'ﾔ': 'ヤ',
    'ｭ': 'ュ',
    'ﾕ': 'ユ',
    'ｮ': 'ョ',
    'ﾖ': 'ヨ',
    'ﾗ': 'ラ',
    'ﾘ': 'リ',
    'ﾙ': 'ル',
    'ﾚ': 'レ',
    'ﾛ': 'ロ',
    'ﾜ': 'ワ',
    'ｦ': 'ヲ',
    'ﾝ': 'ン',
    'ｳﾞ': 'ヴ',
    'ｰ': 'ー',
    '～': '〜'
}

other = character_set("""
〜 ー ･ ・ 々 〇
""")

permitted = hiragana.union(katakana).union(kanji).union(other)
