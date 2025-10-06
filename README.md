# AIP419_G15
Đồ án kì 9 chuyên ngành AI_FPT

# AIP419_G15 – AI Project Baseline

## Giới thiệu
Dự án **AIP419_G15** là baseline nghiên cứu và triển khai mô hình **Text-to-Image Generation** dựa trên các mô hình hiện đại như **BAGEL**, **T2I-R1**, **Show-o**, **Stable Diffusion**, và các hướng kết hợp LLM với Diffusion Model.  
Repo này phục vụ cho việc thử nghiệm, so sánh và đánh giá các phương pháp trong lĩnh vực **AI Multimodal Learning**.
## Hướng dẫn cài đặt

### 1. Clone repository
Trước tiên, hãy mở **Terminal** (hoặc **Command Prompt**) và chạy lệnh sau để sao chép repo về máy:
```bash
git clone https://github.com/dungna13/AIP419_G15
cd AIP419_G15
pip install -r requirement.txt
```

#### Sau khi cài đặt xong 
```bash
cd baseline
python main.py
```

## Cấu trúc thư mục bao gồm
```bash
AIP419_G15/
├── baseline/
│   ├── main.py
│   ├── ...
├── requirement.txt
└── README.md
```

## Mục tiêu nghiên cứu

-  **Kết hợp mô hình LLM (Large Language Model)** với **Text-to-Image Diffusion Model** để tạo nên hệ thống sinh ảnh từ ngôn ngữ có tính ngữ cảnh và nhận thức cao hơn.  
-  **So sánh hiệu quả** giữa các phương pháp baseline hiện có nhằm xác định hướng tiếp cận tối ưu.  
-  **Đánh giá ưu – nhược điểm** của các hệ thống như **Stable Diffusion**, **T2I-R1**, **BAGEL**, **Show-o**, và các mô hình liên quan trong cả hiệu suất sinh ảnh và khả năng hiểu ngữ nghĩa.  
-  **Triển khai và tối ưu hóa** mô hình theo hướng **open-source**, phục vụ mục đích **học thuật**, **nghiên cứu**, và **mở rộng ứng dụng đa phương thức (multimodal AI)** trong tương lai.

---

## Reference Papers

1. [**BAGEL: Bootstrapping Agents with Generative Environment Learning**](https://arxiv.org/abs/2505.14683) — *ByteDance Seed, 2025*  
2. [**T2I-R1: Large-scale Text-to-Image Reinforcement Learning with Human Feedback**](https://arxiv.org/abs/2408.12528) — *Alibaba DAMO Academy, 2024*  
3. [**Show-o: One-step Diffusion via Autoregressive Distillation**](https://arxiv.org/abs/2501.17811) — *Tencent AI Lab, 2025*  
4. [**Improving Text-to-Image Diffusion with Large Language Model Guidance**](https://arxiv.org/abs/2504.16080)  
5. [**LLM-to-Image: Grounded Generation from Language Models**](https://arxiv.org/abs/2505.22525)  
6. [**ReFL: Reinforced Fine-tuning of Diffusion Models via Human Feedback**](https://arxiv.org/abs/2505.00703)  
7. [**Diffusion Policy as Instruction Follower**](https://arxiv.org/abs/2311.13917)  
8. [**GILL: Generative Image-Language Learning with LLMs**](https://arxiv.org/abs/2403.08752)  
9. [**Stable Diffusion: High-Resolution Image Synthesis with Latent Diffusion Models**](https://arxiv.org/abs/2112.10752)  
10. [**DreamFusion: Text-to-3D using 2D Diffusion**](https://arxiv.org/abs/2209.14988)  
11. [**InstructPix2Pix: Learning to Follow Image Editing Instructions**](https://arxiv.org/abs/2211.09800)  
12. [**Visual Instruction Tuning**](https://arxiv.org/abs/2304.08485)


## Nhóm thực hiện

**Tên nhóm:** AIP419_G15  

**Thành viên nhóm:**
-  **Bùi Minh Sơn**
-  **Ngô Anh Dũng**
-  **Hoàng Văn Vũ**
-  **Đào Nhật Tân**
