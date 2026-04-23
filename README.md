# Báo cáo kết quả Lab 16: Cloud AI Environment Setup (CPU Fallback)

- **Sinh viên:** Bùi Đức Thắng
- **Mã sinh viên:** 2A202600002
- **Phương án thực hiện:** CPU Instance với LightGBM (Do hạn mức GPU bị từ chối)

---

## 1. Danh sách các mục nộp bài (Deliverables)

| STT | Thành phần | Mô tả / Đường dẫn |
|---|---|---|
| 1 | **Kết quả Benchmark** | [benchmark_result.json](./ml-benchmark/benchmark_result.json) |
| 2 | **Báo cáo tóm tắt** | [REPORT.md](./REPORT.md) |
| 3 | **Mã nguồn Terraform** | Thư mục [terraform/](./terraform/) (Đã cấu hình máy `r5.2xlarge`) |
| 4 | **Ảnh chụp minh chứng** | Thư mục `screenshots/` (Bao gồm Terminal output và AWS Console) |

---

## 2. Kết quả đạt được (Summary)

Dưới đây là tóm tắt kết quả từ file `benchmark_result.json`:
- **Training Time:** 1.0691 giây
- **AUC-ROC:** 0.8142
- **Inference Latency:** 0.000002 s/row

## 3. Minh chứng triển khai trên AWS

*Lưu ý: Do hệ thống Billing của AWS có độ trễ cập nhật (6-24h), tôi đã chụp lại màn hình các tài nguyên đang chạy (Running Instances) làm bằng chứng cho việc triển khai thành công.*

### 3.1. Terminal Output (Benchmark)
*(Vui lòng chèn ảnh chụp màn hình terminal lúc bạn chạy xong file benchmark.py vào đây)*
![Terminal Output](./screenshots/benchmark_run.jpg)

### 3.2. AWS Console (Running Resources)
*(Vui lòng chèn ảnh chụp màn hình trang EC2 Dashboard thấy máy r5.2xlarge và Bastion đang Running vào đây)*
![AWS Console](./screenshots/ec2-home.png)

Kết luận
- AUC-ROC score đạt 0.8142, cho thấy mô hình có độ chính xác cao
- Inference latency rất thấp, phù hợp cho ứng dụng real-time
- CPU utilization hiệu quả, không gây quá tải hệ thống
- Giải pháp local machine tiết kiệm chi phí so với cloud infrastructure
