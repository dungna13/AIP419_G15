EPOCHS = 1
GRAD_ACCUM = 8   # mô phỏng batch_size=8
device = "cuda"

optimizer = torch.optim.AdamW(llm.parameters(), lr=2e-5)

llm.train()
for epoch in range(EPOCHS):
    for step, batch in enumerate(train_loader):
        # input = conversation
        inputs = tokenizer(
            batch["conversation"],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=256
        ).to(device)

        # forward
        outputs = llm(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss / GRAD_ACCUM
        loss.backward()

        # update mỗi GRAD_ACCUM steps
        if (step + 1) % GRAD_ACCUM == 0:
            optimizer.step()
            optimizer.zero_grad()

        if step % 50 == 0:
            print(f"Epoch {epoch} | Step {step} | Loss: {loss.item() * GRAD_ACCUM:.4f}")



# =========================
# Cell 6: Save LoRA adapter
# =========================
OUTPUT_DIR = "./qwen2.5_lora_sd15"

llm.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"✅ LoRA adapter saved at {OUTPUT_DIR}")
