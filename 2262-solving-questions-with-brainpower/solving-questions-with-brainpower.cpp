class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        int n = questions.size();
        vector<long long> t(n + 1, 0); // DP table to store maximum points
        
        for (int i = n - 1; i >= 0; i--) {
            long long solveCurrent = questions[i][0];
            int nextIndex = i + questions[i][1] + 1;
            
            if (nextIndex < n) {
                solveCurrent += t[nextIndex]; // Add points from valid index
            }

            t[i] = max(solveCurrent, t[i + 1]); // Take max of solving or skipping
        }

        return t[0]; // Maximum points from 0 to n-1
    }
};
