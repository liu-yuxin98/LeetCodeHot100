package codetop;

import java.util.HashMap;

public class Medium3LongestSubstringWithoutRepeatingCharacters {
    public static int lengthOfLongestSubstring(String s) {
        if(s.length()==0){
            return 0;

        }
        int maxl = 0;
        int front = 0;
        int end = 0;
        HashMap<Character,Integer> hmap = new HashMap<>();
        while(end<s.length()){
            if(hmap.containsKey(s.charAt(end))){
                maxl = Math.max(maxl,end-front);
                // move front forward and remove items from hmap
                int preEnd = hmap.get(s.charAt(end));
                while(front<=preEnd){
                    hmap.remove(s.charAt(front));
                    front++;
                }
            }
            hmap.put(s.charAt(end),end);
            end ++;
        }
        maxl = Math.max(maxl,end-front);
        return maxl;
    }

    public static void main(String[] args) {
        String s ="aaa";
        System.out.println(lengthOfLongestSubstring(s));

    }
}
