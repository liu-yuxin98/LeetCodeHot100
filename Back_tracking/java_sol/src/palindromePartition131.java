import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class palindromePartition131 {
    List<List<String>> res = new ArrayList<>();
    List<String> path = new LinkedList<>();
    public List<List<String>> partition(String s) {
        back_track(s,0);
        return res;
    }
    private void back_track(String s, int start){
        if(start>=s.length()){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i=start;i<s.length(); i++){
            String left = s.substring(start,i+1);
            if(isPalindrome(left)){
                path.add(left);
            } else{
                continue;
            }
            back_track(s,i+1);
            path.remove(path.size() - 1);
        }
    }

    private boolean isPalindrome(String s){
        if(s.length()==0){
            return true;
        }
        int start = 0;
        int end = s.length()-1;
        while(true){
            if(start>=end){
                return true;
            }
            if(s.charAt(start) != s.charAt(end)){
                return false;
            }
            start ++;
            end --;
        }
    }

}
