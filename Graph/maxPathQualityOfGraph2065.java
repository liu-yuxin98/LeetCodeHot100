import java.util.*;

public class maxPathQualityOfGraph2065 {

    private int[] dijkstra(List<List<int []>> map){
        int [] minTimeToZero = new int[map.size()];
        Arrays.fill(minTimeToZero,Integer.MAX_VALUE);
        PriorityQueue<int[]> queue = new PriorityQueue<>((a,b)->Integer.compare(a[1],b[1]));
        queue.add(new int[]{0,0});
        minTimeToZero[0] = 0;

        while(!queue.isEmpty()){
            int[] item = queue.poll();
            int node = item[0];
            int value = item[1];
            if(value > minTimeToZero[node]){
                continue;
            }
            List<int []> children = map.get(item[0]);
            for(int[] child:children){
                int childNode = child[0];
                int pathValue = child[1];
                if(value+pathValue<minTimeToZero[childNode]) {
                    minTimeToZero[childNode] = Math.min(value + pathValue, minTimeToZero[childNode]);
                    queue.offer(new int[]{childNode, minTimeToZero[childNode]});
                }
            }
        }

        return minTimeToZero;
    }

    private void dfs(List<List<int []>> map,  int[] minTimeToZero, int[] values, int cur, int maxTime, Set<Integer> visited, int[] res){
        if(cur==0){
            int sum = 0;
            for(int i: visited){
                sum +=values[i];
            }
            res[0] = Math.max(res[0],sum);
        }

        for(int [] neighbor:map.get(cur)){
            if(minTimeToZero[neighbor[0]]+neighbor[1] <=maxTime) {
                System.out.println(visited);
                boolean added = visited.add(neighbor[0]);
                System.out.println(added);
                dfs(map, minTimeToZero, values, neighbor[0], maxTime - neighbor[1], visited, res);
                if (added) {
                    visited.remove(neighbor[0]);
                }
            }
        }
    }

    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {

        final int N = values.length;
        // map: { 0:{[1,10],[2,15]}, 1:...}
        List<List<int[]>> map = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            map.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            map.get(e[0]).add(new int[]{e[1], e[2]});
            map.get(e[1]).add(new int[]{e[0], e[2]});
        }
        int [] minTimeToZero = dijkstra(map);
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        int [] res = new int[]{0};
        dfs(map, minTimeToZero, values, 0, maxTime, visited, res);
        return res[0];
    }
}
