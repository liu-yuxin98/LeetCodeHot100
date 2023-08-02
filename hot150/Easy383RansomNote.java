package hot150;

public class Easy383RansomNote {
    public boolean canConstruct(String ransomNote, String magazine) {
        if(magazine.length()<ransomNote.length()){
            return false;
        }
        int [] chs = new int[26];
        for(Character c : magazine.toCharArray()){
            chs[c-'a']++;
        }
        for(Character c :ransomNote.toCharArray()){
            chs[c-'a']--;
        }
        for(int i=0;i<26;i++){
            if(chs[i]<0){
                return false;
            }
        }
        return true;
    }
}
