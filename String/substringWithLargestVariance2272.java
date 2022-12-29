import java.util.*;
import java.util.concurrent.BrokenBarrierException;

public class substringWithLargestVariance2272 {
    // still has problem in find max variance for a string only contains two characters
    private int maxVarianceSubArray(String s, Character a, Character b, Map<Character, Integer> map) {
        // only calculate max variance between character a and b. ignore other character
        int aRemain = map.get(a);
        int bRemain = map.get(b);
        int aFreq = 0;
        int bFreq = 0;
        int max = 0;
        for(int i = 0; i <s.length();i++){
            if(s.charAt(i) ==b){
                bFreq ++;
            }
            if(s.charAt(i) ==a){
                aFreq ++;
                aRemain --;
            }
            if(aFreq>0){
                max = Math.max(max,bFreq-aFreq);
            }
            if(bFreq<aFreq && aRemain>=1){
                bFreq = 0;
                aFreq = 0;
            }
        }
        return max;
    }

    public int largestVariance(String s){
            // Maintain a map of freq of characters in the string
            Map<Character, Integer> map = new HashMap<>();
            for (char c : s.toCharArray())
                map.put(c, map.getOrDefault(c, 0) + 1);
            System.out.println(map);
            int max = 0;
            // Check for every possible pair of characters in the map with the assumption that the one char is greater than the other
            for (char c1 : map.keySet()) {
                for (char c2 : map.keySet()) {
                    if (c1 == c2 || map.get(c1) == 0 || map.get(c2) == 0) {
                        continue;
                    }
                    max = Math.max(maxVarianceSubArray(s, c1, c2, map),max);
                    System.out.println(c1+" "+c2+" "+max);
                }
            }
            return max;
    }

}


//    public int largestVariance(String s) {
//        Set<Character> maxChars = new HashSet<>();
//        Set<Character> minChars = new HashSet<>();
//        int front = 0;
//        int end = s.length()-1;
//        HashMap<Character,Integer> map = new HashMap<Character, Integer>();
//        for(int i = 0; i <s.length();i++){
//            int val = map.getOrDefault(s.charAt(i),0);
//            map.put(s.charAt(i),val+1);
//        }
////        System.out.println(map);
//        Character maxC = s.charAt(0);
//        Character minC = s.charAt(0);
//        for (Character c:map.keySet()) {
//            if(map.get(c)>map.get(maxC)){
//                maxC = c;
//            }
//            if(map.get(c)<map.get(minC)){
//                minC = c;
//            }
//        }
//        for(Character c:map.keySet()){
//            if(map.get(c) == map.get(maxC)){
//                maxChars.add(c);
//            }
//            if(map.get(c)==map.get(minC)){
//                minChars.add(c);
//            }
//        }
//        int maxV = map.get(maxC) - map.get(minC);
//
//
//        while(end>front){
//
//            if(minChars.contains(s.charAt(end)) ){
//                map.put(s.charAt(end),map.get(s.charAt(end))-1);
//                // decide if s.charAt(end) still in substring
//                if(maxChars.contains(s.charAt(end))){
//                    maxChars.remove(s.charAt(end));
//                }
//                if(map.get(s.charAt(end)) ==0){
//                    map.remove(s.charAt(end));
//                    minChars.remove(s.charAt(end));
//                } else{
//                minChars = new HashSet<>();
//                minChars.add(s.charAt(end));
//                }
//                end -= 1;
//            }  else if(maxChars.contains(s.charAt(end))){
//                Character frontC = s.charAt(front);
//                map.put(frontC,map.get(frontC)-1);
//
//                if(minChars.contains(frontC)){
//                    // decide if frontC still in substring
//                    if(maxChars.contains(frontC)){
//                        maxChars.remove(frontC);
//                    }
//                    if(map.get(frontC) ==0){
//                        map.remove(frontC);
//                        minChars.remove(frontC);
//                    } else{
//                        minChars = new HashSet<>();
//                        minChars.add(frontC);
//                    }
//
//                } else if(maxChars.contains(frontC)){
//                    if(map.get(frontC)==0){
//                        // means all char appears only once in s[front,end]
//                        map.remove(frontC);
//                        //update maxChars and minChars
//                        minChars = new HashSet<>();
//                        maxChars = new HashSet<>();
//                        for(int j=front+1;j<=end;j++){
//                            minChars.add(s.charAt(j));
//                            maxChars.add(s.charAt(j));
//                        }
//                    } else {
//
//                        maxChars = new HashSet<>();
//                        // update maxChars
//                        maxC = s.charAt(end);
//                        for (Character c : map.keySet()) {
//                            if (map.get(c) >= map.get(maxC)) {
//                                maxC = c;
//                            }
//                        }
//                        for (Character c : map.keySet()) {
//                            if (map.get(c) == map.get(maxC)) {
//                                maxChars.add(c);
//                            }
//                        }
//                        // update minChars
//                        for (Character c : minChars) {
//                            minC = c;
//                            break;
//                        }
//                        if (map.get(frontC) == map.get(minC)) {
//                            minChars.add(frontC);
//                        }
//                    }
//
//                } else{
//                    // random select one item from minChars
//                    for(Character c:minChars){
//                        minC = c;
//                        break;
//                    }
//                    if(map.get(frontC)==map.get(minC)){
//                        minChars.add(frontC);
//                    }
//                }
//                front += 1;
//            } else{
//                Character frontC = s.charAt(front);
//
//                if(minChars.contains(frontC)){
//                    map.put(frontC,map.get(frontC)-1);
//                    if(maxChars.contains(frontC)){
//                        maxChars.remove(frontC);
//                    }
//                    if(map.get(frontC) ==0){
//                        map.remove(frontC);
//                        minChars.remove(frontC);
//                    } else{
//                        minChars = new HashSet<>();
//                        minChars.add(frontC);
//                    }
//
//
//                    front += 1;
//                }  else{
//                    Character lastC = s.charAt(end);
//                    map.put(lastC,map.get(lastC)-1);
//
//                    // random select one item from minChars and update minChars
//                    for(Character c:minChars){
//                        minC = c;
//                        break;
//                    }
//                    if(map.get(lastC)==map.get(minC)){
//                        minChars.add(lastC);
//                    }
//                    end -=1;
//                }
//            }
//
//            if(minChars.isEmpty()){
//                minChars = new HashSet<>(maxChars);
//            }
//            if(maxChars.isEmpty()){
//                maxChars = new HashSet<>(minChars);
//            }
//
//            //update maxV
//            // random select one item from minChars and update minChars
//            for(Character c:minChars){
//                minC = c;
//                break;
//            }
//            // random select one item from minChars and update minChars
//            for(Character c:maxChars){
//                maxC = c;
//                break;
//            }
//            System.out.println("substraing =" + s.substring(front,end+1));
//            System.out.println("minChars = " + minChars);
//            System.out.println("maxChars = " + maxChars);
//            System.out.println("map = " + map);
//            maxV = Math.max(maxV, map.get(maxC)- map.get(minC));
//
//        }
//
//        return maxV;
//    }


