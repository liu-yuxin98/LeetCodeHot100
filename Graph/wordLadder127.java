import java.util.*;

public class wordLadder127 {
    private Boolean adjacentPair(String s1, String s2) {
        if (s1.length() != s2.length()) {
            return false;
        }
        int diff = 0;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                diff += 1;
            }
        }
        return diff == 1;
    }


    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        HashMap<String, List<String>> AL = new HashMap<String, List<String>>();
        for (String word1 : wordList) {
            AL.put(word1, new ArrayList<>());
            for (String word2 : wordList) {
                if (adjacentPair(word1, word2)) {
                    AL.get(word1).add(word2);
                }
            }
        }
        AL.put(beginWord, new ArrayList<>());
        for (String word : wordList) {
            if (adjacentPair(beginWord, word)) {
                AL.get(beginWord).add(word);
            }
        }

        // bfs
        HashMap<String, String> parent = new HashMap<>();
        HashSet<String> visited = new HashSet<>();
        parent.put(beginWord, "0");
        Deque<String> fringe = new LinkedList<>();
        fringe.add(beginWord);
        visited.add(beginWord);

        while (fringe.size() > 0) {
            String s = fringe.removeFirst();
            List<String> neighbors = AL.get(s);
            for (String neighbor : neighbors) {
                if (!visited.contains(neighbor)) {
                    fringe.addLast(neighbor);
                    parent.put(neighbor, s);
                    visited.add(neighbor);
                    if (neighbor == endWord) {
                        break;
                    }
                }
            }
        }

        if(!parent.containsKey(endWord)){
            return 0;
        }

//        for (String word : parent.keySet()) {
//                System.out.println(word + " " + parent.get(word));
//        }

        int step = 1;
        String end = endWord;
        while(true){
            System.out.println(end);
            if(end ==beginWord){
                return step;
            }
            String pre = parent.get(end);
            end = pre;
            step += 1;
        }

    }
}
