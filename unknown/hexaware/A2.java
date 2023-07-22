//hexaware code..

package unknown.hexaware;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class A2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List <Integer> l = new ArrayList<>();
        int c=0;
        while (n>1){
            for (int i=1;i<n;i++){
                if (n%i==0){
                    l.add(i);
                }
            }
            n-=l.get(l.size()-1);
            c+=1;
            l.removeAll(l);
            //System.out.println(n);
        }
        System.out.println(c);
    }
}
