import java.util.*;

public class KeysRoom841 {


    public boolean canVisitAllRooms(List<List<Integer>> rooms) {

        int n = rooms.size();  // number of rooms
        Set<Integer> visited = new HashSet<>();
//        visited = dfs(0,visited,rooms);
        visited = bfs(0,rooms);
        System.out.println(visited);
        return visited.size() == n;
    }

    // dfs
    public Set<Integer> dfs(Integer roomNumber, Set<Integer> visited,List<List<Integer>> rooms){
        // O(V+E)
        visited.add(roomNumber);
        List<Integer> neighbors = rooms.get(roomNumber);
        for(Integer NeighborNumber:neighbors){
            if(!visited.contains(NeighborNumber)){
                dfs(NeighborNumber,visited,rooms);
            }
        }
        return visited;
    }

    public Set<Integer> bfs(Integer roomNumber,List<List<Integer>> rooms){
        // O(V+E)
        Set<Integer> visited = new HashSet<Integer>();
        // FIFO QUEUEQ
        Deque<Integer> fringe = new LinkedList<>();
        fringe.add(roomNumber);
        while(!fringe.isEmpty()){
            Integer curRoomNumber = fringe.removeFirst();
            visited.add(curRoomNumber);
            List<Integer> neighbors = rooms.get(curRoomNumber);
            for(Integer neighborNumber:neighbors){
                if(!visited.contains(neighborNumber)){
                    fringe.add(neighborNumber);
                }

            }
        }
        return visited;
    }



}
