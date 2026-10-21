import subprocess
import sys
import tempfile
from pathlib import Path

# The five pilot tasks we are evaluating
PILOT_TASKS = {
    "T01": ("winner", "faulty_no_diag.py"),
    "T08": ("is_valid_row", "faulty_zero_dup.py"),
    "T14": ("merge_row", "faulty_merge_twice.py"),
    "T25": ("step", "faulty_edges_wrap.py"),
    "T31": ("is_valid_reversi_move", "faulty_only_rows.py")
}

def run_spec_against_impl(spec_path, impl_path, func_name):
    """Runs a specification against an implementation. Returns True if accepted."""
    if not Path(spec_path).exists():
        print(f"  [ERROR] Specification not found: {spec_path}")
        return None
    if not Path(impl_path).exists():
        print(f"  [ERROR] Implementation not found: {impl_path}")
        return None

    spec_code = Path(spec_path).read_text()
    impl_code = Path(impl_path).read_text()
    
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # Save implementation as 'impl.py'
        (tmp / "impl.py").write_text(impl_code)
        
        # Create a temporary test file that combines the spec and the function
        test_file_content = f"""
from impl import {func_name} as func

{spec_code}

def test_execution():
    # In this simple pilot, we just check if the spec executes without errors
    pass
"""
        (tmp / "test_spec.py").write_text(test_file_content)
        
        # Run pytest
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(tmp / "test_spec.py"), "-q"],
            capture_output=True, text=True
        )
        return result.returncode == 0 # True (accepted), False (rejected)

def run_pilot():
    print("=== STARTING PILOT HARNESS ===\n")
    
    for task, (func_name, faulty_file) in PILOT_TASKS.items():
        print(f"--- Testing Task {task} ---")
        
        spec_path = f"specs/parsed/{task}/strategy_a.py"
        correct_impl = f"impl/{task}/correct_a.py"
        faulty_impl = f"impl/{task}/{faulty_file}"
        
        # 1. Check against correct implementation
        accept_correct = run_spec_against_impl(spec_path, correct_impl, func_name)
        if accept_correct is True:
            print(" Correct implementation: ACCEPTED (OK)")
        elif accept_correct is False:
            print(" Correct implementation: REJECTED (False Rejection)")
        
        # 2. Check against faulty implementation
        accept_faulty = run_spec_against_impl(spec_path, faulty_impl, func_name)
        if accept_faulty is True:
            print(" Faulty implementation: ACCEPTED (False Acceptance - bug missed!)")
        elif accept_faulty is False:
            print(" Faulty implementation: REJECTED (Bug caught!)")
            
        print() # Empty line for readability

if __name__ == "__main__":
    run_pilot()