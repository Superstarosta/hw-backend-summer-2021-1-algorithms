__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days, seconds = divmod(seconds, 24*3600)
    hours, seconds = divmod(seconds, 3600)
    minuts, seconds = divmod(seconds,60)

    if days > 0:
        return f"{days:02}d{hours:02}h{minuts:02}m{seconds:02}s"
    if hours > 0:
        return f"{hours:02}h{minuts:02}m{seconds:02}s"
    if minuts > 0:
        return f"{minuts:02}m{seconds:02}s"
        
    return f"{seconds:02}s"
