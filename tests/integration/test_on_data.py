import tempfile
from pathlib import Path
from cimrdfs2linkml.main import cli
import pytest

data_dir = Path(__file__).parent.parent.parent / 'data'
assert data_dir.exists()

data_files = [f for f in data_dir.iterdir() if f.is_file()]
assert data_files

@pytest.mark.parametrize("data_file", data_files)
def test_on_data(data_file):
    """Test the CLI on all data files in the data directory.
    
    This test does not check the correctness of the output, 
    but it ensures that the CLI runs without errors and produces an output file. 
    """
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_f:
        temp_file_path = Path(temp_f.name)
        
    try:
        # CLI is expected to exit with SystemExit, so catch it to prevent the test from failing.
        with pytest.raises(SystemExit):
            cli.main([str(data_file), "-o", str(temp_file_path)])
            
        assert temp_file_path.exists()
        
    finally:
        # Cleanup the temporary file after the test
        temp_file_path.unlink(missing_ok=True)