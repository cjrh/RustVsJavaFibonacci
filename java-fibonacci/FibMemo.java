import java.time.Duration;
import java.time.Instant;
import java.util.HashMap;

public class FibMemo {
    private static HashMap<Long, Long> memo = new HashMap<>();
    static {
        memo.put(0l, 0l);
        memo.put(1l, 1l);
        memo.put(2l, 1l);
        memo.put(3l, 2l);
    }

    // 0.004000
    public static void main(String[] args) {
        Instant start = Instant.now();
        for (int i = 0; i < Integer.parseInt(args[0]); i++) {
            fibToN(Integer.parseInt(args[1]));
        }
        Instant end = Instant.now();
        Duration timeElapsed = Duration.between(start, end);
        Long nanos = timeElapsed.toNanos();
        System.out.println(nanos);
    }

    private static void fibToN(long n) {
        for (long i = 0; i < n; i++) {
            fib(i);
        }
    }

    private static long fib(long n) {
        long thisFibbed;
        if (memo.containsKey(n)) {
            thisFibbed = memo.get(n);
        } else {
            thisFibbed = fib(n - 2) + fib(n - 1);
            memo.put(n, thisFibbed);
        }
        return thisFibbed;
    }
}