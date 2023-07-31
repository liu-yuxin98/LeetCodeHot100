package hot150;

public class Easy125ValidPalindrome {
    public static boolean isPalindrome(String s) {
        int front =0;
        int end = s.length()-1;
        while (front<end){
            //skip none alphabetic
            if(!Character.isAlphabetic(s.charAt(front)) && !Character.isDigit(s.charAt(front))){
                front++;
            }
            else if(!Character.isAlphabetic(s.charAt(end))&& !Character.isDigit(s.charAt(end) )){
                end--;
            }else{
                if(Character.toLowerCase(s.charAt(front)) !=Character.toLowerCase(s.charAt(end))){
                    return false;
                }
                front++;
                end--;
            }

        }
        return true;

    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("0p"));
    }
}
