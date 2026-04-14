class Solution {
    public void rotate(int[][] matrix) {

        for(int i=0;i<matrix[i].length;i++){
            for(int j=0;j<mattrix[i].length;j++){
                if(j>=i){
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }
        }
        for (int i = 0;i<matrix.length;i++){
            int left = 0;
            int right = matrix[i].length - 1;
            while(left <= rigth){
                int temp = matrix[i][left];
                matrix[i][left] = matrix[i][right];
                matrix[i][right] = temp;
                left ++;
                right --;
            }
        }
        
    }
}
