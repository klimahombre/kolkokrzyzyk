def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02.0f}:{minutes:02.0f}:{secs:02.0f}"
