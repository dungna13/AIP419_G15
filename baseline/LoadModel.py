import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from diffusers import StableDiffusionPipeline

# LLM (Qwen nhỏ)
LLM_MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

# Stable Diffusion v1.5 (nhẹ hơn v2, hợp T4)
SD_MODEL = "stabilityai/stable-diffusion-2-1-base"

# load tokenizer
tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)

# load LLM ở float16
llm = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    torch_dtype=torch.float16,
    device_map="auto"
)

# load Stable Diffusion pipeline
sd_pipe = StableDiffusionPipeline.from_pretrained(
    SD_MODEL,
    torch_dtype=torch.float16
).to("cuda")

print("✅ Models loaded: Qwen2.5-0.5B + Stable Diffusion v1.5")

