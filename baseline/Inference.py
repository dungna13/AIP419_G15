# =========================
# Cell 7: Load model + LoRA
# =========================
from peft import PeftModel

# load base Qwen
base_llm = AutoModelForCausalLM.from_pretrained(
    LLM_MODEL,
    torch_dtype=torch.float16,
    device_map="auto"
)

# load adapter
llm = PeftModel.from_pretrained(base_llm, OUTPUT_DIR).eval()

print("✅ LoRA adapter loaded for inference")

from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

# load img2img pipeline cho refine
img2img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    SD_MODEL,
    torch_dtype=torch.float16
).to("cuda")

# test với 1 instruction từ dataset
prompt = "a fish, ultra realistic, 8k, photorealistic, cinematic lighting, HDR"

# vòng 1: sinh ảnh gốc (fix seed để ổn định)
generator = torch.manual_seed(42)
image = sd_pipe(prompt, generator=generator).images[0]
image.save("round1.png")

# vòng 2: refine ảnh từ vòng 1
refined_image = img2img_pipe(
    prompt=prompt,
    image=image,
    strength=0.3,   # giữ nhiều chi tiết gốc
    guidance_scale=7.5
).images[0]
refined_image.save("round2.png")

# vòng 3: refine tiếp từ ảnh vòng 2
refined_image2 = img2img_pipe(
    prompt=prompt,
    image=refined_image,
    strength=0.3,
    guidance_scale=7.5
).images[0]
refined_image2.save("round3.png")

refined_image2
