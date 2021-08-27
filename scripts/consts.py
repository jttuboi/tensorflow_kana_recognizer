FONTS_FOLDER = "fonts/"
IMAGES_FOLDER = "images/"
IMAGES_READY_FOLDER = "images_ready/"
IMAGE_EXTENSION_FILE = "png"

INIT_SQUARE_SIZE = 97 # set to 48, take off +-20% of 48 pixels
FINAL_SQUARE_SIZE_X = 128
FINAL_SQUARE_SIZE_Y = 127 # set to 48, 40 pixels is kana, 8 pixels is for border
TRAIN_SQUARE_SIZE_X = 32
TRAIN_SQUARE_SIZE_Y = 32
BACKGROUND_COLOR = (255, 255, 255, 255) # white

HIRAGANA = "hiragana"
KATAKANA = "katakana"

MODEL_FOLDER = "_model/"
TFLITE_EXTENSION = ".tflite"

ACCURACY_ACCEPTED = 97.0
EPOCHS = 30

# it can change the values. these values represent the kana id used by tensorflow.
unicode_map = {
    # hiragana TTF

    "uni3042": "100", # あ
    "uni3044": "101", # い
    "uni3046": "102", # う
    "uni3048": "103", # え
    "uni304A": "104", # お
    
    "uni304B": "105", # か
    "uni304D": "106", # き
    "uni304F": "107", # く
    "uni3051": "108", # け
    "uni3053": "109", # こ
    
    "uni3055": "110", # さ
    "uni3057": "111", # し
    "uni3059": "112", # す
    "uni305B": "113", # せ
    "uni305D": "114", # そ
    
    "uni305F": "115", # た
    "uni3061": "116", # ち
    "uni3064": "117", # つ
    "uni3066": "118", # て
    "uni3068": "119", # と
    
    "uni306A": "120", # な
    "uni306B": "121", # に
    "uni306C": "122", # ぬ
    "uni306D": "123", # ね
    "uni306E": "124", # の
    
    "uni306F": "125", # は
    "uni3072": "126", # ひ
    "uni3075": "127", # ふ
    "uni3078": "128", # へ
    "uni307B": "129", # ほ
    
    "uni307E": "130", # ま
    "uni307F": "131", # み
    "uni3080": "132", # む
    "uni3081": "133", # め
    "uni3082": "134", # も
    
    "uni3084": "135", # や
    "uni3086": "136", # ゆ
    "uni3088": "137", # よ
    
    "uni3089": "138", # ら
    "uni308A": "139", # り
    "uni308B": "140", # る
    "uni308C": "141", # れ
    "uni308D": "142", # ろ
    
    "uni308F": "143", # わ
    "uni3092": "144", # を
    
    "uni3093": "145", # ん
    
    "uni304C": "146", # が
    "uni304E": "147", # ぎ
    "uni3050": "148", # ぐ
    "uni3052": "149", # げ
    "uni3054": "150", # ご
    
    "uni3056": "151", # ざ
    "uni3058": "152", # じ
    "uni305A": "153", # ず
    "uni305C": "154", # ぜ
    "uni305E": "155", # ぞ
    
    "uni3060": "156", # だ
    "uni3062": "157", # ぢ
    "uni3065": "158", # づ
    "uni3067": "159", # で
    "uni3069": "160", # ど
    
    "uni3070": "161", # ば
    "uni3073": "162", # び
    "uni3076": "163", # ぶ
    "uni3079": "164", # べ
    "uni307C": "165", # ぼ
    
    "uni3071": "166", # ぱ
    "uni3074": "167", # ぴ
    "uni3077": "168", # ぷ
    "uni307A": "169", # ぺ
    "uni307D": "170", # ぽ
    
    # "uni3041": "171", # ぁ
    # "uni3043": "172", # ぃ
    # "uni3045": "173", # ぅ
    # "uni3047": "174", # ぇ
    # "uni3049": "175", # ぉ
    
    # "uni3063": "176", # っ
    
    # "uni3083": "177", # ゃ
    # "uni3085": "178", # ゅ
    # "uni3087": "179", # ょ
    
    # hiragana TTF discarted
    
    # "uni309D": "180", # ゝ
    # "uni309E": "181", # ゞ
    
    # "uni308E": "182", # ゎ
    # "uni3094": "183", # ゔ
    # "uni3095": "184", # ゕ
    # "uni3096": "185", # ゖ
    
    # "uni309B": "186", # ゛
    # "uni309C": "187", # ゜
    
    # katakana TTF
    
    "uni30A2": "200", # ア
    "uni30A4": "201", # イ
    "uni30A6": "202", # ウ
    "uni30A8": "203", # エ
    "uni30AA": "204", # オ
    
    "uni30AB": "205", # カ
    "uni30AD": "206", # キ
    "uni30AF": "207", # ク
    "uni30B1": "208", # ケ
    "uni30B3": "209", # コ
    
    "uni30B5": "210", # サ
    "uni30B7": "211", # シ
    "uni30B9": "212", # ス
    "uni30BB": "213", # セ
    "uni30BD": "214", # ソ
    
    "uni30BF": "215", # タ
    "uni30C1": "216", # チ
    "uni30C4": "217", # ツ
    "uni30C6": "218", # テ
    "uni30C8": "219", # ト
    
    "uni30CA": "220", # ナ
    "uni30CB": "221", # ニ
    "uni30CC": "222", # ヌ
    "uni30CD": "223", # ネ
    "uni30CE": "224", # ノ
    
    "uni30CF": "225", # ハ
    "uni30D2": "226", # ヒ
    "uni30D5": "227", # フ
    "uni30D8": "228", # ヘ
    "uni30DB": "229", # ホ
    
    "uni30DE": "230", # マ
    "uni30DF": "231", # ミ
    "uni30E0": "232", # ム
    "uni30E1": "233", # メ
    "uni30E2": "234", # モ
    
    "uni30E4": "235", # ヤ
    "uni30E6": "236", # ユ
    "uni30E8": "237", # ヨ
    
    "uni30E9": "238", # ラ
    "uni30EA": "239", # リ
    "uni30EB": "240", # ル
    "uni30EC": "241", # レ
    "uni30ED": "242", # ロ
    
    "uni30EF": "243", # ワ
    "uni30F2": "244", # ヲ
    
    "uni30F3": "245", # ン
    
    "uni30AC": "246", # ガ
    "uni30AE": "247", # ギ
    "uni30B0": "248", # グ
    "uni30B2": "249", # ゲ
    "uni30B4": "250", # ゴ
    
    "uni30B6": "251", # ザ
    "uni30B8": "252", # ジ
    "uni30BA": "253", # ズ
    "uni30BC": "254", # ゼ
    "uni30BE": "255", # ゾ
    
    "uni30C0": "256", # ダ
    "uni30C2": "257", # ヂ
    "uni30C5": "258", # ヅ
    "uni30C7": "259", # デ
    "uni30C9": "260", # ド
    
    "uni30D0": "261", # バ
    "uni30D3": "262", # ビ
    "uni30D6": "263", # ブ
    "uni30D9": "264", # ベ
    "uni30DC": "265", # ボ
    
    "uni30D1": "266", # パ
    "uni30D4": "267", # ピ
    "uni30D7": "268", # プ
    "uni30DA": "269", # ペ
    "uni30DD": "270", # ポ
    
    # "uni30A1": "271", # ァ
    # "uni30A3": "272", # ィ
    # "uni30A5": "273", # ゥ
    # "uni30A7": "274", # ェ
    # "uni30A9": "275", # ォ
    
    # "uni30C3": "276", # ッ
    
    # "uni30E3": "277", # ャ
    # "uni30E5": "278", # ュ
    # "uni30E7": "279", # ョ
    
    "uni30FC": "280", # ー
    
    # katakana TTF discarted
    
    # "uni30FD": "281", # ヽ
    # "uni30FE": "282", # ヾ
    
    # "uni30EE": "283", # ヮ
    # "uni30F4": "284", # ヴ
    # "uni30F5": "285", # ヵ
    # "uni30F6": "286", # ヶ
    # "uni30F7": "287", # ヷ
    # "uni30FA": "288", # ヺ

    # hiragana OTF

    "Japan1.843": "100", # あ
    "Japan1.845": "101", # い
    "Japan1.847": "102", # う
    "Japan1.849": "103", # え
    "Japan1.851": "104", # お
    
    "Japan1.852": "105", # か
    "Japan1.854": "106", # き
    "Japan1.856": "107", # く
    "Japan1.858": "108", # け
    "Japan1.860": "109", # こ
    
    "Japan1.862": "110", # さ
    "Japan1.864": "111", # し
    "Japan1.866": "112", # す
    "Japan1.868": "113", # せ
    "Japan1.870": "114", # そ
    
    "Japan1.872": "115", # た
    "Japan1.874": "116", # ち
    "Japan1.877": "117", # つ
    "Japan1.879": "118", # て
    "Japan1.881": "119", # と
    
    "Japan1.883": "120", # な
    "Japan1.884": "121", # に
    "Japan1.885": "122", # ぬ
    "Japan1.886": "123", # ね
    "Japan1.887": "124", # の
    
    "Japan1.888": "125", # は
    "Japan1.891": "126", # ひ
    "Japan1.894": "127", # ふ
    "Japan1.897": "128", # へ
    "Japan1.900": "129", # ほ
    
    "Japan1.903": "130", # ま
    "Japan1.904": "131", # み
    "Japan1.905": "132", # む
    "Japan1.906": "133", # め
    "Japan1.907": "134", # も
    
    "Japan1.909": "135", # や
    "Japan1.911": "136", # ゆ
    "Japan1.913": "137", # よ
    
    "Japan1.914": "138", # ら
    "Japan1.915": "139", # り
    "Japan1.916": "140", # る
    "Japan1.917": "141", # れ
    "Japan1.918": "142", # ろ
    
    "Japan1.920": "143", # わ
    "Japan1.923": "144", # を
    
    "Japan1.924": "145", # ん
    
    "Japan1.853": "146", # が
    "Japan1.855": "147", # ぎ
    "Japan1.857": "148", # ぐ
    "Japan1.859": "149", # げ
    "Japan1.861": "150", # ご
    
    "Japan1.863": "151", # ざ
    "Japan1.865": "152", # じ
    "Japan1.867": "153", # ず
    "Japan1.869": "154", # ぜ
    "Japan1.871": "155", # ぞ
    
    "Japan1.873": "156", # だ
    "Japan1.875": "157", # ぢ
    "Japan1.878": "158", # づ
    "Japan1.880": "159", # で
    "Japan1.882": "160", # ど
    
    "Japan1.889": "161", # ば
    "Japan1.892": "162", # び
    "Japan1.895": "163", # ぶ
    "Japan1.898": "164", # べ
    "Japan1.901": "165", # ぼ
    
    "Japan1.890": "166", # ぱ
    "Japan1.893": "167", # ぴ
    "Japan1.896": "168", # ぷ
    "Japan1.899": "169", # ぺ
    "Japan1.902": "170", # ぽ
    
    # "Japan1.842": "171", # ぁ
    # "Japan1.844": "172", # ぃ
    # "Japan1.846": "173", # ぅ
    # "Japan1.848": "174", # ぇ
    # "Japan1.850": "175", # ぉ
    
    # "Japan1.876": "176", # っ
    
    # "Japan1.908": "177", # ゃ
    # "Japan1.910": "178", # ゅ
    # "Japan1.912": "179", # ょ
    
    # hiragana OTF discarted
    
    # "Japan1.653": "180", # ゝ
    # "Japan1.654": "181", # ゞ
    
    # "Japan1.919": "182", # ゎ
    # "Japan1.7958": "183", # ゔ
    # "Japan1.": "184", # ゕ
    # "Japan1.": "185", # ゖ
    
    # "Japan1.643": "186", # ゛
    # "Japan1.644": "187", # ゜
    
    # katakana OTF
    
    "Japan1.926": "200", # ア
    "Japan1.928": "201", # イ
    "Japan1.930": "202", # ウ
    "Japan1.932": "203", # エ
    "Japan1.934": "204", # オ
    
    "Japan1.935": "205", # カ
    "Japan1.937": "206", # キ
    "Japan1.939": "207", # ク
    "Japan1.941": "208", # ケ
    "Japan1.943": "209", # コ
    
    "Japan1.945": "210", # サ
    "Japan1.947": "211", # シ
    "Japan1.949": "212", # ス
    "Japan1.951": "213", # セ
    "Japan1.953": "214", # ソ
    
    "Japan1.955": "215", # タ
    "Japan1.957": "216", # チ
    "Japan1.960": "217", # ツ
    "Japan1.962": "218", # テ
    "Japan1.964": "219", # ト
    
    "Japan1.966": "220", # ナ
    "Japan1.967": "221", # ニ
    "Japan1.968": "222", # ヌ
    "Japan1.969": "223", # ネ
    "Japan1.970": "224", # ノ
    
    "Japan1.971": "225", # ハ
    "Japan1.974": "226", # ヒ
    "Japan1.977": "227", # フ
    "Japan1.980": "228", # ヘ
    "Japan1.983": "229", # ホ
    
    "Japan1.986": "230", # マ
    "Japan1.987": "231", # ミ
    "Japan1.988": "232", # ム
    "Japan1.989": "233", # メ
    "Japan1.990": "234", # モ
    
    "Japan1.992": "235", # ヤ
    "Japan1.994": "236", # ユ
    "Japan1.996": "237", # ヨ
    
    "Japan1.997": "238", # ラ
    "Japan1.998": "239", # リ
    "Japan1.999": "240", # ル
    "Japan1.1000": "241", # レ
    "Japan1.1001": "242", # ロ
    
    "Japan1.1003": "243", # ワ
    "Japan1.1006": "244", # ヲ
    
    "Japan1.1007": "245", # ン
    
    "Japan1.936": "246", # ガ
    "Japan1.938": "247", # ギ
    "Japan1.940": "248", # グ
    "Japan1.942": "249", # ゲ
    "Japan1.944": "250", # ゴ
    
    "Japan1.946": "251", # ザ
    "Japan1.948": "252", # ジ
    "Japan1.950": "253", # ズ
    "Japan1.952": "254", # ゼ
    "Japan1.954": "255", # ゾ
    
    "Japan1.956": "256", # ダ
    "Japan1.958": "257", # ヂ
    "Japan1.961": "258", # ヅ
    "Japan1.963": "259", # デ
    "Japan1.965": "260", # ド
    
    "Japan1.972": "261", # バ
    "Japan1.975": "262", # ビ
    "Japan1.978": "263", # ブ
    "Japan1.981": "264", # ベ
    "Japan1.984": "265", # ボ
    
    "Japan1.973": "266", # パ
    "Japan1.976": "267", # ピ
    "Japan1.979": "268", # プ
    "Japan1.982": "269", # ペ
    "Japan1.985": "270", # ポ
    
    # "Japan1.925": "271", # ァ
    # "Japan1.927": "272", # ィ
    # "Japan1.929": "273", # ゥ
    # "Japan1.931": "274", # ェ
    # "Japan1.933": "275", # ォ
    
    # "Japan1.959": "276", # ッ
    
    # "Japan1.991": "277", # ャ
    # "Japan1.993": "278", # ュ
    # "Japan1.995": "279", # ョ
    
    "Japan1.660": "280", # ー
    
    # katakana OTF discarted
    
    # "Japan1.651": "281", # ヽ
    # "Japan1.652": "282", # ヾ
    
    # "Japan1.1002": "283", # ヮ
    # "Japan1.1008": "284", # ヴ
    # "Japan1.1009": "285", # ヵ
    # "Japan1.1010": "286", # ヶ
    # "Japan1.8313": "287", # ヷ
    # "Japan1.8316": "288", # ヺ

    # hiragana OTF

    "cid843": "100", # あ
    "cid845": "101", # い
    "cid847": "102", # う
    "cid849": "103", # え
    "cid851": "104", # お
    
    "cid852": "105", # か
    "cid854": "106", # き
    "cid856": "107", # く
    "cid858": "108", # け
    "cid860": "109", # こ
    
    "cid862": "110", # さ
    "cid864": "111", # し
    "cid866": "112", # す
    "cid868": "113", # せ
    "cid870": "114", # そ
    
    "cid872": "115", # た
    "cid874": "116", # ち
    "cid877": "117", # つ
    "cid879": "118", # て
    "cid881": "119", # と
    
    "cid883": "120", # な
    "cid884": "121", # に
    "cid885": "122", # ぬ
    "cid886": "123", # ね
    "cid887": "124", # の
    
    "cid888": "125", # は
    "cid891": "126", # ひ
    "cid894": "127", # ふ
    "cid897": "128", # へ
    "cid900": "129", # ほ
    
    "cid903": "130", # ま
    "cid904": "131", # み
    "cid905": "132", # む
    "cid906": "133", # め
    "cid907": "134", # も
    
    "cid909": "135", # や
    "cid911": "136", # ゆ
    "cid913": "137", # よ
    
    "cid914": "138", # ら
    "cid915": "139", # り
    "cid916": "140", # る
    "cid917": "141", # れ
    "cid918": "142", # ろ
    
    "cid920": "143", # わ
    "cid923": "144", # を
    
    "cid924": "145", # ん
    
    "cid853": "146", # が
    "cid855": "147", # ぎ
    "cid857": "148", # ぐ
    "cid859": "149", # げ
    "cid861": "150", # ご
    
    "cid863": "151", # ざ
    "cid865": "152", # じ
    "cid867": "153", # ず
    "cid869": "154", # ぜ
    "cid871": "155", # ぞ
    
    "cid873": "156", # だ
    "cid875": "157", # ぢ
    "cid878": "158", # づ
    "cid880": "159", # で
    "cid882": "160", # ど
    
    "cid889": "161", # ば
    "cid892": "162", # び
    "cid895": "163", # ぶ
    "cid898": "164", # べ
    "cid901": "165", # ぼ
    
    "cid890": "166", # ぱ
    "cid893": "167", # ぴ
    "cid896": "168", # ぷ
    "cid899": "169", # ぺ
    "cid902": "170", # ぽ
    
    # "cid842": "171", # ぁ
    # "cid844": "172", # ぃ
    # "cid846": "173", # ぅ
    # "cid848": "174", # ぇ
    # "cid850": "175", # ぉ
    
    # "cid876": "176", # っ
    
    # "cid908": "177", # ゃ
    # "cid910": "178", # ゅ
    # "cid912": "179", # ょ
    
    # hiragana OTF discarted
    
    # "cid653": "180", # ゝ
    # "cid654": "181", # ゞ
    
    # "cid919": "182", # ゎ
    # "cid7958": "183", # ゔ
    # "cid": "184", # ゕ
    # "cid": "185", # ゖ
    
    # "cid643": "186", # ゛
    # "cid644": "187", # ゜
    
    # katakana OTF
    
    "cid926": "200", # ア
    "cid928": "201", # イ
    "cid930": "202", # ウ
    "cid932": "203", # エ
    "cid934": "204", # オ
    
    "cid935": "205", # カ
    "cid937": "206", # キ
    "cid939": "207", # ク
    "cid941": "208", # ケ
    "cid943": "209", # コ
    
    "cid945": "210", # サ
    "cid947": "211", # シ
    "cid949": "212", # ス
    "cid951": "213", # セ
    "cid953": "214", # ソ
    
    "cid955": "215", # タ
    "cid957": "216", # チ
    "cid960": "217", # ツ
    "cid962": "218", # テ
    "cid964": "219", # ト
    
    "cid966": "220", # ナ
    "cid967": "221", # ニ
    "cid968": "222", # ヌ
    "cid969": "223", # ネ
    "cid970": "224", # ノ
    
    "cid971": "225", # ハ
    "cid974": "226", # ヒ
    "cid977": "227", # フ
    "cid980": "228", # ヘ
    "cid983": "229", # ホ
    
    "cid986": "230", # マ
    "cid987": "231", # ミ
    "cid988": "232", # ム
    "cid989": "233", # メ
    "cid990": "234", # モ
    
    "cid992": "235", # ヤ
    "cid994": "236", # ユ
    "cid996": "237", # ヨ
    
    "cid997": "238", # ラ
    "cid998": "239", # リ
    "cid999": "240", # ル
    "cid1000": "241", # レ
    "cid1001": "242", # ロ
    
    "cid1003": "243", # ワ
    "cid1006": "244", # ヲ
    
    "cid1007": "245", # ン
    
    "cid936": "246", # ガ
    "cid938": "247", # ギ
    "cid940": "248", # グ
    "cid942": "249", # ゲ
    "cid944": "250", # ゴ
    
    "cid946": "251", # ザ
    "cid948": "252", # ジ
    "cid950": "253", # ズ
    "cid952": "254", # ゼ
    "cid954": "255", # ゾ
    
    "cid956": "256", # ダ
    "cid958": "257", # ヂ
    "cid961": "258", # ヅ
    "cid963": "259", # デ
    "cid965": "260", # ド
    
    "cid972": "261", # バ
    "cid975": "262", # ビ
    "cid978": "263", # ブ
    "cid981": "264", # ベ
    "cid984": "265", # ボ
    
    "cid973": "266", # パ
    "cid976": "267", # ピ
    "cid979": "268", # プ
    "cid982": "269", # ペ
    "cid985": "270", # ポ
    
    # "cid925": "271", # ァ
    # "cid927": "272", # ィ
    # "cid929": "273", # ゥ
    # "cid931": "274", # ェ
    # "cid933": "275", # ォ
    
    # "cid959": "276", # ッ
    
    # "cid991": "277", # ャ
    # "cid993": "278", # ュ
    # "cid995": "279", # ョ
    
    "cid660": "280", # ー
    
    # katakana OTF discarted
    
    # "cid651": "281", # ヽ
    # "cid652": "282", # ヾ
    
    # "cid1002": "283", # ヮ
    # "cid1008": "284", # ヴ
    # "cid1009": "285", # ヵ
    # "cid1010": "286", # ヶ
    # "cid8313": "287", # ヷ
    # "cid8316": "288", # ヺ
}

# fonts can be found in
# https://www.freejapanesefont.com/
# https://fonts.google.com/
# https://japanesefreefont.net/
# https://www.freekanjifonts.com/
# https://fontesk.com/
# https://www.fontspace.com/

fonts_names = [
    "9chan Font.ttf",
    "851 Chikara Dzuyoku.ttf",
    "Asobi Memogaki.ttf",
    "Azuki Font.ttf",
    "Bryndan Handwriting Font.ttf",
    "Bryndan Unifont Font.ttf",
    "Chihaya Fude.ttf",
    "Chihaya Gothic.ttf",
    "Chihaya Jun.ttf",
    "Clay One.ttf",
    "Corporate Logo Maru.ttf",
    "Darts Font.ttf",
    "Dining Message Font.ttf",
    "Fuboh Felt Pen 04.otf",
    "Ghatee.ttf",
    "Guzuri Font 1nensei.ttf",
    "Gyate Luminescence.ttf",
    "Hakusyu Kaisho Bold.ttf",
    "Hanazome Font.ttf",
    "HC Maru Gothic font.ttf",
    "Holiday MDJP03.ttf",
    "HonyaJi Re.ttf",
    "HuiFont.ttf",
    "Iroha Maru Mikami.ttf",
    "Japan Sans.ttf",
    "Jin Pen Keba.otf",
    "Jiyucho.ttf",
    "Kaori Gel Font.ttf",
    "Kawaii Handwriting Font.ttf",
    "K Gothic.ttf",
    "Kiloji.ttf",
    "Klee One Font.ttf",
    "Kodomo Rounded Gothic.otf",
    "Kodomo Rounded Gothic Light.otf",
    "Logo Type Gothic.ttf",
    "Logo Type Gothic Condensed.ttf",
    "Mamelon.otf",
    "Migu font.ttf",
    "Mikachan.ttf",
    "Mitimasu handwriting font.ttf",
    "Mochiy Pop One.ttf",
    "Mogiha pen fonts.ttf",
    "Motoya Kosugi Maru.ttf",
    "Mushin.otf",
    "Otsutome Font.ttf",
    "Rii’s Brush Handwriting.otf",
    "Rounded M+ Font Family.ttf",
    "Sanafon Handwriting Font.ttf",
    "SanafonKaku Handwriting Font.ttf",
    "Sanafonmaru Handwriting Font.ttf",
    "SanafonMugi Handwriting Font.ttf",
    "Sawarabi Gothic.otf",
    "Seto Font.ttf",
    "Shigoto Memogaki.ttf",
    "Shirokuma Font.otf",
    "SistersFB.ttf",
    "SistersFL.ttf",
    "SistersFS.ttf",
    "Smart Font UI.ttf",
    "Soukou Mincho.ttf",
    "Tamuragaki Font.ttf",
    "Tanugo.ttf",
    "Tanuki Font.ttf",
    "Tegaki Zatsu.ttf",
    "Tetsubin gothic.ttf",
    "Umeboshi Font.ttf",
    "Ume Font Gothic.ttf",
    "Ume Font Mincho.ttf",
    "Uzura Font.ttf",
    "Wada Lab Maru Gothic.ttf",
    "Y.OzFont Calligraphy.ttf",
    "Y.OzFont Pen.otf",
    "Yasashisa Gothic Tegaki.otf",
    "Yomogi.ttf",
    "Yuji Syuku Font.ttf",
    "Yusei Magic.ttf",
    "Yuta Coco font.otf",
    "Yutapon Coding font.ttc",
    "Yuzu Pen.ttf",
    "Yuzu Pop A series.ttf",
]
