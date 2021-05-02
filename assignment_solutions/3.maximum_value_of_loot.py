import sys
def get_optimal_value(capacity, weights, values):
    value = 0.
    ratio_values_weights = {values[i] / weights[i]: weights[i] for i in range(len(values))}
    sorted_max_values = sorted(ratio_values_weights.keys(), reverse=True)

    while capacity > 0:
        max_value = sorted_max_values[0]
        max_value_weight = ratio_values_weights[max_value]
        value += max_value * min(capacity, max_value_weight)
        capacity -= min(capacity, max_value_weight)
        sorted_max_values = sorted_max_values[1:]
        # if sorted_max_values end early
        if not sorted_max_values:
            return value
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))