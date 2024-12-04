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
        match color_str.parse::<Color>() {
            Ok(color) => Ok(ColorParser { color }),
            Err(e) => Err(pyo3::exceptions::PyValueError::new_err(format!("Failed to parse color: {}", e)))
        }
    }

    #[getter]
    fn rgba_255(&self) -> [u8; 4] {
        self.color.to_rgba8()
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

    // Static method to check if a string is a valid color
    #[staticmethod]
    fn is_valid(color_str: &str) -> bool {
        color_str.parse::<Color>().is_ok()
    }
}

/// A Python module for parsing and converting colors
#[pymodule]
fn color_parser_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<ColorParser>()?;
    Ok(())
}
