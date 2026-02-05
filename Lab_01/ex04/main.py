from quanlysinhvien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU******************************")
    print("** 1. Them sinh vien.                                   **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.              **")
    print("** 3. Xoa sinh vien boi ID.                             **")
    print("** 4. Tim kiem sinh vien theo ten.                      **")
    print("** 5. Sap xep sinh vien theo diem trung binh.           **")
    print("** 6. Sap xep sinh vien theo ten.                       **")
    print("** 7. Hien thi danh sach sinh vien.                     **")
    print("** 0. Thoat                                             **")
    print("***********************************************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("Vui long nhap so!")
        continue

    if (key == 1):
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID can sua: "))
            qlsv.updateSinhVien(ID)
        else: print("Danh sach trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            ID = int(input("Nhap ID can xoa: "))
            if qlsv.deleteById(ID): print("Xoa thanh cong.")
            else: print("Khong tim thay ID.")
        else: print("Danh sach trong!")
    elif (key == 4):
        name = input("Nhap ten can tim: ")
        res = qlsv.findByName(name)
        qlsv.showSinhVien(res)
    elif (key == 7):
        qlsv.showSinhVien(qlsv.getListSinhVien())
    elif (key == 0):
        print("Thoat chuong trinh.")
        break
    else:
        print("Khong co chuc nang nay!")