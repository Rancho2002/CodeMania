static int helper(ArrayList<Integer> neg,ArrayList<Integer> pos, int k){
        int psize=pos.size();
        int nsize=neg.size();
        if(nsize==0){
            return pos.get(k-1);
        }
        if(psize==0){
            return Math.abs(neg.get(nsize-k));
        }
        int ans=Integer.MAX_VALUE;
        if(k<=psize){
            ans=Math.min(ans,pos.get(k-1));
        }
        if(k<=nsize){
            ans=Math.min(ans,Math.abs(neg.get(nsize-k)));
        }
        int pstart=Math.min(k-1,psize-1);
        for(int i=pstart;i>=0;i--){
            int rem=k-i-1;
            if(rem>nsize){
                break;
            }
            if(rem==0){
                continue;
            }
            int pside=pos.get(i);
            int nside=Math.abs(neg.get(nsize-rem));
            if(nside<pside){
                ans=Math.min(ans,2*nside+pside);
            }
            else{
                ans=Math.min(ans,2*pside+nside);
            }
        }
       return ans;
}