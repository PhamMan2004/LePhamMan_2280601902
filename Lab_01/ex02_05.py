sogiolam = float(input("Nhap gio lam moi tuan: "))
luonggio = float(input("Nhap luong cua may, bao nhieu mot gio: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5
print(f"So tien may lanh duoc la: {thuclinh}")