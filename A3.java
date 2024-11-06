import java.util.*;
class A3{
    static{
        System.loadLibrary("MyHello");
    }
    private native int add(int a,int b);
    private native int sub(int a,int b);
    private native int mul(int a,int b);
    private native int div(int a,int b);

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int a,b,c;
        System.out.println("Enter values of a and b: ");
        a=s.nextInt();
        b=s.nextInt();
        do{
            System.out.println("\n(1.add\n2.sub\n3.mul\n4.div\n)Enter Choice: ");
            c=s.nextInt();
            switch(c){
                case 1:new A3().add(a,b);
                    break;
                case 2: new A3().sub(a,b);
                    break;
                case 3 : new A3().mul(a,b);
                    break;
                case 4: new A3().div(a,b);
                    break;
                default:System.out.println("Invalid");
            }
        }while(c<5);
    s.close();
    }
}