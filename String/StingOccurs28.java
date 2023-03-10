import java.util.Arrays;

public class StingOccurs28 {
    public int strStr(String haystack, String needle) {
        return KMP(haystack,needle);
    }

    public int [] buildNext(String p){
        int [] next = new int[p.length()];
        for (int j = 1; j < p.length(); j++) {
            int now = next[j-1];
            if(p.charAt(j) == p.charAt(now)){
                next[j] = now+1;
            } else{
                while(now>0){
                    if(p.charAt(j)==p.charAt(now)){
                        next[j] = now+1;
                        break;
                    }else{
                        now = next[now-1];
                    }
                }
                if(now==0){
                    if(p.charAt(j)==p.charAt(0)){
                        next[j] = 1;
                    }
                }
            }
        }
        return next;
    }

    public int KMP(String s, String p){
        // len(s)>=len(p)>=1
        int i = 0;
        int j = 0;
        int [] next = buildNext(p);
        System.out.println(Arrays.toString(next));
        while( i<s.length()){
            if(s.charAt(i) == p.charAt(j)){
                i++;
                j++;
            } else{ //s[i]!=p[j]
                if(j==0){
                    i ++;
                } else{
                    j = next[j-1];
                }
            }
            if(j==p.length()){
                return i-j;
            }
        }
        return -1;
    }




}
