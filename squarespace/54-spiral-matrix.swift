//  Write some awesome Swift code, or import libraries like "Foundation",
//  "Dispatch", or "Glibc"

print("Hello world!")

var matrix = [[1,2,3,4],[4,5,6,4],[7,8,9,4]]
print(String(matrix.count))
print(String(matrix[0].count))
// Return [1,2,3,4,5,6,7,8,9]

class Solution {
    func spiralOrder(_ matrix: [[Int]]) -> [Int] {
		var result = [Int]()
        if (matrix.count == 0) {
			return result
		}

		var rowStart = 0
		var rowEnd = matrix.count - 1
		var colStart = 0
		var colEnd = matrix[0].count - 1

		while (rowStart <= rowEnd && colStart <= colEnd) {
			// Go to the right
			for j in colStart ... colEnd {
				result.append(matrix[rowStart][j])
			}

            rowStart += 1

            // Go down
			for j in rowStart ... rowEnd {
				result.append(matrix[j][colEnd])
			}
            colEnd -= 1

            if (rowStart <= rowEnd) {
                // Go Left
				for j in revecolEnd ... colStart {
					result.append(matrix[rowEnd][j])
				}
            }
            rowEnd -= 1

            if (colBegin <= colEnd) {
                // Go up
				for j in rowEnd ... rowStart {
					result.append(matrix[j][colStart])
				}
            }
            colStart += 1;
		}
    }
}
