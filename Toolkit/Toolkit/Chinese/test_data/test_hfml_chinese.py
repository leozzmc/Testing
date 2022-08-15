from pathlib import Path

from openpecha.formatters import HFMLFormatter

#hfml_fn = Path("tests") / "formatters" / "hfml" / "data" / "kangyur_01.txt"
#hfml_fn = Path("Chinese") / "test_data" / "Chinese_01.txt"

# Path for testing purpose #
hfml_fn = Path("/mnt/c/Users/Kevin/Toolkit/Chinese/test_data") / "Chinese_02.txt"
m_text = hfml_fn.read_text()

formatter = HFMLFormatter()

text = formatter.text_preprocess(m_text)
formatter.build_layers(text, len([text]))
result_base = formatter.get_base_text()
result_meta = formatter.get_unique_id()
print(result_base)
print("----------------")
print(result_meta)
