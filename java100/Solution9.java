import org.junit.Test;
import static org.junit.Assert.*;
public class Solution9 {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int temp = x;
        int digit = 0;
        while(temp>0){
            digit = 10*digit+ temp%10;
            temp /= 10;
        }
        return digit ==x;
    }
    @Test
    public void Test(){
        assertTrue(isPalindrome(0));
        assertFalse(isPalindrome(-1));
        assertFalse(isPalindrome(-121));
        assertFalse(isPalindrome(112));

    }
}

