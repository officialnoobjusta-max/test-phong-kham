from datetime import date
from models.bac_si import BacSi
from models.benh_nhan import BenhNhan

bs = BacSi("021026001", "Nguyen A", "12 Le Loi", "TP. Hồ Chí Minh", "Phường Bến Nghé",
           "Nam", date(1985, 5, 1), "0901234567",
           "T2-T6", 15000000)
bn = BenhNhan("12102026000001", "Tran B", "5 Nguyen Hue", "TP. Hồ Chí Minh", "Phường Bến Nghé",
              "Nữ", date(2000, 3, 15), "0912345678",
              "", "", "O", "b@mail.com")
assert bn.ngay_tham_kham == date(2026, 10, 12)

print(bs); print(bn)
assert BacSi.from_dict(bs.to_dict()).to_dict() == bs.to_dict()
assert BenhNhan.from_dict(bn.to_dict()).to_dict() == bn.to_dict()

import json
json.dumps(bs.to_dict()); json.dumps(bn.to_dict())   # kiểm tra tuần tự hóa JSON

def loi(f, chua=""):
    try:
        f()
    except ValueError as e:
        assert chua in str(e), f"Báo lỗi nhưng sai lý do: {e}"
        return
    raise AssertionError("Lẽ ra phải báo ValueError")

nb = date(1985, 5, 1)
loi(lambda: BacSi("0210260", "A", "x", "T", "P", "Nam", nb, "0901234567", "T2-T6", 1))       # mã 7 số
loi(lambda: BacSi("021026001", "A", "x", "T", "P", "Nam", nb, "0901234567", "T2-T6", -1))    # lương âm
loi(lambda: BacSi("021026001", "A", "x", "T", "P", "Nam", nb, "123", "T2-T6", 1))            # SĐT sai
loi(lambda: BenhNhan("1210202600001", "B", "x", "T", "P", "Nữ", nb, "0912345678", "", "", "O", ""))          # mã 13 số
loi(lambda: BenhNhan("12102026000001", "B", "x", "T", "P", "Nữ", nb, "0912345678", "", "", "O", "abc@gmail")) # email sai
print("OK")