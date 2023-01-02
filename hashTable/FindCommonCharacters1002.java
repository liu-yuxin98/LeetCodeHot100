import java.util.*;

public class FindCommonCharacters1002 {
    // array to represent hashtable
    public List<String> commonChars(String[] words) {
        int [] allCount = new int[26];
        for(int i = 0; i < words.length; i++){
            int[] chaCount = new int[26];
            for(char c : words[i].toCharArray()){
                chaCount[(int)c-'a'] ++;
            }
            // compare with allCount and update
            if(i==0){
                allCount = chaCount;
            }
            for(int j = 0; j <chaCount.length; j++){
                    allCount[j] = Math.min(allCount[j],chaCount[j]);
            }
        }
        List<String> res = new ArrayList<>();
        for (int i = 0; i < allCount.length; i++) {
            for(int j = 0; j< allCount[i]; j++){
                char c = (char)('a'+i);
                res.add(String.valueOf(c));
            }
        }
        return res;
    }
//    public List<String> commonChars(String[] words) {
//        HashMap<Character,Integer> preTable = new HashMap<>();
//        for(char c : words[0].toCharArray()){
//            preTable.put(c, preTable.getOrDefault(c,0)+1);
//        }
//
//        for (int i = 1; i < words.length; i++) {
//            HashMap<Character,Integer> curTable = new HashMap<>();
//            for(char c : words[i].toCharArray()){
//                curTable.put(c, curTable.getOrDefault(c,0)+1);
//            }
//            // compare two table and only leaves common character
//            HashMap<Character,Integer> temp = new HashMap<>();
//            for(Character c: preTable.keySet()){
//                if(curTable.containsKey(c)){
//                    temp.put(c, Math.min(preTable.get(c), curTable.get(c)));
//                }
//            }
//            preTable = new HashMap<>();
//            preTable.putAll(temp);
//            System.out.println(preTable);
//        }
//
//        System.out.println(preTable);
//
//        List<String> res = new ArrayList<>();
//        for(Character c : preTable.keySet()){
//            for(int i = 0; i < preTable.get(c);i++){
//                res.add(c.toString());
//            }
//        }
//        return res;
//    }
}
