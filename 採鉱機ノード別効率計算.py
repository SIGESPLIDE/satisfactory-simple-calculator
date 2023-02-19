import re

# -----採鉱機-----

採鉱機産出量 = {"採鉱機Mk1": 60, "採鉱機Mk2": 120, "採鉱機Mk3": 240}
採鉱機Mk1産出量, 採鉱機Mk2産出量, 採鉱機Mk3産出量 = 採鉱機産出量["採鉱機Mk1"], 採鉱機産出量["採鉱機Mk2"], 採鉱機産出量["採鉱機Mk3"]
採鉱機 = ("採鉱機Mk1", "採鉱機Mk2", "採鉱機Mk3")

純度 = {"impure": 0.5, "normal": 1, "pure": 2}
低純度, 中純度, 高純度 = 純度["impure"], 純度["normal"], 純度["pure"]

# -----コンベアベルト-----

コンベアベルト運搬量 = {"コンベアベルトMk1": 60, "コンベアベルトMk2": 120,
              "コンベアベルトMk3": 270, "コンベアベルトMk4": 480, "コンベアベルトMk5": 780}
コンベアベルトMk1運搬量, コンベアベルトMk2運搬量, コンベアベルトMk3運搬量, コンベアベルトMk4運搬量, コンベアベルトMk5運搬量 = コンベアベルト運搬量["コンベアベルトMk1"], コンベアベルト運搬量[
    "コンベアベルトMk2"], コンベアベルト運搬量["コンベアベルトMk3"], コンベアベルト運搬量["コンベアベルトMk4"], コンベアベルト運搬量["コンベアベルトMk5"]
コンベアベルト = ("コンベアベルトMk1", "コンベアベルトMk2",
           "コンベアベルトMk3", "コンベアベルトMk4", "コンベアベルトMk5")

# -----標準入力検知-----
text = input()

# -----オーバークロックレート検出-----
idx_OCrate = text.split(" ")

# chk_OCrateで%についている数字の数を抽出（%があるかどうかの判定と、あった場合、数字を取り出す）
target = '%'
for i in range(len(idx_OCrate)):
    chk_OCrate = idx_OCrate[i].find(target)
    if chk_OCrate == -1:
        method_OCrate = ["100%"]
    else:
        method_OCrate = [s for s in idx_OCrate if s.endswith('%')]
        break

OCrate = method_OCrate[0].split("%")
OCrate = int(OCrate[0])
if not 0.0000 <= OCrate <= 250.0000:
    print("オーバークロック率を入力する際は0.0000%～250.0000%の間の数値で指定してください")
else:
    x = 0
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    if re.search('採鉱機', text):
        print("オーバークロック率="+"["+str(OCrate)+"%]")
        if re.search('mk1|Mk1|mK1|MK1|ｍｋ１|Mk１', text):
            if '低' in text:
                x = 採鉱機Mk1産出量*低純度*OCrate/100
                print("採鉱機Mk1の低純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
            if '中' in text:
                x = 採鉱機Mk1産出量*中純度*OCrate/100
                print("採鉱機Mk1の中純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
            if '高' in text:
                x = 採鉱機Mk1産出量*高純度*OCrate/100
                print("採鉱機Mk1の高純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
        if re.search('mk2|Mk2|mK2|MK2|ｍｋ２|Mk２', text):
            if '低' in text:
                x = 採鉱機Mk2産出量*低純度*OCrate/100
                print("採鉱機Mk2の低純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
            if '中' in text:
                x = 採鉱機Mk2産出量*中純度*OCrate/100
                print("採鉱機Mk2の中純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
            if '高' in text:
                x = 採鉱機Mk2産出量*高純度*OCrate/100
                print("採鉱機Mk2の高純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
        if re.search('mk3|Mk3|mK3|MK3|ｍｋ３|Mk３', text):
            if '低' in text:
                x = 採鉱機Mk3産出量*低純度*OCrate/100
                print("採鉱機Mk3の低純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時[", x, "/m]")
            if '中' in text:
                x = 採鉱機Mk3産出量*中純度*OCrate/100
                print("採鉱機Mk3の中純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時", x, "/m")
            if '高' in text:
                x = 採鉱機Mk3産出量*高純度*OCrate/100
                print("採鉱機Mk3の高純度資源ノードでの産出量は 稼働率"+str(OCrate)+"%の時", x, "/m")
    else:
        print("!^-^-^-^-^-^-^-^_Error_^-^-^-^-^-^-^-^!\n各要素を正しく入力してください\nヒント:各要素に含まれる文字は、'採鉱機' 'Mk(1,2,3)' '(低,中,高)'純度 です\n")

    # -----最低コンベアベルト必要量-----

    minerSUM = x
    Mk1minerSUM = コンベアベルトMk1運搬量-minerSUM
    Mk2minerSUM = コンベアベルトMk2運搬量-minerSUM
    Mk3minerSUM = コンベアベルトMk3運搬量-minerSUM
    Mk4minerSUM = コンベアベルトMk4運搬量-minerSUM
    Mk5minerSUM = コンベアベルトMk5運搬量-minerSUM
    Over_rateSUM = minerSUM - コンベアベルトMk5運搬量
    if minerSUM <= 0:
        print("該当するコンベアベルトはありません")
    elif minerSUM >= 780:
        print(
            "780/mを超えたため、コンベアベルトMk5で780/mのレートで運搬可能、["+str(Over_rateSUM)+"/m]の過剰生産です")
    elif 1 <= minerSUM <= コンベアベルトMk1運搬量:
        if Mk1minerSUM == 0:
            print("コンベアベルトMk1で運搬可能、余剰運搬可能領域はありません")
        else:
            print("コンベアベルトMk1で運搬可能、[", Mk1minerSUM, "/m]の余剰運搬可能領域があります")

    elif コンベアベルトMk1運搬量 < minerSUM <= コンベアベルトMk2運搬量:
        if Mk2minerSUM == 0:
            print("コンベアベルトMk2で運搬可能、余剰運搬可能領域はありません")
        else:
            print("コンベアベルトMk2で運搬可能、[", Mk2minerSUM, "/m]の余剰運搬可能領域があります")

    elif コンベアベルトMk2運搬量 < minerSUM <= コンベアベルトMk3運搬量:
        if Mk3minerSUM == 0:
            print("コンベアベルトMk3で運搬可能、余剰運搬可能領域はありません")
        else:
            print("コンベアベルトMk3で運搬可能、[", Mk3minerSUM, "/m]の余剰運搬可能領域があります")

    elif コンベアベルトMk3運搬量 < minerSUM <= コンベアベルトMk4運搬量:
        if Mk4minerSUM == 0:
            print("コンベアベルトMk4で運搬可能、余剰運搬可能領域はありません")
        else:
            print("コンベアベルトMk4で運搬可能、[", Mk4minerSUM, "/m]の余剰運搬可能領域があります")

    elif コンベアベルトMk4運搬量 < minerSUM <= コンベアベルトMk5運搬量:
        if Mk5minerSUM == 0:
            print("コンベアベルトMk5で運搬可能、余剰運搬可能領域はありません")
        else:
            print("コンベアベルトMk5で運搬可能、[", Mk5minerSUM, "/m]の余剰運搬可能領域があります")
print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
