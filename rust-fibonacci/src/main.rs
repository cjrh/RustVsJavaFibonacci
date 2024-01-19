use std::env::args;
use std::time::Instant;
use hashbrown::HashMap;

static mut MEMO: Option<HashMap<u64, u64>> = None;

fn main() {
    unsafe {
        MEMO = Some(HashMap::from([(0, 0), (1, 1), (2, 1), (3, 2)]));
    }
    let iterations = args().nth(1).unwrap().parse::<u64>().unwrap();
    let fib = args().nth(2).unwrap().parse::<u64>().unwrap();
    let start = Instant::now();
    for _ in 0..iterations {
        fib_to_n(fib);
    }
    let end = Instant::now();
    let elapsed_time = end.duration_since(start);
    let nanos = elapsed_time.as_nanos();
    println!("{}", nanos);
}

fn fib_to_n(n: u64) {
    for i in 1..n {
        fib(i);
    }
}

fn fib(n: u64) -> u64 {
    let fib_n;
    unsafe {
        let memo_option = MEMO.as_ref().unwrap().get(&n).map(|x| *x);
        if let Some(val) = memo_option {
            fib_n = val;
        } else {
            let a = fib(n - 1);
            let b = fib(n - 2);
            fib_n = a + b;
            MEMO.as_mut().unwrap().insert(n, fib_n);
        }
    }
    return fib_n;
}
