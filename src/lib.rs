use pyo3::prelude::*;
use csscolorparser::Color;

#[pyclass]
struct ColorParser {
    color: Color,
}

#[pymethods]
impl ColorParser {
    #[new]
    fn new(color_str: &str) -> PyResult<Self> {
        let parse_result = color_str.parse::<Color>();
        match parse_result {
            Ok(color) => {
                // Additional validation for color ranges
                let [r, g, b, a] = color.to_rgba8();
                if r > 255 || g > 255 || b > 255 || a > 255 {
                    return Err(pyo3::exceptions::PyValueError::new_err("Color values out of range"));
                }
                Ok(ColorParser { color })
            },
            Err(e) => Err(pyo3::exceptions::PyValueError::new_err(format!("Failed to parse color: {}", e)))
        }
    }

    #[getter]
    fn rgba_255(&self) -> (u8, u8, u8, u8) {
        let rgba = self.color.to_rgba8();
        (rgba[0], rgba[1], rgba[2], rgba[3])
    }

    #[getter]
    fn rgba_float(&self) -> [f32; 4] {
        self.color.to_array()
    }

    #[getter]
    fn hex(&self) -> String {
        self.color.to_hex_string()
    }

    #[getter]
    fn rgb_string(&self) -> String {
        self.color.to_rgb_string()
    }

    #[staticmethod]
    fn is_valid(color_str: &str) -> bool {
        match color_str.parse::<Color>() {
            Ok(color) => {
                let [r, g, b, a] = color.to_rgba8();
                r <= 255 && g <= 255 && b <= 255 && a <= 255
            },
            Err(_) => false
        }
    }
}

/// A Python module for parsing and converting colors
#[pymodule]
fn color_parser_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<ColorParser>()?;
    Ok(())
}