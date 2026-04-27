metrics = {
    "total_requests": 0,
    "openai_failures": 0,
    "fallback_used": 0,
    "hallucinations_detected": 0
}

def increment(metric_name):
    if metric_name in metrics:
        metrics[metric_name] += 1

def get_metrics():
    return metrics