"""Write the funniest toaster error message to /output/entry.txt."""

import os

LINE = "ERROR: The bread refused to brown. It says it is 'finding itself'."

# The gate accepts 1-120 characters; fail loudly instead of shipping an invalid line.
if not 1 <= len(LINE) <= 120:
    raise ValueError(f"entry must be 1-120 characters, got {len(LINE)}")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
