import tempfile
from pathlib import Path

from openpecha import config
from openpecha.utils import load_yaml
from openpecha.formatters import GoogleOCRFormatter




def test_google_ocr_base_meta():
    work_id = "W24767"
    pecha_id = "I123456"
    
    ocr_path = Path(__file__).parent / "data" / work_id
    expected_meta_path = Path(__file__).parent / "data" / "expected_google_ocr_meta.yml"
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        formatter = GoogleOCRFormatter(output_path=tmpdirname)
        pecha_path = formatter.create_opf(ocr_path, pecha_id)
        output_metadata = load_yaml(Path(f"{pecha_path}/{pecha_path.name}.opf/meta.yml"))
        expected_metadata = load_yaml(expected_meta_path)
        output_base = output_metadata['base']
        expected_base = expected_metadata['base']
        for (_, output_info), (_, expected_info) in zip(output_base.items(), expected_base.items()):
            del output_info['base_file']
            del expected_info['base_file']
            assert output_info == expected_info
            
def test_google_ocr_metadata():
    work_id = "W24767"
    pecha_id = "I123456"
    
    ocr_path = Path(__file__).parent / "data" / work_id
    expected_meta_path = Path(__file__).parent / "data" / "expected_google_ocr_meta.yml"
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        formatter = GoogleOCRFormatter(output_path=tmpdirname)
        pecha_path = formatter.create_opf(ocr_path, pecha_id)
        output_metadata = load_yaml(Path(f"{pecha_path}/{pecha_path.name}.opf/meta.yml"))
        expected_metadata = load_yaml(expected_meta_path)
        assert output_metadata['license'] == expected_metadata['license']
        assert output_metadata['copyright'] == expected_metadata['copyright']
        assert output_metadata['source_metadata']['access'] == expected_metadata['source_metadata']['access']
        assert output_metadata['source_metadata']['restrictedInChina'] == expected_metadata['source_metadata']['restrictedInChina']
        
            
            
            
            
if __name__ == "__main__":
    test_google_ocr_metadata()