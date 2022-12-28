public class UnionFind {
    int [] parents;
    public UnionFind(int n) {
        parents = new int[n];
        for (int i = 0; i < n; i++)  {
            parents[i] = -1;
        }
    }

    int find(int p){
        // find parents of p
        int parent = p;
        while(parents[parent] > 0){
            parent = parents[parent];
        }
        return parent;
    }

    void connect(int p, int q){
        int pParent = find(p);
        int qParent = find(q);
        if(parents[pParent] < parents[qParent]){
            // p parent is larger
            parents[pParent] += parents[qParent];
            parents[qParent] = pParent;
            parents[q] = pParent;
        }else{
            // p parent is larger
            parents[qParent] += parents[pParent];
            parents[pParent] = qParent;
            parents[p] = qParent;
        }
    }

    boolean isConnected(int p, int q){
        int pParent = find(p);
        int qParent = find(q);
        return pParent == qParent;
    }

}
