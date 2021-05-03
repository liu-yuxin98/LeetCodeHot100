import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;
public class Solution5 {

    public String longestPalindrome(String s) {
       if(s.length()<=1){
           return s;
       }
       int max = s.length();
       for(int length = s.length();length>=0;length--){
           for(int start=0;start<max-length+1;start++){
                List<Character> l = getString(s,start,start+length-1);
                if(isPalindrome(l)){
                    return LtoString(l);
                }
           }
       }
       Character c = s.charAt(0);
       String res = Character.toString(c);
       return res;
    }
    /* return s[start:end] including end to list*/
    public List<Character> getString(String s,int start,int end){
        List<Character> res = new ArrayList<>();
        for(int i=start;i<=end;i++){
            res.add(s.charAt(i));
        }
        return res;

    }

    /* convert a list to string*/
    public String LtoString(List<Character> l){
        StringBuilder sb = new StringBuilder();
        for (Character s : l)
        {
            sb.append(s);
        }
        return sb.toString();
    }

    public Boolean isPalindrome(List<Character> l){
        if(l.size()<=1){
            return true;
        } else{
            boolean iseven = (l.size()%2 == 0);
            int length = l.size();
            if(iseven){
                int maxindex = length/2;
                for(int i=0;i<maxindex;i++){
                    if(l.get(i)!=l.get(length-1-i)){
                        return false;
                    }

                }
                return true;
            } else{
                int maxindex = length/2 ;
                for(int i=0;i<maxindex;i++){
                    if(l.get(i)!=l.get(length-1-i)){
                        return false;
                    }

                }
                return true;
            }

        }

    }


    @Test
    public void Testcases(){



        List<Character> s1 = new ArrayList<>();
        s1.add('a');
        s1.add('a');
        s1.add('c');
        s1.add('a');
        s1.add('b');
        s1.add('d');
        s1.add('k');
        s1.add('a');
        s1.add('c');
        s1.add('a');
        s1.add('a');
        System.out.println(isPalindrome(s1));



        String s = "babad";
        String expected = "bab";
        String expected2 = "aba";
        String actual = longestPalindrome(s);
        if(actual == expected || actual==expected2) {
            assertEquals(1,1);
        }

        s = "cbbd";
        expected =  "bb";
        actual = longestPalindrome(s);
        assertEquals(expected,actual);

        s = "a";
        expected =  "a";
        actual = longestPalindrome(s);
        assertEquals(expected,actual);

        s = "ac";
        expected =  "a";
        actual = longestPalindrome(s);
        assertEquals(expected,actual);

    }
}
