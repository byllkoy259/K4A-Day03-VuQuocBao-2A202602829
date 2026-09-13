"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any, List

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "check_fridge_inventory",
        "description": "Kiểm tra tủ lạnh xem đã có đủ nguyên liệu để nấu một món ăn cụ thể hay chưa. Trả về danh sách nguyên liệu còn thiếu (nếu có) hoặc báo NOT_FOUND nếu món ăn không có trong cơ sở dữ liệu công thức.",
        "parameters": {
            "type": "object",
            "properties": {
                "dish_name": {
                    "type": "string",
                    "description": "Tên món ăn người dùng muốn nấu (ví dụ: 'phở bò')"
                }
            },
            "required": ["dish_name"]
        }
    },
    {
        "name": "add_to_shopping_list",
        "description": "Thêm một hoặc nhiều nguyên liệu còn thiếu vào danh sách đi chợ của người dùng.",
        "parameters": {
            "type": "object",
            "properties": {
                "ingredients": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Danh sách tên các nguyên liệu cần thêm vào danh sách đi chợ (ví dụ: ['bánh phở', 'xương bò'])"
                }
            },
            "required": ["ingredients"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

# Nguyên liệu hiện có sẵn trong tủ lạnh (mock)
FRIDGE_INVENTORY = {
    "trứng", "hành lá", "tỏi", "gừng", "nước mắm", "hành tây",
    "cà chua", "rau sống", "chanh", "ớt"
}


# Cơ sở dữ liệu công thức: món ăn -> danh sách nguyên liệu cần có (mock)
RECIPE_DATABASE = {
    "phở bò": ["bánh phở", "xương bò", "thịt bò", "hành tây", "gừng", "gia vị phở", "hành lá", "rau sống"],
    "trứng chiên cà chua": ["trứng", "cà chua", "hành lá", "nước mắm"],
    "gỏi cuốn": ["bánh tráng", "tôm", "thịt heo", "bún", "rau sống"],
}


# Danh sách đi chợ hiện tại (mock, lưu trong bộ nhớ)
SHOPPING_LIST: List[str] = []


def execute_check_fridge_inventory(dish_name: str) -> str:
    """Thực thi kiểm tra tủ lạnh theo tên món ăn"""
    key = dish_name.strip().lower()
    recipe = RECIPE_DATABASE.get(key)
 
    if recipe is None:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy công thức cho món '{dish_name}' trong cơ sở dữ liệu."
        }, ensure_ascii=False)
 
    missing = [ingredient for ingredient in recipe if ingredient not in FRIDGE_INVENTORY]
 
    return json.dumps({
        "status": "SUCCESS",
        "dish_name": dish_name,
        "required_ingredients": recipe,
        "missing_ingredients": missing,
        "is_ready_to_cook": len(missing) == 0
    }, ensure_ascii=False)
 
 
def execute_add_to_shopping_list(ingredients: List[str]) -> str:
    """Thực thi thêm nguyên liệu vào danh sách đi chợ"""
    added = []
    for ingredient in ingredients:
        clean = ingredient.strip()
        if clean and clean not in SHOPPING_LIST:
            SHOPPING_LIST.append(clean)
            added.append(clean)
 
    return json.dumps({
        "status": "SUCCESS",
        "added_ingredients": added,
        "shopping_list": SHOPPING_LIST,
        "message": f"Đã thêm {len(added)} nguyên liệu vào danh sách đi chợ."
    }, ensure_ascii=False)
 
 
# Router gọi tool thực tế
TOOL_ROUTER = {
    "check_fridge_inventory": execute_check_fridge_inventory,
    "add_to_shopping_list": execute_add_to_shopping_list
}
 
def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
