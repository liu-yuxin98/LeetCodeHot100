import java.util.HashMap;
import java.util.Map;

public class ValidAnagram242 {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();
        for(Character ch : s.toCharArray()){
            sMap.put(ch,sMap.getOrDefault(ch,0)  +1);
        }
        for(Character ch : t.toCharArray()){
            tMap.put(ch,tMap.getOrDefault(ch,0)  +1);
        }
        if(!sMap.equals(tMap)){
            return false;
        }
        System.out.println(sMap);
        System.out.println(tMap);
        for(Character ch: tMap.keySet()){
            Integer a = tMap.get(ch);
            Integer b = tMap.get(ch);
            if(a!=b){
                // !tMap.get(ch).equals(sMap.get(ch))
                System.out.println(ch);
                return false;
            }
        }
        return true;
    }

}
