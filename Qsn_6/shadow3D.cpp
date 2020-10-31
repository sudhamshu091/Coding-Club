int shadow3D(vector<vector<int>>& grid) {
        int N = grid.size();
        int ans = 0;

        for (int i = 0; i < N;  ++i) {
            int row = 0;
            int col = 0; 
            for (int j = 0; j < N; ++j) {
                if (grid[i][j] > 0) ans++;
                row = max(row, grid[i][j]);
                col = max(col, grid[j][i]);
            }
            ans += row + col;
        }

        return ans;
    }
