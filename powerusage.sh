#!/usr/bin/env bash
# cpu_avg_power.sh
# Measure average CPU power usage from fam15h_power sensor.

# Usage: ./cpu_avg_power.sh <duration_in_seconds> <interval_in_seconds>
# Example: ./cpu_avg_power.sh 10 1

SENSOR="fam15h_power"
DURATION=${1:-10}
INTERVAL=${2:-1}

# Locate hwmon path
HWMON_PATH=$(for d in /sys/class/hwmon/hwmon*; do
    if [[ "$(cat "$d/name" 2>/dev/null)" == "$SENSOR" ]]; then
        echo "$d"
    fi
done)

if [[ -z "$HWMON_PATH" ]]; then
    echo "Error: Sensor $SENSOR not found."
    exit 1
fi

POWER_FILE="$HWMON_PATH/power1_input"

if [[ ! -f "$POWER_FILE" ]]; then
    echo "Error: Could not find $POWER_FILE"
    exit 1
fi

echo "Measuring average CPU power from $SENSOR over $DURATION seconds..."

samples=()
end_time=$((SECONDS + DURATION))

while [[ $SECONDS -lt $end_time ]]; do
    value=$(cat "$POWER_FILE" 2>/dev/null)
    if [[ -n "$value" ]]; then
        samples+=("$value")
        echo "Sample: $((value / 1000000)) W"
    fi
    sleep "$INTERVAL"
done

# Compute average
sum=0
for v in "${samples[@]}"; do
    sum=$((sum + v))
done

count=${#samples[@]}
if [[ $count -gt 0 ]]; then
    avg=$((sum / count))
    echo "------------------------------------"
    echo "Average CPU Power: $((avg / 1000000)) W"
else
    echo "No samples collected!"
fi
