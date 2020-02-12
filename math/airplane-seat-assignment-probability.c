

double nthPersonGetsNthSeat(int n){
    /*
     * https://leetcode.com/problems/airplane-seat-assignment-probability/
     *
     * f(n) denotes the probability that the n-th person can get his own seat.
     * The first peroson pick a seat randomly, and the probability that he(she)
     * pick his own seat, is 1/n. If he picks the second seat, then for the rest
     * passengers, the situation is similar to there are n-1 seats. The second
     * person has to pick a seat randomly, so the probability that the last
     * person get his own seat, is f(n-1). 
     * So f(n) = 1/n + 1/n * f(n-1) + ... 1/n * f(2). f(1) = 1, thus
     * f(n) = 1/n * (f(n-1)+..+f(1))   (1)
     * f(n-1) = 1/(n-1) * (f(n-2)+..+f(1)) (2) 
     * n > 2.
     * Using (1) subtract (2), f(n)-(n-1)*f(n-1)=f(n-1), n>2.
     * So f(n) = f(n-1) for n>2.
     */
    return n==1?1:0.5;
}

