"""貪欲アルゴリズム本体の実装"""

def greedy(items, maxWeight, keyFunction):
    """品物のリスト、ナップサックの最大容量、ソート用の基準を提供する関数を与えて貪欲アルゴリズムを実行するための関数"""
    copiedItems = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for item in copiedItems:
        if (totalWeight + item.weight) <= maxWeight:
            result.append(item)
            totalWeight += item.weight
            totalValue += item.value
    return result, totalValue
