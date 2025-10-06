"""
main.py — orchestrates the full Bagel-style pipeline.
It runs: LoadModel → Dataset → Training → Inference
"""

import subprocess
import sys
from pathlib import Path

# === CONFIG ===
STEPS = [
    ("Load Model", "LoadModel.py"),
    ("Prepare Dataset", "dataset.py"),
    ("Train Model", "training.py"),
    ("Run Inference", "Inference.py"),
]

def run_step(name: str, file: str) -> None:
    """Run a Python file as a subprocess and handle errors."""
    print(f"\n{'='*80}")
    print(f"🚀 Running step: {name}")
    print(f"{'='*80}\n")

    if not Path(file).exists():
        print(f"❌ File not found: {file}")
        sys.exit(1)

    try:
        result = subprocess.run([sys.executable, file], check=True)
        if result.returncode == 0:
            print(f"✅ Finished: {name}\n")
    except subprocess.CalledProcessError as e:
        print(f"💥 Error while running {name}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("🧩 Starting full pipeline...\n")

    for name, file in STEPS:
        run_step(name, file)

    print("\n🎉 All steps completed successfully!")
