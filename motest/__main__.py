import sys
import subprocess
import pytest
from pathlib import Path

def motest(mofile: Path, *args):    
    temp_path = Path("test_" + mofile.parts[-1])
    
    # Export the marimo notebook to Python
    export_cmd = f"marimo export script --output={temp_path} {mofile}"
    subprocess.run(export_cmd.split(), check=True)

    retcode = pytest.main([str(temp_path), *args])
    
    # Clean up temporary file
    temp_path.unlink()

    # Relay exit code
    return retcode

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: motest <notebook.py> [pytest args]")
        exit(1)
    mofile = Path(sys.argv[1])
    retcode = motest(mofile, *sys.argv[2:])
    # Exit with pytest exit code
    exit(int(retcode))

