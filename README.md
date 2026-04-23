# Báo cáo kết quả Lab 16: Cloud AI Environment Setup (CPU Fallback)

- **Sinh viên:** Bùi Đức Thắng
- **Mã sinh viên:** 2A202600002
- **Phương án thực hiện:** CPU Instance với LightGBM (Do hạn mức GPU bị từ chối)

---

## 1. Danh sách các mục nộp bài (Deliverables)

| STT | Thành phần | Mô tả / Đường dẫn |
|---|---|---|
| 1 | **Kết quả Benchmark** | [benchmark_result.json](./ml-benchmark) |
| 2 | **Báo cáo tóm tắt** | [REPORT.md](./REPORT.md) |
| 3 | **Mã nguồn Terraform** | Thư mục [terraform/](./terraform/) |
| 4 | **Ảnh chụp minh chứng** | Thư mục `screenshots/` (Terminal output ) |

---

## 2. Kết quả đạt được (Summary)

Dưới đây là tóm tắt kết quả từ file `benchmark_result.json`:
- **Training Time:** 1.0691 giây
- **AUC-ROC:** 0.8142
- **Inference Latency:** 0.000002 s/row


Kết luận
- AUC-ROC score đạt 0.8142, cho thấy mô hình có độ chính xác cao
- Inference latency rất thấp, phù hợp cho ứng dụng real-time
- CPU utilization hiệu quả, không gây quá tải hệ thống
- Giải pháp local machine tiết kiệm chi phí so với cloud infrastructure
