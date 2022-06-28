import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;
public class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        // record the previous index of the repeat char
        int[] previous = new int[128];
        for(int i = 0; i < 128; i++) {
            previous[i] = -1;
        }
        int front = 0;/* front of window*/
        int max = 0; /* result*/
        for(int i = 0; i < s.length(); i++) {
            int index = s.charAt(i);
            front = Math.max(front, previous[index] + 1);
            max   = Math.max(max, i - front + 1);
            previous[index] = i;
        }

        return max;


}
@Test
public void Testcases(){
        String s = "abcabcbb";
        int expected = 3;
        int actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);

        s = " ";
        expected = 1;
        actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);

        s = "";
        expected = 0;
        actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);

        s = "bbbbb";
        expected = 1;
        actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);


        s =  "dvdf";
        expected = 3;
        actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);


        s =  "asjrgapa";
        expected = 6;
        actual = lengthOfLongestSubstring(s);
        assertEquals(expected,actual);

}

}


