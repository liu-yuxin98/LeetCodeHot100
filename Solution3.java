import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.junit.Assert.*;
public class Solution3 {
    public int lengthOfLongestSubstring(String s) {

        int max = 0;
        int i =0; /* front index of window*/
        int j = 0; /* back index of window*/
        /* a moving window*/
        HashSet<Character> window = new HashSet<>();
        while(i<s.length() && j<s.length()){

            while(j<s.length()){
                /* decide if s[j] in the window -> repeat*/
                if(window.contains(s.charAt(j))){
                    /* record length if its > max*/
                    if(window.size()>max){
                        max = window.size();
                    }
                    /* find the index of the repeat char and set the front
                    of the window to the first index after it
                     */
                    while(true){
                        if(s.charAt(i) == s.charAt(j)){
                            i += 1;
                            break;
                        }
                        /* delete the char infront of the repeat char including the chr*/
                        window.remove(s.charAt(i));
                        i+=1;
                    }
                } else{
                    /* add s[j] to window*/
                    window.add(s.charAt(j));
                    if(window.size()>max){
                        max = window.size();
                    }
                }
                j += 1;
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


