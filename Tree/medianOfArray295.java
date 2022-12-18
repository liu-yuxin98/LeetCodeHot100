import java.util.Comparator;
import java.util.PriorityQueue;

public class medianOfArray295 {
    public medianOfArray295() {

    }
    PriorityQueue<Integer> minHeap = new PriorityQueue<Integer>();
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
    Integer totalNumbers = 0;
    public void addNum(int num) {
        totalNumbers += 1;
        if(minHeap.isEmpty() && maxHeap.isEmpty()){
            maxHeap.add(num);
        }else{
            if(num <= maxHeap.peek()){
                maxHeap.add(num);
                if(maxHeap.size()- minHeap.size()>1){
                    Integer m = maxHeap.poll();
                    minHeap.add(m);
                }

            } else{
                minHeap.add(num);
                if(minHeap.size() - maxHeap.size()>0) {
                    Integer m = minHeap.poll();
                    maxHeap.add(m);
                }

            }

        }

    }

    public double findMedian() {

        if(totalNumbers%2==0){
            return (minHeap.peek()+ maxHeap.peek())/2.0;
        }else {
            return maxHeap.peek();
        }
    }

}
