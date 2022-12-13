import java.util.*;

public class reconstructItinerary332 {

    Deque<String> res;
    Map<String, Map<String, Integer>> map;


    private void backtrack(String airport, int ticketsNum){
        if(res.size()==ticketsNum+1){
            return;
        }
        if(!map.containsKey(airport)){
            return;
        }
        for(Map.Entry< String,Integer> entry:map.get(airport).entrySet()){
            if(entry.getValue()==0){
                continue;
            }
            res.add(entry.getKey());
            entry.setValue(entry.getValue()-1);
            backtrack(entry.getKey(), ticketsNum);
            if(res.size()==ticketsNum + 1){
                return;
            }
            res.removeLast();
            entry.setValue(entry.getValue()+1);
        }

    }
    public List<String> findItinerary(List<List<String>> tickets) {
        // initial map in form of {A:{B:1,C:2}, B:{A:1,C:1}...}. for each internal map we use tree map to keep the order
        map = new HashMap<String, Map<String,Integer>>();
        res = new LinkedList<>();
        for(List<String> t:tickets){
            Map<String, Integer> temp;
            if(map.containsKey(t.get(0))){
                temp = map.get(t.get(0));
                temp.put(t.get(1),temp.getOrDefault(t.get(1),0)+1);
            } else{
                temp = new TreeMap<>(); // tree map are sorted by key in default
                temp.put(t.get(1),1);
            }
            map.put(t.get(0),temp);
        }
        res.add("JFK");
        backtrack("JFK", tickets.size());
        return new ArrayList<>(res);
    }
}
