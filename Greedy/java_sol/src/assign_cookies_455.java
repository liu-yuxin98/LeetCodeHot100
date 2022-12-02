import java.util.Arrays;

public class assign_cookies_455 {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);

        int pointer_s = 0;
        int pointer_g = 0;
        int contentChildren = 0;
        while(true){
            if(pointer_s >= s.length || pointer_g >= g.length){
                return contentChildren;
            }
            if(s[pointer_s]>=g[pointer_g]){
                // this child will be content with this cookie
                contentChildren ++;
                pointer_s++;
                pointer_g++;
            } else{
                pointer_s++;
            }

        }

    }
}
