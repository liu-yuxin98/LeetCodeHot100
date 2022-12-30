import java.util.Arrays;

public class squareOfSortedArray977 {
    // best way
    public int [] sortedSquares(int[] nums){
        int n = nums.length;
        int[] result = new int[n];
        int left = 0;
        int right = n - 1;

        for (int i = n - 1; i >= 0; i--) {
            int square;
            if (Math.abs(nums[left]) < Math.abs(nums[right])) {
                square = nums[right];
                right--;
            } else {
                square = nums[left];
                left++;
            }
            result[i] = square * square;
        }
        return result;
    }

}

    // fast 100% memory 60%
//    public int [] sortedSquares(int[] nums){
//        int numNegative = 0;
//        for(int i = 0; i < nums.length; i++){
//            if(nums[i]<0){
//                numNegative += 1;
//            }
//            if(nums[i]>=0){
//                break;
//            }
//        }
//        if(numNegative==0){
//            int[] res = new int[nums.length];
//            for(int i = 0; i < nums.length; i++){
//                res[i] = (int)Math.pow(nums[i],2);
//            }
//        }
//        int [] negatives = new int[numNegative];
//        int [] positives = new int[nums.length-numNegative];
//        for(int i= numNegative-1;i>=0;i--){
//            negatives[numNegative-1-i] = (int)Math.pow(nums[i], 2);
//        }
//        for(int i = numNegative; i < nums.length; i++){
//            positives[i-numNegative] = (int) Math.pow(nums[i], 2);
//        }
////        System.out.println(Arrays.toString(negatives));
////        System.out.println(Arrays.toString(positives));
//        int [] res = new int[nums.length];
//        int i = 0;
//        int j = 0;
//        int index = 0;
//        while(true){
//            if(i>=negatives.length || j>= positives.length){
//                break;
//            }
//            if(negatives[i] <=positives[j]){
//                res[index] = negatives[i];
//                i++;
//                index ++;
//            }else{
//                res[index] = positives[j];
//                j++;
//                index++;
//            }
//        }
//        if(i==negatives.length){
//            while(j< positives.length){
//                res[index] = positives[j];
//                j++;
//                index++;
//            }
//        } else{
//            while(i<negatives.length){
//                res[index] = negatives[i];
//                i++;
//                index ++;
//            }
//        }
//
//        return res;
//    }

    // very stupid method
//    public int[] sortedSquares(int[] nums) {
//        int [] res = new int[nums.length];
//        int negative = -1;
//        int positive = -1;
//        int numzero = 0;
//        if(nums.length ==1 ){
//            res[0] = (int)Math.pow(nums[0],2);
//            return res;
//        }
//        for(int i=0;i<nums.length-1; i++){
//            if(nums[i]==0){
//                numzero += 1;
//            }
//            if(nums[i]<0 && nums[i+1]>=0){
//                negative = i;
//            }
//            if(nums[i]<=0 && nums[i+1]>0){
//                positive = i+1;
//            }
//        }
//        if(nums[nums.length - 1] ==0){
//            numzero ++;
//        }
//        // first append 0
//        for(int i=0; i < numzero;i++){
//            res[i] = 0;
//        }
//        int index = numzero;
//        if(numzero==nums.length){
//            return res;
//        }
//        System.out.println(negative+" "+positive+" "+numzero);
//
//        // different situations
//        if(negative>=0 && positive==-1){
//            // none positive
//            for(int i = negative;i>=0;i--){
//                res[index] = (int)Math.pow(nums[i],2);
//                index ++;
//            }
//        } else if(negative >= 0 && positive >= 0){
//            // both negative and positive
//            while(true){
//                if(negative<0 || positive>nums.length-1){
//                    break;
//                }
//                if(Math.pow(nums[positive],2)>=Math.pow(nums[negative],2)){
//                    res[index] = (int)Math.pow(nums[negative], 2);
//                    index += 1;
//                    negative -= 1;
//                }   else{
//                    res[index] = (int)Math.pow(nums[positive], 2);
//                    index += 1;
//                    positive += 1;
//                }
//            }
//            if(negative<0){
//                while(positive<nums.length){
//                    res[index] = (int)Math.pow(nums[positive], 2);
//                    index += 1;
//                    positive += 1;
//                }
//            }
//            if(positive>nums.length-1){
//                while(negative > -1){
//                    res[index] = (int)Math.pow(nums[negative], 2);
//                    index += 1;
//                    negative -= 1;
//                }
//            }
//
//        } else if(negative<0 && positive>=0) {
//            // none negative
//            while (positive < nums.length) {
//                res[index] = (int) Math.pow(nums[positive], 2);
//                index += 1;
//                positive += 1;
//            }
//
//        } else{
//            // negative <0 pos <0
//            // all positive
//            if(nums[0]>0){
//                for(int i = 0; i < nums.length; i++){
//                    res[i] = (int)Math.pow(nums[i], 2);
//                }
//            } else{
//                for(int i = 0; i < nums.length; i++){
//                    res[nums.length - 1-i] = (int)Math.pow(nums[i], 2);
//                }
//            }
//        }
//        return res;
//
//    }

