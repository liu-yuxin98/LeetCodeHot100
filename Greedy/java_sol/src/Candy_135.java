import java.util.ArrayList;

public class Candy_135 {
//    public static int calculate_addvalue(int left, int right){
//        int add_value = 0;
//        for(int k=1;k<1+right-left;k++){
//            add_value +=k;
//        }
//        return add_value;
//    }

//    public static int candy(int[] ratings) {
//
//        if(ratings.length<=1){
//            return 1;
//        }
//        ArrayList<Integer> local_min = new ArrayList<Integer>();
//        ArrayList<Integer> local_max = new ArrayList<Integer>();
//        // begin
//        if(ratings[0] <= ratings[1]){
//            local_min.add(0);
//        }else{
//            local_max.add(0);
//        }
//
//        for(int i=1;i<ratings.length-1; i++){
//                if( (ratings[i] > ratings[i-1] && ratings[i] >= ratings[i+1]) ||
//                        (ratings[i] >= ratings[i-1] && ratings[i] > ratings[i+1])){
//                    local_max.add(i);
//                }
//                if(ratings[i]<= ratings[i-1] && ratings[i] <= ratings[i+1]){
//                    local_min.add(i);
//                }
//        }
//        // end
//        if(ratings[ratings.length - 1] <= ratings[ratings.length - 2]){
//            local_min.add(ratings.length - 1);
//        }else{
//            local_max.add(ratings.length - 1);
//        }
//        System.out.println(local_min.toString());
//        System.out.println(local_max.toString());
//
//        int i = 0;
//        int j = 0;
//        int candy = ratings.length;
//        int left_index = 0;
//        int right_index = 0;
//        int cur_max = 0;
//
//        for(i=0;i<local_max.size();i++){
//
//            if(local_max.get(0) < local_min.get(0)){
//                cur_max = local_max.get(0);
//                right_index = local_min.get(0);
//                int add_value = calculate_addvalue(cur_max,right_index);
//                candy += add_value;
//                continue;
//            }
//            cur_max = local_max.get(i);
//
//
//            while(true){
//                if(j >=local_min.size()){
//                    left_index = local_min.get(local_min.size() - 1);
//                    int add_value = calculate_addvalue(left_index,cur_max);
//                    candy += add_value;
//                    break;
//                }
//
//                if(local_min.get(j)<cur_max && local_min.get(j+1)>cur_max){
//                    left_index = local_min.get(j);
//                    right_index = local_min.get(j+1);
//                    if(cur_max-left_index>=right_index-cur_max){
//                        int add_value = calculate_addvalue(left_index,cur_max);
//                        candy += add_value;
//
//                    } else{
//                        int add_value = calculate_addvalue(cur_max,right_index);
//                        candy += add_value;
//                    }
//                    break;
//                }
//                j++;
//            }
//
//        }
//        return candy ;
//    }
    public static int candy(int[] ratings){
        // store candy values in candy
        int[] candy = new int[ratings.length];
        for(int i=0;i<candy.length; i++){
            candy[i] = 1;
        }
        // from left to right if r[i+1]>r[i]
        for(int i = 0; i < ratings.length-1; i++){
            if(ratings[i+1]>ratings[i] ){
                candy[i+1] = candy[i]+1;
            }
        }
        // from right to left
        for(int i=ratings.length - 1; i > 0; i--){
            if(ratings[i-1]> ratings[i]){
                candy[i-1] =  Math.max(candy[i-1],candy[i]+1);
            }
        }
        int res = 0;
        for(int i = 0; i < candy.length; i++){
            res += candy[i];
        }
        return res;
    }
    public static void main(String[] args) {
        int [] ratings = new int[]{1,2,2};
        int output = candy(ratings);
        System.out.println(output);
    }
}
