func projectionArea(_ grid: [[Int]]) -> Int {
    var N = grid.count
    var ans = 0
    
    var i = 0
    while i < N {
        var bestRow = 0
        var bestCol = 0
        var j = 0
        while j < N {
            if grid[i][j] > 0 {
                ans += 1
            }
            bestRow = max(bestRow, grid[i][j])
            bestCol = max(bestCol, grid[j][i])
            j += 1
        }
        ans += bestRow + bestCol
        i += 1
    }
    
    return ans
}
