"""Extract model state_dicts from latest .ckpt files into weights/ directory."""
from pathlib import Path
import torch

models = {
    "efficientnet_b3": "efficientnet_b3.pth",
    "efficientformerv2_s1": "efficientformerv2_s1.pth",
    "faster_vit_2_224": "faster_vit_2_224.pth",
}

weights_dir = Path("weights")
weights_dir.mkdir(exist_ok=True)

for model_name, out_name in models.items():
    run_dir = Path("runs") / model_name
    # Find the latest timestamped subdirectory that has a checkpoint
    ckpt_candidates = sorted(run_dir.glob("*/checkpoints/latest.ckpt"), reverse=True)
    if not ckpt_candidates:
        print(f"[SKIP] No checkpoint found for {model_name}")
        continue

    ckpt_path = ckpt_candidates[0]
    out_path = weights_dir / out_name

    print(f"Extracting: {ckpt_path}")
    state = torch.load(ckpt_path, map_location="cpu")

    if "model" in state:
        model_state = state["model"]
    elif "state_dict" in state:
        model_state = state["state_dict"]
    else:
        print(f"  [WARN] Unexpected checkpoint keys: {list(state.keys())} - saving full state")
        model_state = state

    torch.save(model_state, out_path)
    size_mib = out_path.stat().st_size / (1024**2)
    print(f"  -> Saved {out_path} ({size_mib:.2f} MiB)")

print("\nDone. Weights saved to weights/")
