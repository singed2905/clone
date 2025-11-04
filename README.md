# ConvertKeylogApp v2.2 - Clone Repository

> Ứng dụng desktop Python chuyển đổi biểu thức toán học thành keylog cho máy tính Casio

## Tổng quan

**ConvertKeylogApp** là ứng dụng desktop Python được thiết kế để chuyển đổi các phép tính toán học phức tạp thành mã keylog tương thích với máy tính Casio. Dự án được phát triển dựa trên kiến trúc modular, hỗ trợ đa mode tính toán.

## 4 Mode Tính Toán

### 🧠 Equation Mode v2.2 - Giải Hệ Phương Trình
- Hệ phương trình tuyến tính 2×2, 3×3, 4×4
- NumPy solver với TL-compatible encoding
- Multi-version support: fx799-fx803
- Excel batch processing

### 📈 Polynomial Mode v2.1 - Giải Phương Trình Đa Thức
- Polynomial bậc 2, 3, 4
- Complex roots handling
- Multi-version keylog: fx799/fx991/fx570/fx580/fx115
- Template generator system

### 📐 Geometry Mode v2.1 - Hình Học (Production Ready)
- 5 hình dạng: Điểm, Đường thẳng, Mặt phẳng, Đường tròn, Mặt cầu
- 5 phép toán: Tương giao, Khoảng cách, Diện tích, Thể tích, PT đường thẳng
- Excel integration với memory monitoring
- LaTeX to calculator encoding

### 🔢 Vector Mode v1.0 - Vector (Beta)
- Tính toán vector 2D/3D
- Scalar-Vector và Vector-Vector operations
- Auto-detection 2D/3D
- TL-compatible keylog encoding

## Cài đặt

### Yêu cầu hệ thống
- Python 3.9+ (khuyến nghị 3.11+)
- RAM: Tối thiểu 4GB, khuyến nghị 8GB
- OS: Windows 10+, macOS 10.14+, Ubuntu 18.04+

### Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### Khởi động
```bash
python main.py
```

## Cấu trúc dự án

```
ConvertKeylogApp/
├── main.py                     # Entry point
├── views/                      # UI Layer (Tkinter)
│   ├── main_view.py            # Mode selector
│   ├── equation_view.py        # Equation Mode UI
│   ├── polynomial_equation_view.py # Polynomial UI
│   ├── geometry_view.py        # Geometry UI
│   └── vector_view.py          # Vector UI
├── services/                   # Business Logic Layer
│   ├── equation/               # Equation services
│   ├── polynomial/            # Polynomial services
│   ├── geometry/              # Geometry services
│   ├── vector/                # Vector services
│   └── excel/                 # Excel processing
├── config/                    # Configuration system
│   ├── modes.json             # Main modes configuration
│   ├── equation_mode/         # Equation configs
│   ├── polynomial_mode/       # Polynomial configs
│   ├── geometry_mode/         # Geometry configs
│   └── vector_mode/           # Vector configs
├── utils/                     # Utility functions
├── docs/                      # Documentation
└── tests/                     # Test files
```

## Công nghệ sử dụng

- **Python 3.9+** - Main language
- **Tkinter** - GUI framework
- **NumPy** - Numerical computing
- **Pandas** - Excel data processing
- **psutil** - System monitoring
- **JSON** - Configuration management

## Tính năng nổi bật

- **Multi-mode architecture**: 4 mode tính toán chuyên biệt
- **Excel integration**: Batch processing với progress tracking
- **Memory monitoring**: Anti-crash protection cho file lớn
- **Multi-version support**: Hỗ trợ nhiều phiên bản máy tính Casio
- **Template system**: Auto-generate Excel templates
- **TL-compatible encoding**: Keylog format chuẩn

## Hướng dẫn sử dụng

1. **Chọn mode** từ main screen
2. **Setup parameters** (số ẩn/bậc/phép toán, version máy tính)
3. **Input data** (manual hoặc import Excel)
4. **Processing** (auto validate → solve → encode keylog)
5. **Export results** (copy clipboard hoặc export Excel)

## Performance

- Manual calculation: <1s response time
- Excel processing: 100-500 rows/second
- Memory usage: <500MB cho file <50MB
- Chunked processing cho file lớn

## Phiên bản

**Version**: 2.2  
**Last Updated**: November 4, 2025  
**Status**: Production Ready

## Tác giả

ConvertKeylogApp Development Team
