class Solution {
    public String removeOccurrences(String s, String part) {
        StringBuilder str = new StringBuilder(s);

        while(true){
            int index = str.indexOf(part);
            if(index == -1){
                break;
            }
            str.delete(index , index + part.length());
        }

        return str.toString();
        
    }
}