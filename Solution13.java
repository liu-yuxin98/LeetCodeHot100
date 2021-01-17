import org.junit.Test;

import java.util.HashMap;
import java.util.Map;
/*
*
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
。*/
public class Solution13 {
    public int romanToInt(String s) {
        Map<Character,Integer> maches = new HashMap<>();
        maches.put('I',1);
        maches.put('V',5);
        maches.put('X',10);
        maches.put('L',50);
        maches.put('C',100);
        maches.put('D',500);
        maches.put('M',1000);
        int res = 0;
        for(int i=0;i<s.length();i++){
          if(s.charAt(i) =='I'){
              if(i<s.length()-1){
                  if(s.charAt(i+1) =='V'){
                      res += 3;
                      i += 1;
                  } else if(s.charAt(i+1) == 'X'){
                      res += 8;
                      i += 1;
                  }
              }
              res += 1;
          }
          else if(s.charAt(i) =='X'){
              if(i<s.length()-1){
                  if(s.charAt(i+1) =='L'){
                      res += 30;
                      i += 1;
                  } else if(s.charAt(i+1) == 'C'){
                      res += 80;
                      i += 1;
                  }
              }
              res += 10;
          } else if(s.charAt(i) =='C'){
              if(i<s.length()-1){
                  if(s.charAt(i+1) =='D'){
                      res += 300;
                      i += 1;
                  } else if(s.charAt(i+1) == 'M'){
                      res += 800;
                      i += 1;
                  }
              }
              res += 100;
          } else{
              res += maches.get(s.charAt(i));
          }

        }
        return res;
    }

    @Test
    public void tes(){
        System.out.println(romanToInt("IV"));
    }

}
