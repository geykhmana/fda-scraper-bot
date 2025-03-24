import time
import scanner_globe
import scanner_bw
import scanner_sec

print("🧠 FDA Sniper Bot (Filtered) Running...")

while True:
    try:
        scanner_globe.scan()
        scanner_bw.scan()
        scanner_sec.scan()
        time.sleep(30)  # 30s interval
    except Exception as e:
        print(f"⚠️ Error: {e}")
        time.sleep(60)