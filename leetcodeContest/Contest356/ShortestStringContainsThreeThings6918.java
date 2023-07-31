package leetcodeContest.Contest356;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ShortestStringContainsThreeThings6918 {
    public static String minimumString(String a, String b, String c) {

        List<String> res = new ArrayList<>();
        List<List<String>> choices = new ArrayList<>();
        choices.add(new ArrayList<>(List.of(a,b,c)));
        choices.add(new ArrayList<>(List.of(a,c,b)));
        choices.add(new ArrayList<>(List.of(b,a,c)));
        choices.add(new ArrayList<>(List.of(b,c,a)));
        choices.add(new ArrayList<>(List.of(c,a,b)));
        choices.add(new ArrayList<>(List.of(c,b,a)));
        int sameDigit =0;
        for(List<String> choice:choices){
            sameDigit = countSameDigits(choice.get(0),choice.get(1));

            String combined1 = choice.get(0)+choice.get(1).substring(sameDigit);

            sameDigit =countSameDigits(combined1, choice.get(2));
            String combined2 = combined1+choice.get(2).substring(sameDigit);
            res.add(combined2);
        }
        res.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.length()-o2.length();
            }
        });
        int minLength = res.get(0).length();
        List<String> result = new ArrayList<String>();
        for(String s:res){
            if(s.length()==minLength){
                result.add(s);
            }else{
                break;
            }
        }
        result.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return o1.compareTo(o2);
            }
        });
        return result.get(0);
    }

    public static int countSameDigits(String a, String b) {
        // count same digits of the end of a with start of b
        int starta = 0;
        int enda = 0;
        int endb = 0;
        while (starta < a.length() && enda < a.length()) {
            if (a.charAt(starta) == b.charAt(0)) {
                enda = starta;
                endb = 0;
                while ( a.charAt(enda) == b.charAt(endb)) {
                    enda += 1;
                    endb += 1;
                    if (enda == a.length()) {
                        return enda - starta;
                    }
                    if (endb == b.length()) {
                        return endb;
                    }
                }
            }
            starta += 1;

        }
        return 0;
    }

    public static void main(String[] args) {
        String a = "abc";
        String b = "bca";
        String c = "aaa";
        System.out.println(countSameDigits(b,a));
        String out = minimumString(a,b,c);
        System.out.println(out);

    }
}
