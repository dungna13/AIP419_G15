from datasets import load_dataset

dataset = load_dataset("Osilly/IRG-Toy-Dataset")

from torch.utils.data import DataLoader
from peft import LoraConfig, get_peft_model

# DataLoader
train_loader = DataLoader(dataset["train"], batch_size=1, shuffle=True)

# bật gradient checkpointing
llm.gradient_checkpointing_enable()

# LoRA config
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],  # inject vào attention
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
)

# Wrap model thành LoRA
llm = get_peft_model(llm, lora_config)
llm.print_trainable_parameters()
