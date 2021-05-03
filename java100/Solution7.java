import org.junit.Test;
import static org.junit.Assert.*;
public class Solution7 {
    public int reverse(int x) {
        if(  x >Integer.MAX_VALUE || x<Integer.MIN_VALUE ){
            return 0;
        } else{
            int sum = 0;
            int flag = x;
            x = Math.abs(x);
            /* reverse*/
            while(x>0){
                /* outflow*/
                if(sum >Integer.MAX_VALUE/10){
                    return 0;
                }
                sum = sum*10+x%10;
                x = x/10;
            }
            /* output*/
            if(flag >= 0){
                /* outflow*/
                if(sum >Integer.MAX_VALUE){
                    return 0;
                }
                    return sum;
            } else{
                if(sum<Integer.MIN_VALUE){
                    return 0;
                }
                return -sum;
            }

        }

    }

    @Test
    public void Testcases(){

        int num = 123;
        int expected = 321;
        int actual = reverse(num);
        assertEquals(expected,actual);

        num = 1534236469;
        expected = 0;
        actual = reverse(num);
        assertEquals(expected,actual);


        num = -123;
        expected = -321;
        actual = reverse(num);
        assertEquals(expected,actual);

        num = 1463847412;
        expected = 2147483641;
        actual = reverse(num);
        assertEquals(expected,actual);

    }
}
