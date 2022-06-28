import org.junit.Test;
import static org.junit.Assert.*;
public class Solution14 {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length<2){
            if(strs.length==0){
                return "";
            }
            return strs[0];
        }

        int i = 1;
        while(i<strs.length){
            String temp = PrefixBetweenTwoS(strs[i-1],strs[i]);
            strs[i] = temp;
            if(temp.equals("")){
                return temp;
            }
            i += 1;
        }

        return strs[strs.length-1];


    }

    public String PrefixBetweenTwoS(String s1,String s2){
        if(s1.length()==0 || s2.length()==0){
            return "";
        } else{
            int end = 0;
            int i = 0;
            int minl = Math.min(s1.length(),s2.length());
            String res;
            while(i<minl){
                if(s1.charAt(i)!=s2.charAt(i)){
                    end = i;
                    break;
                }
                i+=1;
                end = i;
            }
            res = s2.substring(0,end);
            return res;

        }

    }
    @Test
    public void Testcases(){
        /* test PrefixBetweenTwoS*/
        String pref = PrefixBetweenTwoS("abcd","abc");
        assertEquals("abc",pref);
        pref = PrefixBetweenTwoS("","ab");
        assertEquals("",pref);
        pref = PrefixBetweenTwoS("","");
        assertEquals("",pref);
        pref = PrefixBetweenTwoS("ABG","hks");
        assertEquals("",pref);
        pref = PrefixBetweenTwoS("123","123");
        assertEquals("123",pref);


        String[] inputs = new String[]{"flower","flow","flight"};
        String expected ="fl";
        String actual = longestCommonPrefix(inputs);
        assertEquals(expected,actual);

        inputs = new String[]{"dog","racecar","car"};
        expected = "";
        actual = longestCommonPrefix(inputs);
        assertEquals(expected,actual);
    }

}
