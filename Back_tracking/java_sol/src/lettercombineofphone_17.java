import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class lettercombineofphone_17 {

    List<String> res = new ArrayList<>();
    List<String> path = new ArrayList<>();
    HashMap<String, String> map = new HashMap<String, String>();

    public List<String> letterCombinations(String digits) {
        if(digits.length()==0){
            return res;
        }
        map.put("2","abc");
        map.put("3","def");
        map.put("4","ghi");
        map.put("5","jkl");
        map.put("6","mno");
        map.put("7","pqrs");
        map.put("8","tuv");
        map.put("9","wxyz");
        backtrack(digits,0);
        return res;
    }

    private void backtrack(String digits, int start){
        if(path.size()==digits.length()){
            res.add(String.join("",path));
            return;
        }

        String chr = Character.toString(digits.charAt(start));
        String s = map.get(chr);
        for(int j=0;j<s.length();j++){
                String c = Character.toString(s.charAt(j));
                path.add(c);
                backtrack(digits,start+1);
                path.remove(path.size() - 1);
            }

        }

    }

