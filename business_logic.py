from decimal import Decimal, getcontext

# 设置 Decimal 精度
getcontext().prec = 20

def calculate_gacha_probability(pull_num):
    """
    计算原神抽卡概率
    
    Args:
        pull_num: 抽数，正整数
    
    Returns:
        float: 当前抽的概率
    
    Raises:
        ValueError: 当输入为0或负数时
    """
    if pull_num <= 0:
        raise ValueError("抽数必须是正整数")
    
    # 重置为当前轮次的抽数（超过90抽后重置）
    current_pull = pull_num % 90
    if current_pull == 0:
        current_pull = 90
    
    # 第90抽必定出五星
    if current_pull == 90:
        return 1.0
    
    # 基础概率
    base_prob = Decimal('0.006')
    
    # 软保底：从第74抽开始，每抽递增6%
    if current_pull >= 74:
        # 计算当前概率，使用 Decimal 避免浮点数误差
        increase_count = current_pull - 73
        current_prob = base_prob + (Decimal(str(increase_count)) * Decimal('0.06'))
        # 确保概率不超过1.0
        current_prob = min(current_prob, Decimal('1.0'))
        # 转换为 float 返回
        return float(current_prob)
    
    # 74抽之前保持基础概率
    return float(base_prob)