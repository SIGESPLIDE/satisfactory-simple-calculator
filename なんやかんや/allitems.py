#! usr/bin/env python3.9

'''
───────────────────────────────────────
    #-named     = 表示名
    #-type      = アイテムのタイプ
    #-unity     = アイテムの大きな区分
    #-quantity  = 計算に使うための数字
    #-MAXamount = 1スタックあたりの最大数
    #-energy    = エネルギー量[MJ]
───────────────────────────────────────
'''
#----ALL ITEMS DESCRIPTION BELOW
allitems= {

#----ORES
    'Ores':{

        'Iron_Ore': {
            'named'    : '鉄鉱石',
            'type'     : 'ore_deposit',  #--鉱床
            'unity'    : 'raw_material', #--未加工鉱物
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Copper_Ore': {
            'named'    : '銅鉱石',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Caterium_Ore': {
            'named'    : 'カテリウム鉱石',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Coal': {
            'named'    : '石炭',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 300,
            },

        'Raw_Quartz': {
            'named'    : '未加工石英',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Limestone': {
            'named'    : '石灰石',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Sulfur': {
            'named'    : '硫黄',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Bauxite': {
            'named'    : 'ボーキサイト',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'Uranium': {
            'named'    : 'ウラン',
            'type'     : 'ore_deposit',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
            },

        'S.A.M._Ore': {
            'named'    : 'S.A.M.鉱石',
            'type'     : 'ore_deposit',
            'unity'    : 'in_dev',     #--開発段階(?)のため、本編未使用のものの部類
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
            },
    },

#----INGOTS
    'Ingots':{
        'Iron_Ingot':{
            'named'    : '鉄のインゴット',
            'type'     : 'component',    #--未加工の資源を製錬、精製、または加工したもの
            'unity'    : 'material',     #--一般的な意味での材料
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Copper_Ingot':{
            'named'    : '銅のインゴット',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Caterium_Ingot': {
            'named'    : 'カテリウムのインゴット',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Steel_Ingot':    {
            'named'    : '鋼鉄のインゴット',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Aluminum_Ingot': {
            'named'    : 'アルミのインゴット',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

    },

#----MINERALS
    'Minerals':{
        'Concrete': {
            'named'    : 'コンクリート',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Quartz_Crystal': {
            'named'    : '石英結晶',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Silica': {
            'named'    : 'シリカ',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Copper_Powder': {
            'named'    : '銅粉',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Polymer_Resin': {
            'named'    : '合成樹脂',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Petroleum_Coke': {
            'named'    : '石油コークス',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 180,
        },

        'Aluminum_Scrap': {
            'named'    : 'アルミのスクラップ',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },
    },

#----ALIENS
    'Aliens':{
        'Alien_Protein': {
            'named'    : 'エイリアンのタンパク質',
            'type'     : 'alien',      #--異星生物関連
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Alien_DNA_Capsule': {
            'named'    : 'エイリアンのDNAカプセル',
            'type'     : 'alien',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },
    },

#----LIQUIDS
    'Liquids':{
        'Water_': {
            'named'    : '水',
            'type'     : 'liquid',   #--液体類
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0,
        },

        'Crude_Oil': {
            'named'    : '原油',
            'type'     : 'liquid',
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0.32,
        },

        'Heavy_Oil_Residue': {
            'named'    : '重廃油',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0.4,
        },

        'Fuel': {
            'named'    : '燃料',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0.75,
        },

        'Liquid_Biofuel': {
            'named'    : '液体バイオ燃料',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0.75,
        },

        'Turbofuel': {
            'named'    : 'ターボ燃料',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 2,
        },

        'Alumina_Solution': {
            'named'    : 'アルミナ溶液',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0,
        },

        'Sulfuric_Acid': {
            'named'    : '硫酸',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0,
        },

        'Nitric_Acid': {
            'named'    : '硝酸',
            'type'     : 'liquid',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0,
        },
    },

#----GAS
    'Gas':{
        'Nitrogen_Gas': {
            'named'    : '窒素ガス',
            'type'     : 'Gas',     #--気体類
            'unity'    : 'raw_material',
            'quantity' : 1,
            'MAXamount': 1,
            'energy'   : 0,
        },
    },

#----STANDARD PARTS
    'Standard_Parts':{
        'Iron_Rod': {
            'named'    : '鉄のロッド',
            'type'     : 'parts',    #--基本的にインゴットを加工して得られる基礎部品
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Screw': {
            'named'    : 'ネジ',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Iron_Plate': {
            'named'    : '鉄板',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },
        'Reinforced_Iron_Plate': {
            'named'    : '強化鉄板',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Copper_Sheet': {
            'named'    : '銅のシート',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Alclad_Aluminum_Sheet': {
            'named'    : 'アルクラッド・アルミシート',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Aluminum_Casing': {
            'named'    : 'アルミ筐体',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Steel_Pipe': {
            'named'    : '鋼鉄のパイプ',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Steel_Beam': {
            'named'    : '鋼梁',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Encased_Industrial_Beam': {
            'named'    : 'コンクリート被覆型鋼梁',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Modular_Frame': {
            'named'    : 'モジュラー・フレーム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Heavy_Modular_Frame': {
            'named'    : 'ヘビー・モジュラー・フレーム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Fused_Modular_Frame': {
            'named'    : '溶融モジュラー・フレーム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Fabric': {
            'named'    : '布地',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 15,
        },

        'Plastic': {
            'named'    : 'プラスチック',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Rubber': {
            'named'    : 'ゴム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },
    },

#----INDUSTRIAL PARTS
    'Industrial_Parts':{
        'Rotor': {
            'named'    : 'ローター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Stator': {
            'named'    : '固定子',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Battery': {
            'named'    : 'バッテリー',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 6000,

        },

        'Motor': {
            'named'    : 'モーター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,

        },

        'Heat_Sink': {
            'named'    : 'ヒートシンク',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,

        },

        'Cooling_System': {
            'named'    : '冷却システム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,

        },

        'Turbo_Motor': {
            'named'    : 'ターボモーター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,

        },
    },

#----ELECTRONICS
    'Electronics':{
        'Wire': {
            'named'    : 'ワイヤー',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,

        },

        'Cable': {
            'named'    : 'ケーブル',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Quickwire': {
            'named'    : 'クイックワイヤー',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Circuit_Board': {
            'named'    : '回路基板',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'AI_Limiter': {
            'named'    : 'AIリミッター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'High-Speed_Connector': {
            'named'    : '高速コネクター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },
    },

#----COMMUNICATIONS
    'Communications': {
        'Computer': {
            'named'    : 'コンピューター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Supercomputer': {
            'named'    : 'スーパーコンピューター',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Quantum_Computer': {
            'named'    : '量子コンピューター',
            'type'     : 'parts',
            'unity'    : 'in_dev',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Radio_Control_Unit': {
            'named'    : '無線制御ユニット',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Crystal_Oscillator': {
            'named'    : '水晶発振器',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Superposition_Oscillator': {
            'named'    : '重ね合わせ発振器',
            'type'     : 'parts',
            'unity'    : 'in_dev',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },
    },

#----CONTAINERS
    'Containers':{
        'Empty_Canister': {
            'named'    : '空の容器',
            'type'     : 'container',    #--容器関係
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Empty_Fluid_Tank': {
            'named'    : '空の液体タンク',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Pressure_Conversion_Cube': {
            'named'    : '圧力変換キューブ',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Packaged_Water': {
            'named'    : '容器入り水',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Packaged_Alumina_Solution': {
            'named'    : '容器入りアルミナ溶液',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Packaged_Sulfuric_Acid': {
            'named'    : '容器入り硫酸',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Packaged_Nitric_Acid': {
            'named'    : '容器入り硝酸',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Packaged_Nitrogen_Gas': {
            'named'    : '容器入り窒素ガス',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

    },

#----FUELS
    'Fuels':{
        'Leaves': {
            'named'    : '葉',
            'type'     : 'biomass',    #--バイオマス関連
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 15,
        },

        'Mycelia': {
            'named'    : '菌糸',
            'type'     : 'biomass',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 20,
        },

        'Flower_Petals': {
            'named'    : '花弁',
            'type'     : 'special',     #--パーツでも材料でもない特殊枠
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 100,
        },

        'Wood': {
            'named'    : '木',
            'type'     : 'biomass',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 100,
        },

        'Biomass': {
            'named'    : 'バイオマス',
            'type'     : 'biomass',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 180,
        },

        'Compacted_Coal': {
            'named'    : '圧縮石炭',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 630,
        },

        'Packaged_Oil': {
            'named'    : '容器入り原油',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 320,
        },

        'Packaged_Heavy_Oil_Residue': {
            'named'    : '容器入り廃重油',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 400,
        },

        'Solid_Biofuel': {
            'named'    : '個体バイオ燃料',
            'type'     : 'biomass',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 450,
        },

        'Packaged_Fuel': {
            'named'    : '容器入り燃料',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 750,
        },

        'Packaged_Liquid_Biofuel': {
            'named'    : '容器入り液体バイオ燃料',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 750,
        },

        'Packaged_Turbofuel': {
            'named'    : '容器入りターボ燃料',
            'type'     : 'container',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 2000,
        },

        'Uranium_Fuel_Rod': {
            'named'    : 'ウラン燃料棒',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 750000,
        },

        'Plutonium_Fuel_Rod': {
            'named'    : 'プルトニウム燃料棒',
            'type'     : 'component',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 1500000,
        },

    },

#----CONSUMED
    'Consumed':{
        'Black_Powder': {
            'named'    : '黒色火薬',
            'type'     : 'consumed',   #--消耗品類
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Smokeless_Powder': {
            'named'    : '無煙火薬',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Gas_Filter': {
            'named'    : 'ガスフィルター',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Color_Cartridge': {
            'named'    : 'カラー弾薬',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 900,
        },

        'Beacon': {
            'named'    : 'ビーコン',
            'type'     : 'consumed',
            'unity'    : 'in_dev',   #将来のアップデートで消される可能性あり
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Iodine_Infused_Filter': {
            'named'    : 'ヨウ素充填フィルター',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

    },

#----AMMOS
    'Ammos':{
        'Iron_Rebar': {
            'named'    : '鉄筋',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Stun_Rebar': {
            'named'    : 'スタン鉄筋',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Shatter_Rebar': {
            'named'    : '破砕鉄筋',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Explosive_Rebar': {
            'named'    : '爆砕鉄筋',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Rifle_Ammo': {
            'named'    : 'ライフル弾',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Homing_Rifle_Ammo': {
            'named'    : 'ホーミングライフル弾',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Turbo_Rifle_Ammo': {
            'named'    : 'ターボライフル弾',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Nobelisk': {
            'named'    : 'ノーべリスク',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Gas_Nobelisk': {
            'named'    : 'ガス・ノーべリスク',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Pulse_Nobelisk': {
            'named'    : 'パルス・ノーべリスク',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Cluster_Nobelisk': {
            'named'    : 'クラスター・ノーべリスク',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Nuke_Nobelisk': {
            'named'    : 'ニューク・ノーべリスク',
            'type'     : 'consumed',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

    },

#----NUCLEAR
    'Nuclear':{
        'Electromagnetic_Control_Rod': {
            'named'    : '電磁制御棒',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Encased_Uranium_Cell': {
            'named'    : '被覆型ウラン・セル',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

        'Non-fissile_Uranium': {
            'named'    : '非分裂製ウラン',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Plutonium_Pellet': {
            'named'    : 'プルトニウム・ペレット',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'Encased_Plutonium_Cell': {
            'named'    : '被覆型プルトニウム・セル',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 200,
            'energy'   : 0,
        },

    },

#----WASTE
    'Waste':{
        'Uranium_Waste': {
            'named'    : 'ウラン廃棄物',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Plutonium_Waste': {
            'named'    : 'プルトニウム廃棄物',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

    },

#----SPECIAL
    'Special':{
        'Blue_Power_Slug': {
            'named'    : '青いパワー・スラッグ',
            'type'     : 'special',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Yellow_Power_Slug': {
            'named'    : '黄色いパワー・スラッグ',
            'type'     : 'special',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Purple_Power_Slug': {
            'named'    : '紫のパワー・スラッグ',
            'type'     : 'special',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Power_Shard': {
            'named'    : 'パワー・シャード',
            'type'     : 'special',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 100,
            'energy'   : 0,
        },

        'FICSIT_Coupon': {
            'named'    : 'FICSITクーポン',
            'type'     : 'special',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 500,
            'energy'   : 0,
        },

        'Smart_Plating': {
            'named'    : 'スマート・プレート',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Versatile_Framework': {
            'named'    : '多目的フレームワーク',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Automated_Wiring': {
            'named'    : '自動ワイヤー',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Modular_Engine': {
            'named'    : 'モジュラーエンジン',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Adaptive_Control_Unit': {
            'named'    : '自律制御ユニット',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Assembly_Director_System': {
            'named'    : '組立指揮システム',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Magnetic_Field_Generator': {
            'named'    : '磁界発生装置',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Thermal_Propulsion_Rocket': {
            'named'    : '熱推進型ロケット',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

        'Nuclear_Pasta': {
            'named'    : '核パスタ',
            'type'     : 'parts',
            'unity'    : 'material',
            'quantity' : 1,
            'MAXamount': 50,
            'energy'   : 0,
        },

    },

}