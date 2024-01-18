import subprocess
import os
import time

ITER = 100000
FIB = 50

def main():
    compile_rust()
    compile_java()
    rust_time = int(run_rust(ITER, FIB))
    java_time = int(run_java(ITER, FIB))
    result = compare(rust_time, java_time)
    print(result)

# rust
def compile_rust():
    os.chdir('./rust-fibonacci')
    subprocess.run(["cargo", "build", "--release"], check=True)
    os.chdir('..')
    
def run_rust(iterations, max_fib):
    result = subprocess.run(["./rust-fibonacci/target/release/rust-fibonacci", str(iterations), str(max_fib)], capture_output=True, text=True, check=True)
    return result.stdout

def compile_java():
    os.chdir('./java-fibonacci')
    subprocess.run(["javac", "FibMemo.java"], check=True)
    os.chdir('..')

def run_java(iterations, max_fib):
    os.chdir('./java-fibonacci')
    result = subprocess.run(["java", "FibMemo", str(iterations), str(max_fib)], capture_output=True, text=True, check=True)
    return result.stdout

def compare(rust_time, java_time):
    ratio = min(rust_time, java_time) / max(rust_time, java_time)
    winner = 'rust' if rust_time < java_time else 'java'
    not_winner = 'rust' if winner == 'java' else 'java'
    return f"""
The winner is {winner} which finished in {ratio:.2f}% of the time that {not_winner} took.
Rust time: {rust_time}
Java time: {java_time}
"""

if __name__ == '__main__':
    main()