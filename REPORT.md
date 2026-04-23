# Báo cáo Chi tiết Lab 16 - Giải pháp Thay thế sử dụng Nút CPU

## Tổng Quan

Dự án này được thực hiện dựa trên phương án dự phòng do gặp phải những hạn chế về hạn mức tài nguyên GPU trên nền tảng AWS. Khi yêu cầu tăng hạn mức bị từ chối hoặc trì hoãn, chúng tôi đã quyết định sử dụng máy chủ CPU hiệu năng cao (r5.2xlarge) để đảm bảo hoàn thành bài Lab đúng tiến độ.

## Chi Tiết Kết Quả

### 1. Hiệu Suất Huấn Luyện
Mô hình LightGBM được huấn luyện trên nút CPU đã cho kết quả vô cùng tốt, với thời gian xử lý chỉ 1.0691 giây. Điều này chứng minh rằng các thuật toán Gradient Boosting có thể hoạt động hiệu quả trên CPU mạnh mà không cần thiết phải sử dụng GPU.

### 2. Độ Chính Xác Mô Hình
Chỉ số AUC-ROC của mô hình đạt 0.7809, cho thấy hiệu suất khá tốt cho bài toán phát hiện gian lận thẻ tín dụng. Mặc dù chưa được tinh chỉnh sâu, kết quả này vẫn đạt mức chấp nhận được.

### 3. Tốc Độ Suy Diễn
Khả năng dự đoán của mô hình rất nhanh với độ trễ khoảng 0.000002 giây cho mỗi dòng dữ liệu. Điều này cho phép ứng dụng có thể được triển khai trong các hệ thống yêu cầu phản hồi tức thời.

### 4. Kết Luận Chung
Việc lựa chọn sử dụng nút CPU thay vì GPU không chỉ là một giải pháp khả thi mà còn là lựa chọn tối ưu về mặt kinh tế. Khi gặp phải những rào cản về hạn mức tài nguyên trên nền tảng đám mây, phương án này chứng tỏ khả năng triển khai hiệu quả và tiết kiệm chi phí.

