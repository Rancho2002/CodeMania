int Solution::singleNumber(const vector<int> &A) {
    int ans = 0;  // Initialize the answer variable to store the result.
    
    // Iterate through each bit position from 31 to 0 (32 bits in an integer).
    for (int j = 31; j >= 0; j--) {
        int bit = 0;  // Counter to keep track of the number of '1' bits at position j.
        
        // Iterate through the given array A.
        for (int i = 0; i < A.size(); i++) {
            // Check if the j-th bit of A[i] is set (i.e., '1').
            if (A[i] & (1 << j)) {
                bit++;  // Increment the bit counter.
            }
        }
        
        // If the count of '1' bits at position j is not a multiple of 3, set the corresponding bit in the answer.
        if (bit % 3 != 0) {
            ans |= (1 << j);  // Set the j-th bit of ans to '1'.
        } else {
            ans |= (0 << j);  // Set the j-th bit of ans to '0' (this line is not necessary).
        }
    }
    
    return ans;  // Return the final answer.
}
