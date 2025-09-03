class Solution { 
private:
    // sum of squares of digits of num
    int next(int num) {
        int sum = 0;
        while (num != 0) {
            int digit = num % 10;
            sum += (digit * digit);
            num /= 10;
        }
        return sum;
    }
public:
    bool isHappy(int n) {
        if (n == 1) return true;
        int slow = n, fast = next(n);
        do {
            slow = next(slow);
            fast = next(next(fast));
            if (fast == 1) return true;
        } while (slow != fast);
        return false;
    }
};