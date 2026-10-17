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
print("OK")