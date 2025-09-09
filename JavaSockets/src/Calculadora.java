public class Calculadora {
    private double num1;
    private double num2;
    private byte op;

    public void preencher(double num1, double  num2, byte op){
        this.num1 = num1;
        this.num2 = num2;
        this.op = op;
    }

    public double getNum1(){return num1;}
    public void setNum1(double num1){this.num1 = num1;}

    public double getNum2(){return num2;}
    public void setNum2(double num2){this.num2 = num2;}
    
    public byte getOp(){return op;}
    public void setOp(byte op){this.op = op;}

    public double Adicao(){return num1 + num2;}
    public double Subtracao(){return num1 - num2;}
    public double Multiplicacao(){return num1 * num2;}
    public double Divisao(){return num1 / num2;}

    public String calcular(){
        switch(this.op){
            case 1:
        }
    }
}
