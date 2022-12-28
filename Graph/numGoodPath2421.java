import java.util.*;

public class numGoodPath2421 {
    public int numberOfGoodPaths(int[] vals, int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            // == python dict default
            adj.computeIfAbsent(a, value -> new ArrayList<Integer>()).add(b);
            adj.computeIfAbsent(b, value -> new ArrayList<Integer>()).add(a);
        }
        System.out.println(adj);
        int n = vals.length;
        TreeMap<Integer, List<Integer>> valuesToNodes = new TreeMap<>();
        for(int i = 0; i < n; i++){
            valuesToNodes.computeIfAbsent(vals[i],value->new ArrayList<Integer>()).add(i);
        }
        System.out.println(valuesToNodes);

        UnionFind dsu = new UnionFind(n);
        int goodPaths = 0;
        for(int value:valuesToNodes.keySet()){
            for(int node:valuesToNodes.get(value)){
                if(!adj.containsKey(node)){
                    continue;
                }
                for(int neighbor:adj.get(node)){
                    if(vals[node] >= vals[neighbor]){
                        dsu.connect(node,neighbor);
                    }
                }
            }
            Map<Integer,Integer> group = new HashMap<>();
            for(int u:valuesToNodes.get(value)){
                group.put(dsu.find(u), group.getOrDefault(dsu.find(u),0)+1);
            }

            for(int key:group.keySet()){
                int size = group.get(key);
                goodPaths += size*(size+1)/2;
            }

        }

        return goodPaths;
    }

//    int cnt;
//    Set<List<Integer>> allPath;
//    List<List<Integer>> map;
//    boolean[] visited;
//    private void dfs(int start, int cur, int[] values ,List<Integer> curPath){
//        curPath.add(cur);
//        visited[cur] = true;
//        List<Integer> neighbors = map.get(cur);
//        // check if curPath is good
//        if(start ==cur || values[start] == values[cur] ){
//            List<Integer> reverseCurPath = new ArrayList<>();
//            for(int i= curPath.size() - 1; i >= 0; i--){
//                reverseCurPath.add(curPath.get(i));
//            }
//           if(!allPath.contains(curPath) && !allPath.contains(reverseCurPath)){
//               cnt += 1;
//               allPath.add(new ArrayList<>(curPath));
//           }
//        }
//
//        for(Integer neighbor:neighbors){
//            if(values[neighbor]>values[start] || visited[neighbor]){
//                continue;
//            }
//            dfs(start,neighbor,values,curPath);
//        }
//        visited[cur] = false;
//        curPath.removeIf(val->val.equals(cur));
//    }
//    public int numberOfGoodPaths(int[] vals, int[][] edges) {
//        map = new ArrayList<>();
//        visited = new boolean[vals.length];
//        Arrays.fill(visited, false);
//        allPath = new HashSet<>();
//        cnt = 0;
//
//        for (int i = 0; i < vals.length; i++) {
//            map.add(new ArrayList<>());
//        }
//        for(int [] edge:edges){
//            map.get(edge[0]).add(edge[1]);
//            map.get(edge[1]).add(edge[0]);
//        }
//
//        for(int start = 0; start < vals.length; start++){
//            List<Integer> curPath = new ArrayList<>();
//            dfs(start,start,vals,curPath);
//        }
//        System.out.println(allPath);
//        return cnt;
//    }
}
