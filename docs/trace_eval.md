# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Vũ Quốc Bảo  
> **Mã Sinh Viên / Mã Học viên:** 2A202602829  
> **Chủ đề Lựa chọn:** Đề tài Mở - Trợ lý Lập Kế hoạch Đi Chợ / Nấu Ăn (Meal Planning Assistant)

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Agent phải so khớp nguyên liệu đang có trong tủ lạnh với công thức món người dùng muốn nấu trước khi quyết định nguyên liệu nào cần thêm vào danh sách đi chợ. |
| **2. Tool Interaction** | 3 / 5 | Hệ thống cần 2 tool: check_fridge_inventory (tra cứu nguyên liệu hiện có) và add_to_shopping_list (hành động ghi nhận nguyên liệu cần mua). Không cần kết nối MCP Server hay CSDL ngoài phức tạp, dữ liệu có thể mock bằng JSON. |
| **3. Dynamic Decision** | 4 / 5 | Bước tiếp theo phụ thuộc trực tiếp vào kết quả tra cứu: nếu tủ lạnh đủ nguyên liệu thì không cần thêm gì; nếu thiếu, Agent phải tự xác định thiếu món gì và có thể đề xuất món thay thế dùng nguyên liệu sẵn có thay vì máy móc thêm mọi thứ vào danh sách. |
| **4. Long Horizon Goal** | 2 / 5 | Mỗi lượt lập kế hoạch bữa ăn tương đối độc lập; Agent không bắt buộc phải giữ mục tiêu xuyên suốt qua nhiều lượt xử lý (có thể mở rộng bằng cách nhớ danh sách đã mua lần trước, nhưng không phải yêu cầu bắt buộc của bản demo). |
| **TỔNG ĐIỂM AGENTIC FIT** | **13 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Hãy kiểm tra xem tủ lạnh của tôi có đủ nguyên liệu để nấu món phở bò không?",
    "action_type": "TOOL_EXECUTION",
    "thought": "Gemini quyết định gọi công cụ 'check_fridge_inventory' với tham số: {\"dish_name\": \"phở bò\"}",
    "tool_name": "check_fridge_inventory",
    "arguments": {
      "dish_name": "phở bò"
    },
    "observation": {
      "status": "SUCCESS",
      "dish_name": "phở bò",
      "required_ingredients": [
        "bánh phở",
        "xương bò",
        "thịt bò",
        "hành tây",
        "gừng",
        "gia vị phở",
        "hành lá",
        "rau sống"
      ],
      "missing_ingredients": [
        "bánh phở",
        "xương bò",
        "thịt bò",
        "gia vị phở"
      ],
      "is_ready_to_cook": false
    },
    "latency_ms": 1917.47
  },
  {
    "step": 2,
    "query": "Hãy kiểm tra xem tủ lạnh của tôi có đủ nguyên liệu để nấu món phở bò không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Để nấu món 'phở bò', tủ lạnh hiện đang thiếu: bánh phở, xương bò, thịt bò, gia vị phở. Bạn có muốn thêm các nguyên liệu này vào danh sách đi chợ không?",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt (TC02, TC03, TC04 mỗi cái 1 lượt. TC05 1 lượt gọi nhưng trả NOT_FOUND - vẫn tính là 1 lượt gọi tool hợp lệ; TC01 không gọi tool).
- **Kết quả đẩy Repo nộp bài:** [x] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
