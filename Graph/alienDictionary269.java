import java.util.*;

public class alienDictionary269 {
    public String alienOrder(String[] words) {
        // Step 0: Create data structures and find all unique letters.
        Map<Character, List<Character>> adjList = new HashMap<>();
        // counts record how many incoming edges of a node
        Map<Character, Integer> counts = new HashMap<>();
        for (String word : words) {
            for (char c : word.toCharArray()) {
                counts.put(c, 0);
                adjList.put(c, new ArrayList<>());
            }
        }
        // find all edges " relationship we can obtain from the words"
        for(int i = 0; i < words.length-1; i++){
            String word1 = words[i];
            String word2 = words[i+1];
            System.out.println(word1+" "+word2);
            // check if word2 is the prefix of word1
            if(word1.length()>word2.length() && word1.startsWith(word2)){
                return "";
            }
            // find first char that not match and insert edge into relations
            for(int j = 0; j < Math.min(word1.length(), word2.length()); j++){
                    if(word1.charAt(j) != word2.charAt(j)){
                        System.out.println(word1.charAt(j) + " " +word2.charAt(j));
                        adjList.get(word1.charAt(j)).add(word2.charAt(j));
                        counts.put(word2.charAt(j), counts.get(word2.charAt(j))+1);
                        break;
                    }
            }
        }
        System.out.println(adjList);
        // bfs Kahn's Algorithm
        StringBuilder sb = new StringBuilder();
        Queue<Character> queue = new LinkedList<>();
        for(Character c: counts.keySet()){
            // no incoming edges
            if(counts.get(c).equals(0)){
                queue.add(c);
            }
        }
        while(!queue.isEmpty()){
            Character c = queue.remove();
            sb.append(c);
            for(Character next: adjList.get(c)){
                counts.put(next, counts.get(next)-1);
                if(counts.get(next).equals(0)){
                    queue.add(next);
                }
            }

        }
        if(sb.length() < counts.size()){
            return "";
        }
        return sb.toString();

    }



//    HashMap<Character, HashSet<Character>> relationshipPreChar ;
//    HashMap<Character, HashSet<Character>> relationshipLaterChar ;
//
//    HashMap<Character,Character> relationshipFinal;
//    private Character [] relation(String word1, String word2){
//        Character [] res = null;
//        // return a relationship we get from word1 and word2.
//        int n = Math.min(word1.length(),word2.length());
//        int diff = 0;
//        // add char to map
//        for (int i = 0; i < n; i++) {
//            //forward
//            if(!relationshipLaterChar.containsKey(word1.charAt(i))){
//                relationshipLaterChar.put(word1.charAt(i),new HashSet<>());}
//            if(!relationshipLaterChar.containsKey(word2.charAt(i))){
//                relationshipLaterChar.put(word2.charAt(i),new HashSet<>());}
//            // back
//            if(!relationshipPreChar.containsKey(word1.charAt(i))){
//            relationshipPreChar.put(word1.charAt(i),new HashSet<>());}
//            if(!relationshipPreChar.containsKey(word2.charAt(i))){
//            relationshipPreChar.put(word2.charAt(i),new HashSet<>());}
//        }
//        if(word1.length()>n){
//            for(int i = n-1; i < word1.length(); i++){
//                if(!relationshipLaterChar.containsKey(word1.charAt(i))){
//                    relationshipLaterChar.put(word1.charAt(i),new HashSet<>());}
//                if(!relationshipPreChar.containsKey(word1.charAt(i))){
//                    relationshipPreChar.put(word1.charAt(i),new HashSet<>());}
//            }
//
//        }
//        if(word2.length()>n){
//            for(int i = n-1; i < word2.length(); i++){
//                if(!relationshipLaterChar.containsKey(word2.charAt(i))){
//                    relationshipLaterChar.put(word2.charAt(i),new HashSet<>());}
//                if(!relationshipPreChar.containsKey(word2.charAt(i))){
//                    relationshipPreChar.put(word2.charAt(i),new HashSet<>());}
//            }
//        }
//        for (int i = 0; i < n; i++) {
//            if(word1.charAt(i) == word2.charAt(i)){
//                continue;
//            }
//
//            if(word1.charAt(i) != word2.charAt(i)){
//                diff +=1 ;
//                if(diff==1) {
//                    res = new Character[]{word1.charAt(i), word2.charAt(i)};
//                }
//            }
//        }
//
//        if(diff==0 && word1.length()>word2.length()){
//            return new Character[] {'0','0'};
//        }
//
//        return res;
//    }
//    public String alienOrder(String[] words) {
//        if(words.length == 1){
//            HashSet<Character> chars = new HashSet<>();
//            for(int i = 0; i < words[0].length(); i++) {
//                chars.add(words[0].charAt(i));
//            }
//            StringBuilder sb = new StringBuilder();
//            for(Character c:chars){
//                sb.append(c);
//            }
//            return sb.toString();
//        }
//        relationshipPreChar = new HashMap<>();
//        relationshipLaterChar = new HashMap<>();
//        relationshipFinal = new HashMap<>();
//
//        for(int i = 0; i < words.length-1; i++){
//            Character [] relation = relation(words[i],words[i+1]);
//            System.out.println(words[i]+" "+words[i+1]+" "+Arrays.toString(relation));
//            if(relation==null){
//                continue;
//            }
//            if(relation[0] =='0' && relation[1]=='0'){
//                return "";
//            }
//            relationshipPreChar.get(relation[1]).add(relation[0]);
//            relationshipLaterChar.get(relation[0]).add(relation[1]);
//        }
//        System.out.println(relationshipPreChar);
//        System.out.println(relationshipLaterChar);
//
//
//        // find last char
//        Character last = null;
//        for(Character c:relationshipLaterChar.keySet()){
//            if(relationshipLaterChar.get(c).isEmpty()){
//                last = c;
//                break;
//            }
//        }
//        System.out.println(last);
//        if(last == null){
//            return "";
//        }
//        // remove reduction in relationshipLaterChar
//        for(Character c : relationshipLaterChar.keySet()){
//            HashSet<Character> oriset = relationshipLaterChar.get(c);
//            Character next = null;
//            for(Character child:oriset){
//                // check if loop exists
//                HashSet<Character> childLater = relationshipLaterChar.get(child);
//                if(childLater.contains(c)){
//                    return "";
//                }
//                HashSet<Character> childPres = relationshipPreChar.get(child);
//                Boolean containsPre = false;
//                for(Character pre:childPres){
//                    if(oriset.contains(pre)){
//                        containsPre = true;
//                    }
//                }
//                if(!containsPre){
//                    next = child;
//                }
//            }
//            relationshipFinal.put(c,next);
//        }
//
//        System.out.println(relationshipFinal);
//
//        int totalLength = 0;
//        // find first char
//        Character first = 'a';
//        for(Character c:relationshipPreChar.keySet()){
//            totalLength += 1;
//            if(relationshipPreChar.get(c).isEmpty()){
//                first = c;
//            }
//        }
//        // convert relationshipLaterChar to string
//        System.out.println(totalLength);
//        System.out.println("=======================");
//        List<Character> alinewords = new ArrayList<>();
//
//        while(true){
//            if(alinewords.size() == totalLength){
//                StringBuilder sb = new StringBuilder();
//                for (Character c : alinewords) {
//                    sb.append(c);
//                }
//                String res = sb.toString();
//                return res;
//            }
//            alinewords.add(first);
//            Character next = relationshipFinal.get(first);
//
//            System.out.println(first+" "+next);
//            if(alinewords.contains(next)){
//                // invalid
//                return "";
//            }
//            if(next==null){
//                // random select a new char that not in alinewords to represent first
//                for (Character c : relationshipPreChar.keySet()) {
//                    if(!alinewords.contains(c)){
//                        HashSet<Character> set = relationshipPreChar.get(c);
//                        Boolean containsallpre =  true;
//                        // make sure all c's pre is already in alinewords
//                        for(Character temppre:set){
//                            if(!alinewords.contains(temppre)){
//                                containsallpre = false;
//                                break;
//                            }
//                        }
//                        if(containsallpre){
//                        next = c;
//                        System.out.println(next);
//                        break;}
//                    }
//                }
//            } else{
//                // check if next can be placed at next
//
//                    // check if there must be some c in front of next
//                    for(Character c : relationshipFinal.keySet()){
//                        if(alinewords.contains(c)){
//                        } else{
//                            // word not in alinewords and must be put in front of next
//                            if(relationshipFinal.get(c) ==next){
//                                next = c;
//                            }
//
//                        }
//                    }
//
//
//
//            }
//            first = next;
//
//        }
//
//    }
}
