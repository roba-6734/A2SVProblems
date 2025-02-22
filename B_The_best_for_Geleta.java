import java.util.*;

public class Main{
    public static void main (String[] args){
        Scanner scanner = new Scanner(System.in);
        int rounds = scanner.nextInt();
        for (int t =0; t < rounds; t++){
            int n = scanner.nextInt();
            int m =scanner.nextInt();
            int [] arr = new int[n];
            for (int i=0; i<n; i++){
                arr[i] = scanner.nextInt();
            }
            for (int j=0;j<m;j++){
                String sign = scanner.next();
                int l = scanner.nextInt();
                int r = scanner.nextInt();

                for (int i=0;i<n;i++){
                    if (l <= arr[i] && arr[i]<=r){
                        arr[i] = (sign.equals("+"))? arr[i]+1:arr[i]-1

                    }
                }
                  System.out.print(Collections.max(Arrays.asList(Arrays.stream(arr).boxed().toArray((Integer[]::new))))+" ");
            }
          System.out.println();

        }

    }
}