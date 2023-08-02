package hot150;

public class Easy67AddBinary {
    public static String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int pa = a.length() - 1;
        int pb = b.length() - 1;
        char digit = '0';
        while (pa >= 0 && pb >= 0) {
            if (a.charAt(pa) == '0' && b.charAt(pb) == '0') {
                sb.append(digit);
                digit = '0';
            } else if (a.charAt(pa) == '1' && b.charAt(pb) == '1') {
                if (digit == '1') {
                    sb.append('1');
                } else {
                    sb.append('0');
                    digit = '1';
                }
            } else {
                if (digit == '1') {
                    sb.append('0');
                } else {
                    sb.append('1');
                }
            }
            pa--;
            pb--;
        }
        if (pa < 0) {
            while (pb >= 0) {
                if (b.charAt(pb) == '0') {
                    sb.append(digit);
                    digit = '0';
                } else {
                    if (digit == '1') {
                        sb.append('0');
                    } else {
                        sb.append('1');
                    }
                }
                pb--;
            }
        } else {
            while (pa >= 0) {
                if (a.charAt(pa) == '0') {
                    sb.append(digit);
                    digit = '0';
                } else {
                    if (digit == '1') {
                        sb.append('0');
                    } else {
                        sb.append('1');
                    }
                }
                pa--;
            }
        }
        if(digit=='1'){
            sb.append('1');
        }
        String s = sb.toString();
        StringBuilder sb2 = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            sb2.append(s.charAt(i));
        }
        String res = sb2.toString();
        return res;
    }

    public static void main(String[] args) {
        String a = "1";
        String b = "1";
        System.out.println(addBinary(a,b));
    }
}
