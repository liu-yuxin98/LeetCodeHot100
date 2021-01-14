import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;
public class Solution3 {
    public int lengthOfLongestSubstring(String s) {
        int max =0;
        /* store chars without repeating*/
        Set<Character> chars = new HashSet();
        /* iterate through s*/
        for(int i=0;i<s.length();i++) {
            for(int j=i;j<s.length();j++){
                /* repeat*/
                if (chars.contains(s.charAt(j))) {
                    /* decide if the length of the set exceeds max*/
                    if (chars.size() > max) {
                        max = chars.size();
                    }
                    /* renew set*/
                    chars = new HashSet<>();
                    break;
                }
                /* add this char to set*/
                chars.add(s.charAt(j));
                if(chars.size()>max){
                    max = chars.size();
                }

            }
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


