namespace AroundEarth
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double coindiameeter = 0.02575; //m      
            double maaraadius = 6378000; //m           
            double ümbermõõt = (2 * Math.PI * maaraadius);
            double coinamount = ümbermõõt / coindiameeter;

            Console.WriteLine("Maa ümbermõõt on " + ümbermõõt/1000 + " kilomeetrit."); // converted to km
            Console.WriteLine("Ümber maa läheb " + coinamount + " 2 eurost münti.");
        }
    }
}
